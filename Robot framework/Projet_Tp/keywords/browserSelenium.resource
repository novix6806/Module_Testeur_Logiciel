*** Settings ***
Library    SeleniumLibrary


*** Keywords ***
Open Form Page Selenium
    [Documentation]    Open the form page using Selenium.
    Open Browser    ${FORM_PAGE_URL}    chrome