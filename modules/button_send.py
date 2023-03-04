import customtkinter as ctk
import modules.screen_app as m_app
import modules.text_input as m_input

button_width = 40
button_height = 40
# text_size = 15
margin_left = 40
button_color = "orange"
text_color = "black"


def send_message():
    button_label = ctk.CTkLabel(
        master = m_app.main_app, 
        text = m_input.text.get(),
        font = m_input.font_size
    )
    button_label.place(x = 890, 
                       y = 105,
                       anchor = ctk.SE)
    m_input.text.set("")
    # button_label.pack(padx= 10, pady= 20)
    # button_label.bind()
    


send_button = ctk.CTkButton(
    master = m_app.main_app, 
    text =">",
    text_color = text_color,
    # text_size = text_size,
    width = button_width,
    height = button_height,
    fg_color = button_color,
    command= send_message
)

send_button.place(
    x = 891, 
    y = 691,
    anchor = ctk.SE
)
# send_button.place(
#     x = 1, 
#     y = 1,
#     anchor = ctk.SE
# )
