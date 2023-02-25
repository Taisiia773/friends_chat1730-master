import customtkinter as ctk 

class My_Frame(ctk.CTkFrame):
    def __init__(self, text, master, width, height, border_width, fg_color, **kwargs):
        super().__init__(master = master, 
                        width = width, 
                        height = height, 
                        border_width = border_width, 
                        fg_color = fg_color, 
                        **kwargs)

        # self.LABEL = ctk.CTkLabel(self, text= text)
        # self.LABEL.grid(row= 0, column= 0, padx = 10, pady = 10)
        self.LABEL = ctk.CTkLabel(self, text= text)
        self.LABEL.place(relx = 0.2, rely = 0.01,anchor = ctk.NW )
        # self.LABEL1 = ctk.CTkLabel(self, text= text)
        # self.LABEL1.place(relx = 0.5, rely = 0.01,anchor = ctk.NW )
