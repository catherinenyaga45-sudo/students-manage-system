import json
from datetime import datetime

class Logger:
    def __init__(self):
        self.logs = self.load_logs()

    def load_logs(self):
        try:
            with open('data/log.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print('日志文件不存在')
            return {}

    def log(self,message,name = '全班'):
        now = datetime.now()
        self.logs[now.strftime('%Y-%m-%d %H:%M:%S')] = {'name':name, 'message': message}
        with open('data/log.json', 'w', encoding='utf-8') as f:
            json.dump(self.logs, f, ensure_ascii=False, indent=4)

logger = Logger()

