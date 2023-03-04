import os
import customtkinter as ctk
import PIL
import modules.screen_app as m_app

# def find_path_file(filename):
#     abs_path = __file__.split("\\")
#     del abs_path[-1]
#     abs_path = '\\'.join(abs_path)
#     abs_path = os.path.join(filename)
#     return abs_path

# # def load_image(self, direction= False): #Метод загрузки картинки
# #         path_image = create_path() #Переменная хранящяя заданый путь к картинке
# #         path_image = os.path.join(path_image, self.NAME_IMAGE) #Сшивает пути
# #         self.IMAGE = pygame.image.load(path_image) #Загружает картинку
# #         self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT)) #Задает размеры
# #         self.IMAGE = pygame.transform.flip(self.IMAGE, direction, False) #Подготавливает к загрузке

# # img = ImageTk.PhotoImage(Image.open("C:/Users/Public/Pictures/Sample Pictures/Lighthouse.jpg"))


# # img_background = ctk.CTkImage(master , 
# #                                             light_image = PIL.Image.open(im.find_path_file("images\\2.png")), 
# #                                             size = (self.APP_WIDTH, self.APP_HEIGHT))

# # class Image(ctk.CTkImage):
# #     def __init__(self, master, light_image, size, **kwargs):
# #         super().__init__(master = master,
# #                         light_image = light_image,
# #                         size = size, 
# #                         **kwargs)
        
    
# def image(master, light_image, size):
#     img = ctk.CTkButton(master = master,
#                            light_image = light_image,
#                            size = size)
#     return img
        
# img_background = image(master = m_app.main_app.FRAME4,
#                        light_image = PIL.Image.open(find_path_file("images\\2.png")),
#                        size = (m_app.main_app.APP_WIDTH, m_app.main_app.APP_HEIGHT)
#                        )

# img_background.place(relx = 0.343, rely= 0.094, anchor=ctk.CENTER)

# def find_path_file(filename):
#     abs_path = __file__.split("\\")
#     del abs_path[-1]
#     abs_path = '\\'.join(abs_path)
#     abs_path = os.path.join(filename)
#     return abs_path
    
# def image(master, light_image, size):
#     img = ctk.CTkImage(master = master,
#                            light_image = light_image,
#                            size = size)
#     return img
        
# img_background = image(master = m_app.main_app.FRAME4,
#                        light_image = PIL.Image.open(find_path_file("images\\2.png")),
#                        size = (m_app.main_app.APP_WIDTH, m_app.main_app.APP_HEIGHT)
#                        )

# img_background.place(relx = 0.343, rely= 0.094, anchor=ctk.CENTER)