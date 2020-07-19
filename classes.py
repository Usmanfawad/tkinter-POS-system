class Users:
    users = {}
    def __init__(self,id,username,password):
        self.id       = id
        self.username = username
        self.password = password
        Users.users[self.id]=self

    