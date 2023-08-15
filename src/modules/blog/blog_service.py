from src.commons import config as c
from src.modules.mega import mega as m

class BlogService:
    def get_many(self):
        mega = m.Mega()
        r = mega.login(email=c.MEGA_NZ_USERNAME, password=c.MEGA_NZ_PASSWORD)
        users = r.get_files()
        print(users)
        return users