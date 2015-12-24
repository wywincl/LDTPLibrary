*** Settings ***
Documentation     高级用户自定义中文关键字

*** Keywords ***
点击
    [Arguments]    ${args1}    ${args2}
    [Documentation]    鼠标（左键）点击操作
    [Tags]    LDTP
    ${ret}=    Click    ${args1}    ${args2}
    [Return]    ${ret}

打印日志
    [Arguments]    ${message}
    [Documentation]    打印日志信息
    [Tags]    BuiltIn
    Log    ${message}

获取文本框内容
    [Arguments]    ${args1}    ${args2}
    [Documentation]    获取指定文本框中的内容字段
    [Tags]    LDTP
    ${return_value}=    Get Text Value    ${args1}    ${args2}
    [Return]    ${return_value}

整数值应该相等
    [Arguments]    ${args1}    ${args2}
    [Documentation]    数值相等操作判断，只针对整数
    [Tags]    BuiltIn
    Should Be Equal As Integers    ${args1}    ${args2}

启动程序
    [Arguments]    ${app_name}    ${version}=zh_CN.UTF-8    ${delay}=0    ${env}=1
    [Documentation]    根据命令，启动一个应用程序
    [Tags]    LDTP
    ${ret}=    Launch App    cmd=${app_name}    lang=${version}    delay=${delay}    env=${env}
    [Return]    ${ret}

选择菜单标题栏
    [Arguments]    ${args1}    ${args2}
    [Documentation]    选择指定菜单|标题栏
    [Tags]    LDTP
    ${ret}=    Select Menu Item    ${args1}    ${args2}
    [Return]    ${ret}

等待直到窗口${window}存在
    [Documentation]    等待窗口${window}出现才继续往下执行, 否则等待默认时间
    [Timeout]    1 minute 30 seconds
    [Tags]    LDTP
    ${ret}=    Wait Till GUI Exist    ${window}
    [Return]    ${ret}

等待直到窗口${win}中的对象${obj}存在
    [Documentation]    等待窗口 ${win} 下的对象 ${obj} 出现才继续往下执行, 否则等待默认时间, 默认时间在中文版本关键字中不可以直接设置,可通过系统环境变量'GUI_TIMEOUT'修改, 默认值30s.
    [Timeout]    1 minute 30 seconds
    [Tags]    LDTP
    ${ret}=    Wait Till GUI Exist    ${win}    ${obj}
    [Return]    ${ret}

等待直到窗口${window}不存在
    [Documentation]    等待窗口${window}消失才继续往下执行, 否则等待默认时间
    [Timeout]    1 minute 30 seconds
    [Tags]    LDTP
    ${ret}=    Wait Till GUI No Exist    ${window}
    [Return]    ${ret}

等待直到窗口${win}中的对象${obj}不存在
    [Documentation]    等待窗口 ${win} 下的对象 ${obj} 消失才继续往下执行, 否则等待默认时间, 默认时间在中文版本关键字中不可以直接设置,可通过系统环境变量'GUI_TIMEOUT'修改, 默认值30s.
    [Timeout]    1 minute 30 seconds
    [Tags]    LDTP
    ${ret}=    Wait Till GUI No Exist    ${win}    ${obj}
    [Return]    ${ret}