import tkinter

def upload_image():
    pass

root = tkinter.Tk()
root.title("HTR Demo")
root.geometry("900x720")

header = tkinter.Frame(root)
header.pack(fill="x", side="top")

button = tkinter.Button(header, text="Upload Image", command=upload_image)
button.pack(side="left", padx=10, pady=10)

root.mainloop()
