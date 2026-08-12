*** Settings *** 
Documentation   A simple test suite to demonstrate Robot Framework

Resource    resources/keywords.resource
Variables    resources/variables.py
Suite Setup    Log To Console    Dans Suite Setup
Suite Teardown    Log To Console    Dans Suite Teardown
Test Setup    Log To Console    Dans Test Setup
Test Teardown    Log To Console    Dans Test Teardown    
Library    SeleniumLibrary
Test Tags    demonstration 

*** Variables ***
${variable}    Ceci est une variable simple    #Variable simple
@{list}    element1    element2    element3    #Une liste
&{dictionary}    key1=value1    key2=value2    example=value3    #Un dictionnaire avec des paires clé-valeur
 
*** Test Cases ***

Premier test
    [Tags]    premier
    [documentation]    Ce test ouvre le navigateur et affiche un message dans la console
    [timeout]    1 minute
    Open Browser    https://www.google.com/    chrome
    Sleep    5s
    ${message}=    Set Variable    Premier message avec robot Framework
    Log To Console    ${message}

Deuxieme Test
    [Tags]    deuxieme    autretag
    [documentation]    Ce test affiche la valeur d'une variable dans la console
    [timeout]    1 minute
    Log To Console    ${variable}
    Log to Console    ${list}[0]
    Log to Console    ${list}[1]
    #Log to Console    ${dictionary}[key1]
    Log to Console    ${dictionary.key1}
    Log to Console    ${dictionary.example}

Troisieme Test
    [Tags]    troisieme
    [documentation]    Ce test appelle un keyword custom et affiche un message dans la console
    [timeout]    1 minute
    Log Custom
    ${result}=    Addition    5    10
    Log To Console    Le résultat de l'addition est : ${result}

Quatrieme Test
    [Tags]    quatrieme
    [Template]    Addition et Log
    7    3
    4    6

Condition
    ${temperature}=    Set Variable    150
    IF    ${temperature} < 0
        Log To Console    Il neige actuellement
    ELSE IF    ${temperature} > 100
        Log To Console    L'eau s'évapore
    ELSE
        Log To Console    Il ne neige pas actuellement
    END

Loop
    @{europe}=    Create List    France    Allemagne    Italie    Espagne
    FOR    ${pays}    IN    @{europe}
        Log To Console    ${pays}
    END

    FOR    ${i}    IN RANGE    1    6
        Log To Console    ${i}
    END