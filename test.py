import json
import random
import bpy


bpy.data.objects["primary_spot"].data.color = (0.5, 0.5, 0.5)
bpy.data.objects["primary_spot_2"].data.color = (0.5, 0.5, 0.5)
bpy.data.objects["secondary_spot"].data.color = (0.0, 0.0, 0.0)
bpy.data.objects["secondary_spot_2"].data.color = (0.0, 0.0, 0.0)
bpy.data.objects["accent_spot"].data.color = (1.0, 1.0, 1.0)
bpy.data.objects["accent_spot_2"].data.color = (1.0, 1.0, 1.0)


# countries = [
#     "Albania",
#     "Andorra",
#     "Argentina",
#     "Armenia",
#     "Australia",
#     "Austria",
#     "Azerbaijan",
#     "Belarus",
#     "Belgium",
#     "Bolivia",
#     "Bosnia and Herzegovina",
#     "Brazil",
#     "Bulgaria",
#     "Canada",
#     "Chile",
#     "China",
#     "Chinese Taipei",
#     "Colombia",
#     "Croatia",
#     "Cyprus",
#     "Czech Republic",
#     "Denmark",
#     "East Timor",
#     "Ecuador",
#     "Eritrea",
#     "Estonia",
#     "Finland",
#     "France",
#     "Georgia",
#     "Germany",
#     "Ghana",
#     "Great Britain",
#     "Greece",
#     "Haiti",
#     "Hong Kong",
#     "Hungary",
#     "Iceland",
#     "India",
#     "Iran",
#     "Ireland",
#     "Israel",
#     "Italy",
#     "Jamaica",
#     "Japan",
#     "Kazakhstan",
#     "Kenya",
#     "Kosovo",
#     "Kyrgyzstan",
#     "Latvia",
#     "Lebanon",
#     "Liechtenstein",
#     "Lithuania",
#     "Luxembourg",
#     "Madagascar",
#     "Malaysia",
#     "Malta",
#     "Mexico",
#     "Moldova",
#     "Monaco",
#     "Mongolia",
#     "Montenegro",
#     "Morocco",
#     "Netherlands",
#     "New Zealand",
#     "Nigeria",
#     "North Macedonia",
#     "Norway",
#     "Pakistan",
#     "Peru",
#     "Philippines",
#     "Poland",
#     "Portugal",
#     "Puerto Rico",
#     "ROC",
#     "Romania",
#     "San Marino",
#     "Saudi Arabia",
#     "Serbia",
#     "Slovakia",
#     "Slovenia",
#     "South Korea",
#     "Spain",
#     "Sweden",
#     "Switzerland",
#     "Thailand",
#     "Trinidad and Tobago",
#     "Turkey",
#     "Ukraine",
#     "United States",
#     "Uzbekistan",
# ]
# print(len(countries))

# disciplines_file = open("metamorfan/data/disciplines.json")
# DISCIPLINES_DATA = json.load(disciplines_file)

# types_file = open("metamorfan/data/types.json")
# TYPES_DATA = json.load(types_file)

# events_file = open("metamorfan/data/events.json")
# EVENTS_DATA = json.load(events_file)

# attributes_file = open("metamorfan/data/attributes.json")
# ATTRIBUTES_DATA = json.load(attributes_file)

# hair_file = open("metamorfan/data/hair.json")
# HAIR_DATA = json.load(hair_file)

# skin_file = open("metamorfan/data/skin_color.json")
# SKIN_DATA = json.load(skin_file)

# BASE_JSON = {
#     "name": "",
#     "symbol": "MFAN",
#     "description": "Each of these 3200 Metamorfans has a chance to win! Welcome aboard!",
#     "image": "image.png",
#     "seller_fee_basis_points": 500,
#     "attributes": [],
#     "properties": {
#         "creators": [
#             {"address": "AfabEY9MxXDWJQM4vAn8CLdCLEMzVK8o89CiMq5gGDkU", "share": 100}
#         ],
#         "files": [{"uri": "image.png", "type": "image/png"}],
#     },
# }


# def set_background():
#     b = random.randrange(0, 10, 1)
#     if b in range(0, 7):
#         return "Flag"
#     elif b in range(7, 9):
#         ACTIVE_COLLECTIONS.append("background.mountains")
#         bpy.data.collections["background.mountains"].hide_render = False
#         return "Mountains"
#     else:
#         ACTIVE_COLLECTIONS.append("snowy.day")
#         bpy.data.collections["snowy.day"].hide_render = False
#         return "Snowday"


# def build_json(count, attributes):
#     meta_data = BASE_JSON
#     meta_data["name"] = "Metamorfans #" + str(count)
#     meta_data["attributes"] = attributes
#     json_path = (
#         "/Users/nolanbetts/Blender/renders/metamorfan/final/" + str(count) + ".json"
#     )
#     json_string = json.dumps(meta_data, indent=2)
#     json_file = open(json_path, "w")
#     json_file.write(json_string)
#     json_file.close()
#     return str(count) + " complete"


# # print(list(DISCIPLINES_DATA["Disciplines"].keys()))
# # for x in range(100):
# #     print(set_background())
# attr = [
#     {"trait_type": "Gender", "value": "Male"},
#     {"trait_type": "Type", "value": "Human"},
#     {"trait_type": "Country", "value": "USA"},
#     {"trait_type": "Discipline", "value": "Hockey"},
#     {"trait_type": "Event", "value": "Men's"},
#     {"trait_type": "Skin", "value": "Light"},
#     {"trait_type": "Hair", "value": "Short"},
#     {"trait_type": "Hair Color", "value": "Blonde"},
#     {"trait_type": "Background", "value": "Flag"},
#     {"trait_type": "Extra", "value": "None"},
#     {"trait_type": "Score", "value": 0},
# ]


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


# import random
# from random import randrange
# import bpy
# import math

# spacing = 2.2
# circumcenter = 0.675
# mat_list = ['primary','secondary','accent']


# h = math.sin(math.pi / 3)
# for x in range(-1, 20, 3):
#     for y in range(-1, int(20 / h) + 1):
#         # Add the horizontal offset on every other row
#         x_ = x if (y % 2 == 0) else x + 1.5
#         location = (x_ * spacing, y *spacing, random.random() * 2)
#         bpy.ops.mesh.primitive_cylinder_add(vertices=3, enter_editmode=False, align='WORLD', location=location, scale=(1.8, 1.8, 1.8),rotation=(0,0,1.5708))
#         item = bpy.context.object
#         mat = mat_list[randrange(0,3)]
#         item.active_material = bpy.data.materials[mat]
#         location = (x_ * spacing - circumcenter, y * spacing - spacing, random.random() * 2)
#         bpy.ops.mesh.primitive_cylinder_add(vertices=3, enter_editmode=False, align='WORLD', location=location, scale=(1.8, 1.8, 1.8),rotation=(0,0,4.71239))
#         item = bpy.context.object
#         mat = mat_list[randrange(0,3)]
#         item.active_material = bpy.data.materials[mat]

# import random
# from random import randrange
# import bpy
# import math

# mat_list = ['primary','secondary','accent']

# for count in range(0,150):
#     offset = count // 15
#     x_offset = count % 15
#     plane = bpy.ops.mesh.primitive_plane_add(location=(x_offset*2, offset*2, 0), scale=(1.0, 1.0, 1.0))
#     bpy.data.objects["Plane"].name = str(count)
#     item = bpy.context.object
#     mat = mat_list[randrange(0,3)]
#     item.active_material = bpy.data.materials[mat]
