*** Settings ***
Library    Browser

*** Variables ***
${URL}            https://fluentforms.com/forms/contact-form-demo/
${FIRST_NAME}     Test
${LAST_NAME}      User
${EMAIL}          test.user@example.com
${SUBJECT}        Form test
${MESSAGE}        This is a test message.

*** Test Cases ***
Submit Contact Form
    [Documentation]    Test submitting the contact form with valid data.
    New Browser    chromium    headless=False
    New Page       ${URL}
    Fill Text      id=ff_3_names_first_name_    ${FIRST_NAME}
    Fill Text      id=ff_3_names_last_name_     ${LAST_NAME}
    Fill Text      id=ff_3_email                ${EMAIL}
    Fill Text      id=ff_3_subject               ${SUBJECT}
    Fill Text      id=ff_3_message               ${MESSAGE}
    Click           //button[text()="Send Message"]
    Wait For Elements State    id=fluentform_3_success    visible    timeout=15s
    Get Text        css=body    contains    Thank you for your message. We will get in touch with you shortly
    Close Browser