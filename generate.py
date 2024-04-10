from mp_api.client import MPRester
# from pymatgen import MPRester
import pymatgen
import pymatgen.io.prismatic
import os
#MP_API_KEY=os.environ.get("sWu28OFsgfp9cs0Co6BMeh74Lhm1usNt")
import yaml
import argparse
from pymatgen.core.operations import SymmOp
import requests


api_key = "sWu28OFsgfp9cs0Co6BMeh74Lhm1usNt"
 
query = retrieve_material(mat_id, api_key)

# Get the pretty chemical formula
pretty_formula = query.formula_pretty # python string

# Get the strucutre details
structure = query.structure # pymatgen strucutre class

# Symmetry information
symmetry = query.symmetry

# Save material information
print(symmetry)
material_dict = {}
d = {}
d['pretty_formula'] = pretty_formula
d['symmetry_symbol'] = symmetry.symbol
d['crystal_sytem'] = f'{symmetry.crystal_system}'
mat_id = mat_id.replace(",", "")
material_dict[mat_id] = d

existing_info: dict = {}
if os.path.exists(MATERIALS_INFO_FILE):
    with open(MATERIALS_INFO_FILE, 'r') as f:
        existing_info = yaml.safe_load(f)

existing_info.update(material_dict)
with open(MATERIALS_INFO_FILE, 'w') as f:
    yaml.dump(existing_info, f)
    operation = SymmOp.from_axis_angle_and_translation(rotation_axis, angle)
    structure.apply_operation(operation)
prismatic_str = pymatgen.io.prismatic.Prismatic(structure).to_string()


## make material id