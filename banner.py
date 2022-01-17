import json
import bpy

# countries_file = open("country_data.json")
# countries_data = json.load(countries_file)
# count = 0
# for each in countries_data:
#     alpha2Code = countries_data[each]["alpha-2-code"].lower()

#     plane = bpy.ops.mesh.primitive_plane_add(
#         location=(0, count * 2, 0), scale=(1.0, 1.0, 1.0)
#     )
#     bpy.data.objects["Plane"].name = alpha2Code
#     count = count + 1
# bpy.data.objects["Plane"].scale = (1.0, 2.0, 1.0)


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

# countries_file = open("country_data.json")
# countries_data = json.load(countries_file)

# for each in countries_data:
#     alpha2Code = countries_data[each]["alpha-2-code"].lower()
#     item = bpy.data.objects[alpha2Code]
#     mat = bpy.data.materials[alpha2Code]
#     item.active_material = mat

countries_file = open("country_data.json")
countries_data = json.load(countries_file)

count = 0
for each in countries_data:
    alpha2Code = countries_data[each]["alpha-2-code"].lower()
    item = bpy.data.objects[alpha2Code]
    item.scale = (1.5, 1.0, 1.0)
    offset = count // 15
    x_offset = count % 15
    item.location = (x_offset * 3, offset * 2, 0.0)
    count = count + 1
