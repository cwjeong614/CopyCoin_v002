import telegram
import os

class Telegram_Bot():
    def __init__(self):
        self.tele_token = ''
        self.chat_id = ''

        # 실투:0 / 모투:1 =========================================
        test = 0
        # =======================================================

        f = open('pwd.csv')
        lines = f.readlines()

        if test == 0:       # 실투
            self.tele_token = lines[2].split(',')[-1].rstrip('\n')
        else:
            self.tele_token = lines[4].split(',')[-1].rstrip('\n')

        self.bot = telegram.Bot(token=self.tele_token)

        if self.chat_id == '':
            if os.path.exists('chat_id.txt'):
                with open('chat_id.txt', mode='r') as chatfile:
                    try:
                        self.chat_id = int(chatfile.readline().strip())
                    except Exception as e:
                        pass

        if self.chat_id == '':
            updates = self.bot.getUpdates()
            last_message = None
            for u in updates:
                if u is not None:
                    last_message = u

            if last_message is not None:
                self.chat_id = last_message.message.chat_id
                with open('chat_id.txt', mode='w') as chatfile:
                    chatfile.write('%s' % self.chat_id)

    def send_msg(self, text):
        chat_id = self.chat_id
        self.bot.sendMessage(chat_id=chat_id, text=text)

if __name__ == '__main__':
    Telegram_Bot().__init__()
    Telegram_Bot().send_msg('테스트')