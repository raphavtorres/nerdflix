import tkinter as tk
from tkinter import ttk

from create import register_user_window
from update import update
from read import read_user_window, search_user_window
from delete import delete_user_window
import pyautogui
pyautogui.PAUSE = 1

window = tk.Tk()


class Application():
    def __init__(self):
        self. window = window
        self.screen()
        self.frame()
        self.buttons()
        self.labels()
        self.inputs()
        self.list_frame_2()
        self.input_id.focus_set()
        window.mainloop()

    def screen(self):
        self.window.title("Nerdflix")
        self.window.geometry('700x700')
        self.window.configure(background='#4edb3b')
        self.window.resizable(False, False)
        # self.window.minsize(width=300, height=200)
        # self.window.maxsize(width=700, height=900)

    def frame(self):
        self.frame_0 = tk.Frame(self.window, bg='#db3b4e')
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.09)

        self.frame_1 = tk.Frame(self.window, bg='#db3b4e')
        self.frame_1.place(relx=0.03, rely=0.16, relwidth=0.94, relheight=0.25)

        self.frame_2 = tk.Frame(self.window, bg='#db3b4e')
        self.frame_2.place(relx=0.03, rely=0.42, relwidth=0.94, relheight=0.15)

        self.frame_3 = tk.Frame(self.window, bg='#db3b4e')
        self.frame_3.place(relx=0.03, rely=0.60, relwidth=0.94, relheight=0.20)

    def buttons(self):
        self.btn_search = tk.Button(self.frame_0, text='Search', bg='#70bfb3', command=self.search_user)
        self.btn_search.place(relx=0.25, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btn_clear = tk.Button(self.frame_0, text='Clear', bg='#70bfb3', command=self.clear)
        self.btn_clear.place(relx=0.40, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btn_create = tk.Button(self.frame_0, text='Create', bg='#70bfb3', command=self.insert_user)
        self.btn_create.place(relx=0.55, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btn_read = tk.Button(self.frame_0, text='Read', bg='#70bfb3', command=self.read_user)
        self.btn_read.place(relx=0.65, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btn_update = tk.Button(self.frame_0, text='Update', bg='#70bfb3', command=self.update_user)
        self.btn_update.place(relx=0.75, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btn_delete = tk.Button(self.frame_0, text='Delete', bg='#70bfb3', command=self.delete_user)
        self.btn_delete.place(relx=0.85, rely=0.25, relwidth=0.1, relheight=0.5)

        #  posic mover bot alerta captura
        self.btn_dimension = tk.Button(self.frame_3, text='Monitor', bg='#70bfb3', command=self.monitor)
        self.btn_dimension.place(relx=0.02, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btn_mouse_position = tk.Button(self.frame_3, text='Position', bg='#70bfb3', command=self.mouse_position)
        self.btn_mouse_position.place(relx=0.15, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btn_move_mouse = tk.Button(self.frame_3, text='Move', bg='#70bfb3', command=self.move_mouse)
        self.btn_move_mouse.place(relx=0.3, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btn_bot = tk.Button(self.frame_3, text='Bot', bg='#70bfb3', command=self.bot)
        self.btn_bot.place(relx=0.42, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btn_alert = tk.Button(self.frame_3, text='Alert', bg='#70bfb3', command=self.alert)
        self.btn_alert.place(relx=0.55, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btn_capture = tk.Button(self.frame_3, text='Capture', bg='#70bfb3', command=self.capture)
        self.btn_capture.place(relx=0.65, rely=0.25, relwidth=0.1, relheight=0.5)

    def labels(self):
        self.lb_id_user = tk.Label(self.frame_0, text='ID', background='#db3b4e')
        self.lb_id_user.place(relx=0.005, rely=0.07, relwidth=0.1, relheight=0.4)

        self.lb_name = tk.Label(self.frame_1, text='Name:', background='#db3b4e')
        self.lb_name.place(relx=0.005, rely=0.04, relwidth=0.1, relheight=0.15)

        self.lb_email = tk.Label(self.frame_1, text='E-mail:', background='#db3b4e')
        self.lb_email.place(relx=0.005, rely=0.2, relwidth=0.1, relheight=0.15)

        self.lb_plan = tk.Label(self.frame_1, text='Plan:', background='#db3b4e')
        self.lb_plan.place(relx=0.005, rely=0.36, relwidth=0.1, relheight=0.15)

        self.lb_type = tk.Label(self.frame_1, text='Type:', background='#db3b4e')
        self.lb_type.place(relx=0.38, rely=0.36, relwidth=0.1, relheight=0.15)

        self.lb_age = tk.Label(self.frame_1, text='Age:', background='#db3b4e')
        self.lb_age.place(relx=0.7, rely=0.36, relwidth=0.1, relheight=0.15)

        self.lb_update_element = tk.Label(self.frame_1, text="Update:", background='#db3b4e')
        self.lb_update_element.place(relx=0.005, rely=0.65, relwidth=0.1, relheight=0.15)

        self.lb_update_value = tk.Label(self.frame_1, text="New Value:", background='#db3b4e')
        self.lb_update_value.place(relx=0.31, rely=0.65, relwidth=0.1, relheight=0.15)

    def inputs(self):
        self.input_id = tk.Entry(self.frame_0)
        self.input_id.place(relx=0.005, rely=0.45, relwidth=0.1, relheight=0.5)

        self.input_name = tk.Entry(self.frame_1)
        self.input_name.place(relx=0.12, rely=0.04, relwidth=0.8, relheight=0.15)

        self.input_email = tk.Entry(self.frame_1)
        self.input_email.place(relx=0.12, rely=0.2, relwidth=0.8, relheight=0.15)

        self.input_plan = tk.Entry(self.frame_1)
        self.input_plan.place(relx=0.12, rely=0.36, relwidth=0.1, relheight=0.15)

        self.input_type = tk.Entry(self.frame_1)
        self.input_type.place(relx=0.5, rely=0.36, relwidth=0.1, relheight=0.15)

        self.input_age = tk.Entry(self.frame_1)
        self.input_age.place(relx=0.82, rely=0.36, relwidth=0.1, relheight=0.15)

        self.input_update_element = tk.Entry(self.frame_1)
        self.input_update_element.place(relx=0.12, rely=0.65, relwidth=0.19, relheight=0.15)

        self.input_update_value = tk.Entry(self.frame_1)
        self.input_update_value.place(relx=0.41, rely=0.65, relwidth=0.19, relheight=0.15)

    def list_frame_2(self):
        self.list_client = ttk.Treeview(
            self.frame_2,
            height=3,
            columns=(
                'col0', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7'
                )
            )
        self.list_client.heading('#0', text='')
        self.list_client.heading('#1', text='ID')
        self.list_client.heading('#2', text='NAME')
        self.list_client.heading('#3', text='EMAIL')
        self.list_client.heading('#4', text='AGE')
        self.list_client.heading('#5', text='TYPE')
        self.list_client.heading('#6', text='PLAN')

        self.list_client.column('#0', width=0)
        self.list_client.column('#1', width=30)
        self.list_client.column('#2', width=190)
        self.list_client.column('#3', width=190)
        self.list_client.column('#4', width=50)
        self.list_client.column('#5', width=50)
        self.list_client.column('#6', width=70)

        self.list_client.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.96)

        self.scrool_list = tk.Scrollbar(self.frame_2, orient='vertical')
        self.list_client.configure(yscrollcommand=self.scrool_list.set)
        self.scrool_list.place(relx=0.97, rely=0.03, relwidth=0.03, relheight=0.949)

    def insert_user(self):
        register_user_window(
            self.input_name.get(),
            self.input_email.get(),
            self.input_age.get(),
            self.input_type.get(),
            self.input_plan.get()
        )
        self.read_user()

    def update_user(self):
        update(
            'user',
            self.input_update_element.get(),
            self.input_update_value.get(),
            self.input_id.get(),
        )
        self.read_user()

    def clear(self):
        self.list_client.delete(*self.list_client.get_children())
        self.input_age.delete(0, tk.END)
        self.input_email.delete(0, tk.END)
        self.input_id.delete(0, tk.END)
        self.input_name.delete(0, tk.END)
        self.input_plan.delete(0, tk.END)
        self.input_type.delete(0, tk.END)
        self.input_update_element.delete(0, tk.END)
        self.input_update_value.delete(0, tk.END)

    def read_user(self):
        self.clear()
        users = read_user_window()
        for user in users:
            self.list_client.insert("", "end", values=user)

    def search_user(self):
        users = search_user_window(self.input_id.get())
        self.clear()
        for user in users:
            self.list_client.insert("", "end", values=user)

    def delete_user(self):
        delete_user_window(
            self.input_id.get(),
        )
        self.read_user()

    def monitor(self):  # to discover the windows size
        wind_x, wind_y = pyautogui.size()
        print(wind_x)
        print(wind_y)

    def mouse_position(self):  # to discover mouse position
        mouse_x, mouse_y = pyautogui.position()
        print(mouse_x)
        print(mouse_y)

    def move_mouse(self):
        pyautogui.moveTo(100, 150)

    def bot(self):
        pyautogui.press("win")
        pyautogui.write("txt")
        pyautogui.press("enter")
        pyautogui.write("Raphael")
        pyautogui.hotkey('ctrl', 's')
        pyautogui.write("salvandomermao")
        for i in range(10):
            pyautogui.press('tab')
        for i in range(2):
            pyautogui.press('up')
        pyautogui.press('enter')
        pyautogui.hotkey('alt', 'l')
        pyautogui.hotkey('win', 'd')
        pyautogui.hotkey('win', 'l')

    def alert(self):
        pyautogui.alert(text="Test", title="Text Box", button="OK")
        print(pyautogui.confirm(text="Test", title="Text Box", buttons=["OK", "Cancel"]))

    def capture(self):
        ...
