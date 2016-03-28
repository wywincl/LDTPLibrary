*** Settings ***
Documentation    Suite description
Library    LDTPLibrary

*** Variables ***
${window}    frmCalculator
${dialog}    dlgPreferences

*** Test Cases ***
Test title
    Launch APP    gnome-calculator
    Sleep    5s
    Close Window    ${window}

*** Keywords ***
