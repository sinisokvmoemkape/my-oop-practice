import platform
import urllib.request
import socket
def check_connection():
    try:
        urllib.request.urlopen('https://www.google.com/',timeout=3)
        return 'Online'
    except (urllib.request.URLError, socket.timeout):
        return 'Offline'

class user_status:
    user_name = None
    user_platform = None
    user_connection_status = None
    
    def __init__(self,user_name,user_platform,user_connection_status):
        self.user_name = user_name
        self.user_platform = user_platform
        self.user_connection_status = user_connection_status
        
        print(f'''User Name - {self.user_name}
User Use - {self.user_platform}
User is - {self.user_connection_status}''')

user_name_enter = input('Введите имя: ')
user_platform_name = platform.system()
check_connection()
user_status_name = check_connection()
user1 = user_status(user_name_enter, user_platform_name, user_status_name)

