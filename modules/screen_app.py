import customtkinter
import modules.create_frame as m_frame
#
class App(customtkinter.CTk):
    def __init__(self,app_width,app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        #
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        self.resizable(False, False)
        self.title("Головне вікно програми")
        # self.FRAME = m_frame.My_Frame(text= "Friendly Chat", master = self, width= 130, height= app_height - 20, border_width= 5)
        self.FRAME1 = m_frame.My_Frame(text= "Friendly Chat", text_color= "orange", master = self, width= 130, height= app_height - 10, border_width= None, fg_color= None)
        self.FRAME2 = m_frame.My_Frame(text= "Чати", text_color= "orange", master = self, width= 165, height= app_height - 10, border_width= None, fg_color= None)
        # self.FRAME = customtkinter.CTkFrame(master=self, width=300, height= app_height)
        
        self.FRAME1.grid(row = 0, column = 0, padx = 5, pady = 5)
        # self.FRAME2.grid(row = 0, column = 0, padx = 140, pady = 5)
        # self.FRAME1.pack(padx= 10, pady = 10, expand = True)
        # self.FRAME1.place(relx = 0, rely= 0)
        # self.FRAME1.place(relx = 0.1, rely= 0.1, anchor = customtkinter.NW)
        self.FRAME2.place(relx = 0.155, rely= 0.008)

main_app = App(900, 700)