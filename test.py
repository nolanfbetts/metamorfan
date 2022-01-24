import json
import random

disciplines_file = open("metamorfan/data/disciplines.json")
DISCIPLINES_DATA = json.load(disciplines_file)

types_file = open("metamorfan/data/types.json")
TYPES_DATA = json.load(types_file)

events_file = open("metamorfan/data/events.json")
EVENTS_DATA = json.load(events_file)

attributes_file = open("metamorfan/data/attributes.json")
ATTRIBUTES_DATA = json.load(attributes_file)

hair_file = open("metamorfan/data/hair.json")
HAIR_DATA = json.load(hair_file)

skin_file = open("metamorfan/data/skin_color.json")
SKIN_DATA = json.load(skin_file)


def set_background():
    b = random.randrange(0, 10, 1)
    if b in range(0, 7):
        return "Flag"
    elif b in range(7, 9):
        ACTIVE_COLLECTIONS.append("background.mountains")
        bpy.data.collections["background.mountains"].hide_render = False
        return "Mountains"
    else:
        ACTIVE_COLLECTIONS.append("snowy.day")
        bpy.data.collections["snowy.day"].hide_render = False
        return "Snowday"


# print(list(DISCIPLINES_DATA["Disciplines"].keys()))
for x in range(100):
    print(set_background())


# test = [
#     "China",
#     "Canada",
#     "ROC",
#     "Finland",
#     "Sweden",
#     "Czech Republic",
#     "United States",
#     "Germany",
#     "Switzerland",
#     "Slovakia",
#     "Latvia",
#     "Denmark",
#     "Switzerland",
#     "Japan",
# ]
# test.sort()
# print(test)

# ---------------------------------------------------------------------------------- #
# Loads all country flags into blender (crashes blender not sure why)
# ---------------------------------------------------------------------------------- #
# alpha2 = countries_data[each]["alpha-2-code"].lower()
# f_path = "//../Downloads/flags/" + alpha2 + ".png"
# f_name = alpha2 + ".png"
# bpy.ops.image.open(
#     filepath=f_path,
#     directory="/Users/nolanbetts/Downloads/flags/",
#     files=[{"name": f_name, "name": f_name}],
#     show_multiview=False,
# )
# bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)


# ---------------------------------------------------------------------------------- #
# Loads all country flags into materials
# ---------------------------------------------------------------------------------- #
# countries_file = open("country_data.json")
# countries_data = json.load(countries_file)
# for each in countries_data:
#     alpha2Code = countries_data[each]["alpha-2-code"].lower()
#     mat = bpy.data.materials.new(name=alpha2Code)
#     mat.use_nodes = True
#     nodes = mat.node_tree.nodes
#     nodes.clear()
#     # Add the Principled Shader node
#     node_principled = nodes.new(type="ShaderNodeBsdfPrincipled")
#     node_principled.location = 0, 0
#     # Add the Image Texture node
#     node_tex = nodes.new("ShaderNodeTexImage")
#     # Assign the image
#     img = bpy.data.images.get(alpha2Code + ".png")
#     if img:
#         node_tex.image = img
#     node_tex.location = -400, 0
#     # Add the Output node
#     node_output = nodes.new(type="ShaderNodeOutputMaterial")
#     node_output.location = 400, 0

#     # Link all nodes
#     links = mat.node_tree.links
#     link = links.new(node_tex.outputs["Color"], node_principled.inputs["Base Color"])
#     link = links.new(node_principled.outputs["BSDF"], node_output.inputs["Surface"])
