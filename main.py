import tkinter as tk
from tkinter import colorchooser, font
import pillow_88x31 as pil

# CREER LA FENETRE
window = tk.Tk()
window.title = "88x31 Project"
window.geometry("880x310")
window.resizable(False, False)
window.config(bg="#EE92C2")

# POLICE
FONT = font.Font(family="Times New Roman", size=12)

# CREER UN LABEL POUR AFFICHER DU TEXTE
label = tk.Label(window, text="Create your own 88x31 style button !", font=FONT, bg="#EE92C2")
label.pack()

label_2 = tk.Label(window, text="Use the buttons below to get your 88x31 button ! It will be saved for every modification in the \"button.png\" file !", font=FONT, bg="#EE92C2")
label_2.pack()

class Button88x31:
    def __init__(self):
        self.path = "button.png"
        self.image = pil.create_image(self.path)
        self.photo = None
        self.label = None

        self.entries = {}
        self.colors = []
        self.text = ""
        self.text_color = (0, 0, 0)
        self.template = "horizontal"
        self.create_elements()
        self.display_preview()

    def create_elements(self):
        menus_color = "#9AC4F8"
        reset_button_color = "#9A275A"
        button_color = "#99EDCC"
        entry_color = "#99EDCC"

        menu_2 = tk.Frame(window, bg=menus_color)
        menu_2.pack(fill=tk.X, side=tk.BOTTOM)

        button_vertical = tk.Button(menu_2, text="Vertical lines", bg=button_color,command=lambda: self.set_template_to("vertical"))
        button_vertical.pack(side=tk.LEFT, padx=8, pady=4)

        button_horizontal = tk.Button(menu_2, text="Horizontal lines", bg=button_color,command=lambda: self.set_template_to("horizontal"))
        button_horizontal.pack(side=tk.RIGHT, padx=8, pady=4)

        label_c = tk.Label(menu_2, text="Made with ❤ by M_", bg=menus_color)
        label_c.pack(padx=8, pady=4)

        menu = tk.Frame(window, bg=menus_color)
        menu.pack(fill=tk.X, side=tk.BOTTOM)

        button_clear = tk.Button(menu, text="Clear", command=self.reset, bg=reset_button_color)
        button_clear.pack(side=tk.LEFT, padx=8, pady=4)

        button_color_choose = tk.Button(menu, text="Add a Color", bg=button_color, command=self.add_color)
        button_color_choose.pack(side=tk.LEFT, padx=8, pady=4)

        button_remove_color = tk.Button(menu, text="Remove last color", bg=button_color, command=self.remove_color)
        button_remove_color.pack(side=tk.LEFT, padx=8, pady=4)

        button_text = tk.Button(menu, text="Display the text", bg=button_color, command=self.add_text)
        button_text.pack(side=tk.RIGHT, padx=8, pady=4)   

        text_entry = tk.Entry(menu, bg=entry_color)
        text_entry.pack(side=tk.RIGHT, padx=8, pady=4)
        self.entries["display_text"] = text_entry

        text_entry_label = tk.Label(menu, text="Enter here the text you want to display:", bg=menus_color)
        text_entry_label.pack(side=tk.RIGHT, padx=15, pady=4)

    def add_color(self):
        color = colorchooser.askcolor()
        if color[0] != None:
            self.colors.append(color[0]) # RGB TUPLE
        self.display_preview()
    
    def remove_color(self):
        if self.colors != []:
            self.colors.pop()
        self.display_preview()

    def set_template_to(self, template):
        self.template = template
        self.display_preview()

    def add_text(self):
        text = self.entries["display_text"].get()
        self.text = text
        self.display_preview()
    
    def reset(self):
        self.entries = {}
        self.colors = []
        self.text = ""
        self.text_color = (0, 0, 0)
        self.template = "horizontal"
        self.display_preview()

    def save_a_version(self):
        pass

    def display_preview(self):
        """
        Permet d'afficher le bouton 88x31
        """
        # D'ABORD LE MOTIF
        if self.colors == []:
            pil.horizontal_flag(self.image, [(255, 255, 255)], self.image.width, self.image.height)
        if self.template == "horizontal":
            pil.horizontal_flag(self.image, self.colors, self.image.width, self.image.height)
        elif self.template == "vertical":
            pil.vertical_flag(self.image, self.colors, self.image.width, self.image.height)
        # ENSUITE UN ICONE A AFFICHER
        if False:
            pass

        # ENSUITE LE TEXTE A AFFICHER
        pil.write_text(self.image, self.text, self.text_color)

        # ENFIN ON ENREGISTRE
        pil.save(self.image, self.path)

        # ON AFFICHE SUR LA FENETRE L'IMAGE
        self.photo = tk.PhotoImage(file="button.png")
        if self.label != None:
            self.label.destroy() # POUR REMPLACER LE LABEL EXISTANT ON DOIT FAIRE DE LA PLACE
        self.label = tk.Label(window, image=self.photo)
        self.label.pack()

B = Button88x31()
window.mainloop()