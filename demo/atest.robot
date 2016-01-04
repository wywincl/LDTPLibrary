*** Settings ***
Documentation     Suite description
Library           LDTPLibrary    Capture Screenshot    out_file=/tmp/demo.png    #Resource | LDTPLibrary/keywords/high-level-keywords_zh.robot | #Resource | LDTPLibrary/keywords/high-level-keywords_en.robot

*** Variables ***
${window}         frmCalculator
${dialog}         dlgPreferences

*** Test Cases ***
Test title
    Launch APP    gnome-calculator2    zh_CN.utf-8
    # 等待直到窗口${window}存在
    # 选择菜单标题栏    ${window}    mnuApplication;mnuPreferences
    #    ${ret}=    等待直到窗口${window}中的对象${dialog}存在
    #    打印日志    ${ret}
    #    ${ret}=    Wait Till frmCalculator Exist
    #    Log    ${ret}

*** Keywords ***
