class Messenger:

    sms_store = [{'text': 'Some text here', 'read': False, 'sender': '073456789'}]

    def __init__(self, fromNumber, messageText):
        self.fromNumber = fromNumber
        self.messageText = messageText
        self.greeting()
        self.prompt()


    def greeting(self, *arg, **kw):
        print('Hello there!')
        print('In your inbox {} messeges, ({} is new)'.format(
            len(self.sms_store), len(list(filter(bool, [not x.get('readed') for x in self.sms_store])))))

    def prompt(self):
        while True:
            command, *args =  input("\nWhat would you like to do?\n> add_sms/read/quit:").split()
            if command == 'quit':
                break
            elif hasattr(self, command):
                getattr(self, command)(*args)
            else:
                print('>>> Wrong command! <<<')

    #Show a list of messages
    def read(self, *arg, **kw):
        print('Messeges:')
        for n, sms in enumerate(self.sms_store):
            print('Num:', n, 'Read:', sms.get('read'), 'sender:', self.fromNumber)
    #see message details and mark as read
    def get(self, sms_num, *arg, **kw):
        if not sms_num or int(sms_num) >= len(self.sms_store):
            print('>>> Wrong msg Number! <<<')
        else:
            sms = self.sms_store[int(sms_num)]
            print(sms.get('text'))
            self.mark_read(int(sms_num))

    def mark_read(self, sms_num, *arg, **kw):
        self.sms_store[sms_num]['read'] = True

    def add_sms(self):
        self.sms_store.append({'text': self.messageText, 'read': False, 'sender': self.fromNumber})
        print('Msg added!')

    def remove_sms(self, sms_num, *arg, **kw):
        if not sms_num or int(sms_num) >= len(self.sms_store):
            print('>>> Wrong msg Number! <<<')
        else:
            self.sms_store.pop(int(sms_num))


if __name__ == "__main__":
    m = Messenger("0612345678", "Hello, There")