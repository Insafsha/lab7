#доп задание
import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

def get_fox():
    response = requests.get("https://randomfox.ca/floof/")
    return response.json().get("image") if response.status_code == 200 else None

def update_image():
    image_url = get_fox()
    if image_url:
        response = requests.get(image_url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content)).resize((400, 400), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img

root = tk.Tk()
root.title("Случайная лиса")
root.geometry("450x500")
image_label = tk.Label(root)
image_label.pack()
tk.Button(root, text="Новая лиса!", command=update_image, font=("Arial", 14)).pack(pady=10)
update_image()
root.mainloop()
