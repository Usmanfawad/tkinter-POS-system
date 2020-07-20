from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import tkinter as tk
from classes import *
from PIL import Image
from PIL import ImageTk
import sqlite3
from tkinter import messagebox

class main_interface:
    def __init__(self):
        self.load_data()
        # self.login_screen()
        self.normal_order_screen()



    def load_data(self):
        conn=sqlite3.connect("subway.db")
        u=  conn.cursor()
        u.execute("SELECT * FROM users")
        i=  conn.cursor()
        i.execute("SELECT * FROM items")
        r= conn.cursor()
        r.execute("SELECT * FROM reference_table")
        b = conn.cursor()
        b.execute("SELECT * FROM bill")
        for all in u.fetchall():
            Users(str(all[0]),all[1],all[2])
        for all in i.fetchall():
            Items(str(all[0]),all[1],all[2],all[3])
        for all in r.fetchall():
            Reference_table(str(all[0]),all[1],all[2])
        for all in b.fetchall():
            Bill(str(all[0]))


    def login_screen(self):

        def proceed():
            # self.root.destroy()
            user_name = username.get()
            pass_word = password.get()
            print("Username: ", user_name)
            print("Password: ",pass_word)
            for k,v in Users.users.items():
                try:
                    if v.username.lower() == user_name.lower():
                        if int(v.password) == int(pass_word):
                            self.root.destroy()
                            self.main_screen()
                        else:
                            messagebox.showinfo("Password", "Wrong password")
                            self.root.destroy()
                            self.login_screen()
                            break;
                    else:
                        messagebox.showinfo("Username", "Wrong username")
                        self.root.destroy()
                        self.login_screen()
                except:
                    pass
        #this is the login screen that will be shown each time the user opens this software
        self.root = Tk()
        self._geom='1000x1000+0+0'
        pad = 3
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth()-pad, self.root.winfo_screenheight()-pad))
        self.root.bind('<Escape>',self.toggle_geometry)
            
        canvas = Canvas(self.root, width = 1300 , height = 400)
        canvas.pack()
        img = PhotoImage(file="Subway.png") 
        canvas.create_image(-130,-200, anchor = NW, image= img)
        username = tk.StringVar()
        password = tk.StringVar()
        label_1=Label(self.root,text="Username",font='Helvetica 20 italic',height=2, width=57, fg="black").pack()
        e1     =Entry(self.root,textvariable = username,width = 30).pack()
        label_2=Label(self.root,text="Password",font='Helvetica 20 italic',height=2, width=57, fg="black").pack()
        e2     =Entry(self.root,textvariable = password,show = "*",width = 30).pack()
        Button(self.root, text="Login",command = proceed, height=2, width=10, bg="#015643", fg="white").pack()
        self.root.mainloop()


    def toggle_geometry(self,event):
        #the escape key is bind to this function, exits full screen 
        geom = self.root.winfo_geometry()
        self.root.geometry(self._geom)
        self._geom=geom

    def main_screen(self):
        
        def logout():
            messagebox.showinfo("Logout","You have been logged out!")
            self.main.destroy()
            self.login_screen()

        def main_order():
            self.main.destroy()
            self.normal_order_screen()

        def custom_order():
            self.main.destroy()
            self.custom_order_screen()
            
        self.main = Tk()
        self.main.geometry("500x500")
        self.main.configure(background = '#015643')
        button_1 = Button(self.main, font='Helvetica 30 italic', text="Normal Order",command = main_order, height=4, width=500, bg="#fec90a", fg="#015643").pack()
        button_2 = Button(self.main, font='Helvetica 30 italic', text="Custom Order",command = custom_order, height=4, width=500, bg="#fec90a", fg="#015643").pack()
        button_3 = Button(self.main, font='Helvetica 30 italic', text="Logout",command = logout, height=2, width=500, bg="#015643", fg="#fec90a").pack()
        self.main.mainloop()
        
    def custom_order_screen(self):
        self.load_data()
        #creating a bill object
        self.bill = Bill.create_bill()
        self.bill_id = self.bill[1]
        self.bill_items = []
        self.order = Tk()
        self._geom='1000x500+0+0'
        self.order.configure(background = '#015643')
        self.order.resizable(0,0)
        #fec90a
        pad = 3
        self.order.geometry("{0}x{1}+0+0".format(self.order.winfo_screenwidth()-pad, self.order.winfo_screenheight()-pad))
        width = 250
        height = 150
        Label(self.order,font='Helvetica 20 italic', text=" ",height=2, width=100, bg="#fec90a", fg="#015643").place(x=0,y=20)
        Label(self.order,font='Helvetica 20 italic', text="CUSTOM ORDER",height=2, width=15, bg="#fec90a", fg="#015643").place(x=15,y=20)
        def view_cart():
            pass
        def back():
            try:
                self.order.destroy()
                self.main_screen()
            except:
                pass
    
        def logout():
            try:
                self.order.destroy()
                self.login_screen()
            except:
                pass
        img = Image.open("drinks.png")
        img = img.resize((250,150), Image.ANTIALIAS)
        img_11 =  ImageTk.PhotoImage(img)   
        img = Image.open("10.png")
        img = img.resize((120,62), Image.ANTIALIAS)
        img_10 =  ImageTk.PhotoImage(img)        
        
        self.custom_counter = 0
        self.custom_total = 0
        self.custom_cart = {}

        def details_item_10():
            # item_id     = "9"
            # item_name   = Items.items[item_id].item_name
            # item_price  = Items.items[item_id].price
            def add_to_cart():
                self.load_data()
                # Reference_table.create_reference_table_object(self.bill_id,item_id)
                quantity_item   = quantity.get()
                size_item       = size.get()
                drink_item      = drink.get()
                if size_item.lower() == "small":
                    self.custom_total += 100*int(quantity_item)
                elif size_item.lower() == "medium":
                    self.custom_total += 150*int(quantity_item)
                else:
                    self.custom_total += 200*int(quantity_item)
                self.custom_cart[str(self.counter)]= [quantity_item,size_item,drink_item]
                self.custom_counter+=1
                details.destroy()
            details = Tk()
            details.resizable(0,0)
            details.configure(background = '#015643')
            details.geometry("500x500")
            Label(details,font='Helvetica 9 italic', text="*The prices mentioned are for small items, 50 rs increase in price for larger items",height=1, width=80, bg="red", fg="#015643").pack()
            Label(details,font='Helvetica 20 italic', text="Price: 100",height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=30)
            Label(details,font='Helvetica 20 italic', text="Drinks",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=110)
            Label(details,font='Helvetica 20 italic', text="Quantity",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=190)
            quantity    = tk.StringVar(details)
            size        = tk.StringVar(details)
            drink       = tk.StringVar(details)
            drink.set("Pepsi")
            quantity.set("1")
            drink_entry    = OptionMenu(details,drink,"Pepsi","Dew","Seven Up","Whiskey").place(x= 290,y=110,height = 50)
            quantity_entry = OptionMenu(details,quantity,"1","2","3","4","5","6","7","8","9","10").place(x= 290,y=200,height = 50)
            Label(details,font='Helvetica 20 italic', text="Size",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=270)
            size.set("Small")
            w = OptionMenu(details, size, "Small", "Medium", "Large").place(x=290,y=290)
            Button(details, font='Helvetica 30 italic', text="Add to cart",command = add_to_cart, height=1, width=20, bg="#015643", fg="#fec90a").place(x=10,y=350)
            details.mainloop()

        # one     = Button(self.order,image = img_10, command = view_cart).place(x=200,y=20)
        Label(self.order,font='Helvetica 20 italic', text="Add drink",height=2, width=13, bg="#fec90a", fg="#015643").place(x=1100,y=100)
        eleven  = Button(self.order,image = img_11, command = details_item_10).place(x=1080,y=180)
        back    = Button(self.order,font='Helvetica 15 italic', text="Back",command = back, height=2, width=10, bg="#015643", fg="white").place(x=1050,y=21)
        logout  = Button(self.order,font='Helvetica 15 italic', text="Logout",command = logout, height=2, width=10, bg="#015643", fg="white").place(x=1200,y=21)
        

        def get_all_values():
            spice_level = str(v1.get())
            sauce_user  = sauces.get()
            bread_user  = bread.get()
            meat_user   = meat.get()
            veg_user    = veg.get()
            self.custom_cart[str(self.counter)]= [spice_level,sauce_user,bread_user,meat_user,veg_user]
            self.custom_counter+=1
            view_cart_custom()

        def view_cart_custom():
            
            cart = Tk()
            cart.geometry("600x600")
            cart.resizable(0, 0)
            cart.title("Cart")
            window_height = 700
            window_width = 600
            screen_width = cart.winfo_screenwidth()
            screen_height = cart.winfo_screenheight()
            x_cordinate = int((screen_width / 2) - (window_width / 2))
            y_cordinate = int((screen_height / 2) - (window_height / 2))
            cart.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            cart.configure(background='#015643')
            style = ttk.Style()
            style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
            style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
            x = Label(cart, text="CART VIEW", font='Helvetica 18 bold', height=2, width=100, fg="#015643",bg="#fec90a").pack()
            frame = Frame(cart)
            frame.pack()
            tree = ttk.Treeview(frame, columns=(1, 2, 3), height=20, show="headings", style="mystyle.Treeview")
            tree.pack(side='left')
            tree.heading(1, text="Name")
            tree.heading(2, text="Size")
            tree.heading(3, text="Quantity")
            tree.column(1, width=200)
            tree.column(2, width=100)
            tree.column(3, width=100)           
            scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            scroll.pack(side='right', fill='y')
            tree.configure(yscrollcommand=scroll.set)
            for k,v in self.custom_cart.items():
                tree.insert('', 'end', values=(self.custom_cart[k][2],self.custom_cart[k][1],self.custom_cart[k][0]))

            x = Label(cart, text="Total= "+str(self.total), font='Helvetica 18 bold', height=2, width=100, fg="#015643",bg="#fec90a").pack()

            def ExitApplication():
                MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to cancel the order?',icon = 'warning')
                if MsgBox == 'yes':
                    try:
                        cart.destroy()
                        self.order.destroy()
                        self.custom_order_screen()
                    except:
                        pass
                else:
                    cart.destroy()
                    view_cart()
                    pass
                    # tk.messagebox.showinfo('Return','You will now return to the application screen')

            def confirm():
                messagebox.showinfo(title="Order placed", message="Your order has been placed.")
                try:
                    self.order.destroy()
                    cart.destroy()

                except:
                    pass

            confirm_order = Button(cart,font='Helvetica 20 italic', text="Confirm order",command = confirm, height=1, width=20, bg="#015643", fg="#fec90a").pack()
            cancel_order  = Button(cart,font='Helvetica 20 italic', text="Cancel order",command = ExitApplication, height=1, width=20, bg="#015643", fg="#fec90a").pack()

            cart.mainloop()


        v1 = IntVar() 
        def show1():   
            
            if str(v1.get()) == "1":
                sel = "Selected spice level is = " + "Low" 
                l1.config(text = sel, font =("Courier", 14),bg = "#fec90a",fg = "#015643")   
            elif str(v1.get()) == "2":
                sel = "Selected spice level is = " + "Medium" 
                l1.config(text = sel, font =("Courier", 14),bg = "#fec90a",fg = "#015643")
            else:
                sel = "Selected spice level is = " + "High" 
                l1.config(text = sel, font =("Courier", 14),bg = "#fec90a",fg = "#015643")  
        
        s1 = Scale(self.order, variable = v1, from_ = 1, to = 3, orient = HORIZONTAL,bg="#fec90a")
        b1 = Button(self.order, text ="Confirm Spice level",command = show1,bg = "#fec90a",fg = "#015643")
        l1 = Label(self.order) 
        s1.place(x=700,y=100)
        b1.place(x=700,y=150) 
        l1.place(x=550,y=180) 
        

# Here sauces are added inside the variable sauces_entry
        Label(self.order,font='Helvetica 20 italic', text="Choose sauce",height=2, width=14, bg="#fec90a", fg="#015643").place(x=10,y=100)
        sauces    = tk.StringVar(self.order)
        sauces.set("Sauce_1")
        sauces_entry = OptionMenu(self.order,sauces,"Sauce_1","Sauce_2","Sauce_3").place(x= 70,y=180,height = 50)    
# Here Bread are added inside the variable sauces_entry
        Label(self.order,font='Helvetica 20 italic', text="Choose bread",height=2, width=14, bg="#fec90a", fg="#015643").place(x=250,y=100)
        bread    = tk.StringVar(self.order)
        bread.set("Bread_1")
        sauces_entry = OptionMenu(self.order,bread,"Bread","Bread_2","Bread_3").place(x= 310,y=180,height = 50)   
# Here meat are added inside the variable sauces_entry
        Label(self.order,font='Helvetica 20 italic', text="Choose Meat",height=2, width=14, bg="#fec90a", fg="#015643").place(x=10,y=300)
        meat    = tk.StringVar(self.order)
        meat.set("Meat_1")
        sauces_entry = OptionMenu(self.order,meat,"Meat_1","Meat_2","Meat_3").place(x= 70,y=380,height = 50) 
# Here veggies are added inside the variable sauces_entry
        Label(self.order,font='Helvetica 20 italic', text="Choose Vegetable",height=2, width=14, bg="#fec90a", fg="#015643").place(x=250,y=300)
        veg    = tk.StringVar(self.order)
        veg.set("Veggie_1")
        sauces_entry = OptionMenu(self.order,veg,"Veggie_1","Veggie_2","Veggie_3").place(x= 310,y=380,height = 50) 

#Confirm order button
        Button(self.order,font='Helvetica 20 italic',command= get_all_values, text="Confirm order",height=2, width=14, bg="#fec90a", fg="#015643").place(x=650,y=300)

        self.order.mainloop()

    def normal_order_screen(self):
        self.load_data()
        #creating a bill object
        self.bill = Bill.create_bill()
        self.bill_id = self.bill[1]
        self.bill_items = []
        self.order = Tk()
        self._geom='1000x1000+0+0'
        self.order.configure(background = '#015643')
        #fec90a
        pad = 3
        self.order.geometry("{0}x{1}+0+0".format(self.order.winfo_screenwidth()-pad, self.order.winfo_screenheight()-pad))
        width = 250
        height = 150
        img = Image.open("1.png")
        img = img.resize((width,height), Image.ANTIALIAS)
        img_1 =  ImageTk.PhotoImage(img)
        img = Image.open("2.png")
        img = img.resize((width,height), Image.ANTIALIAS)
        img_2 =  ImageTk.PhotoImage(img)
        img = Image.open("3.png")
        img = img.resize((width,height), Image.ANTIALIAS)
        img_3 =  ImageTk.PhotoImage(img)
        img = Image.open("4.png")
        img = img.resize((width,height), Image.ANTIALIAS)
        img_4 =  ImageTk.PhotoImage(img)
        img = Image.open("5.png")
        img = img.resize((width,height), Image.ANTIALIAS)
        img_5 =  ImageTk.PhotoImage(img)
        img = Image.open("6.png")
        img = img.resize((width,height), Image.ANTIALIAS)
        img_6 =  ImageTk.PhotoImage(img)
        img = Image.open("7.png")
        img = img.resize((width,height), Image.ANTIALIAS)
        img_7 =  ImageTk.PhotoImage(img)
        img = Image.open("8.png")
        img = img.resize((width,height), Image.ANTIALIAS)
        img_8 =  ImageTk.PhotoImage(img)
        img = Image.open("9.png")
        img = img.resize((width,height), Image.ANTIALIAS)
        img_9 =  ImageTk.PhotoImage(img)
        img = Image.open("10.png")
        img = img.resize((120,62), Image.ANTIALIAS)
        img_10 =  ImageTk.PhotoImage(img)
        img = Image.open("drinks.png")
        img = img.resize((250,150), Image.ANTIALIAS)
        img_11 =  ImageTk.PhotoImage(img)



        self.total = 0
        self.cart_objs = {}

        def view_cart():
            
            cart = Tk()
            cart.geometry("600x600")
            cart.resizable(0, 0)
            cart.title("Cart")
            window_height = 700
            window_width = 600
            screen_width = cart.winfo_screenwidth()
            screen_height = cart.winfo_screenheight()
            x_cordinate = int((screen_width / 2) - (window_width / 2))
            y_cordinate = int((screen_height / 2) - (window_height / 2))
            cart.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            cart.configure(background='#015643')
            style = ttk.Style()
            style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
            style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
            x = Label(cart, text="CART VIEW", font='Helvetica 18 bold', height=2, width=100, fg="#015643",bg="#fec90a").pack()
            frame = Frame(cart)
            frame.pack()
            tree = ttk.Treeview(frame, columns=(1, 2, 3), height=20, show="headings", style="mystyle.Treeview")
            tree.pack(side='left')
            tree.heading(1, text="Name")
            tree.heading(2, text="Size")
            tree.heading(3, text="Quantity")
            tree.column(1, width=200)
            tree.column(2, width=100)
            tree.column(3, width=100)           
            scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            scroll.pack(side='right', fill='y')
            tree.configure(yscrollcommand=scroll.set)
            for k,v in self.cart_objs.items():
                tree.insert('', 'end', values=(self.cart_objs[k][2],self.cart_objs[k][1],self.cart_objs[k][0]))

            x = Label(cart, text="Total= "+str(self.total), font='Helvetica 18 bold', height=2, width=100, fg="#015643",bg="#fec90a").pack()

            def ExitApplication():
                MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to cancel the order?',icon = 'warning')
                if MsgBox == 'yes':
                    try:
                        cart.destroy()
                        self.order.destroy()
                        self.normal_order_screen()
                    except:
                        pass
                else:
                    cart.destroy()
                    view_cart()
                    pass
                    # tk.messagebox.showinfo('Return','You will now return to the application screen')

            confirm_order = Button(cart,font='Helvetica 20 italic', text="Confirm order",command = None, height=1, width=20, bg="#015643", fg="#fec90a").pack()
            cancel_order  = Button(cart,font='Helvetica 20 italic', text="Cancel order",command = ExitApplication, height=1, width=20, bg="#015643", fg="#fec90a").pack()

            cart.mainloop()
        self.counter= 1

        def details_item_1():
            item_id     = "1"
            item_name   = Items.items[item_id].item_name
            item_price  = Items.items[item_id].price
            def add_to_cart():
                self.load_data()
                Reference_table.create_reference_table_object(self.bill_id,item_id)
                quantity_item   = quantity.get()
                size_item       = size.get()
                if size_item.lower() == "small":
                    self.total += (int(item_price)*int(quantity_item))
                elif size_item.lower() == "medium":
                    self.total+= 100 + (int(item_price)*int(quantity_item))
                else:
                    self.total+= 200 + (int(item_price)*(quantity_item))
                self.cart_objs[str(self.counter)]= [quantity_item,size_item,item_name]
                self.counter+=1
                details.destroy()
            details = Tk()
            details.resizable(0,0)
            details.configure(background = '#015643')
            details.geometry("500x500")
            Label(details,font='Helvetica 9 italic', text="*The prices mentioned are for small items, 100 rs increase in price for larger items",height=1, width=80, bg="red", fg="#015643").pack()
            Label(details,font='Helvetica 20 italic', text="Price: "+str(item_price),height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=30)
            Label(details,font='Helvetica 20 italic', text=item_name,height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=110)
            Label(details,font='Helvetica 20 italic', text="Quantity",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=190)
            quantity    = tk.StringVar(details)
            size        = tk.StringVar(details)
            quantity.set("1")
            quantity_entry = OptionMenu(details,quantity,"1","2","3","4","5","6","7","8","9","10").place(x= 290,y=200,height = 50)
            Label(details,font='Helvetica 20 italic', text="Size",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=270)
            size.set("Small")
            w = OptionMenu(details, size, "Small", "Medium", "Large").place(x=290,y=290)
            Button(details, font='Helvetica 30 italic', text="Add to cart",command = add_to_cart, height=1, width=20, bg="#015643", fg="#fec90a").place(x=10,y=350)
            details.mainloop()


            
        def details_item_2():
            item_id     = "2"
            item_name   = Items.items[item_id].item_name
            item_price  = Items.items[item_id].price
            def add_to_cart():
                self.load_data()
                Reference_table.create_reference_table_object(self.bill_id,item_id)
                quantity_item   = quantity.get()
                size_item       = size.get()
                if size_item.lower() == "small":
                    self.total += (int(item_price)*int(quantity_item))
                elif size_item.lower() == "medium":
                    self.total+= 100 + (int(item_price)*int(quantity_item))
                else:
                    self.total+= 200 + (int(item_price)*(int(quantity_item)))
                self.cart_objs[str(self.counter)]= [quantity_item,size_item,item_name]
                self.counter+=1
                details.destroy()
            details = Tk()
            details.resizable(0,0)
            details.configure(background = '#015643')
            details.geometry("500x500")
            Label(details,font='Helvetica 9 italic', text="*The prices mentioned are for small items, 100 rs increase in price for larger items",height=1, width=80, bg="red", fg="#015643").pack()
            Label(details,font='Helvetica 20 italic', text="Price: "+str(item_price),height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=30)
            Label(details,font='Helvetica 20 italic', text=item_name,height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=110)
            Label(details,font='Helvetica 20 italic', text="Quantity",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=190)
            quantity    = tk.StringVar(details)
            size        = tk.StringVar(details)
            quantity.set("1")
            quantity_entry = OptionMenu(details,quantity,"1","2","3","4","5","6","7","8","9","10").place(x= 290,y=200,height = 50)
            Label(details,font='Helvetica 20 italic', text="Size",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=270)
            size.set("Small")
            w = OptionMenu(details, size, "Small", "Medium", "Large").place(x=290,y=290)
            Button(details, font='Helvetica 30 italic', text="Add to cart",command = add_to_cart, height=1, width=20, bg="#015643", fg="#fec90a").place(x=10,y=350)
            details.mainloop()

        def details_item_3():
            item_id     = "3"
            item_name   = Items.items[item_id].item_name
            item_price  = Items.items[item_id].price
            def add_to_cart():
                self.load_data()
                Reference_table.create_reference_table_object(self.bill_id,item_id)
                quantity_item   = quantity.get()
                size_item       = size.get()
                if size_item.lower() == "small":
                    self.total += (int(item_price)*int(quantity_item))
                elif size_item.lower() == "medium":
                    self.total+= 100 + (int(item_price)*int(quantity_item))
                else:
                    self.total+= 200 + (int(item_price)*(int(quantity_item)))
                self.cart_objs[str(self.counter)]= [quantity_item,size_item,item_name]
                self.counter+=1
                details.destroy()
            details = Tk()
            details.resizable(0,0)
            details.configure(background = '#015643')
            details.geometry("500x500")
            Label(details,font='Helvetica 9 italic', text="*The prices mentioned are for small items, 100 rs increase in price for larger items",height=1, width=80, bg="red", fg="#015643").pack()
            Label(details,font='Helvetica 20 italic', text="Price: "+str(item_price),height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=30)
            Label(details,font='Helvetica 20 italic', text=item_name,height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=110)
            Label(details,font='Helvetica 20 italic', text="Quantity",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=190)
            quantity    = tk.StringVar(details)
            size        = tk.StringVar(details)
            quantity.set("1")
            quantity_entry = OptionMenu(details,quantity,"1","2","3","4","5","6","7","8","9","10").place(x= 290,y=200,height = 50)
            Label(details,font='Helvetica 20 italic', text="Size",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=270)
            size.set("Small")
            w = OptionMenu(details, size, "Small", "Medium", "Large").place(x=290,y=290)
            Button(details, font='Helvetica 30 italic', text="Add to cart",command = add_to_cart, height=1, width=20, bg="#015643", fg="#fec90a").place(x=10,y=350)
            details.mainloop()

        def details_item_4():
            item_id     = "4"
            item_name   = Items.items[item_id].item_name
            item_price  = Items.items[item_id].price
            def add_to_cart():
                self.load_data()
                Reference_table.create_reference_table_object(self.bill_id,item_id)
                quantity_item   = quantity.get()
                size_item       = size.get()
                if size_item.lower() == "small":
                    self.total += (int(item_price)*int(quantity_item))
                elif size_item.lower() == "medium":
                    self.total+= 100 + (int(item_price)*int(quantity_item))
                else:
                    self.total+= 200 + (int(item_price)*(int(quantity_item)))
                self.cart_objs[str(self.counter)]= [quantity_item,size_item,item_name]
                self.counter+=1
                details.destroy()
            details = Tk()
            details.resizable(0,0)
            details.configure(background = '#015643')
            details.geometry("500x500")
            Label(details,font='Helvetica 9 italic', text="*The prices mentioned are for small items, 100 rs increase in price for larger items",height=1, width=80, bg="red", fg="#015643").pack()
            Label(details,font='Helvetica 20 italic', text="Price: "+str(item_price),height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=30)
            Label(details,font='Helvetica 20 italic', text=item_name,height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=110)
            Label(details,font='Helvetica 20 italic', text="Quantity",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=190)
            quantity    = tk.StringVar(details)
            size        = tk.StringVar(details)
            quantity.set("1")
            quantity_entry = OptionMenu(details,quantity,"1","2","3","4","5","6","7","8","9","10").place(x= 290,y=200,height = 50)
            Label(details,font='Helvetica 20 italic', text="Size",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=270)
            size.set("Small")
            w = OptionMenu(details, size, "Small", "Medium", "Large").place(x=290,y=290)
            Button(details, font='Helvetica 30 italic', text="Add to cart",command = add_to_cart, height=1, width=20, bg="#015643", fg="#fec90a").place(x=10,y=350)
            details.mainloop()

        def details_item_5():
            item_id     = "5"
            item_name   = Items.items[item_id].item_name
            item_price  = Items.items[item_id].price
            def add_to_cart():
                self.load_data()
                Reference_table.create_reference_table_object(self.bill_id,item_id)
                quantity_item   = quantity.get()
                size_item       = size.get()
                if size_item.lower() == "small":
                    self.total += (int(item_price)*int(quantity_item))
                elif size_item.lower() == "medium":
                    self.total+= 100 + (int(item_price)*int(quantity_item))
                else:
                    self.total+= 200 + (int(item_price)*(int(quantity_item)))
                self.cart_objs[str(self.counter)]= [quantity_item,size_item,item_name]
                self.counter+=1
                details.destroy()
            details = Tk()
            details.resizable(0,0)
            details.configure(background = '#015643')
            details.geometry("500x500")
            Label(details,font='Helvetica 9 italic', text="*The prices mentioned are for small items, 100 rs increase in price for larger items",height=1, width=80, bg="red", fg="#015643").pack()
            Label(details,font='Helvetica 20 italic', text="Price: "+str(item_price),height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=30)
            Label(details,font='Helvetica 20 italic', text=item_name,height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=110)
            Label(details,font='Helvetica 20 italic', text="Quantity",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=190)
            quantity    = tk.StringVar(details)
            size        = tk.StringVar(details)
            quantity.set("1")
            quantity_entry = OptionMenu(details,quantity,"1","2","3","4","5","6","7","8","9","10").place(x= 290,y=200,height = 50)
            Label(details,font='Helvetica 20 italic', text="Size",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=270)
            size.set("Small")
            w = OptionMenu(details, size, "Small", "Medium", "Large").place(x=290,y=290)
            Button(details, font='Helvetica 30 italic', text="Add to cart",command = add_to_cart, height=1, width=20, bg="#015643", fg="#fec90a").place(x=10,y=350)
            details.mainloop()

        def details_item_6():
            item_id     = "6"
            item_name   = Items.items[item_id].item_name
            item_price  = Items.items[item_id].price
            def add_to_cart():
                self.load_data()
                Reference_table.create_reference_table_object(self.bill_id,item_id)
                quantity_item   = quantity.get()
                size_item       = size.get()
                if size_item.lower() == "small":
                    self.total += (int(item_price)*int(quantity_item))
                elif size_item.lower() == "medium":
                    self.total+= 100 + (int(item_price)*int(quantity_item))
                else:
                    self.total+= 200 + (int(item_price)*(int(quantity_item)))
                self.cart_objs[str(self.counter)]= [quantity_item,size_item,item_name]
                self.counter+=1
                details.destroy()
            details = Tk()
            details.resizable(0,0)
            details.configure(background = '#015643')
            details.geometry("500x500")
            Label(details,font='Helvetica 9 italic', text="*The prices mentioned are for small items, 100 rs increase in price for larger items",height=1, width=80, bg="red", fg="#015643").pack()
            Label(details,font='Helvetica 20 italic', text="Price: "+str(item_price),height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=30)
            Label(details,font='Helvetica 20 italic', text=item_name,height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=110)
            Label(details,font='Helvetica 20 italic', text="Quantity",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=190)
            quantity    = tk.StringVar(details)
            size        = tk.StringVar(details)
            quantity.set("1")
            quantity_entry = OptionMenu(details,quantity,"1","2","3","4","5","6","7","8","9","10").place(x= 290,y=200,height = 50)
            Label(details,font='Helvetica 20 italic', text="Size",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=270)
            size.set("Small")
            w = OptionMenu(details, size, "Small", "Medium", "Large").place(x=290,y=290)
            Button(details, font='Helvetica 30 italic', text="Add to cart",command = add_to_cart, height=1, width=20, bg="#015643", fg="#fec90a").place(x=10,y=350)
            details.mainloop()

        def details_item_7():
            item_id     = "7"
            item_name   = Items.items[item_id].item_name
            item_price  = Items.items[item_id].price
            def add_to_cart():
                self.load_data()
                Reference_table.create_reference_table_object(self.bill_id,item_id)
                quantity_item   = quantity.get()
                size_item       = size.get()
                if size_item.lower() == "small":
                    self.total += (int(item_price)*int(quantity_item))
                elif size_item.lower() == "medium":
                    self.total+= 100 + (int(item_price)*int(quantity_item))
                else:
                    self.total+= 200 + (int(item_price)*(int(quantity_item)))
                self.cart_objs[str(self.counter)]= [quantity_item,size_item,item_name]
                self.counter+=1
                details.destroy()
            details = Tk()
            details.resizable(0,0)
            details.configure(background = '#015643')
            details.geometry("500x500")
            Label(details,font='Helvetica 9 italic', text="*The prices mentioned are for small items, 100 rs increase in price for larger items",height=1, width=80, bg="red", fg="#015643").pack()
            Label(details,font='Helvetica 20 italic', text="Price: "+str(item_price),height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=30)
            Label(details,font='Helvetica 20 italic', text=item_name,height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=110)
            Label(details,font='Helvetica 20 italic', text="Quantity",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=190)
            quantity    = tk.StringVar(details)
            size        = tk.StringVar(details)
            quantity.set("1")
            quantity_entry = OptionMenu(details,quantity,"1","2","3","4","5","6","7","8","9","10").place(x= 290,y=200,height = 50)
            Label(details,font='Helvetica 20 italic', text="Size",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=270)
            size.set("Small")
            w = OptionMenu(details, size, "Small", "Medium", "Large").place(x=290,y=290)
            Button(details, font='Helvetica 30 italic', text="Add to cart",command = add_to_cart, height=1, width=20, bg="#015643", fg="#fec90a").place(x=10,y=350)
            details.mainloop()

        def details_item_8():
            item_id     = "8"
            item_name   = Items.items[item_id].item_name
            item_price  = Items.items[item_id].price
            def add_to_cart():
                self.load_data()
                Reference_table.create_reference_table_object(self.bill_id,item_id)
                quantity_item   = quantity.get()
                size_item       = size.get()
                if size_item.lower() == "small":
                    self.total += (int(item_price)*int(quantity_item))
                elif size_item.lower() == "medium":
                    self.total+= 100 + (int(item_price)*int(quantity_item))
                else:
                    self.total+= 200 + (int(item_price)*(int(quantity_item)))
                self.cart_objs[str(self.counter)]= [quantity_item,size_item,item_name]
                self.counter+=1
                details.destroy()
            details = Tk()
            details.resizable(0,0)
            details.configure(background = '#015643')
            details.geometry("500x500")
            Label(details,font='Helvetica 9 italic', text="*The prices mentioned are for small items, 100 rs increase in price for larger items",height=1, width=80, bg="red", fg="#015643").pack()
            Label(details,font='Helvetica 20 italic', text="Price: "+str(item_price),height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=30)
            Label(details,font='Helvetica 20 italic', text=item_name,height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=110)
            Label(details,font='Helvetica 20 italic', text="Quantity",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=190)
            quantity    = tk.StringVar(details)
            size        = tk.StringVar(details)
            quantity.set("1")
            quantity_entry = OptionMenu(details,quantity,"1","2","3","4","5","6","7","8","9","10").place(x= 290,y=200,height = 50)
            Label(details,font='Helvetica 20 italic', text="Size",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=270)
            size.set("Small")
            w = OptionMenu(details, size, "Small", "Medium", "Large").place(x=290,y=290)
            Button(details, font='Helvetica 30 italic', text="Add to cart",command = add_to_cart, height=1, width=20, bg="#015643", fg="#fec90a").place(x=10,y=350)
            details.mainloop()


        def details_item_9():
            item_id     = "9"
            item_name   = Items.items[item_id].item_name
            item_price  = Items.items[item_id].price
            def add_to_cart():
                self.load_data()
                Reference_table.create_reference_table_object(self.bill_id,item_id)
                quantity_item   = quantity.get()
                size_item       = size.get()
                if size_item.lower() == "small":
                    self.total += (int(item_price)*int(quantity_item))
                elif size_item.lower() == "medium":
                    self.total+= 100 + (int(item_price)*int(quantity_item))
                else:
                    self.total+= 200 + (int(item_price)*(int(quantity_item)))
                self.cart_objs[str(self.counter)]= [quantity_item,size_item,item_name]
                self.counter+=1
                details.destroy()
            details = Tk()
            details.resizable(0,0)
            details.configure(background = '#015643')
            details.geometry("500x500")
            Label(details,font='Helvetica 9 italic', text="*The prices mentioned are for small items, 100 rs increase in price for larger items",height=1, width=80, bg="red", fg="#015643").pack()
            Label(details,font='Helvetica 20 italic', text="Price: "+str(item_price),height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=30)
            Label(details,font='Helvetica 20 italic', text=item_name,height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=110)
            Label(details,font='Helvetica 20 italic', text="Quantity",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=190)
            quantity    = tk.StringVar(details)
            size        = tk.StringVar(details)
            quantity.set("1")
            quantity_entry = OptionMenu(details,quantity,"1","2","3","4","5","6","7","8","9","10").place(x= 290,y=200,height = 50)
            Label(details,font='Helvetica 20 italic', text="Size",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=270)
            size.set("Small")
            w = OptionMenu(details, size, "Small", "Medium", "Large").place(x=290,y=290)
            Button(details, font='Helvetica 30 italic', text="Add to cart",command = add_to_cart, height=1, width=20, bg="#015643", fg="#fec90a").place(x=10,y=350)
            details.mainloop()

        def details_item_10():
            # item_id     = "9"
            # item_name   = Items.items[item_id].item_name
            # item_price  = Items.items[item_id].price
            def add_to_cart():
                self.load_data()
                # Reference_table.create_reference_table_object(self.bill_id,item_id)
                quantity_item   = quantity.get()
                size_item       = size.get()
                drink_item      = drink.get()
                if size_item.lower() == "small":
                    self.total += 100*int(quantity_item)
                elif size_item.lower() == "medium":
                    self.total += 150*int(quantity_item)
                else:
                    self.total += 200*int(quantity_item)
                self.cart_objs[str(self.counter)]= [quantity_item,size_item,drink_item]
                self.counter+=1
                details.destroy()
            details = Tk()
            details.resizable(0,0)
            details.configure(background = '#015643')
            details.geometry("500x500")
            Label(details,font='Helvetica 9 italic', text="*The prices mentioned are for small items, 50 rs increase in price for larger items",height=1, width=80, bg="red", fg="#015643").pack()
            Label(details,font='Helvetica 20 italic', text="Price: 100",height=2, width=13, bg="#fec90a", fg="#015643").place(x=150,y=30)
            Label(details,font='Helvetica 20 italic', text="Drinks",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=110)
            Label(details,font='Helvetica 20 italic', text="Quantity",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=190)
            quantity    = tk.StringVar(details)
            size        = tk.StringVar(details)
            drink       = tk.StringVar(details)
            drink.set("Pepsi")
            quantity.set("1")
            drink_entry    = OptionMenu(details,drink,"Pepsi","Dew","Seven Up","Whiskey").place(x= 290,y=110,height = 50)
            quantity_entry = OptionMenu(details,quantity,"1","2","3","4","5","6","7","8","9","10").place(x= 290,y=200,height = 50)
            Label(details,font='Helvetica 20 italic', text="Size",height=2, width=13, bg="#fec90a", fg="#015643").place(x=50,y=270)
            size.set("Small")
            w = OptionMenu(details, size, "Small", "Medium", "Large").place(x=290,y=290)
            Button(details, font='Helvetica 30 italic', text="Add to cart",command = add_to_cart, height=1, width=20, bg="#015643", fg="#fec90a").place(x=10,y=350)
            details.mainloop()

        Label()
        one     = Button(self.order,image = img_1,  command = details_item_1).place(x=150,y=100)
        two     = Button(self.order,image = img_2,  command = details_item_2).place(x=450,y=100)
        three   = Button(self.order,image = img_3,  command = details_item_3).place(x=750,y=100)
        four    = Button(self.order,image = img_4,  command = details_item_4).place(x=150,y=300)
        five    = Button(self.order,image = img_5,  command = details_item_5).place(x=450,y=300)
        six     = Button(self.order,image = img_6,  command = details_item_6).place(x=750,y=300)
        seven   = Button(self.order,image = img_7,  command = details_item_7).place(x=150,y=500)
        eight   = Button(self.order,image = img_8,  command = details_item_8).place(x=450,y=500)
        nine    = Button(self.order,image = img_9,  command = details_item_9).place(x=750,y=500)

        def back():
            try:
                self.order.destroy()
                self.main_screen()
            except:
                pass
    
        def logout():
            try:
                self.order.destroy()
                self.login_screen()
            except:
                pass
        
        Label(self.order,font='Helvetica 20 italic', text=" ",height=2, width=100, bg="#fec90a", fg="#015643").place(x=0,y=20)
        Label(self.order,font='Helvetica 20 italic', text="View cart",height=2, width=13, bg="#fec90a", fg="#015643").place(x=10,y=20)
        ten     = Button(self.order,image = img_10, command = view_cart).place(x=200,y=20)
        Label(self.order,font='Helvetica 20 italic', text="Add drink",height=2, width=13, bg="#fec90a", fg="#015643").place(x=1100,y=220)
        eleven  = Button(self.order,image = img_11, command = details_item_10).place(x=1080,y=300)
        back    = Button(self.order,font='Helvetica 15 italic', text="Back",command = back, height=2, width=10, bg="#015643", fg="white").place(x=1050,y=21)
        logout  = Button(self.order,font='Helvetica 15 italic', text="Logout",command = logout, height=2, width=10, bg="#015643", fg="white").place(x=1200,y=21)
        

        self.order.mainloop()


x = main_interface()

#015643
#fec90a