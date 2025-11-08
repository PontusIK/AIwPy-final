import tkinter
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import aipi

file_types = [("Image files", "*jpg *png")]
gc_safe_zone = []
def upload_image():
    global path
    path = filedialog.askopenfilename(title="Select Image", filetypes=file_types)
    if not path:
        return
    
    try:
        img = Image.open(path)
        img.thumbnail((600, 400))
        tk_image = ImageTk.PhotoImage(img)
        gc_safe_zone.append(tk_image)
        image_label.config(image=tk_image)

    except Exception:
        messagebox.showerror("Could not open image")

def get_response():
    global ai_respone
    global path
    ai_respone.set(aipi.get_response(path))

root = tkinter.Tk()
root.title("HTR Demo")
root.geometry("900x720")

header = tkinter.Frame(root)
header.pack(fill="x", side="top")

upload_button = tkinter.Button(header, text="Upload Image", command=upload_image)
upload_button.pack(side="left", padx=10, pady=10)

response_button = tkinter.Button(header, text="Analyze", command=get_response)
response_button.pack(side="left", padx=10, pady=10)

image_label = tkinter.Label(root)
image_label.pack(fill="both", padx=10, pady=10)

output = tkinter.Frame(root)
output.pack(fill="x", side="bottom")

global ai_respone
ai_respone = tkinter.StringVar(value="...")
response_label = tkinter.Label(
    output,
    textvariable=ai_respone,
    anchor="w",
    padx=10
)
response_label.pack(fill="both", padx=10, pady=10)

root.mainloop()
