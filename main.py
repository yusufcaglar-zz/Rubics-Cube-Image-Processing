import tkinter as tk
from tkinter.filedialog import askopenfile
import PIL
from PIL import Image, ImageTk
import numpy as np
import cv2
import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))
window = tk.Tk()
window.title("Image Processing - HW #1")
window.iconbitmap("Yildiz_Technical_University_Logo.ico")

# Variables
color_selection = 0
image_check = [0, 0, 0, 0, 0]
img = [0, 0, 0, 0, 0]
addr = ["", "", "", "", ""]

click_counter = 0
lower_white = [0, 0, 0]
upper_white = [0, 0, 0]
lower_red = [0, 0, 0]
upper_red = [0, 0, 0]
lower_blue = [0, 0, 0]
upper_blue = [0, 0, 0]
lower_orange = [0, 0, 0]
upper_orange = [0, 0, 0]
lower_green = [0, 0, 0]
upper_green = [0, 0, 0]
lower_yellow = [0, 0, 0]
upper_yellow = [0, 0, 0]

rgb_img = [0, 0, 0, 0, 0]
rgb_check = [0, 0, 0, 0, 0]

#Canvas Image Setting
def browse(i):
    global image_check
    global color_selection
    global rgb_check

    if 1 != image_check[i]:
        file = askopenfile(
            initialdir = BASEDIR,
            title = "Choose the image file",
            filetypes = [("Image Files", "*.jpg *.jpeg *.png *.bmp *.tmp")]
        )

        if file is not None:
            global img
            global addr
            global label
            global hsi_img

            addr[i] = file.name
            img[i] = Image.open(addr[i])
            img[i] = img[i].resize((182, 162), Image.ANTIALIAS)
            img[i] = ImageTk.PhotoImage(image = img[i])
            canvas[i].create_image(0, 0, image = img[i], anchor = "nw")

            image_check[i] = 1

            if (image_check[0] == 1 and image_check[1] == 1 and image_check[2] == 1
                and image_check[3] == 1 and image_check[4] == 1):
                # Label
                label = tk.Label(window, text="Now by clicking images above select 2 pixels per color at different surfaces for each image."
                                              "\n With order of 'white, red, blue, orange, green, and yellow'.",
                                 font=('Helvetica 12'), pady=5);
                label.grid(row=1, column=0, columnspan=5)

                color_selection = 1
    elif color_selection == 1 and 1 != rgb_check[i]:
        global rgb_img

        # Color Selection
        image = cv2.imread(addr[i])
        image = cv2.resize(image, (360, 320))

        def mouseRGB(event, x, y, flags, param):
            global click_counter
            global lower_white
            global upper_white
            global lower_red
            global upper_red
            global lower_blue
            global upper_blue
            global lower_orange
            global upper_orange
            global lower_green
            global upper_green
            global lower_yellow
            global upper_yellow

            if event == cv2.EVENT_LBUTTONDOWN:
                click_counter = click_counter + 1

                colorsR = image[y, x, 0]
                colorsG = image[y, x, 1]
                colorsB = image[y, x, 2]

                images = cv2.resize(image, (182, 162))

                if click_counter == 1:
                    lower_white = [colorsR, colorsG, colorsB]
                    upper_white = [colorsR, colorsG, colorsB]
                elif click_counter == 2:
                    if colorsR < lower_white[0]:
                        lower_white[0] = colorsR
                    if colorsG < lower_white[1]:
                        lower_white[1] = colorsG
                    if colorsB < lower_white[2]:
                        lower_white[2] = colorsB

                    if colorsR > upper_white[0]:
                        upper_white[0] = colorsR
                    if colorsG > upper_white[1]:
                        upper_white[1] = colorsG
                    if colorsB > upper_white[2]:
                        upper_white[2] = colorsB
                elif click_counter == 3:
                    lower_red = [colorsR, colorsG, colorsB]
                    upper_red = [colorsR, colorsG, colorsB]
                elif click_counter == 4:
                    if colorsR < lower_red[0]:
                        lower_red[0] = colorsR
                    if colorsG < lower_red[1]:
                        lower_red[1] = colorsG
                    if colorsB < lower_red[2]:
                        lower_red[2] = colorsB

                    if colorsR > upper_red[0]:
                        upper_red[0] = colorsR
                    if colorsG > upper_red[1]:
                        upper_red[1] = colorsG
                    if colorsB > upper_red[2]:
                        upper_red[2] = colorsB
                elif click_counter == 5:
                    lower_blue = [colorsR, colorsG, colorsB]
                    upper_blue = [colorsR, colorsG, colorsB]
                elif click_counter == 6:
                    if colorsR < lower_blue[0]:
                        lower_blue[0] = colorsR
                    if colorsG < lower_blue[1]:
                        lower_blue[1] = colorsG
                    if colorsB < lower_blue[2]:
                        lower_blue[2] = colorsB

                    if colorsR > upper_blue[0]:
                        upper_blue[0] = colorsR
                    if colorsG > upper_blue[1]:
                        upper_blue[1] = colorsG
                    if colorsB > upper_blue[2]:
                        upper_blue[2] = colorsB
                elif click_counter == 7:
                    lower_orange = [colorsR, colorsG, colorsB]
                    upper_orange = [colorsR, colorsG, colorsB]
                elif click_counter == 8:
                    if colorsR < lower_orange[0]:
                        lower_orange[0] = colorsR
                    if colorsG < lower_orange[1]:
                        lower_orange[1] = colorsG
                    if colorsB < lower_orange[2]:
                        lower_orange[2] = colorsB

                    if colorsR > upper_orange[0]:
                        upper_orange[0] = colorsR
                    if colorsG > upper_orange[1]:
                        upper_orange[1] = colorsG
                    if colorsB > upper_orange[2]:
                        upper_orange[2] = colorsB
                elif click_counter == 9:
                    lower_green = [colorsR, colorsG, colorsB]
                    upper_green = [colorsR, colorsG, colorsB]
                elif click_counter == 10:
                    if colorsR < lower_green[0]:
                        lower_green[0] = colorsR
                    if colorsG < lower_green[1]:
                        lower_green[1] = colorsG
                    if colorsB < lower_green[2]:
                        lower_green[2] = colorsB

                    if colorsR > upper_green[0]:
                        upper_green[0] = colorsR
                    if colorsG > upper_green[1]:
                        upper_green[1] = colorsG
                    if colorsB > upper_green[2]:
                        upper_green[2] = colorsB
                elif click_counter == 11:
                    lower_yellow = [colorsR, colorsG, colorsB]
                    upper_yellow = [colorsR, colorsG, colorsB]
                else:
                    if colorsR < lower_yellow[0]:
                        lower_yellow[0] = colorsR
                    if colorsG < lower_yellow[1]:
                        lower_yellow[1] = colorsG
                    if colorsB < lower_yellow[2]:
                        lower_yellow[2] = colorsB

                    if colorsR > upper_yellow[0]:
                        upper_yellow[0] = colorsR
                    if colorsG > upper_yellow[1]:
                        upper_yellow[1] = colorsG
                    if colorsB > upper_yellow[2]:
                        upper_yellow[2] = colorsB

                    cv2.destroyAllWindows()
                    rgb_check[i] = 1
                    click_counter = 0

                    if (rgb_check[0] == 1 and rgb_check[1] == 1 and rgb_check[2] == 1
                            and rgb_check[3] == 1 and rgb_check[4] == 1):
                        # Label
                        label.config(text="RGB Color Detection Is Below")

                lower_white = np.array(lower_white, dtype="uint8")
                upper_white = np.array(upper_white, dtype="uint8")
                lower_red = np.array(lower_red, dtype="uint8")
                upper_red = np.array(upper_red, dtype="uint8")
                lower_blue = np.array(lower_blue, dtype="uint8")
                upper_blue = np.array(upper_blue, dtype="uint8")
                lower_orange = np.array(lower_orange, dtype="uint8")
                upper_orange = np.array(upper_orange, dtype="uint8")
                lower_green = np.array(lower_green, dtype="uint8")
                upper_green = np.array(upper_green, dtype="uint8")
                lower_yellow = np.array(lower_yellow, dtype="uint8")
                upper_yellow = np.array(upper_yellow, dtype="uint8")

                mask_white = cv2.inRange(images, lower_white, upper_white)
                mask_red = cv2.inRange(images, lower_red, upper_red)
                mask_blue = cv2.inRange(images, lower_blue, upper_blue)
                mask_orange = cv2.inRange(images, lower_orange, upper_orange)
                mask_green = cv2.inRange(images, lower_green, upper_green)
                mask_yellow = cv2.inRange(images, lower_yellow, upper_yellow)

                output_white = cv2.bitwise_and(images, images, mask=mask_white)
                output_red = cv2.bitwise_and(images, images, mask=mask_red)
                output_blue = cv2.bitwise_and(images, images, mask=mask_blue)
                output_orange = cv2.bitwise_and(images, images, mask=mask_orange)
                output_green = cv2.bitwise_and(images, images, mask=mask_green)
                output_yellow = cv2.bitwise_and(images, images, mask=mask_yellow)

                output_mask = cv2.bitwise_or(output_white, output_red, mask=None)
                output_mask = cv2.bitwise_or(output_mask, output_blue, mask=None)
                output_mask = cv2.bitwise_or(output_mask, output_orange, mask=None)
                output_mask = cv2.bitwise_or(output_mask, output_green, mask=None)
                output_mask = cv2.bitwise_or(output_mask, output_yellow, mask=None)

                # RGB Canvas
                rgb_canvas = tk.Canvas(window, width=180, height=160)
                rgb_canvas.config(highlightthickness=2, highlightbackground="black")
                rgb_canvas.grid(row=2, column=i, padx=10, pady=10)
                output_mask = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(output_mask))
                rgb_img[i] = output_mask
                rgb_canvas.create_image(0, 0, image=rgb_img[i], anchor="nw")

                # Label
                label2 = tk.Label(window,
                                  text="HSI Color Detection Is Below",
                                  font=('Helvetica 12'), pady=5);
                label2.grid(row=3, column=0, columnspan=5)

        cv2.imshow(f"Image {i + 1}", image)
        cv2.setMouseCallback(f"Image {i + 1}", mouseRGB)

#Canvas Creation
canvas = (tk.Canvas(window, width = 180, height = 160), tk.Canvas(window, width = 180, height = 160),
          tk.Canvas(window, width = 180, height = 160), tk.Canvas(window, width = 180, height = 160),
          tk.Canvas(window, width = 180, height = 160))
for i in range(5):
    canvas[i].create_text(90, 80, text = "Click to insert image", fill = "black", font = ('Helvetica 12 bold'))
    canvas[i].config(highlightthickness = 2, highlightbackground = "black")
    canvas[i].grid(row = 0, column = i, padx = 10, pady = 10)

    if i == 0:
        canvas[i].bind("<Button-1>", lambda event:browse(0))
    elif i == 1:
        canvas[i].bind("<Button-1>", lambda event: browse(1))
    elif i == 2:
        canvas[i].bind("<Button-1>", lambda event: browse(2))
    elif i == 3:
        canvas[i].bind("<Button-1>", lambda event: browse(3))
    else:
        canvas[i].bind("<Button-1>", lambda event:browse(4))

window.mainloop()