import sqlite3

class Users:
    users = {}
    def __init__(self,id,username,password):
        self.id       = id
        self.username = username
        self.password = password
        Users.users[self.id]=self

    
class Items:
    items = {}
    def __init__(self,id,item_name,item_picture,price):
        self.id                 = id
        self.item_name          = item_name
        self.item_picture       = item_picture
        self.price              = price 
        Items.items[self.id]    = self


class Bill:
    bill= {}
    bill_id    = "B000"
    def __init__(self,id):
        Bill.bill_id    = id
        self.id         = id
        self.total      = 0

    @classmethod
    def create_bill(cls): 
        def assign_id():
            x=list(Bill.bill_id)
            y=x[1]+x[2]+x[3]
            y=int(y)
            y+=1
            if len(str(y))==1:
                y='0'+'0'+str(y)
            elif len(str(y))==2:
                y='0'+str(y)
            f=x[0]+str(y)
            return f
        id= assign_id()
        conn = sqlite3.connect("subway.db")
        d = conn.cursor()
        d.execute("INSERT into bill VALUES(?)",(id,))
        conn.commit()
        conn.close()
        return(cls,id)

class Reference_table:
    reference_table = {}
    reference_id    = "1"
    def __init__(self,id,bill_id,item_id):
        Reference_table.reference_id                = id
        self.id                                     = id
        self.bill_id                                = bill_id
        self.item_id                                = item_id
        Reference_table.reference_table[self.id]    = self

    @classmethod
    def create_reference_table_object(cls,bill_id,item_id):    
        def assign_id():
            x=Reference_table.reference_id
            id = int(x)
            id+=1
            return str(id)
        id = assign_id()
        conn = sqlite3.connect("subway.db")
        d = conn.cursor()
        d.execute("INSERT into reference_table VALUES(?,?,?)",(id,item_id,bill_id))
        conn.commit()
        conn.close()
        return(cls,id,item_id,bill_id)
        

