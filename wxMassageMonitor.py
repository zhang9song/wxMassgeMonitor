import time

from pywinauto import application
from pywinauto import findwindows
# Use pywinauto to record WeChat Massages.
# Tencent never to block your account :)
# Time line come soon.

class Monitor():

    def __init__(self, wnd_title):
        '''wnd_title is wechat window that you want to record.
        Please drag it from wechat main window to independent window'''
        hwnid = findwindows.find_window(class_name='ChatWnd', title='参谋二部')
        app = application.Application(backend="uia").connect(handle=hwnid)
        self.win_main_Dialog = self.app.window(class_name='ChatWnd')

    def record_msg(self, freq=1, file_name=None):
        '''freq is record frequency, default is 1 second'''
        msg_file = None
        if file_name:
            msg_file = open(file_name, 'a', encoding='utf8')
        last_msg = ''
        user = ''
        while True:
            user = ''
            msg = ''
            chat_list = self.win_main_Dialog.child_window(control_type='List', title='消息')
            user = chat_list.children()[-1].children()[0].children()[0].window_text()
            if user == '':
                user = '我'
            msg = '%s:%s\n' % (user, chat_list[-1].window_text())
            if last_msg == msg:
                pass
            else:
                last_msg = msg
                if msg_file:
                    msg_file.write(msg)
                print(msg)
            time.sleep(freq)
        msg_file.close()


if '__main__' == __name__:
    monit = Monitor(wnd_title='测试群')
    monit.record_msg(1)
