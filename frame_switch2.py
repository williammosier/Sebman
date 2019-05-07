# Multi-frame tkinter application v2.3
import tkinter as tk
import personmanager as pm

WIDTH = 850
HEIGHT = 500

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT).pack()
        self._frame = None
        self.data_base = pm.PersonManager()
        self.title("Sebman")
        self.resizable(width=False, height=False)

        menu = tk.Menu(self)
        submenu = tk.Menu(menu, tearoff=0)
        submenu.add_command(label="one", command=self.output)
        submenu.add_command(label="two", command=self.output)
        submenu.add_command(label="three", command=self.output)
        menu.add_cascade(label="file", menu=submenu)

        self.config(menu=menu)

        self.switch_frame(PersonViewPage)

    def output(self):
        print("menu item pressed!")

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(x=0, y=0, relwidth=1, relheight=1)

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg='blue')
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Open page one", command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Open page two", command=lambda: master.switch_frame(PageTwo)).pack()
        tk.Button(self, text="Open person view", command=lambda: master.switch_frame(PersonViewPage)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page", command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page", command=lambda: master.switch_frame(StartPage)).pack()

class PersonViewPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg='#030303')

        tk.Frame(self, bg='#171717').place(x=530, y=5, width=320, height=400)
        left_box = tk.Frame(self, bg='#171717')
        left_box.place(x=5, y=5, width=515, height=400)

        self.data_base = master.data_base
        #buttons
        tk.Button(self, text="search", command=self.changeList).place(x=705, y=15)
        tk.Button(self, text="select person", command=self.displaySelectedPerson).place(x=760, y=15)
        tk.Button(self, text="Return to start page", command=lambda: master.switch_frame(StartPage)).place(x=0, y=450)
        tk.Button(self, text="New Person", command=self.createPerson).place(x=540, y=370)
        tk.Button(self, text="Update Person", command=self.updateSelectedPerson).place(x=642, y=370)
        tk.Button(self, text="Delete Person").place(x=757, y=370)

        #entry text
        self.select_entry_text = tk.StringVar()
        self.select_entry_text.set('')

        self.full_entry_text = tk.StringVar()
        self.full_entry_text.set('')

        self.first_entry_text = tk.StringVar()
        self.first_entry_text.set('')

        self.last_entry_text = tk.StringVar()
        self.last_entry_text.set('')

        self.birth_entry_text = tk.StringVar()
        self.birth_entry_text.set('')

        self.phone_entry_text = tk.StringVar()
        self.phone_entry_text.set('')

        self.email_entry_text = tk.StringVar()
        self.email_entry_text.set('')

        self.address_entry_text = tk.StringVar()
        self.address_entry_text.set('')

        self.known_entry_text = tk.StringVar()
        self.known_entry_text.set('')

        self.id = tk.IntVar()
        self.id.set(0)

        #entries
        self.select_entry = tk.Entry(self, bd=4, width=24)
        self.select_entry.place(x=540, y=15)

        self.full_entry = tk.Entry(self, textvar=self.full_entry_text)
        self.full_entry.place(x=267, y=15)

        self.first_entry = tk.Entry(self, textvar=self.first_entry_text)
        self.first_entry.place(x=15, y=70)

        self.last_entry = tk.Entry(self, textvar=self.last_entry_text)
        self.last_entry.place(x=180, y=70)

        self.birth_entry = tk.Entry(self, textvar=self.birth_entry_text)
        self.birth_entry.place(x=340, y=70)

        self.phone_entry = tk.Entry(self, textvar=self.phone_entry_text)
        self.phone_entry.place(x=15, y=122)

        self.email_entry = tk.Entry(self, textvar=self.email_entry_text)
        self.email_entry.place(x=180, y=122)

        self.address_entry = tk.Entry(self, textvar=self.address_entry_text)
        self.address_entry.place(x=340, y=122)

        self.known_entry = tk.Entry(self, textvar=self.known_entry_text)
        self.known_entry.place(x=15, y=222)

        #labels
        tk.Label(self, text='person:', bg='#171717', fg='white').place(x=220, y=15)
        tk.Label(self, text='first name').place(x=15, y=48)
        tk.Label(self, text='last name').place(x=180, y=48)
        tk.Label(self, text='birth day').place(x=340, y=48)
        tk.Label(self, text='phone').place(x=15, y=100)
        tk.Label(self, text='email').place(x=180, y=100)
        tk.Label(self, text='address').place(x=340, y=100)
        tk.Label(self, text='known from').place(x=15, y=200)

        #scrolling list starts here
        scrollbar_width = 15
        scrollframe_width = 300

        scrollframe = tk.Frame(self)
        scrollframe.place(x=540, y=55, width=scrollframe_width, height=200)

        scrollbar = tk.Scrollbar(scrollframe)
        scrollbar.place(x=scrollframe_width - scrollbar_width, y=0, width=scrollbar_width, relheight=1)

        self.mylist = tk.Listbox(scrollframe, selectmode='SINGLE', yscrollcommand = scrollbar.set )
        self.people = self.data_base.selectAllPeople()
        for person in self.people:
           self.mylist.insert(tk.END, person[0])

        self.mylist.place(x=0, y=0, width=scrollframe_width - scrollbar_width, relheight=1)

        scrollbar.config( command = self.mylist.yview )
        #scrolling list ends here

    def changeList(self):
        if self.people != None:
            # print(len(self.people))
            self.mylist.delete(0, len(self.people) - 1)
        if self.select_entry.get() == "":
            self.people = self.data_base.selectAllPeople()
        else:
            self.people = self.data_base.selectPeople(self.select_entry.get())
        if self.people != None:
            for person in self.people:
                # print(person)
                self.mylist.insert(tk.END, person[0])
        # print(self.people)

    def createPerson(self):
        birth = self.birth_entry_text.get().split("-")
        month = birth[0]
        day = ""
        year = ""
        if len(birth) == 3:
            day = birth[1]
            year = birth[2]
        elif len(birth) == 2:
            day = birth[1]
        ID = self.data_base.getMaxId() + 1
        self.data_base.importPerson([self.full_entry_text.get(),\
                                    self.first_entry_text.get(),\
                                    self.last_entry_text.get(),\
                                    ID,
                                    month, day, year,\
                                    self.phone_entry_text.get(),\
                                    self.email_entry_text.get(),\
                                    self.address_entry_text.get(),\
                                    self.known_entry_text.get()])
        self.changeList()
        print(ID)

    def displaySelectedPerson(self):
        index = self.mylist.curselection()
        if index != ():
            person = self.people[index[0]]
            self.full_entry_text.set(person[0])
            self.first_entry_text.set(person[1])
            self.last_entry_text.set(person[2])
            self.id.set(person[3])
            if person[4] != "" and person[5] != "" and person[6] != "":
                self.birth_entry_text.set(str(person[4]) + "-" + str(person[5]) + "-" + str(person[6]))
            else:
                self.birth_entry_text.set("")
            self.phone_entry_text.set(person[7])
            self.email_entry_text.set(person[8])
            self.address_entry_text.set(person[9])
            self.known_entry_text.set(person[10])
        #print(self.id.get())

    def updateSelectedPerson(self):
        birth = self.birth_entry_text.get().split("-")
        month = birth[0]
        day = ""
        year = ""
        if len(birth) == 3:
            day = birth[1]
            year = birth[2]
        elif len(birth) == 2:
            day = birth[1]
        
        self.data_base.updatePerson(self.id.get(),[self.first_entry_text.get(),\
                                                    self.last_entry_text.get(),\
                                                    month, day, year,\
                                                    self.phone_entry_text.get(),\
                                                    self.email_entry_text.get(),\
                                                    self.address_entry_text.get(),\
                                                    self.known_entry_text.get()])
        self.changeList()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    app.data_base.conn.close()