import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from PIL import Image, ImageDraw

def select_file_1():
    global file_path_1
    file_path_1 = filedialog.askopenfilename()
    label_file_1.config(text="Выбранный файл 1: " + file_path_1)

def select_file_2():
    global file_path_2
    file_path_2 = filedialog.askopenfilename()
    label_file_2.config(text="Выбранный файл 2: " + file_path_2)

def convert_and_save():
    if file_path_1 and file_path_2:
        image = Image.open(file_path_1)
        replacement_image = Image.open(file_path_2)
        x1, y1, x2, y2 = 14, 125, 239, 263
        width = x2 - x1
        height = y2 - y1
        replacement_image = replacement_image.resize((width, height))
        image.paste(replacement_image, (x1, y1))
        image.save('final_image.png')
        label_result.config(text="Итоговое изображение сохранено как 'final_image.png'")

file_path_1 = ""
file_path_2 = ""

root = tk.Tk()
root.geometry("400x400")
root.title("sampgui creater")

button_select_file_2 = tk.Button(root, text="Выбрать фон", command=select_file_2)
button_convert_and_save = tk.Button(root, text="Создать sampgui", command=convert_and_save)

label_file_1 = tk.Label(root, text="Выбранный sampgui: ")
label_file_2 = tk.Label(root, text="Выбранный фон: ")
label_result = tk.Label(root, text="")

# Создаем PhotoImage изображение
image = PhotoImage(file="bitton.png")

# Создаем кнопку с изображением и прикрепляем обработчик событий
image_button = tk.Button(root, image=image, command=select_file_1)
image_button.image = image  # Не забудьте сохранить ссылку на изображение

image_button.pack()
label_file_1.pack()
button_select_file_2.pack()
label_file_2.pack()
button_convert_and_save.pack()
label_result.pack()

root.mainloop()
