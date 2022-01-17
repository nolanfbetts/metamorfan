import json
import random
import bpy

# CONSTANTS
countries_file = open("country_data.json")
COUNTRIES_DATA = json.load(countries_file)

skin_file = open("skin_color.json")
SKIN_DATA = json.load(skin_file)

hair_file = open("hair_color.json")
HAIR_DATA = json.load(hair_file)

# Main OBJECT Tracker
ACTIVE_OBJECTS = []

# Main COLLECTIONS Tracker
ACTIVE_COLLECTIONS = []

# ---------------------------------------------------------------------------------- #
# Definition: srgb_to_linearrgb
# Purpose: Convert srgb to linear rgb
# Input: c (individual color of srgb)
# Ouput: color as linear r,g, or b in decimal format
# ---------------------------------------------------------------------------------- #
def srgb_to_linearrgb(c):
    if c < 0:
        return 0
    elif c < 0.04045:
        return c / 12.92
    else:
        return ((c + 0.055) / 1.055) ** 2.4


# ---------------------------------------------------------------------------------- #
# Definition: hex_to_rgb
# Purpose: Convert hexidecial value to rgb tuple
# Input: hexidecimal value
# Ouput: RGB tuple in decimal format
# ---------------------------------------------------------------------------------- #
def hex_to_rgb(hex_input, alpha=1):
    h = int("0x" + hex_input[1:7], 16)
    r = (h & 0xFF0000) >> 16
    g = (h & 0x00FF00) >> 8
    b = h & 0x0000FF
    return tuple([srgb_to_linearrgb(c / 0xFF) for c in (r, g, b)] + [alpha])


# ---------------------------------------------------------------------------------- #
# Definition: random_creation_example
# Purpose: Randomly select a value for NFT creation to promote random order
# Input: None
# Ouput: None
# ---------------------------------------------------------------------------------- #
def random_creation_example():
    test = list(range(10))
    print(test)
    for x in range(10):
        value = random.choice(test)
        print(value)
        test.remove(value)
        print(test)


# ---------------------------------------------------------------------------------- #
# Definition: set_texture_image
# Purpose: set loaded image to material
# Input: material, f_name
# Ouput: None
# ---------------------------------------------------------------------------------- #
def set_texture_image(material, f_name):
    node_tex = bpy.data.materials[material].node_tree.nodes["Image Texture"]
    node_tex.image = bpy.data.images[f_name]


# ---------------------------------------------------------------------------------- #
# Definition: position_letters
# Purpose: set letter to appropraite position based on country code
# Input: country
# Ouput: None
# ---------------------------------------------------------------------------------- #
def position_letters(country):
    # NEED TO ADD EDGE CASE FOR REPEATING LETTER COUNTRIES
    # get the appropriate country letters
    alpha_3_code = COUNTRIES_DATA[country]["alpha-3-code"]
    first, second, accent = (
        alpha_3_code[0].lower(),
        alpha_3_code[1].lower(),
        alpha_3_code[2].lower(),
    )
    # add letters to active list
    ACTIVE_OBJECTS.append(first)
    ACTIVE_OBJECTS.append(second)
    ACTIVE_OBJECTS.append(accent)
    print(ACTIVE_OBJECTS)
    # set objects to true for render view
    bpy.data.objects[first].hide_render = False
    bpy.data.objects[second].hide_render = False
    bpy.data.objects[accent].hide_render = False
    # position letters accordingly
    bpy.data.objects[first].location = (-0.9, -0.7, -3.3)
    bpy.data.objects[second].location = (0, -0.7, -3.3)
    bpy.data.objects[accent].location = (0.9, -0.7, -3.3)
    return 0


# ---------------------------------------------------------------------------------- #
# Definition: set_country_colors
# Purpose: set the primary, secondary and accent colors by country
# Input: country
# Ouput: None
# ---------------------------------------------------------------------------------- #
def set_country_colors(country):
    # convert the country colors to linear hex
    primary = hex_to_rgb(COUNTRIES_DATA[country]["primary"])
    seconday = hex_to_rgb(COUNTRIES_DATA[country]["secondary"])
    accent = hex_to_rgb(COUNTRIES_DATA[country]["accent"])
    # set the primary, secondary, and accent color in blender
    bpy.data.materials["primary"].node_tree.nodes["Principled BSDF"].inputs[
        "Base Color"
    ].default_value = primary
    bpy.data.materials["secondary"].node_tree.nodes["Principled BSDF"].inputs[
        "Base Color"
    ].default_value = seconday
    bpy.data.materials["accent"].node_tree.nodes["Principled BSDF"].inputs[
        "Base Color"
    ].default_value = accent


# ---------------------------------------------------------------------------------- #
# Definition: set_hair_color
# Purpose: set the character hair color
# Input: None
# Ouput: None
# ---------------------------------------------------------------------------------- #
def set_hair_color():
    hair_options = list(HAIR_DATA["Hair"].keys())
    hair_color = random.choice(hair_options)
    print(hair_color, HAIR_DATA["Hair"][hair_color])
    hair_rgb = hex_to_rgb(HAIR_DATA["Hair"][hair_color])
    bpy.data.materials["hair"].node_tree.nodes["Principled BSDF"].inputs[
        "Base Color"
    ].default_value = hair_rgb


# ---------------------------------------------------------------------------------- #
# Definition: set_skin_color
# Purpose: set the character hair color
# Input: None
# Ouput: None
# ---------------------------------------------------------------------------------- #
def set_skin_color():
    skin_options = list(SKIN_DATA["Skin"].keys())
    skin_color = random.choice(skin_options)
    print(skin_color, SKIN_DATA["Skin"][skin_color])


# ---------------------------------------------------------------------------------- #
# Definition: render_nft
# Purpose: render the NFT as a PNG
# Input: number
# Ouput: None (PNG file to directory)
# ---------------------------------------------------------------------------------- #
def render_nft(number):
    bpy.context.scene.render.image_settings.file_format = "PNG"
    file_path = (
        "/Users/nolanbetts/Blender/renders/metamorfan/final/" + str(number) + ".png"
    )
    bpy.context.scene.render.filepath = file_path
    bpy.ops.render.render(write_still=True)


# ---------------------------------------------------------------------------------- #
# Definition: reset_scene
# Purpose: set all active attributes to hide in render view
# Input: None
# Ouput: None
# ---------------------------------------------------------------------------------- #
def reset_scene():
    for obj in ACTIVE_OBJECTS:
        bpy.data.objects[obj].hide_render = True
    for col in ACTIVE_COLLECTIONS:
        bpy.data.collections[col].hide_render = True


# random_creation_example()
country = "Ireland"
position_letters(country)
set_texture_image("flag", COUNTRIES_DATA[country]["alpha-2-code"].lower() + ".png")
set_country_colors(country)
set_skin_color()
set_hair_color()
render_nft("1")
reset_scene()
