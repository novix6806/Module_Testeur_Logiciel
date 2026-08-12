*** Settings ***
Library    Browser



*** Keywords ***
Open Form Page Playwright
    [Documentation]    Open the form page using Playwright.
    New Browser    chromium    headless=False
    New Page       ${FORM_PAGE_URL}


