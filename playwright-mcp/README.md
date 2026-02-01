# Playwright MCP Tests

Automated test cases for [generatedata.com](https://generatedata.com) that select various data types and generate JSON output.

## Setup

### 1. Install dependencies

```bash
cd playwright-mcp
npm install
```

### 2. Install Playwright browsers

```bash
npx playwright install chromium
```

## Running Tests

```bash
# Run tests in headless mode
npm test

# Run tests with browser visible
npm run test:headed

# Run tests with Playwright UI
npm run test:ui
```

## Test Cases

The test suite includes 10 tests that verify JSON data generation for:
- Names
- Email
- Phone
- Multiple fields (Name, Email, Phone combined)
- Country
- Street Address
- Custom row count
- Currency
- GUID
- Date

---

## MCP Server Configuration

### Claude Code

To use the Playwright MCP server with Claude Code, add it to your Claude Code settings file (`~/.claude/settings.json`):

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-server-playwright"]
    }
  }
}
```

Alternatively, you can use the official Playwright MCP package:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

After adding the configuration, restart Claude Code for the changes to take effect.

### GitHub Copilot

**No configuration needed.** GitHub Copilot's coding agent comes with the Playwright MCP server pre-configured by default. It provides web page interaction capabilities including reading, interacting with, and taking screenshots of web content.

See: [MCP and the coding agent - Default MCP servers](https://docs.github.com/en/copilot/concepts/agents/coding-agent/mcp-and-coding-agent#default-mcp-servers)

---

## Project Structure

```
playwright-mcp/
├── test.ts              # Test cases
├── playwright.config.ts # Playwright configuration
├── package.json         # Project dependencies
├── playwright-report/   # HTML test reports (generated)
└── test-results/        # Failed test artifacts (generated)
```
