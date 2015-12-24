*** Settings ***
Documentation     High Level Keywords In English
Library    LDTPLibrary

*** Keywords ***
Wait Till ${window} Exist
    [Documentation]    wait till ${window} exist and go on, otherwise wait for defaut time, setting in environment variable 'GUI_TIMEOUT'
    [Timeout]    1 minute 30 seconds
    [Tags]    LDTP
    ${ret}=    LDTPLibrary.Wait Till GUI Exist    ${window}
    [Return]    ${ret}

Wait Till ${window}'s Component ${object} Exist
    [Documentation]    wait till ${window}'s component ${object} exist and go on, otherwise wait for defaut time, setting in environment variable 'GUI_TIMEOUT'
    [Timeout]    1 minute 30 seconds
    [Tags]    LDTP
    ${ret}=    Wait Till GUI Exist    ${window}    ${object}
    [Return]    ${ret}