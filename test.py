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


def set_type():
    t = random.randrange(0, 20, 1)
    if t in range(0, 15):
        bpy.data.objects["eye"].hide_render = False
        return "Human"
    elif t in range(15, 17):
        bpy.data.objects["eye"].hide_render = False
        ACTIVE_COLLECTIONS.append("cyborg.face")
        bpy.data.objects["cyborg.face"].hide_render = False
        return "Robotic"
    elif t in range(17, 19):
        bpy.data.objects["eye"].hide_render = True
        skin_hex = SKIN_DATA["Alien"]["green"]
        skin = hex_to_rgb(skin_hex)
            bpy.data.materials["skin"].node_tree.nodes["Principled BSDF"].inputs[
                "Base Color"
            ].default_value = skin
        ACTIVE_COLLECTIONS.append("alien.face")
        bpy.data.objects["alien.face"].hide_render = False
        return "Extraterrestrial"
    else:
        bpy.data.objects["eye"].hide_render = True
        skin_hex = SKIN_DATA["Snowman"]["white"]
        skin = hex_to_rgb(skin_hex)
            bpy.data.materials["skin"].node_tree.nodes["Principled BSDF"].inputs[
                "Base Color"
            ].default_value = skin
        ACTIVE_COLLECTIONS.append("snowman.face")
        bpy.data.objects["snowman.face"].hide_render = False
        return "Snowman"
    # hair_color = HAIR_DATA["Attributes"][discipline][gender]


# print(list(DISCIPLINES_DATA["Disciplines"].keys()))
for x in range(100):
    print(set_type())


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
