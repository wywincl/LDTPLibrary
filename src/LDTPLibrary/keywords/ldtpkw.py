#!/usr/bin/env python
# coding=utf-8
"""
Robot Framework LDTP Library

LDTPLibrary is a gui application testing library for Robot Framework.

It uses the LDTP (Linux Desktop Test Project) libraries internally to control a gui application.
See http://ldtp.freedesktop.org/wiki/ for more information on LDTP.

@author: Wang Yang <wywincl@gmail.com>
@copyright: Copyright (c) 2015-2016 Wang Yang
@license: GPLv3

See 'LICENSE' in the source distribution for more information.
"""

import sys
try:
    import ldtp
except ImportError:
    if sys.platform != "darwin":
        raise
    import atomac.ldtp as ldtp
from keywordgroup import KeywordGroup
try:
    from ldtp.client_exception import LdtpExecutionError
except ImportError:
    if sys.platform != "darwin":
        raise
    from atomac.ldtp.client_exception import LdtpExecutionError
from _exception import LdtpError
from robot.api.deco import keyword

try:
    from robot.api import logger
except ImportError:
    logger = None


class LDTPKeywords(KeywordGroup):
    # Public

    def __init__(self):
        self._client = ldtp

        if sys.version_info[:2] < (3, 0):
            reload(sys)
            sys.setdefaultencoding('utf-8')

    def launch_app(self, cmd, lang='zh_CN.UTF-8', delay=0, env=1, *args):
        """
        [关键字概要] 启动应用程序

        :@参数 cmd: 应用程序名称, 如gedit, gnome-calculator等。

        :@参数 lang: 语言版本, 'C'表示英文版本, 'zh_CN.UTF-8'表示英文。

        :@参数 env: 环境变量

        :@参数 args: 应用程序参数列表

        :@参数 delay: 启动延时

        :@返回值: 成功或失败, 执行异常时，抛出LdtpExecutionError异常类型, 执行成功返回进程PID.

        Examples:

        |  *Test Cases*  |  *Returns*   |  *Action*    |  *Arguments*  |
        |  Example_Test  |  ${PID}      |  Launch App  | ${APP_NAME}   |

        """
        try:
            self._info("launch app (APP Name: %s)..." % cmd)
            # print("*INFO* Launch app [%s]...\r\n" % cmd)
            return self._client.launchapp(cmd, list(args), int(delay), int(env), lang)
        except LdtpError:
            raise LdtpError("launch app failed, please check if the input parameters are correct.")

    def click(self, window_name, object_name):
        """
        [关键字概要] 鼠标点击操作， 点击对象包括radio button/check box/push button/combo box/radio menu item/toggle button.

        :@参数 window_name: 窗口名称

        :@参数 object_name: 对象名称

        :@返回值: 成功或失败，执行异常时，抛出LdtpExecutionError异常类型

        Examples:

        |  *Test Cases*  |  *Action*  |  *Argument*  |  *Arguments*  |
        |  Example_Test  |   Click    |  ${FRM_NAME} | ${BTN_NAME}   |


        """
        try:
            self._info("mouse click... （%s, %s)" % (window_name, object_name))
            # print("*INFO* Mouse click ... [%s, %s] \r\n" % (window_name, object_name))
            return ldtp.click(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("click failed, please check if the input parameters are correct.")

    def get_text_value(self, window_name, object_name):
        """
        *[关键字概要]* 获取Text文本框内容

        :@参数 window_name: 窗口名称

        :@参数 object_name: 对象名称

        :@返回值: 文本框内容

        *Examples*:

        |  *Test Cases*  |  *Returns*  |  *Action*    |  *Arguments*  |  *Arguments*   |
        |  Example_Test  | ${text}=    | Get Text Value |  ${FRM_NAME} | ${TXT_NAME}   |

        """
        try:
            self._info("get text value ... (%s, %s)" % (window_name, object_name))
            # print("*INFO* get text value ... [%s, %s]\r\n" % (window_name, object_name))
            return ldtp.gettextvalue(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("get text value failed, please check if the input parameters are correct. ")

    def set_text_value(self, window_name, object_name, data):
        """
        [关键字概要] 设置Text文本框内容

        :@参数 window_name: 窗口名称

        :@参数 object_name: 对象名称

        :@参数 data: 要设置的内容

        :@返回值: 成功或失败

        Examples:

        |  *Test Cases*  |  *Action*    |  *Arguments*  |  *Arguments*   |  *Arguments*  |
        |  Example_Test  | Set Text Value |  ${FRM_NAME} | ${TXT_NAME}   |   ${DATA}     |


        """
        try:
            self._info("set text value ... (%s, %s)\r\n" % (window_name, object_name))
            # print("*INFO* set text value ... [%s, %s]\r\n" % (window_name, object_name))
            return ldtp.settextvalue(window_name, object_name, data)
        except LdtpExecutionError:
            raise LdtpExecutionError(" set text value failed, please check if the input parameters are correct. ")

    def select_menu_item(self, window_name, object_name):
        """
        [关键字概要] 选择菜单栏, 菜单栏可以以`;`符号表示层级， 如mnuFile;mnuNew

        :@参数 window_name: 窗口名称

        :@参数 object_name: 对象名称

        :@返回值: 成功或失败


        Examples:

        |  *Test Cases*  |        *Action*       |  *Argument*  |  *Arguments*   |
        |  Example_Test  |   Select Menu Item    |  ${FRM_NAME} | ${MENU_ITEM_NAME}   |


        """
        try:
            self._info("select menu item ... (%s, %s)" % (window_name, object_name))
            # print("*INFO* select menu item ... [%s, %s]\r\n" % (window_name, object_name))
            return ldtp.selectmenuitem(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("select menu item failed, please check if the input parameters are correct. ")

    def select_row(self, window_name, object_name, row_text):
        """
        [关键字概要] 选择列表中的一行内容.

        :@参数 window_name: 窗口名称

        :@参数 object_name: 对象名称

        :@参数 row_text: 选择的一行文本行

        :@返回值: 1 on success.

        Examples:

        |  *Test Cases*  |        *Action*       |    *Argument*   |  *Arguments*  |  *Arguments*  |
        |  Example_Test  |      Select Row       |  ${window_name} | ${table_name} |   ${row_text} |


        """
        try:
            self._info("select row (%s, %s, %s)" % (window_name, object_name, row_text))
            return ldtp.selectrow(window_name, object_name, row_text)
        except LdtpExecutionError:
            raise LdtpExecutionError("select row failed, please check if the input parameters are correct. ")

    def activate_window(self, window_name):
        """
        [关键字概要] 使用wnck机制激活一个窗口

        :@参数 window_name: 窗口名称

        :@返回值: 1 on success.

        Examples:

        |  *Test Cases*  |        *Action*       |    *Argument*   |
        |  Example_Test  |     Activate Window   |  ${window_name} |

        """
        try:
            self._info("activate window %s" % window_name)
            return ldtp.activatewindow(window_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("activate window failed, please check if the input parameters are correct. ")

    def gui_exist(self, window_name, object_name=''):
        """
        [关键字概要] 检查窗口或者组件对象是否存在

        :@参数 window_name: 窗口名称

        :@参数 object_name: 对象名称

        :@返回值: 存在返回 1,不存在返回 0

        Examples:

        |  *Test Cases*  |        *Action*       |    *Argument*   |    *Argument*   |
        |  Example_Test  |       GUI Exist       |  ${window_name} |                 |
        |                |       GUI Exist       |  ${window_name} |  ${object_name} |

        """
        try:
            self._info("gui exist (%s, %s)" % (window_name, object_name))
            return ldtp.guiexist(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("gui exist failed, please check if the input parameters are correct. ")

    def wait_till_gui_exist(self, window_name, object_name='', gui_time_out=30, state=''):
        """
        Wait till a window or component exists.

        :param window_name:  Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        :param object_name: Object name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        :param gui_time_out: Wait timeout in seconds.

        @type gui_time_out: integer

        :param state: Object state used only when object_name is provided.

        @type state: string

        :return: 1 if GUI was found, 0 if not.

        @rtype: integer
        """
        try:
            self._info(
                    "wait till a window or component exists. [%s, %s, %d]" % (window_name, object_name, gui_time_out))
            return ldtp.waittillguiexist(window_name, object_name, gui_time_out, state)
        except LdtpExecutionError:
            raise LdtpExecutionError("exec ldtp.waittillguiexist failed")

    def wait_till_gui_not_exist(self, window_name, object_name='', gui_time_out=30):
        """
        Wait till a window or component doesn't exist.

        :param window_name:  Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        :param object_name: Object name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        :param gui_time_out: Wait timeout in seconds.

        @type gui_time_out: integer

        :return: 1 if GUI has gone away, 0 if not

        @rtype: integer
        """
        try:
            self._info(
                    "wait till a window or component exists. [%s, %s, %d]" % (window_name, object_name, gui_time_out))
            return ldtp.waittillguinotexist(window_name, object_name, gui_time_out)
        except LdtpExecutionError:
            raise LdtpExecutionError("exec ldtp.waittillguinotexist failed")

    def close_window(self, window_name=''):
        """
        [关键字概要] 关闭窗口

        :@参数 window_name: 窗口名称

        :@返回值: 1 on success.


        Examples:

        |  *Test Cases*  |        *Action*       |    *Argument*   |
        |  Example_Test  |      Close Window     |  ${window_name} |

        """
        try:
            self._info("close window (%s)" % window_name)
            return ldtp.closewindow(window_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("close window failed, please check if the input parameters are correct. ")

    def get_window_size(self, window_name):
        """
        Description: Get the window size, of the given window name. If window does not exist,
        then LdtpExecutionError will be thrown.

        :param window_name:

        :return: [x,y,width,height]	as a list and as int type will be returned on success,
        LdtpExecutionError exception on failure

        Examples:

        |  *Test Cases*  |    *Returns*   |        *Action*       |    *Argument*   |
        |  Example_Test  |     @{size}=   |    Get Window Size    |  ${window_name} |


        """
        try:
            self._info("get window size of (%s) " % window_name)
            return ldtp.getwindowsize(window_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("get window size failed!")

    def get_row_count(self, window_name, object_name):
        """
        Description: Get count of rows in table object.

        :param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        :param object_name: Object name to look for, either full name,
        LDTP's name convention, or a Unix glob. Or menu heirarchy

        :return: Number of rows.
        """
        try:
            self._info("get row count of table [%s, %s]" % (window_name, object_name))
            return ldtp.getrowcount(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("get row count of table failed")

    def maximize_window(self, window_name=None):
        """
        Description: Maximize window based on the given name,
         default None. If None, will maximize all window one by one

        :param window_name:

        :return: 1 on success, LdtpExecutionError exception will be thrown on failure
        """
        try:
            self._info("maximize a windows")
            return ldtp.maximizewindow(window_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("maximize window failed")

    def unmaximize_window(self, window_name=None):
        """
        Description: UnMaximize window based on the given name,
         default None. If None, will unmaximize all window one by one

        :param window_name:

        :return: 1 on success, LdtpExecutionError exception will be thrown on failure
        """
        try:
            self._info("unmaximize a windows")
            return ldtp.unmaximizewindow(window_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("unmaximize window failed")

    def minimize_window(self, window_name=None):
        """
        Description: Minimize window based on the given name,
         default None. If None, will minimize all window one by one

        :param window_name:

        :return: 1 on success, LdtpExecutionError exception will be thrown on failure
        """
        try:
            self._info("minimize a windows")
            return ldtp.minimizewindow(window_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("minimize window failed")

    def unminimize_window(self, window_name=None):
        """
        Description: UnMinimize window based on the given name,
         default None. If None, will unminimize all window one by one

        :param window_name:

        :return: 1 on success, LdtpExecutionError exception will be thrown on failure
        """
        try:
            self._info("unminimize a windows")
            return ldtp.unminimizewindow(window_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("unminimize window failed")

    def enter_string(self, window_name, object_name='', data=''):
        """
        Description: Functionality of enterstring is similar to typekey of LTFX project.
        Main difference is this function works based on accessibility. So, we could specify the window name,
         object name and finally the data string.

        :param window_name:

        :param object_name:

        :param data:

        :return: Returns 1 on success, LdtpExecutionError exception will be thrown on failure
        """
        try:
            self._info("enter string with keyboard")
            return ldtp.enterstring(window_name, object_name, data)
        except LdtpExecutionError:
            raise LdtpExecutionError("enter string with keyboard failed")

    @keyword('Capture Screenshot')
    def image_capture(self, window_name=None, out_file=None, x=0, y=0,
                      width=None, height=None):
        """
        Captures screenshot of the whole desktop or given window

        @param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @:argument out_file: the capture screenshot file save path.

        @type out_file: string

        @param x: x co-ordinate value

        @type x: int

        @param y: y co-ordinate value

        @type y: int

        @param width: width co-ordinate value

        @type width: int

        @param height: height co-ordinate value

        @type height: int

        @return: screenshot with base64 encoded for the client

        @rtype: string
        """
        try:
            self._info("screen capture, and the out file: %s " % out_file)
            self._html('the capture picture is <a href="%s"><img src="%s" width="800px">%s</a>' % (out_file, out_file,
                                                                                                   out_file))
            return ldtp.imagecapture(window_name, out_file, x, y, width, height)
        except LdtpExecutionError:
            raise LdtpExecutionError("image capture failed")

    @keyword('Capture Screenshot Without Embedding')
    def image_capture_2(self, window_name=None, out_file=None, x=0, y=0,
                        width=None, height=None):
        """
        Captures screenshot of the whole desktop or given window

        @param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @:argument out_file: the capture screenshot file save path.

        @type out_file: string

        @param x: x co-ordinate value

        @type x: int

        @param y: y co-ordinate value

        @type y: int

        @param width: width co-ordinate value

        @type width: int

        @param height: height co-ordinate value

        @type height: int

        @return: screenshot with base64 encoded for the client

        @rtype: string
        """
        try:
            self._info("screen capture without embedding, and the out file: %s " % out_file)
            self._html('the capture picture is <a href="%s">%s</a>' % (out_file, out_file))
            return ldtp.imagecapture(window_name, out_file, x, y, width, height)
        except LdtpExecutionError:
            raise LdtpExecutionError("image capture failed")

    def object_exist(self, window_name, object_name):
        """
        [关键字概要] 判断窗口是否存在

        :@参数 window_name: 窗口名称

        :@参数 object_name: 对象名称

        :@返回值: 1 on success, 0 on failure

        Examples:

        |  *Test Cases*  |    *Returns*   |        *Action*       |    *Argument*   |    *Argument*   |
        |  Example_Test  |   @{return}=   |      Object Exist     |  ${window_name} |  ${object_name} |


        """
        try:
            self._info("object exist :(%s, %s)" % (window_name, object_name))
            return ldtp.objectexist(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("objectexist failed")

    def check(self, window_name, object_name):
        """
        Check item.

        :param window_name:

        :param object_name:

        :return:
        """
        try:
            self._info("check item (%s, %s)" % (window_name, object_name))
            return ldtp.check(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("check item failed")

    def uncheck(self, window_name, object_name):
        """
        Uncheck item.

        :param window_name:

        :param object_name:

        :return:
        """
        try:
            self._info("uncheck item (%s, %s)" % (window_name, object_name))
            return ldtp.uncheck(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("uncheck item failed")

    def verify_check(self, window_name, object_name):
        """
        Verify check items

        :param window_name:

        :param object_name:

        :return:
        """
        try:
            self._info("verify check items")
            return ldtp.verifycheck(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("verify check items failed")

    def verify_uncheck(self, window_name, object_name):
        """
        Verify uncheck items

        :param window_name:

        :param object_name:

        :return:
        """
        try:
            self._info("verify uncheck items")
            return ldtp.verifyuncheck(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("verify uncheck items failed")
			
    def select_panel(self, window_name, object_name, index):
        """
        Select panel based on index.

        :param window_name:

        :param object_name:

        :param index:

        :return:
        """
        try:
            self._info("select panel based on index")
            return ldtp.selectpanel(window_name, object_name, index)
        except LdtpExecutionError:
            raise LdtpExecutionError("select panel based on index failed")

    def menu_check(self, window_name, object_name):
        """
        Check(click) a menu item.

        :param window_name:

        :param object_name:

        :return:
        """
        try:
            self._info("check a menu item")
            return ldtp.menucheck(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("check a menu item failed")

    def menu_uncheck(self, window_name, object_name):
        """
        Uncheck(click) a menu item.

        :param window_name:

        :param object_name:

        :return:
        """
        try:
            self._info("uncheck a menu item")
            return ldtp.menuuncheck(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("uncheck a menu item failed")

    def verify_menu_check(self, window_name, object_name):
        """
        Verify whether a menu is checked or not.

        :param window_name:

        :param object_name:

        :return:
        """
        try:
            self._info("verify a menu item is checked (%s, %s)" % (window_name, object_name))
            return ldtp.verifymenucheck(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("verify a menu item is checked failed")

    def verify_menu_uncheck(self, window_name, object_name):
        """
        Verify whether a menu is unchecked or checked.

        :param window_name:

        :param object_name:

        :return:
        """
        try:
            self._info("verify a menu item is unchecked (%s, %s)" % (window_name, object_name))
            result = ldtp.verifymenuuncheck(window_name, object_name)
            print (result)
            return result
        except LdtpExecutionError:
            raise LdtpExecutionError("verify a menu item is unchecked failed")

    def get_object_property(self, window_name, object_name, property_name):
        """
        [关键字概要] 获取一个对象的属性值

        :@参数 window_name: 窗口名称

        :@参数 object_name: 对象名称

        :@参数 property_name: 属性名称

        :@返回值: 属性值字符串

        Examples:

        |  *Test Cases*  |      *Returns*     |   *Action*       |    *Argument*   |    *Argument*   | *Argument* |
        |  Example_Test  | ${property_value}= | Get Object Property | ${window_name} |  ${object_name} | ${prop_name} |

        """
        try:
            self._info("Get object property value (%s, %s, %s)" % (window_name, object_name, property_name))
            return ldtp.getobjectproperty(window_name, object_name, property_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("get object property failed")

    def double_click(self, window_name, object_name):
        """
        [Description] Double clicks the row in table whose first column's(0th column) value
        is same as the contents of the third argument in the function call.

        :@参数 window_name:

        :@参数 object_name:

        :@返回值: 1 on success, else 0

        Examples:

        |  *Test Cases*  |      *Returns*     |    *Action*      |    *Argument*   |    *Argument*   |
        |  Example_Test  |    ${exec_status}= |   Double Click   |  ${window_name} |  ${object_name} |

        """
        try:
            self._info("double click the mouse")
            return ldtp.doubleclick(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("Double Click failed")

    def get_all_states(self, window_name, object_name):
        """
        [关键字概要] 获取指定对象的所有状态

        :@参数 window_name: 窗口名称

        :@参数 object_name: 对象名称

        :@返回值: 状态列表

        Examples:

        |  *Test Cases*  |      *Returns*     |    *Action*      |    *Argument*   |    *Argument*   |
        |  Example_Test  |    @{states_list}= |  Get All States  |  ${window_name} |  ${object_name} |

        """
        try:
            self._info("Get all states of given object (%s, %s)" % (window_name, object_name))
            return ldtp.getallstates(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError("get all states failed")

    def state_enabled(self, window_name, component_name):
        """
        [关键字概要] Checks the radio button object state enabled or not

        :param window_name: 窗口名称

        :param component_name: 组件名称

        :return: 1 if state is enabled, else 0.

        """
        try:
            self._info('state enabled of given component (%s, %s)' % (window_name, component_name))
            return ldtp.stateenabled(window_name, component_name)
        except LdtpExecutionError:
            raise LdtpExecutionError('state enabled failed.')

    def menu_item_enabled(self, window_name, menu_item):
        """
        [关键字概要] Verify whether a menu is enabled or not

        :param window_name: 窗口名称

        :param menu_item: 菜单名

        :return: 1 on success, 0 on failure
        """
        try:
            self._info('menu item enabled of given menu item (%s, %s)' % (window_name, menu_item))
            return ldtp.menuitemenabled(window_name, menu_item)
        except LdtpExecutionError:
            raise LdtpExecutionError("menu item enabled failed.")

    def combo_select(self, window_name, component_name, item_name):
        """
        [关键字概要] Select a menu item or list item in a combo box based on name

        :param window_name: 窗口名称

        :param component_name: 组件名称

        :param item_name: menu item or list item

        :return: 1 on success, LdtpExecutionError exception on failure
        """
        try:
            self._info('combo select (%s, %s, %s)' % (window_name, component_name, item_name))
            return ldtp.comboselect(window_name, component_name, item_name)
        except LdtpExecutionError:
            raise LdtpExecutionError('combo select failed.')

    def select_tab(self, window_name, tab_list_name, tab_name):
        """
        Select the given tab name in the tab list
        :param window_name:

        :param tab_list_name:

        :param tab_name:

        :return:1 if the tab is selected, otherwise LdtpExecutionError will be thrown

        """
        try:
            self._info('select tab (%s, %s, %s)' % (window_name, tab_list_name, tab_name))
            return ldtp.selecttab(window_name, tab_list_name, tab_name)
        except LdtpExecutionError:
            raise LdtpExecutionError('select tab failed.')

    def select_tab_index(self, window_name, tab_list_name, tab_index):
        """
        Select the given tab name in the tab list

        :param window_name:

        :param tab_list_name:

        :param tab_index:

        :return:1 if the tab is selected, otherwise LdtpExecutionError will be thrown

        """
        try:
            self._info('select tab index(%s, %s, %s)' % (window_name, tab_list_name, tab_index))
            return ldtp.selecttabindex(window_name, tab_list_name, int(tab_index))
        except LdtpExecutionError:
            raise LdtpExecutionError('select tab index failed.')

    def set_value(self, window_name, spin_button_name, value):
        """
        Sets the value of the spin button.

        :param window_name:

        :param spin_button_name:

        :param value:

        :return: 1 on success, else LdtpExecutionError exception

        """
        try:
            self._info('set value (%s, %s, %s)' % (window_name, spin_button_name, value))
            return ldtp.setvalue(window_name, spin_button_name, value)
        except LdtpExecutionError:
            raise LdtpExecutionError('set value failed.')

    def get_value(self, window_name, spin_button_name):
        """
        Gets the value in the spin button.

        :param window_name:

        :param spin_button_name:

        :return: value in the spin button on success, else LdtpExecutionError exception

        """
        try:
            self._info("get value of (%s, %s)" % (window_name, spin_button_name))
            return ldtp.getvalue(window_name, spin_button_name)
        except LdtpExecutionError:
            raise LdtpExecutionError('get value failed.')

    def get_object_size(self, window_name, object_name=None):
        """
        Get the object size, of the given window. If object does not exist, then LdtpExecutionError will be thrown.

        :param window_name:

        :param object_name:

        :return: [x,y,width,height] as a list and as int type will be returned on success, LdtpExecutionError exception on failure

        """
        try:
            self._info('get object size of (%s, %s)' % (window_name, object_name))
            return ldtp.getobjectsize(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError('get object size failed.')

    def has_state(self, window_name, object_name, state, gui_time_out=0):
        """
        has state

        @param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type object_name: string

        @param state: State of the current object.

        @type object_name: string

        @param gui_time_out: Wait timeout in seconds

        @type gui_time_out: integer

        @return: 1 on success.

        @rtype: integer
        """
        try:
            self._info('(%s,%s) has state (%s) or not.' % (window_name, object_name, state))
            return ldtp.hasstate(window_name, object_name, state, gui_time_out)
        except LdtpExecutionError:
            raise LdtpExecutionError('has state failed.')

    def grab_focus(self, window_name, object_name):
        """
        Grab focus.

        @param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type object_name: string

        @return: 1 on success.

        @rtype: integer
        """
        try:
            self._info('grab focus (%s, %s)' % (window_name, object_name))
            return ldtp.grabfocus(window_name, object_name)
        except LdtpExecutionError:
            raise LdtpExecutionError('grab focus object failed.')

    def remap(self, window_name):
        """
        We can handle dynamically created widgets(meaning widgets created at run time) using this remap function.
        Calling remap will generate appmap for the given dialog at run time and update the hash table.
        Then we can access the new widgets. But please make sure to call undoremap() once the required functions are
        performed so that the hash table will be reverted back to its original state. The reason for having undoremap()
        is that subsequent calls to remap() might corrupt the hash table containg the appmap entries.

        Please not that the <application-name> should be same as the one given as the commmand-line argument
         for appmap generation.

        :param window_name: 窗口名称

        :return:

        """
        try:
            self._info('remap (%s)' % window_name)
            return ldtp.remap(window_name)
        except LdtpExecutionError as e:
            self._debug(e.message)
            raise LdtpExecutionError('remap failed.')

    def wait(self, timeout=5):
        """
        Wait a given amount of seconds.

        @param timeout: Wait timeout in seconds

        @type timeout: double

        @return: 1

        @rtype: integer
        """
        try:
            self._info('wait ' + timeout)
            return ldtp.wait(timeout)
        except LdtpExecutionError:
            raise LdtpExecutionError('wait exec failed.')

    def generate_mouse_event(self, x, y, eventType='b1c'):
        """
        Generate mouse event on x, y co-ordinates.
        Used SPI_generateMouseEvent to generate the mouse events.

        @param x: X co-ordinate
        @type x: int
        @param y: Y co-ordinate
        @type y: int
        @param eventType: Mouse click type
        @type eventType: string

        @return: 1 on success.
        @rtype: integer
        """
        try:
            self._info("generate mouse event (%s) at point (%d, %d)" % (eventType, x, y))
            return ldtp.generatemouseevent(int(x), int(y), eventType)
        except LdtpError:
            raise LdtpError('generate mouse event failed, please check the parameters.')

    def generate_key_event(self, data):
        """
        Functionality of generatekeyevent is similar to typekey of LTFX project.
        Used SPI_generateKeyboardEvent to generate the keyboard events.

        :param data:

        :return: Returns 1 on success, LdtpExecutionError exception will be thrown on failure
        """
        try:
            self._info("generate key event with <%s>" % data)
            return ldtp.generatekeyevent(data)
        except LdtpExecutionError as e:
            print (e.message)
            raise LdtpExecutionError

    def get_window_list(self):
        """
        Gets all the window name, that are currently opened. If none of the windows are opened, then LdtpExecutionError
         will be thrown.

        :return: windows list
        """
        try:
            self._info("get window list ")
            return ldtp.getwindowlist()
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def get_object_list(self, window_name):
        """
        Get list of items in given GUI.

        @param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @return: list of items in LDTP naming convention.

        @rtype: list
        """
        try:
            self._info("get object list of (%s)" % window_name)
            return ldtp.getobjectlist(window_name)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def get_object_name_at_coords(self, wait=5):
        """
        Get object name at the mouse coordinates

        :param wait:

        :return: 1on success, 0 on failure

        """
        try:
            self._info("get object name at the mouse coordinates ")
            return ldtp.getobjectnameatcoords(wait)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def mouse_left_click(self, window_name, object_name):
        """
        Mouse left click on an object.

        @param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to look for, either full name,
        LDTP's name convention, or a Unix glob. Or menu heirarchy

        @type object_name: string

        @return: 1 on success.

        @rtype: integer
        """
        try:
            self._info("Mouse left click on an object")
            return ldtp.mouseleftclick(window_name, object_name)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def mouse_right_click(self, window_name, object_name):
        """
        Mouse right click on an object.

        @param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to look for, either full name,
        LDTP's name convention, or a Unix glob. Or menu heirarchy

        @type object_name: string

        @return: 1 on success.

        @rtype: integer
        """
        try:
            self._info("Mouse right click on an object")
            return ldtp.mouserightclick(window_name, object_name)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def mouse_move(self, window_name, object_name):
        """
        Mouse move on an object.

        @param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to look for, either full name,
        LDTP's name convention, or a Unix glob. Or menu heirarchy

        @type object_name: string

        @return: 1 on success.

        @rtype: integer
        """
        try:
            self._info("Mouse move on object (%s) " % object_name)
            return ldtp.mousemove(window_name, object_name)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def simulate_mouse_move(self, source_x, source_y, dest_x, dest_y, delay=0.0):
        """
        @param source_x: Source X

        @type source_x: integer

        @param source_y: Source Y

        @type source_y: integer

        @param dest_x: Dest X

        @type dest_x: integer

        @param dest_y: Dest Y

        @type dest_y: integer

        @param delay: Sleep time between the mouse move

        @type delay: double

        @return: 1 if simulation was successful, 0 if not.

        @rtype: integer
        """
        try:
            self._info("simulate mouse move from (%d, %d) to (%d, %d)" % (source_x, source_y, dest_x, dest_y))
            return ldtp.simulatemousemove(source_x, source_y, dest_x, dest_y, delay)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def get_tab_count(self, window_name, object_name):
        """
        Get tab count.

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.

        @type object_name: string

        @return: tab count on success.

        @rtype: integer
        """
        try:
            self._info("Get tab count (%s, %s)" % (window_name, object_name))
            return ldtp.gettabcount(window_name, object_name)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def get_tab_name(self, window_name, object_name, tab_index):
        """
        Get tab name

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.

        @type object_name: string

        @param tab_index: Index of tab (zero based index)

        @type object_name: int

        @return: text on success.

        @rtype: string
        """
        try:
            self._info("get tab name (%s, %s, %d)" % (window_name, object_name, tab_index))
            return ldtp.gettabname(window_name, object_name, tab_index)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def select_index(self, window_name, object_name, item_index):
        """
        Select combo box item / layered pane based on index

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.

        @type object_name: string

        @param item_index: Item index to select

        @type object_name: integer

        @return: 1 on success.

        @rtype: integer
        """
        try:
            self._info("select combo box item or layered pane based on index")
            return ldtp.selectindex(window_name, object_name, item_index)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    # Since selectindex and comboselectindex implementation are same,
    # for backward compatibility let us assign selectindex to comboselectindex
    combo_select_index = select_index

    def select_item(self, window_name, object_name, item_name):
        """
        Select combo box / layered pane item

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.

        @type object_name: string

        @param item_name: Item name to select

        @type object_name: string

        @return: 1 on success.

        @rtype: integer
        """
        try:
            self._info("Select combo box / layered pane item")
            return ldtp.selectitem(window_name, object_name, item_name)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def get_combo_value(self, window_name, object_name):
        """
        Get current selected combobox value

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.

        @type object_name: string

        @return: selected item on success, else LdtpExecutionError on failure.

        @rtype: string
        """
        try:
            self._info("Get current selected combobox value (%s-->%s)" % (window_name, object_name))
            return ldtp.getcombovalue(window_name, object_name)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def verify_select(self, window_name, object_name, item_name):
        """
        Verify the item selected in combo box

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.

        @type object_name: string

        @param item_name: Item name to select

        @type object_name: string

        @return: 1 on success.

        @rtype: integer
        """
        try:
            self._info("Verify the item selected in combo box (%s-->%s[:%s])" % (window_name, object_name, item_name))
            return ldtp.verifyselect(window_name, object_name, item_name)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def verify_statusbar_visible(self, window_name, status_bar_name):
        """
        Checks whether the status bar object is visible or not

        :param window_name: 窗口名称

        :param status_bar_name: 状态栏名称

        :return: 1 on success, 0 on failure
        """
        try:
            self._info("check whether the status bar (%s-->%s) is visible or not" % (window_name, status_bar_name))
            return ldtp.verifystatusbarvisible(window_name, status_bar_name)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def verify_button_count(self, window_name, toolbar_name, count):
        """
        Verifies whether the toolbar button count matches with the argument count. 1 based index.

        :param window_name: 窗口名称

        :param toolbar_name: 工具栏名称

        :param count: button个数

        :return: 1 on success, else 0

        """
        try:
            self._info("Verifies whether the toolbar(%s-->%s) button count matches with the argument count (%d)" %
                       (window_name, toolbar_name, count))
            return ldtp.verifybuttoncount(window_name, toolbar_name, count)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    verify_visible_button_count = verify_button_count

    def does_menu_item_exist(self, window_name, object_name,
                             strict_hierarchy=False):
        """
         Check a menu item exist.

         @param window_name: Window name to look for, either full name,
         LDTP's name convention, or a Unix glob.

         @type window_name: string

         @param object_name: Object name to look for, either full name,
         LDTP's name convention, or a Unix glob. Or menu heirarchy

         @type object_name: string

         @param strict_hierarchy: Mandate menu hierarchy if set to True

         @type object_name: boolean

         @return: 1 on success.

         @rtype: integer
         """
        try:
            self._info("check menu item exist (%s-->%s)" % (window_name, object_name))
            return ldtp.doesmenuitemexist(window_name, object_name, strict_hierarchy)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def list_sub_menus(self, window_name, object_name):
        """
        List children of menu item

        @param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to look for, either full name,
        LDTP's name convention, or a Unix glob. Or menu heirarchy

        @type object_name: string

        @return: menu item in list on success.

        @rtype: list
        """
        try:
            self._info("list children of menu item (%s-->%s)" % (window_name, object_name))
            return ldtp.listsubmenus(window_name, object_name)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def invoke_menu(self, window_name, object_name):
        """
        Invoke menu item.

        @param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type object_name: string

        @return: 1 on success.

        @rtype: integer
        """

        try:
            self._info("Invoke menu item (%s-->%s)" % (window_name, object_name))
            return ldtp.invokemenu(window_name, object_name)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def get_slider_value(self, window_name, object_name):
        """
        Get slider value.

        @param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type object_name: string

        @return: slider value on success.

        @rtype: float
        """

        try:
            self._info("Get slider value (%s, %s)" % (window_name, object_name))
            return ldtp.getslidervalue(window_name, object_name)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def increase(self, window_name, object_name, iterations):
        """
        Increase slider value.

        @param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type object_name: string

        @return: 1 on success.

        @rtype: integer
        """

        try:
            self._info("Increase slider value (%s, %s)" % (window_name, object_name))
            return ldtp.increase(window_name, object_name, iterations)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def decrease(self, window_name, object_name, iterations):
        """
        Decrease slider value.

        @param window_name: Window name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type window_name: string

        @param object_name: Object name to look for, either full name,
        LDTP's name convention, or a Unix glob.

        @type object_name: string

        @return: 1 on success.

        @rtype: integer
        """

        try:
            self._info("Decrease slider value (%s, %s)" % (window_name, object_name))
            return ldtp.decrease(window_name, object_name, iterations)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)
