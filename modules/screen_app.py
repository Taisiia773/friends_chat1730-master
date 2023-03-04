import customtkinter
import modules.create_frame as m_frame
import modules.image as im
import PIL
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
        # self.FRAME = customtkinter.CTkFrame(master=self, width=300, height= app_height)
        self.FRAME1 = m_frame.My_Frame(text= "Friendly Chat", text_color= "orange", master = self, width= 130, height= app_height - 10, border_width= None, fg_color= None)
        self.FRAME2 = m_frame.My_Frame(text= "Чати", text_color= "orange", master = self,  width= 165, height= app_height - 10, border_width= None, fg_color= None)
        self.FRAME3 = m_frame.My_Frame(text= None, text_color= None, master = self,  width= 588, height= 55, border_width= None, fg_color= None)
        self.FRAME4 = m_frame.My_Frame(text= None, text_color= None, master = self, width= 588, height= 630, border_width= None, fg_color= None)
        # self.IMAGE_LABEL1 = customtkinter.CTkLabel(master=self, text = None, image = self.PROJECT_IMAGE, bg_color='black')
        # self.PROJECT_IMAGE = customtkinter.CTkImage(master = self.FRAME4, light_image = PIL.Image.open(im.find_path_file("images\\2.png")), size = (self.APP_WIDTH, self.APP_HEIGHT))

        self.FRAME1.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.FRAME2.place(relx = 0.155, rely= 0.008)
        self.FRAME3.place(relx = 0.343, rely= 0.008)
        self.FRAME4.place(relx = 0.343, rely= 0.094)
        # self.IMAGE_LABEL1.place(relx = 0.343, rely= 0.094)
        # self.IMAGE_LABEL1.grid(row= 5, column= 5)
        # self.FRAME.grid(row = 0, column = 0, padx = 20, pady = 10)
        # self.FRAME.pack(padx= 10, pady = 10, expand = True)
        # self.FRAME.place(relx = 0, rely= 0)

main_app = App(900, 700)

 