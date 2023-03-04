import customtkinter as ctk 

# class My_Frame(ctk.CTkFrame):
#     def __init__(self, text, master, width, height, border_width, **kwargs):
#         super().__init__(master = master,width = width, height = height, border_width = border_width, **kwargs)
#         # self.LABEL = ctk.CTkLabel(self, text= text)
#         # self.LABEL.grid(row= 0, column= 0, padx = 10, pady = 10)


class My_Frame(ctk.CTkFrame):
    def __init__(self, text, text_color, master, width, height, border_width, fg_color, **kwargs):
        super().__init__(master = master, 
                        width = width, 
                        height = height, 
                        border_width = border_width, 
                        fg_color = fg_color, 
                        **kwargs)

        self.LABEL = ctk.CTkLabel(self, text= text, text_color = text_color)
        self.LABEL.place(relx = 0.2, rely = 0.01,anchor = ctk.NW )

