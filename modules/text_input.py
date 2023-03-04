import customtkinter as ctk
import modules.screen_app as m_app

width_input = 535
height_input = 40

font_size = ctk.CTkFont(
    family= "Arial",
    size= 15,
    weight= "bold"
)

text = ctk.StringVar()

text_input = ctk.CTkEntry(
    master= m_app.main_app,
    width= width_input,
    height= height_input,
    fg_color= "grey",
    text_color= "black",
    font= font_size,
    textvariable= text
)

# text_input.place(x = m_app.main_app.APP_WIDTH // 2, y = m_app.main_app.APP_HEIGHT - height_input // 2, anchor = ctk.CENTER)
text_input.place(x = 312, y = 651)

# text_input.insert(0, "0")
# text_input.pack( padx = 10, pady = 20)
# text_input.get()
# text_input.setvar()
# text.set("dfv")
