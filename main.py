from tkinter import filedialog
from tkinter import *
from PIL import Image


# -- Create Watermark -- #

def add_watermark():
    selected_img = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("JPG files", "*.jpg"), ("PNG files", "*.png")))

    if selected_img:
        orig_img = Image.open(selected_img)
        watermark = Image.open("logo.png")
        watermark_adj = watermark.resize((int(orig_img.width * .4), int(orig_img.height * .15)))
        new_img = orig_img.copy()
        new_img.paste(im=watermark_adj, box=(10, orig_img.height - watermark_adj.height - 10), mask=watermark_adj)
        new_img.save("watermarked-img.png")

        displayed_img = Image.open("watermarked-img.png")
        displayed_img.show()


# -- UI Setup -- #

app = Tk()
app.title("Image Watermarker")
app.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
header = Label(image=logo_img)
header.grid(row=0, column=0, columnspan=2)

upload_but = Button(text="Select Image",
                    width=20,
                    command=add_watermark)
upload_but.grid(row=1, column=0,
                pady=(20, 0))

quit_but = Button(text="Quit",
                  width=20,
                  command=app.destroy)
quit_but.grid(row=1, column=1,
              pady=(20, 0))

file_explorer = Label()

app.mainloop()
