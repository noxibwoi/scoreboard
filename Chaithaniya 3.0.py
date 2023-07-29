import customtkinter 
import tkinter.messagebox
import csv
from PIL import Image
import os,sys


customtkinter.set_appearance_mode("dark")

path = 'Scoreboard\data_chaitanya.csv'
hex_colour = '#FEE900'      
flag = 0 

try:
    with open(path):
        pass
except:
    if not os.path.exists('Scoreboard'):
        os.mkdir("Scoreboard")
    with open(path,"w") as f: 
        f.write('''School,FP,Aaja Nach Le,Rhythm Ki Rang,Phir Hera Pheri,Vogue Veda,Kab? Kyoon? Aur Kahan?,Jeet Ki Aawaz,Total
ASSISI VIDYANIKETAN,0,0,0,0,0,0,0,0
BHAVAN'S ELAMAKKARA,0,0,0,0,0,0,0,0
BHAVAN'S EROOR,0,0,0,0,0,0,0,0
BHAVAN'S GIRINAGAR,0,0,0,0,0,0,0,0
BHAVAN'S NEWSPRINT,0,0,0,0,0,0,0,0
BHAVAN'S THRIKAKARA,0,0,0,0,0,0,0,0
CHINMAYA KANNAMALLY*,10,0,0,0,0,0,0,0
CHINMAYA TRIPUNITHURA,0,0,0,0,0,0,0,0
GLOBAL PUBLIC SCHOOL,0,0,0,0,0,0,0,0
KMJ PUBLIC SCHOOL,0,0,0,0,0,0,0,0
SBOA PUBLIC SR SEC SCHOOL,0,0,0,0,0,0,0,0
THE CHOICE SCHOOL*,10,0,0,0,0,0,0,0
THE DELTA STUDY,0,0,0,0,0,0,0,0
Toc H PUBLIC SCHOOL*,10,0,0,0,0,0,0,0
VIDYODAYA THEVAKKAL,0,0,0,0,0,0,0,0
''')
        
def resource_path(relative_path):

    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

image_path = resource_path('image_chaithanya.png')
icon = resource_path('logo.ico')


class home_page(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Results")
        self.attributes('-fullscreen',True)
        self.after(100,self.lift)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2,3), weight=0)
        self.grid_rowconfigure((0,1,2), weight=1)

        picture = customtkinter.CTkImage(Image.open(image_path), size = (1920,1080))
        bg_image = customtkinter.CTkLabel(self,text = "" ,image=picture)
        bg_image.grid(row=0,column=1,rowspan=3,columnspan=3)

        sidebar_frame = customtkinter.CTkFrame(self, width=190,fg_color='#fedd1a',corner_radius=0)
        sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        sidebar_frame.grid_rowconfigure(4, weight=1) 
        
        def home_event():
            for i in self.winfo_children():
                i.destroy()

            global flag

            

            self.grid_columnconfigure((0,1,2,3,4,5,6,7,8), weight=0)
            self.grid_rowconfigure((0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30), weight = 0)

            picture = customtkinter.CTkImage(Image.open(image_path), size = (1920,1080))
            bg_image = customtkinter.CTkLabel(self,text = "" ,image=picture)
            bg_image.grid(row=0,column=1,rowspan=3,columnspan=3)
            
            sidebar_frame = customtkinter.CTkFrame(self, width=190,fg_color='#fedd1a',corner_radius=0)
            sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
            sidebar_frame.grid_rowconfigure(4, weight=1) 

            Home_button = customtkinter.CTkButton(sidebar_frame,text='Chaitanya',command=home_event)

            Home_button.place(relx=.5, rely=.05, anchor=tkinter.CENTER)        
            event1_button = customtkinter.CTkButton(sidebar_frame,text=event_list[0],command=lambda: get_event_name(event_list[0]))
            event1_button.place(relx=.5, rely=.15, anchor=tkinter.CENTER)

            event2_button = customtkinter.CTkButton(sidebar_frame,text=event_list[1],command=lambda: get_event_name(event_list[1]))
            event2_button.place(relx=.5, rely=.2, anchor=tkinter.CENTER)

            event3_button = customtkinter.CTkButton(sidebar_frame,text=event_list[2],command=lambda: get_event_name(event_list[2]))
            event3_button.place(relx=.5, rely=.25, anchor=tkinter.CENTER)

            event4_button = customtkinter.CTkButton(sidebar_frame,text=event_list[3],command=lambda: get_event_name(event_list[3]))
            event4_button.place(relx=.5, rely=.3, anchor=tkinter.CENTER)

            event5_button = customtkinter.CTkButton(sidebar_frame,text=event_list[4],command=lambda: get_event_name(event_list[4]))
            event5_button.place(relx=.5, rely=.35, anchor=tkinter.CENTER)

            event6_button = customtkinter.CTkButton(sidebar_frame,text=event_list[5],command=lambda: get_event_name(event_list[5]),state='disabled')
            event6_button.place(relx=.5, rely=.4, anchor=tkinter.CENTER)

            scoreboard_button = customtkinter.CTkButton(sidebar_frame,text='Scoreboard',command=scoreboard_event)
            scoreboard_button.place(relx=.5, rely=.6, anchor=tkinter.CENTER)

            result_button = customtkinter.CTkButton(sidebar_frame,text='Result',command=results_event)
            result_button.place(relx=.5, rely=.65, anchor=tkinter.CENTER)   

            title = tkinter.Label(self,text='SUVARNA CHAITANYA',bg=hex_colour,font=("Roboto", 75),wraplength=550)         
            title.place(relx=.5,rely=.5,anchor=tkinter.CENTER)    

            back_button = customtkinter.CTkButton(sidebar_frame,text='Go Back',command=self.go_back_event)
            back_button.place(relx=.5, rely=.95, anchor=tkinter.CENTER)

            if flag != 0:
                event6_button.configure(state='normal')


        def csv_results():
            with open(path) as file:
                data = list(csv.reader(file))
                data_copy = []
                for i in data:
                    list1 = []
                    for j in i:
                        if j.isdigit():
                            list1.append(int(j))
                        else:
                            list1.append(j)
                    data_copy.append(list1)
                reserv_data = []
                for i in data_copy:
                    list1 = []
                    if isinstance(i[1], int):
                        list1.append(sum(i[1:8]))
                        list1.append(i[0])
                        reserv_data.append(list1)
                reserv_data.sort(key=lambda x: x[0],reverse=True)

                school_points_dict = {}
                for points, school_name in reserv_data:
                    if points in school_points_dict:
                        school_points_dict[points].append(school_name)
                    else:
                        school_points_dict[points] = [school_name]
                
                return school_points_dict
            
        def results_event():
            global flag

            data = csv_results()

            check = 0
            
            for i in data:
                if check == 1:
                    runner_list = data[i]
                    runner = ", ".join(runner_list)
                    break
                champ_list = data[i]
                champ = ", ".join(champ_list)
                check = 1


                
            picture = customtkinter.CTkImage(Image.open(image_path), size = (1920,1080))

            image_label = customtkinter.CTkLabel(self,text = "" ,image=picture)
            image_label.place(relx = .5,rely= .5,anchor = tkinter.CENTER)

            if len(champ_list) > 1:
                flag = 1
                messagebox = tkinter.messagebox.showwarning(parent=self,title='Caution',message='2 or more schools had tied. Please mark their cheering to proceed')
                if messagebox:
                    home_event()
            
            elif len(runner_list) > 1:
                flag = 2
                messagebox = tkinter.messagebox.showwarning(parent=self,title='Caution',message='2 or more schools had tied. Please mark their cheering to proceed')
                if messagebox:
                    home_event()

            else:
                back_button = customtkinter.CTkButton(self,text='Go Back',command=home_event,bg_color=hex_colour,width=95)
                back_button.place(relx=.99, rely=.99, anchor=tkinter.SE)   

                title1 = tkinter.Label(self,text = "CHAMPIONS",font = ("Roboto",100),bg=hex_colour)
                title1.place(relx = .5, rely = .25,anchor  = tkinter.CENTER)

                label1 = tkinter.Label(self, text = champ,font = ("Roboto",30),bg=hex_colour,wraplength=1000)
                label1.place(relx = .5,rely = .4
                ,anchor = tkinter.CENTER )

                title2 = tkinter.Label(self,text = "RUNNERS UP", font = ("Roboto",70), bg=hex_colour)
                title2.place(relx = .5,rely = .6,anchor = tkinter.CENTER)

                label2 = tkinter.Label(self,text = runner, font = ("Robooto",25), bg=hex_colour,wraplength=1000)
                label2.place(relx = .5, rely = .75, anchor = tkinter.CENTER)

            

        def csv_event_name():
            with open(path) as r_data:
                reader = list(csv.reader(r_data))
                data = reader[0][2:8]
                return data
        event_list = csv_event_name()

        def get_event_name(n):
            newname = n
            for i in self.winfo_children():
                if i != sidebar_frame:
                    i.place_forget()
            marking_event(newname)
            
        def marking_event(event_name):

            picture = customtkinter.CTkImage(Image.open(image_path), size = (1920,1080))
            bg_image = customtkinter.CTkLabel(self,text = "" ,image=picture)
            bg_image.grid(row=0,column=1,rowspan=3,columnspan=3)
            

            def csv_school_name():
                with open(path) as r_data:
                    reader = csv.reader(r_data)
                    data = []
                    next(reader)
                    for i in reader:
                        data.append(i[0]) 
                    return data

            def submit():
                events,points=[],[]
                points.extend((first_option.get(),sec_option.get(),third_option.get()))
                events.append(event_name)
                events.append(points)
                messagebox = tkinter.messagebox.askyesno(parent=self,title='Caution', message=f'You have chosen: \n \nFirst: {points[0]} \nSecond: {points[1]} \nThird: {points[2]} \n \nDo you wish to Proceed?')
                if messagebox:
                    csv_marking(events)
                    home_event()

            def csv_marking(data):

                with open(path) as file:
                    pradeep = list(csv.reader(file))
                    event_var1 = 0
                    school_var1 = 0
                    final_data = pradeep.copy()
                    for i in pradeep:
                        if school_var1 == 0:
                            for event in i:
                                if data[0] == event:
                                    break
                                else:
                                    event_var1 += 1
                        
                        if Event1_label.cget('text') == 'Jeet Ki Aawaz':
                            if i[0] in data[1]:
                                if data[1][0] == i[0]:
                                    final_data[school_var1][event_var1] = 2
                                if data[1][1] == i[0]:
                                    final_data[school_var1][event_var1] = 1
                                if data[1][2] == i[0]:
                                    final_data[school_var1][event_var1] = 0
                        else:
                            if i[0] in data[1]:
                                if data[1][0] == i[0]:
                                    final_data[school_var1][event_var1] = 10
                                if data[1][1] == i[0]:
                                    final_data[school_var1][event_var1] = 7
                                if data[1][2] == i[0]:
                                    final_data[school_var1][event_var1] = 5
                            
                        school_var1 += 1
                    with open(path,'w',newline='\n') as w_data:
                        writer = csv.writer(w_data)
                        writer.writerows(final_data)

            

            Event1_label = tkinter.Label(self, text=event_name,font=("Times New Roman", 64),bg=hex_colour)
            Event1_label.place(relx=.5, rely=.1, anchor=tkinter.CENTER)

            if Event1_label.cget('text') == 'Jeet Ki Aawaz':
                data = csv_results()
                check = 0
                for i in data:
                    if check == 1:
                        runner_list = data[i]
                        break
                    champ_list = data[i]
                    check = 1
                if len(champ_list) > 1:
                    value_list = champ_list
                elif len(runner_list) > 1:
                    value_list = runner_list
            else:
                value_list = csv_school_name()

            firstlabel = tkinter.Label(self, text = "First",bg=hex_colour,font = ("Times New Roman",40))
            firstlabel.place(relx=.22,rely=.25,anchor="center")

            secondlabel = tkinter.Label(self, text = "Second",bg=hex_colour,font = ("Times New Roman",40))
            secondlabel.place(relx=.22,rely=.45,anchor="center")

            thirdlabel = tkinter.Label(self, text = "Third",bg=hex_colour,font = ("Times New Roman",40))
            thirdlabel.place(relx=.22,rely=.65,anchor="center")

            first_option = customtkinter.CTkOptionMenu(self, values=value_list, bg_color=hex_colour,width = 900,height=65,)
            first_option.place(relx=.97,rely=.25,anchor="e")
            first_option.set("Select school")

            sec_option = customtkinter.CTkOptionMenu(self, values=value_list, bg_color=hex_colour, width = 900,height = 65)
            sec_option.place(relx=.97,rely=.45,anchor="e")
            sec_option.set("Select school")

            third_option = customtkinter.CTkOptionMenu(self, values=value_list, bg_color=hex_colour, width = 900,height = 65)
            third_option.place(relx=.97,rely=.65,anchor="e")
            third_option.set("Select school")

            submit_button = customtkinter.CTkButton(self,bg_color=hex_colour,text='Submit',width=150, height = 50,command=submit)
            submit_button.place(relx=.50, rely=.95, anchor='center')

        def scoreboard_display():
            with open(path) as r_data:
                reader = csv.reader(r_data)
                data = []
                for i in reader:
                    list1 = ()
                    for j in i:
                        if j.isdigit():
                            list1 += (int(j),)
                        else:
                            list1 += (j,)
                    data.append(list1)
                return data

        def scoreboard_event():
            for i in self.winfo_children():
                i.destroy()

            self.grid_columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)
            self.grid_rowconfigure((0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30), weight = 1)

            data = scoreboard_display()

            c=0
            r=0
            for i in data:
                for j in i:

                    if c==0 and r != 0:
                        school_name_frame = customtkinter.CTkFrame(self,border_color='black',fg_color=hex_colour,bg_color=hex_colour,border_width=1,corner_radius=0,height=40,width=570)
                        school_name_frame.grid(row=r,column=0,sticky="nsew")
                        school_name_frame.pack_propagate(False)

                        school_label=tkinter.Label(school_name_frame,text=j,bg=hex_colour,font=('Roboto',14))
                        school_label.pack(expand=False,side='left',padx=10)

                    elif r == 0:
                        event_name_frame = customtkinter.CTkFrame(self,height=100,width=350,border_color='black',fg_color=hex_colour,bg_color=hex_colour,border_width=1,corner_radius=0)
                        event_name_frame.grid(row=r,column=c,sticky="nsew")
                        event_name_frame.pack_propagate(False)
                        event_label=tkinter.Label(event_name_frame,text=j,bg=hex_colour,font=('Times New Roman',18),wraplength=120)
                        event_label.pack(expand=True)

                    else:
                        total=sum(i[1:8])
                        if c==8:
                            j=total
                        
                        event_name_frame = customtkinter.CTkFrame(self,height=40,width=350,border_color='black',fg_color=hex_colour,bg_color=hex_colour,border_width=1,corner_radius=0)
                        event_name_frame.grid(row=r,column=c,sticky="nsew")
                        event_name_frame.pack_propagate(False)
                        
                        
                        if j == 0:
                            event_label=tkinter.Label(event_name_frame,text="",bg=hex_colour,font=('Roboto',18))
                            event_label.pack(expand=True)
                        else:
                            event_label=tkinter.Label(event_name_frame,bg=hex_colour,text=j,font=('Roboto',18))
                            event_label.pack(expand=True)

                    c+=1

                    if c==9:
                        c=0
                        r+=2

            back_button = customtkinter.CTkButton(self,text='Go Back',command=home_event)
            back_button.grid(row=32,column=8,padx=20, pady=10, sticky="e")

        Home_button = customtkinter.CTkButton(sidebar_frame,text='Chaitanya',command=home_event)
        Home_button.place(relx=.5, rely=.05, anchor=tkinter.CENTER)

        event1_button = customtkinter.CTkButton(sidebar_frame,text=event_list[0],command=lambda: get_event_name(event_list[0]))
        event1_button.place(relx=.5, rely=.15, anchor=tkinter.CENTER)

        event2_button = customtkinter.CTkButton(sidebar_frame,text=event_list[1],command=lambda: get_event_name(event_list[1]))
        event2_button.place(relx=.5, rely=.2, anchor=tkinter.CENTER)

        event3_button = customtkinter.CTkButton(sidebar_frame,text=event_list[2],command=lambda: get_event_name(event_list[2]))
        event3_button.place(relx=.5, rely=.25, anchor=tkinter.CENTER)

        event4_button = customtkinter.CTkButton(sidebar_frame,text=event_list[3],command=lambda: get_event_name(event_list[3]))
        event4_button.place(relx=.5, rely=.3, anchor=tkinter.CENTER)

        event5_button = customtkinter.CTkButton(sidebar_frame,text=event_list[4],command=lambda: get_event_name(event_list[4]))
        event5_button.place(relx=.5, rely=.35, anchor=tkinter.CENTER)

        event6_button = customtkinter.CTkButton(sidebar_frame,text=event_list[5],command=lambda: get_event_name(event_list[5]),state='disabled')
        event6_button.place(relx=.5, rely=.4, anchor=tkinter.CENTER)

        scoreboard_button = customtkinter.CTkButton(sidebar_frame,text='Scoreboard',command=scoreboard_event)
        scoreboard_button.place(relx=.5, rely=.6, anchor=tkinter.CENTER)

        result_button = customtkinter.CTkButton(sidebar_frame,text='Result',command=results_event)
        result_button.place(relx=.5, rely=.65, anchor=tkinter.CENTER)   

        title = tkinter.Label(self,text='SUVARNA CHAITANYA',bg=hex_colour,font=("Roboto", 75),wraplength=550)         
        title.place(relx=.5,rely=.5,anchor=tkinter.CENTER)    

        back_button = customtkinter.CTkButton(sidebar_frame,text='Go Back',command=self.go_back_event)
        back_button.place(relx=.5, rely=.95, anchor=tkinter.CENTER)   
    
    def go_back_event(self):
            self.destroy()


class Register(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Register")
        self.attributes('-fullscreen',True)
        self.after(100,self.lift)
        
        Register_label = customtkinter.CTkLabel(self, text="Register",fg_color="transparent",font=("Roboto", 64))
        Register_label.place(relx=.5, rely=.1, anchor=tkinter.CENTER)

        school_name_label = customtkinter.CTkLabel(self, text="Enter School Name: ",fg_color="transparent",font=("Roboto", 32))
        school_name_label.place(relx=.1, rely=.25, anchor=tkinter.W)
        school_name_entry = customtkinter.CTkEntry(self, placeholder_text="Type",fg_color="transparent", width=500)
        school_name_entry.place(relx=.95,rely=.25, anchor=tkinter.E)

        participating_label = customtkinter.CTkLabel(self, text="Participating Event:",fg_color="transparent",font=("Roboto", 32))
        participating_label.place(relx=.5, rely=.5, anchor=tkinter.CENTER)

        event1_checkvar = customtkinter.StringVar(value="off")
        event1_checkbox = customtkinter.CTkCheckBox(self,text="Event1",variable=event1_checkvar,onvalue="on", offvalue="off")
        event1_checkbox.place(relx=.15, rely=.375, anchor=tkinter.W)

        event2_checkvar = customtkinter.StringVar(value="off")
        event2_checkbox = customtkinter.CTkCheckBox(self,text="Event2",variable=event2_checkvar,onvalue="on", offvalue="off")
        event2_checkbox.place(relx=.3, rely=.375, anchor=tkinter.W)

        event3_checkvar = customtkinter.StringVar(value="off")
        event3_checkbox = customtkinter.CTkCheckBox(self,text="Event3",variable=event3_checkvar,onvalue="on", offvalue="off")
        event3_checkbox.place(relx=.45, rely=.375, anchor=tkinter.W)

        event4_checkvar = customtkinter.StringVar(value="off")
        event4_checkbox = customtkinter.CTkCheckBox(self,text="Event4",variable=event4_checkvar,onvalue="on", offvalue="off")
        event4_checkbox.place(relx=.6, rely=.375, anchor=tkinter.W)

        event5_checkvar = customtkinter.StringVar(value="off")
        event5_checkbox = customtkinter.CTkCheckBox(self,text="Event5",variable=event5_checkvar,onvalue="on", offvalue="off")
        event5_checkbox.place(relx=.75, rely=.375, anchor=tkinter.W)

        
                        
        back_button = customtkinter.CTkButton(self,text='Go Back',command=self.go_back_event,width=95)
        back_button.place(relx=.99, rely=.99, anchor=tkinter.SE)   
    
    def go_back_event(self):
            self.destroy()


class Add_events(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("add events")
        self.attributes('-fullscreen',True)
        self.after(100,self.lift)

        back_button = customtkinter.CTkButton(self,text='Go Back',command=self.go_back_event,width=95)
        back_button.place(relx=.99, rely=.99, anchor=tkinter.SE)   
    
    def go_back_event(self):
            self.destroy()

class Options(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Options")
        self.geometry('300x500')
        self.after(100,self.lift) 

        bg_image = customtkinter.CTkImage(Image.open(image_path),size=(1080,1920))
        label1 = customtkinter.CTkLabel(self,text="",image=(bg_image))
        label1.pack()


        def reset():
            messagebox = tkinter.messagebox.askokcancel(parent=self,title='Caution', message='Do you wish to proceed? (This will reset all the ranking you made so far!)')
            if messagebox:
                with open(path) as file:
                    data = list(csv.reader(file))
                    data_copy = []
                    for i in data:
                        list1 = []
                        for j in i:
                            if j.isdigit():
                                list1.append(0)
                            elif j.isdigit() == 10:
                                list1.append(10)
                            else:
                                list1.append(j)
                        data_copy.append(list1)
                    with open(path,"w") as f:
                        f.write('''School,FP,Aaja Nach Le,Rhythm Ki Rang,Phir Hera Pheri,Vogue Veda,Kab? Kyoon? Aur Kahan?,Jeet Ki Aawaz,Total
ASSISI VIDYANIKETAN,0,0,0,0,0,0,0,0
BHAVAN'S ELAMAKKARA,0,0,0,0,0,0,0,0
BHAVAN'S EROOR,0,0,0,0,0,0,0,0
BHAVAN'S GIRINAGAR,0,0,0,0,0,0,0,0
BHAVAN'S NEWSPRINT,0,0,0,0,0,0,0,0
BHAVAN'S THRIKAKARA,0,0,0,0,0,0,0,0
CHINMAYA KANNAMALLY*,10,0,0,0,0,0,0,0
CHINMAYA TRIPUNITHURA,0,0,0,0,0,0,0,0
GLOBAL PUBLIC SCHOOL,0,0,0,0,0,0,0,0
KMJ PUBLIC SCHOOL,0,0,0,0,0,0,0,0
SBOA PUBLIC SR SEC SCHOOL,0,0,0,0,0,0,0,0
THE CHOICE SCHOOL*,10,0,0,0,0,0,0,0
THE DELTA STUDY,0,0,0,0,0,0,0,0
Toc H PUBLIC SCHOOL*,10,0,0,0,0,0,0,0
VIDYODAYA THEVAKKAL,0,0,0,0,0,0,0,0''')

                messagebox = tkinter.messagebox.showinfo(parent=self,title='Done',message='Ranking has been reset')

        reset_button = customtkinter.CTkButton(self,text='reset ranking',command=reset,bg_color=hex_colour)
        reset_button.place(relx=.5,rely=.15,anchor=tkinter.CENTER)

    
    def go_back_event(self):
            self.destroy()


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        app_width = 400
        app_height = 300
        self.geometry(f"{app_width}x{app_height}")
        self.title("Chaitanya")

        bg_image = customtkinter.CTkImage(Image.open(image_path),size=(1920,1080))
        label1 = customtkinter.CTkLabel(self,text="",image=(bg_image))
        label1.pack()

        title = tkinter.Label(self,text='Chaithanya',font = ("Roboto",16),bg=hex_colour)
        title.place(relx=.5,rely=.15,anchor=tkinter.CENTER)

        add_event = customtkinter.CTkButton(self, text="Add Events",height= 55, width=10, command=self.add_event_clicked,bg_color=hex_colour)
        add_event.place(relx=.5, rely=0.5, anchor=tkinter.CENTER)

        reg_button = customtkinter.CTkButton(self, text="Register",command=self.register_clicked,width=95,bg_color=hex_colour)
        reg_button.place(relx=.45, rely=.75, anchor=tkinter.SE)

        result_button = customtkinter.CTkButton(self, text="Results",command=self.result_clicked,width=95,bg_color=hex_colour)
        result_button.place(relx=.55, rely=.75, anchor=tkinter.SW)

        options_button = customtkinter.CTkButton(self,text="Options",command=self.option_event_clicked,width=95,bg_color=hex_colour)
        options_button.place(relx=.5, rely=.85, anchor=tkinter.CENTER)

        self.toplevel_window = None
    
    def option_event_clicked(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Options(self)  
        else:
            self.toplevel_window.focus()

    def add_event_clicked(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Add_events(self)  
        else:
            self.toplevel_window.focus()

    def result_clicked(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = home_page(self)  
        else:
            self.toplevel_window.focus()
    
    def register_clicked(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Register(self)  
        else:
            self.toplevel_window.focus()


mainwindow = App()
mainwindow.resizable(False,False)
mainwindow.iconbitmap(icon)
mainwindow.mainloop()