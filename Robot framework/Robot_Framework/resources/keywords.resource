*** Keywords ***
Log Custom
    [Documentation]    Ce keyword affiche un message dans la console
    Log To Console    Dans le keyword custom

Addition
    [Documentation]    Ce keyword effectue une addition
    [Arguments]    ${a}    ${b}
    ${result}=    Evaluate    ${a} + ${b}
    [RETURN]    ${result}

Addition et Log
    [Documentation]    Ce keyword effectue une addition et affiche le résultat dans la console
    [Arguments]    ${a}    ${b}
    ${result}=    Evaluate    ${a} + ${b}
    Log To Console    Le résultat de l'addition est : ${result}


