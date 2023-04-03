import time
import requests
import json


class TelegramHandler:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def get_url(self, method):
        api_url = "https://api.telegram.org/bot{}/{}".format(
            self.token, method)
        return api_url

    def tg_msg_send(self, msg, mode="QR", QRID=0):
        headers = {"Content-Type": "application/json"}

        if mode == "QR":
            text = "#### 学习强国登录学习\n > ![](" + msg + ")\n > ###### 二维码生成时间" + \
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()
                              ) + "\n > ###### 二维码ID:" + str(QRID)
        elif mode == "link":
            text = "点击打开强国App进行登录\n" + msg
        else:
            text = msg

        data = {
            "chat_id": self.chat_id,
            "text": text,
            "parse_mode": "Markdown"
        }

        try:
            res = requests.post(
                self.get_url("sendMessage"), data=json.dumps(data), headers=headers)
            print("已通过 Telegram 机器人发送成功")
        except Exception as e:
            print("发送失败. 错误信息: " + str(e))
