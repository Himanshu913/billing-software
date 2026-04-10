from tkinter import *
import random
import os
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#badc57"
        title = Label(self.root, text="Billing Software", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg=bg_color, fg="Black", relief=GROOVE)
        title.pack(fill=X)

        # ================== Variables =================
        
        self.medical_prices_dict = {
            "sanitizer": 50, "mask": 20, "hand_gloves": 10, "dettol": 30,
            "newsprin": 25, "thermal_gun": 2000, "bandage": 15, "cotton": 5
        }

        self.grocery_prices_dict = {
            "rice": 40, "food_oil": 120, "wheat": 35, "daal": 100,
            "flour": 60, "maggi": 12, "biskit": 20, "salt": 10
        }

        self.cold_prices_dict = {
            "sprite": 40, "limka": 35, "mazza": 45, "coke": 40,
            "fanta": 40, "mountain_duo": 45, "pepsi": 40, "thumsup": 40
        }

        # Medical
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.dettol = IntVar()
        self.newsprin = IntVar()
        self.thermal_gun = IntVar()
        self.bandage = IntVar()
        self.cotton = IntVar()

        # Grocery
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()
        self.biskit = IntVar()
        self.salt = IntVar()

        # Cold Drinks
        self.sprite = IntVar()
        self.limka = IntVar()
        self.mazza = IntVar()
        self.coke = IntVar()
        self.fanta = IntVar()
        self.mountain_duo = IntVar()
        self.pepsi = IntVar()
        self.thumsup = IntVar()

        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()

        # Total product price

        # Customer
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # Tax
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()

        # ================= Customer Details Frame =================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg=bg_color, font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

        # ================= Medical Frame =================
        F2 = LabelFrame(self.root, text="Medical Purpose", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=450)

        items_medical = [("Sanitizer", self.sanitizer), ("Mask", self.mask), ("Hand Gloves", self.hand_gloves),
                         ("Dettol", self.dettol), ("Newsprin", self.newsprin), ("Thermal Gun", self.thermal_gun),
                         ("Bandage", self.bandage), ("Cotton", self.cotton)]

        for i, (name, var) in enumerate(items_medical):
            lbl = Label(F2, text=name, font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
            lbl.grid(row=i, column=0, padx=10, pady=5, sticky='W')
            txt = Entry(F2, width=10, textvariable=var, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
            txt.grid(row=i, column=1, padx=10, pady=5)

        # ================= Grocery Frame =================
        F3 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        items_grocery = [("Rice", self.rice), ("Food Oil", self.food_oil), ("Wheat", self.wheat),
                         ("Daal", self.daal), ("Flour", self.flour), ("Maggi", self.maggi),
                         ("Biskit", self.biskit), ("Salt", self.salt)]

        for i, (name, var) in enumerate(items_grocery):
            lbl = Label(F3, text=name, font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
            lbl.grid(row=i, column=0, padx=10, pady=5, sticky='W')
            txt = Entry(F3, width=10, textvariable=var, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
            txt.grid(row=i, column=1, padx=10, pady=5)

        # ================= Cold Drinks Frame =================
        F4 = LabelFrame(self.root, text="Cold Drinks", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        items_cold = [("Sprite", self.sprite), ("Limka", self.limka), ("Mazza", self.mazza),
                      ("Coke", self.coke), ("Fanta", self.fanta), ("Mountain Duo", self.mountain_duo),
                      ("Pepsi", self.pepsi), ("ThumsUp", self.thumsup)]

        for i, (name, var) in enumerate(items_cold):
            lbl = Label(F4, text=name, font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
            lbl.grid(row=i, column=0, padx=10, pady=5, sticky='W')
            txt = Entry(F4, width=10, textvariable=var, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
            txt.grid(row=i, column=1, padx=10, pady=5)

        # ================= Bill Area =================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ================= Button Frame =================
        F6 = LabelFrame(self.root, text="Bill Menu", font=('times new roman', 14, 'bold'), bd=10, fg="Black", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        # ===== Total Labels =====
        lbl_medical = Label(F6, text="Medical Total", font=('times new roman', 12, 'bold'), bg=bg_color)
        lbl_medical.grid(row=0, column=0, padx=10, pady=5)

        txt_medical = Entry(F6, textvariable=self.medical_price, width=15, font='arial 12', bd=5, relief=GROOVE)
        txt_medical.grid(row=0, column=1, padx=10, pady=5)

        lbl_grocery = Label(F6, text="Grocery Total", font=('times new roman', 12, 'bold'), bg=bg_color)
        lbl_grocery.grid(row=1, column=0, padx=10, pady=5)

        txt_grocery = Entry(F6, textvariable=self.grocery_price, width=15, font='arial 12', bd=5, relief=GROOVE)
        txt_grocery.grid(row=1, column=1, padx=10, pady=5)

        lbl_cold = Label(F6, text="Cold Drinks Total", font=('times new roman', 12, 'bold'), bg=bg_color)
        lbl_cold.grid(row=2, column=0, padx=10, pady=5)

        txt_cold = Entry(F6, textvariable=self.cold_drinks_price, width=15, font='arial 12', bd=5, relief=GROOVE)
        txt_cold.grid(row=2, column=1, padx=10, pady=5)

        # Correct footer (same indentation)
        footer = Label(self.root, text="Made by Himanshu(https://github.com/Himanshu913)", font=('arial', 12, 'bold'), bg="#badc57", fg="black")
        footer.pack(side=BOTTOM)

        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="white", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="white", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)

        self.welcome_bill()

    # ================= Functions =================
    def total(self):
        # Prices
        # Medical total
        self.total_medical = (self.sanitizer.get()*self.medical_prices_dict["sanitizer"] +
                              self.mask.get()*self.medical_prices_dict["mask"] +
                              self.hand_gloves.get()*self.medical_prices_dict["hand_gloves"] +
                              self.dettol.get()*self.medical_prices_dict["dettol"] +
                              self.newsprin.get()*self.medical_prices_dict["newsprin"] +
                              self.thermal_gun.get()*self.medical_prices_dict["thermal_gun"] +
                              self.bandage.get()*self.medical_prices_dict["bandage"] +
                              self.cotton.get()*self.medical_prices_dict["cotton"])
        self.medical_price.set(f"Rs. {self.total_medical}")

        # Grocery total
        self.total_grocery = (self.rice.get()*self.grocery_prices_dict["rice"] +
                              self.food_oil.get()*self.grocery_prices_dict["food_oil"] +
                              self.wheat.get()*self.grocery_prices_dict["wheat"] +
                              self.daal.get()*self.grocery_prices_dict["daal"] +
                              self.flour.get()*self.grocery_prices_dict["flour"] +
                              self.maggi.get()*self.grocery_prices_dict["maggi"] +
                              self.biskit.get()*self.grocery_prices_dict["biskit"] +
                              self.salt.get()*self.grocery_prices_dict["salt"])
        self.grocery_price.set(f"Rs. {self.total_grocery}")

        # Cold drinks total
        self.total_cold = (self.sprite.get()*self.cold_prices_dict["sprite"] +
                           self.limka.get()*self.cold_prices_dict["limka"] +
                           self.mazza.get()*self.cold_prices_dict["mazza"] +
                           self.coke.get()*self.cold_prices_dict["coke"] +
                           self.fanta.get()*self.cold_prices_dict["fanta"] +
                           self.mountain_duo.get()*self.cold_prices_dict["mountain_duo"] +
                           self.pepsi.get()*self.cold_prices_dict["pepsi"] +
                           self.thumsup.get()*self.cold_prices_dict["thumsup"])
        self.cold_drinks_price.set(f"Rs. {self.total_cold}")

        # Taxes (5%)
        self.medical_tax.set(f"Rs. {round(self.total_medical*0.05,2)}")
        self.grocery_tax.set(f"Rs. {round(self.total_grocery*0.05,2)}")
        self.cold_drinks_tax.set(f"Rs. {round(self.total_cold*0.05,2)}")

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to Billing Software\n")
        self.txtarea.insert(END, f"\nBill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, "\n====================================\n")
        self.txtarea.insert(END, "Products\t\tQty\tPrice\n")
        self.txtarea.insert(END, "====================================\n")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are required")
            return

        self.welcome_bill()
        # Loop through items
        items = [
            ("Sanitizer", self.sanitizer.get(), self.medical_prices_dict["sanitizer"]),
            ("Mask", self.mask.get(), self.medical_prices_dict["mask"]),
            ("Hand Gloves", self.hand_gloves.get(), self.medical_prices_dict["hand_gloves"]),
            ("Dettol", self.dettol.get(), self.medical_prices_dict["dettol"]),
            ("Newsprin", self.newsprin.get(), self.medical_prices_dict["newsprin"]),
            ("Thermal Gun", self.thermal_gun.get(), self.medical_prices_dict["thermal_gun"]),
            ("Bandage", self.bandage.get(), self.medical_prices_dict["bandage"]),
            ("Cotton", self.cotton.get(), self.medical_prices_dict["cotton"]),

            ("Rice", self.rice.get(), self.grocery_prices_dict["rice"]),
            ("Food Oil", self.food_oil.get(), self.grocery_prices_dict["food_oil"]),
            ("Wheat", self.wheat.get(), self.grocery_prices_dict["wheat"]),
            ("Daal", self.daal.get(), self.grocery_prices_dict["daal"]),
            ("Flour", self.flour.get(), self.grocery_prices_dict["flour"]),
            ("Maggi", self.maggi.get(), self.grocery_prices_dict["maggi"]),
            ("Biskit", self.biskit.get(), self.grocery_prices_dict["biskit"]),
            ("Salt", self.salt.get(), self.grocery_prices_dict["salt"]),

            ("Sprite", self.sprite.get(), self.cold_prices_dict["sprite"]),
            ("Limka", self.limka.get(), self.cold_prices_dict["limka"]),
            ("Mazza", self.mazza.get(), self.cold_prices_dict["mazza"]),
            ("Coke", self.coke.get(), self.cold_prices_dict["coke"]),
            ("Fanta", self.fanta.get(), self.cold_prices_dict["fanta"]),
            ("Mountain Duo", self.mountain_duo.get(), self.cold_prices_dict["mountain_duo"]),
            ("Pepsi", self.pepsi.get(), self.cold_prices_dict["pepsi"]),
            ("ThumsUp", self.thumsup.get(), self.cold_prices_dict["thumsup"]),
        ]

        total_bill = 0
        for item, qty, price in items:
            if qty != 0:
                self.txtarea.insert(END, f"{item}\t\t{qty}\t{qty*price}\n")
                total_bill += qty*price

        total_tax = round(total_bill*0.05,2)  # simple total tax 5%
        self.txtarea.insert(END, "====================================\n")
        self.txtarea.insert(END, f"Total Bill: Rs. {total_bill+total_tax}\n")
        self.txtarea.insert(END, "====================================\n")
        self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            if not os.path.exists("bills"):
                os.makedirs("bills")
            bill_data = self.txtarea.get('1.0', END)
            f = open(f"bills/{self.bill_no.get()}.txt", "w")
            f.write(bill_data)
            f.close()
            messagebox.showinfo("Saved", f"Bill no. {self.bill_no.get()} saved successfully")

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills"):
            if i.split('.')[0] == self.search_bill.get():
                f = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f:
                    self.txtarea.insert(END, d)
                f.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill Number")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear?")
        if op > 0:
            # Reset all quantity variables
            for var in [self.sanitizer, self.mask, self.hand_gloves, self.dettol, self.newsprin, self.thermal_gun, self.bandage, self.cotton,
                        self.rice, self.food_oil, self.wheat, self.daal, self.flour, self.maggi, self.biskit, self.salt,
                        self.sprite, self.limka, self.mazza, self.coke, self.fanta, self.mountain_duo, self.pepsi, self.thumsup]:
                var.set(0)

            # Reset all text variables
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")
            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            # Customer details clear
            self.c_name.set("")
            self.c_phone.set("")
            self.search_bill.set("")

            # New bill number
            x = random.randint(1000,9999)
            self.bill_no.set(str(x))

            # Clear bill area
            self.txtarea.delete('1.0', END)

            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

# ================= Main =================
root = Tk()
obj = Bill_App(root)
root.mainloop()