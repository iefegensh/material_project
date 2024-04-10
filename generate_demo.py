from mp_api.client import MPRester

with MPRester("sWu28OFsgfp9cs0Co6BMeh74Lhm1usNt") as mpr:
    docs = mpr.summary.search(material_ids=["mp-149"])
    #docs = MPRester.materials.summary.search(material_ids=["mp-149", "mp-13", "mp-22526"],  fields=["initial_structures"])

    # structure = docs[0].structure
    # # -- Shortcut for a single Materials Project ID:
    # structure = mpr.get_structure_by_material_id("mp-149")
    #docs = mpr.summary.search(material_ids=["mp-149"])


query = docs[0]
print(query)
#print("mat_id: ", query.material_id)
pretty_formula = query.formula_pretty
#print(pretty_formula)
# # # # Symmetry information
symmetry = query.symmetry

# # # # Save material information
#print(symmetry)
list_of_available_fields = mpr.summary.available_fields
#print(list_of_available_fields)

# material_dict = {}
# for mat_id in ["mp-149", "mp-13", "mp-22526"]:
#     d = {}
#     d['pretty_formula'] = pretty_formula
#     d['symmetry_symbol'] = symmetry.symbol
#     d['crystal_system'] = f'{symmetry.crystal_system}'
#     material_dict[mat_id] = d
# print(material_dict)
# initial_structures = query.initial_structures
# print(initial_structures)
