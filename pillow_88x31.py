# -------------------- IMPORTS --------------------
from PIL import Image, ImageDraw, ImageFont
# -------------------- TRAITEMENT DES IMAGES --------------------

def create_image(path):
    IMAGE = Image.new("RGB", (88, 31), color=(255, 255, 255))
    IMAGE.save(path)
    return IMAGE

def hex_code_to_rgb(hex): # BETA
    """
    Convertit les codes HEX en tuple RGB 
    """
    assert type(hex) == str, "PBLM AVEC LE TYPE DU CODE HEX"

    if hex[0] == "#":
        hex = hex[1:]

    assert len(hex) == 6, "PBLM AVEC LA LONGUEUR DU CODE HEX"

    R = hex[:2] # [start:stop:step] stop EXCLUS
    G = hex[2:4]
    B = hex[4:]

    hex_to_dec = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }

    R = hex_to_dec[R[0]] * 16 + hex_to_dec[R[1]]
    G = hex_to_dec[G[0]] * 16 + hex_to_dec[G[1]]
    B = hex_to_dec[B[0]] * 16 + hex_to_dec[B[1]]

    return (R, G, B)

# DESSINER DES RECTANGLES

# DRAPEAU VERTICAL
def vertical_flag(image, colors, width, height):
    DRAW = ImageDraw.Draw(image)

    for i in range(len(colors)):
        DRAW.rectangle([((i * width) // len(colors), 0), ( ((i+1) * width) // len(colors), height)], fill=colors[i])
    return None

# DRAPEAU HORIZONTAL
def horizontal_flag(image, colors, width, height):
    DRAW = ImageDraw.Draw(image)

    for i in range(len(colors)):
        DRAW.rectangle([(0, (i * height) // len(colors)), (width , ((i+1) * height) // len(colors))], fill=colors[i])
    return None


# ICONE 

def add_icon(image, icon, position, color = (255, 255, 255)): # BETA
    # MODIFIER LES COULEURS DES PIXELS
    for x in range(icon.width):
        for y in range(icon.height):
            r, g, b, o = icon.getpixel((x, y))
            if r == 255 and g == 255 and b == 255:
                # ICI DONNER LA POSSIBILITE DE MODIFIER LA COULEUR DE L'ICONE
                r, g, b = color
                px = (r, g, b, 255) # NOUVELLE OPACITE A 255
                icon.putpixel((x, y), px)

    image.paste(icon, position, icon)
    return None

# TEXTE

def write_text(image, text, color, font = ImageFont.truetype("Silkscreen-Regular.ttf", 17), position = None):    
    DRAW = ImageDraw.Draw(image)
    # D'ABORD TROUVER LES COORDONNEES POUR CENTRER LE TEXTE SI LA POSITION N'A PAS ETE FOURNIE
    POS = position
    if POS == None:
        text_width = DRAW.textlength(text, font=font)
        text_height = font.size

        x_text = (image.width - text_width) // 2
        y_text = ((image.height - text_height) // 2)

        POS = (x_text, y_text)

    # ON PEUT MAINTENANT ECRIRE LE TEXTE
    DRAW.text(POS, text, font=font, fill=color)
    return None

def save(IMAGE, PATH):
    IMAGE.save(PATH)
