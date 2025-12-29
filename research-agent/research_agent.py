import os
import json
from typing import Dict, List
import anthropic
from tavily import TavilyClient


class DeepResearchAgent:
    def __init__(self, resume_text: str, tavily_api_key: str, anthropic_api_key: str):
        """
        Initialize the research agent with resume and API credentials.
        
        Args:
            resume_text: Your resume as a string
            tavily_api_key: Tavily API key for web search
            anthropic_api_key: Anthropic API key for Claude
        """
        self.resume = resume_text
        self.tavily_client = TavilyClient(api_key=tavily_api_key)
        self.claude_client = anthropic.Anthropic(api_key=anthropic_api_key)
    
    def search(self, query: str, max_results: int = 5) -> List[Dict]:
        """
        Perform a Tavily search and return results.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            List of search results with title, content, and URL
        """
        try:
            response = self.tavily_client.search(
                query=query,
                max_results=max_results,
                search_depth="advanced"
            )
            return response.get('results', [])
        except Exception as e:
            print(f"Search error for query '{query}': {e}")
            return []
    
    def research_company(self, company_name: str) -> Dict:
        """
        Conduct comprehensive research on a company.
        
        Args:
            company_name: Name of the company to research
            
        Returns:
            Dictionary containing company profile and interview questions
        """
        print(f"\n🔍 Researching {company_name}...")
        
        # Step 1: Gather information through multiple searches
        print("  → Searching company overview...")
        overview_results = self.search(f"{company_name} company overview funding team size")
        
        print("  → Searching technology stack...")
        tech_results = self.search(f"{company_name} engineering blog tech stack architecture")
        
        print("  → Searching recent news...")
        news_results = self.search(f"{company_name} news recent developments 2024 2025")
        
        print("  → Searching culture and team...")
        culture_results = self.search(f"{company_name} engineering culture team values")
        
        print("  → Searching product and market...")
        product_results = self.search(f"{company_name} product features AI machine learning")
        
        # Step 2: Synthesize research into structured profile
        print("\n📊 Synthesizing research...")
        company_profile = self._synthesize_company_profile(
            company_name,
            overview_results,
            tech_results,
            news_results,
            culture_results,
            product_results
        )
        
        # Step 3: Generate tailored interview questions
        print("💡 Generating interview questions...")
        interview_questions = self._generate_interview_questions(
            company_name,
            company_profile
        )
        
        return {
            'company_name': company_name,
            'profile': company_profile,
            'questions': interview_questions
        }
    
    def _synthesize_company_profile(
        self,
        company_name: str,
        overview_results: List[Dict],
        tech_results: List[Dict],
        news_results: List[Dict],
        culture_results: List[Dict],
        product_results: List[Dict]
    ) -> str:
        """
        Use Claude to synthesize search results into a structured company profile.
        """
        # Prepare search results for Claude
        search_data = {
            'overview': self._format_search_results(overview_results),
            'technology': self._format_search_results(tech_results),
            'news': self._format_search_results(news_results),
            'culture': self._format_search_results(culture_results),
            'product': self._format_search_results(product_results)
        }
        
        synthesis_prompt = f"""Based on the following search results about {company_name}, create a comprehensive company profile organized into these sections:

1. **Company Overview** - founding, mission, stage, size, funding
2. **Product & Technology** - what they build, key features, technical approach
3. **Tech Stack & Engineering** - technologies used, engineering practices, technical blog insights
4. **Recent Developments** - latest news, product launches, growth indicators
5. **Culture & Team** - engineering culture, values, team structure
6. **Key Challenges & Opportunities** - industry position, competitive landscape, growth areas

Search Results:

OVERVIEW:
{search_data['overview']}

TECHNOLOGY:
{search_data['technology']}

NEWS:
{search_data['news']}

CULTURE:
{search_data['culture']}

PRODUCT:
{search_data['product']}

Provide a well-structured, informative profile that would help someone prepare for a job interview. Focus on concrete details and skip generic statements. If certain information isn't available in the search results, note that briefly rather than speculating."""

        message = self.claude_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": synthesis_prompt}]
        )
        
        return message.content[0].text
    
    def _generate_interview_questions(
        self,
        company_name: str,
        company_profile: str
    ) -> str:
        """
        Generate tailored interview questions based on company profile and resume.
        """
        questions_prompt = f"""You are helping a candidate prepare for an interview at {company_name}.

COMPANY PROFILE:
{company_profile}

CANDIDATE'S RESUME:
{self.resume}

Generate 10-15 thoughtful interview questions the candidate should ask, organized into these categories:

1. **Technical Deep-Dive** (3-4 questions)
   - Questions that show technical expertise and understanding of their stack
   - Connect candidate's experience (LLM observability, multi-model systems) to their needs

2. **Product & Strategy** (3-4 questions)
   - Questions about product roadmap, technical challenges, market position
   - Show strategic thinking and business understanding

3. **Team & Culture** (2-3 questions)
   - Engineering practices, team structure, growth opportunities
   - Demonstrate interest in long-term fit

4. **Role-Specific** (2-3 questions)
   - Questions about the specific role, expectations, success metrics
   - Show preparedness and seriousness about the opportunity

For each question, include a brief note on why this question is strategically good (e.g., "This highlights your observability experience at Quotient").

Make questions specific to this company - avoid generic questions that could apply anywhere."""

        message = self.claude_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": questions_prompt}]
        )
        
        return message.content[0].text
    
    def _format_search_results(self, results: List[Dict]) -> str:
        """
        Format search results into readable text for Claude.
        """
        if not results:
            return "No results found."
        
        formatted = []
        for i, result in enumerate(results, 1):
            title = result.get('title', 'No title')
            content = result.get('content', 'No content')
            url = result.get('url', 'No URL')
            formatted.append(f"[{i}] {title}\n{content}\nSource: {url}\n")
        
        return "\n".join(formatted)
    
    def save_results(self, results: Dict, filename: str):
        """
        Save research results to a JSON file.
        
        Args:
            results: Research results dictionary
            filename: Output filename
        """
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n✅ Results saved to {filename}")


def main():
    """
    Example usage of the DeepResearchAgent.
    """
    # Load API keys from environment
    TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    
    if not TAVILY_API_KEY or not ANTHROPIC_API_KEY:
        print("Error: Please set TAVILY_API_KEY and ANTHROPIC_API_KEY environment variables")
        return
    
    # Your resume text (replace with actual resume)
    RESUME = """
    [Your resume text here - include key experiences, skills, projects]
    
    Example:
    - Founding engineer at Quotient AI (11 months)
    - Built LLM observability infrastructure using OpenTelemetry
    - Developed multi-model hallucination detection system (8 models, 14M-140M params)
    - Achieved 100x cost reduction and 20x performance improvement vs GPT-4
    - Skills: Python, LLMs, observability, system architecture
    """
    
    # Initialize agent
    agent = DeepResearchAgent(
        resume_text=RESUME,
        tavily_api_key=TAVILY_API_KEY,
        anthropic_api_key=ANTHROPIC_API_KEY
    )
    
    # Research a company
    company_name = "MyJunior AI"  # Replace with target company
    results = agent.research_company(company_name)
    
    # Print results
    print("\n" + "="*80)
    print(f"RESEARCH RESULTS: {results['company_name']}")
    print("="*80)
    print("\nCOMPANY PROFILE:")
    print(results['profile'])
    print("\n" + "-"*80)
    print("\nINTERVIEW QUESTIONS:")
    print(results['questions'])
    print("\n" + "="*80)
    
    # Optionally save to file
    agent.save_results(results, f"{company_name.lower()}_research.json")


if __name__ == "__main__":
    main()