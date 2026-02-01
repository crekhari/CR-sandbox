import { test, expect } from '@playwright/test';

test.describe('GenerateData.com - JSON Data Generation', () => {
  test.beforeEach(async ({ page }) => {
    // Navigate to the generator page
    await page.goto('https://generatedata.com/generator');

    // Handle cookie consent if it appears
    const cookieButton = page.getByRole('button', { name: 'Okay' });
    if (await cookieButton.isVisible({ timeout: 3000 }).catch(() => false)) {
      await cookieButton.click();
    }
  });

  test('should generate JSON data with Names field', async ({ page }) => {
    // Click the first row's data type dropdown
    await page.getByText('Select...').first().click();

    // Select "Names" from the dropdown
    await page.getByText('Names', { exact: true }).click();

    // Verify Names is selected
    await expect(page.getByText('Names').first()).toBeVisible();

    // Verify JSON format button is visible (default format)
    await expect(page.getByRole('button', { name: 'JSON' })).toBeVisible();

    // Verify the preview panel shows JSON data with "name" field
    await expect(page.locator('text="name":').first()).toBeVisible();

    // Click Generate button
    await page.getByRole('button', { name: 'Generate' }).click();

    // In the dialog, verify it's visible and click Generate
    await expect(page.getByRole('dialog')).toBeVisible();
    await page.getByRole('dialog').getByRole('button', { name: 'Generate' }).click();

    // Verify data was generated
    await expect(page.getByText('Data generated.')).toBeVisible();
  });

  test('should generate JSON data with Email field', async ({ page }) => {
    // Click the first row's data type dropdown
    await page.getByText('Select...').first().click();

    // Select "Email" from the dropdown
    await page.getByText('Email', { exact: true }).click();

    // Verify Email is selected
    await expect(page.getByText('Email').first()).toBeVisible();

    // Verify JSON format is selected
    await expect(page.getByRole('button', { name: 'JSON' })).toBeVisible();

    // Click Generate button
    await page.getByRole('button', { name: 'Generate' }).click();

    // Generate the data
    await page.getByRole('dialog').getByRole('button', { name: 'Generate' }).click();

    // Verify data was generated
    await expect(page.getByText('Data generated.')).toBeVisible();
  });

  test('should generate JSON data with Phone field', async ({ page }) => {
    // Click the first row's data type dropdown
    await page.getByText('Select...').first().click();

    // Select "Phone / Fax" from the dropdown
    await page.getByText('Phone / Fax').click();

    // Verify Phone is selected
    await expect(page.getByText('Phone / Fax').first()).toBeVisible();

    // Verify JSON format is selected
    await expect(page.getByRole('button', { name: 'JSON' })).toBeVisible();

    // Click Generate button
    await page.getByRole('button', { name: 'Generate' }).click();

    // Generate the data
    await page.getByRole('dialog').getByRole('button', { name: 'Generate' }).click();

    // Verify data was generated
    await expect(page.getByText('Data generated.')).toBeVisible();
  });

  test('should generate JSON data with multiple fields (Name, Email, Phone)', async ({ page }) => {
    // Select Names for first row
    await page.getByText('Select...').first().click();
    await page.getByText('Names', { exact: true }).click();

    // Select Email for second row
    await page.getByText('Select...').first().click();
    await page.getByText('Email', { exact: true }).click();

    // Select Phone for third row
    await page.getByText('Select...').first().click();
    await page.getByText('Phone / Fax').click();

    // Verify JSON format is selected
    await expect(page.getByRole('button', { name: 'JSON' })).toBeVisible();

    // Verify preview shows all fields
    await expect(page.locator('text="name":').first()).toBeVisible();
    await expect(page.locator('text="email":').first()).toBeVisible();
    await expect(page.locator('text="phone":').first()).toBeVisible();

    // Click Generate button
    await page.getByRole('button', { name: 'Generate' }).click();

    // Generate the data
    await page.getByRole('dialog').getByRole('button', { name: 'Generate' }).click();

    // Verify data was generated
    await expect(page.getByText('Data generated.')).toBeVisible();
  });

  test('should generate JSON data with Country field', async ({ page }) => {
    // Click the first row's data type dropdown
    await page.getByText('Select...').first().click();

    // Select "Country" from the Geo section
    await page.getByText('Country', { exact: true }).click();

    // Verify Country is selected
    await expect(page.getByText('Country').first()).toBeVisible();

    // Verify JSON format is selected
    await expect(page.getByRole('button', { name: 'JSON' })).toBeVisible();

    // Click Generate button
    await page.getByRole('button', { name: 'Generate' }).click();

    // Generate the data
    await page.getByRole('dialog').getByRole('button', { name: 'Generate' }).click();

    // Verify data was generated
    await expect(page.getByText('Data generated.')).toBeVisible();
  });

  test('should generate JSON data with Street Address field', async ({ page }) => {
    // Click the first row's data type dropdown
    await page.getByText('Select...').first().click();

    // Select "Street Address" from the Geo section
    await page.getByText('Street Address').click();

    // Verify Street Address is selected
    await expect(page.getByText('Street Address').first()).toBeVisible();

    // Verify JSON format is selected
    await expect(page.getByRole('button', { name: 'JSON' })).toBeVisible();

    // Click Generate button
    await page.getByRole('button', { name: 'Generate' }).click();

    // Generate the data
    await page.getByRole('dialog').getByRole('button', { name: 'Generate' }).click();

    // Verify data was generated
    await expect(page.getByText('Data generated.')).toBeVisible();
  });

  test('should generate JSON data with custom row count', async ({ page }) => {
    // Select Names for first row
    await page.getByText('Select...').first().click();
    await page.getByText('Names', { exact: true }).click();

    // Click Generate button
    await page.getByRole('button', { name: 'Generate' }).click();

    // Change row count to 50
    const rowInput = page.getByRole('dialog').getByRole('textbox');
    await rowInput.clear();
    await rowInput.fill('50');

    // Generate the data
    await page.getByRole('dialog').getByRole('button', { name: 'Generate' }).click();

    // Verify data was generated
    await expect(page.getByText('Data generated.')).toBeVisible();
  });

  test('should generate JSON data with Currency field', async ({ page }) => {
    // Click the first row's data type dropdown
    await page.getByText('Select...').first().click();

    // Select "Currency" from the Financial section
    await page.getByText('Currency', { exact: true }).click();

    // Verify Currency is selected
    await expect(page.getByText('Currency').first()).toBeVisible();

    // Verify JSON format is selected
    await expect(page.getByRole('button', { name: 'JSON' })).toBeVisible();

    // Click Generate button
    await page.getByRole('button', { name: 'Generate' }).click();

    // Generate the data
    await page.getByRole('dialog').getByRole('button', { name: 'Generate' }).click();

    // Verify data was generated
    await expect(page.getByText('Data generated.')).toBeVisible();
  });

  test('should generate JSON data with GUID field', async ({ page }) => {
    // Click the first row's data type dropdown
    await page.getByText('Select...').first().click();

    // Select "GUID" from the Numeric section
    await page.getByText('GUID', { exact: true }).click();

    // Verify GUID is selected
    await expect(page.getByText('GUID').first()).toBeVisible();

    // Verify JSON format is selected
    await expect(page.getByRole('button', { name: 'JSON' })).toBeVisible();

    // Click Generate button
    await page.getByRole('button', { name: 'Generate' }).click();

    // Generate the data
    await page.getByRole('dialog').getByRole('button', { name: 'Generate' }).click();

    // Verify data was generated
    await expect(page.getByText('Data generated.')).toBeVisible();
  });

  test('should generate JSON data with Date field', async ({ page }) => {
    // Click the first row's data type dropdown
    await page.getByText('Select...').first().click();

    // Select "Date" from the Human Data section
    await page.getByText('Date', { exact: true }).click();

    // Verify Date is selected
    await expect(page.getByText('Date').first()).toBeVisible();

    // Verify JSON format is selected
    await expect(page.getByRole('button', { name: 'JSON' })).toBeVisible();

    // Click Generate button
    await page.getByRole('button', { name: 'Generate' }).click();

    // Generate the data
    await page.getByRole('dialog').getByRole('button', { name: 'Generate' }).click();

    // Verify data was generated
    await expect(page.getByText('Data generated.')).toBeVisible();
  });
});
