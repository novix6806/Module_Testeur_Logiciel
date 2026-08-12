*** Settings ***
Library    Browser
Suite Setup                     New Browser            chromium        headless=False    New Page       ${FORM_PAGE_URL}
                                      
Suite Teardown                  Close Browser


*** Variables ***
${base_url}                     https://saucedemo.com
${username}                     standard_user
${password}                     secret_sauce


*** Test Cases ***
Recorded Test
    #New Browser               chromium                                      headless=False
    #New Context               viewport={'width': 1920, 'height': 1080}
    #New Page                  ${base_url}
    Fill Text                 data-test=username                            ${username}
    Fill Text                 data-test=password                            ${password}
    Click                     data-test=login-button
    Get Element States        data-test=item-4-img-link                     validate            visible
    Click                     role=button[name='Open Menu']
    Get Element States        data-test=inventory-sidebar-link              validate            visible
    Click                     data-test=logout-sidebar-link
    Close Browser
