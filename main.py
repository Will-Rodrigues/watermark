from tkinter import *
from PIL import ImageTk, Image

watermark = Image.open("Example.jpg")

def putWatermark ():  
    url = entry1.get()
    img = Image.open(url)
    img.paste(watermark)
    img = img.save('Img_watermark.jpg')


root = Tk()
root.geometry("700x500")
root.tk.call('tk', 'scaling', 1.5)

canvas1 = Canvas(root, width = 400, height = 300)
entry1 = Entry(root) 
canvas1.create_window(200, 140, window=entry1)
search_button = Button(text='Put Watermark', command=putWatermark)
canvas1.create_window(200, 180, window=search_button)
canvas1.pack()

root.mainloop()
