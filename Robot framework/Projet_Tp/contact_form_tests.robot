*** Settings ***
library    SeleniumLibrary
Variables    pages/form_page.py
Variables    pages/confirmation_page.py
Resource    keywords/browserSelenium.resource
Test Setup    Open Form Page Selenium
Test Teardown    Close Browser



*** Test Cases ***
Submit Contact Form
    [Documentation]    Go to the contact form page, fill in the form with valid data, submit it, and verify the confirmation message.
    ${user}=    Set Variable    ${USERS}[0]
    Input Text    ${FIRST_NAME_LOCATOR}    ${user}[first_name]
    Input Text    ${LAST_NAME_LOCATOR}    ${user}[last_name]
    Input Text    ${EMAIL_LOCATOR}    ${user}[email]
    Input Text    ${SUBJECT_LOCATOR}    ${user}[subject]
    Input Text    ${MESSAGE_LOCATOR}    ${user}[message]
    Click Button    ${SEND_BUTTON_LOCATOR}
    Wait Until Element Is Visible    ${CONFIRMATION_TEXT_LOCATOR}    15
    Page Should Contain    Thank you for your message. We will get in touch with you shortly


Soumission Formulaire Pour Chaque Utilisateur
    [Documentation]    Aller à la page du formulaire de contact, remplir le formulaire avec les données de chaque utilisateur dans la liste, le soumettre et vérifier le message de confirmation.
    FOR    ${user}    IN    @{USERS}
        Open Browser    ${FORM_PAGE_URL}    chrome
        Input Text    ${FIRST_NAME_LOCATOR}    ${user}[first_name]
        Input Text    ${LAST_NAME_LOCATOR}    ${user}[last_name]
        Input Text    ${EMAIL_LOCATOR}    ${user}[email]
        Input Text    ${SUBJECT_LOCATOR}    ${user}[subject]
        Input Text    ${MESSAGE_LOCATOR}    ${user}[message]
        Click Button    ${SEND_BUTTON_LOCATOR}
        Wait Until Element Is Visible    ${CONFIRMATION_TEXT_LOCATOR}    15
        Page Should Contain    Thank you for your message. We will get in touch with you shortly
        Close Browser
    END