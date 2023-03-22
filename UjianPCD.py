import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

root = tk.Tk()
root.title('Ujian PCD')
root.geometry("900x500")

main_frame = tk.LabelFrame(root, text="Perbaikan Citra",padx=10,pady=10)
main_frame.pack(padx=100, pady=10)

label_frame = tk.LabelFrame(main_frame)
label_frame.pack(fill=tk.BOTH, padx=10, pady=10)

def browse_file():
    global img
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    image2 = img
    image3 = img
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
    label7 = tk.Label(label_frame ,image=img)
    label7.pack(side=tk.LEFT, padx=5)
    
    image2 = image2.resize((200,200))
    image2 = sharpened_image = image2.filter(ImageFilter.SHARPEN)
    photo2 = ImageTk.PhotoImage(image2)
    label8 = tk.Label(label_frame, image=photo2)
    label8.image = photo2
    label8.pack(side=tk.LEFT, padx=5)
    
    image3 = image3.resize((200,200))
    image3 = blurred_image = image3.filter(ImageFilter.BLUR)
    photo3 = ImageTk.PhotoImage(image3)
    label9 = tk.Label(label_frame, image=photo3)
    label9.image = photo3
    label9.pack(side=tk.LEFT, padx=5)

btnimage = tk.Button(main_frame, text="Search Image", command=browse_file)
label1 = tk.Label(main_frame, text="Original Image")
label2 = tk.Label(main_frame, text="Metode sharpen")
label3 = tk.Label(main_frame, text="Metode blur")

btnimage.pack(side=tk.LEFT, padx=5)
label1.pack(side=tk.LEFT, padx=5)
label2.pack(side=tk.LEFT, padx=100)
label3.pack(side=tk.LEFT, padx=5)

main_frame2 = tk.LabelFrame(root, text="Creator",padx=60,pady=5)
main_frame2.pack()

label4 = tk.Label(main_frame2, text="Nama : Wahyudi. Z")
label5 = tk.Label(main_frame2, text="NIM : F55121078")
label6 = tk.Label(main_frame2, text="Kelas : TI C")

label4.pack(side=tk.LEFT, padx=10)
label5.pack(side=tk.LEFT, padx=50)
label6.pack(side=tk.LEFT, padx=10)

root.mainloop()