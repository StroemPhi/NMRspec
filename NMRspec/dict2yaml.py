from NMRspec import *
from Provenance import *
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.loaders import yaml_loader
from datetime import date
from jdx import jdx2dict

today_str = str(date.today())

# Setting provenance metadata values from manually pre generated files
assay_info = yaml_loader.loads(source="NMRspec/jdx_files/SG-V3259 (41-52)_10.yaml", target_class=Provenance)
dataset_info = yaml_loader.loads(source="NMRspec/jdx_files/dataset_info.yaml", target_class=Provenance)
# TODO: get sample info from some API like ChEBI or PubChem
sample = yaml_loader.loads(source="NMRspec/jdx_files/sample_info.yaml", target_class=NmrSample)

# load the jdx data into a dict
jdx_dict = jdx2dict(filepath="NMRspec/jdx_files/SG-V3259 (41-52)_10.dx")

# get solvent from jdx
solvent_name = jdx_dict['.solvent name']
solvent_name = "deuterated chloroform"

def get_solvent_details(solvent_name) -> str:
    """A function to get the detail infos on the solvent bases on looking up the value provided in the JCAMP-DX file
    in the dictionary "nmrSolvents" defined here. As the value in the .jdx could be a synonym of the name,
    we need to include synonyms as a list of possible names in this dictionary"""
    nmrSolvents = [{"name": ["chloroform-d", "deuterated chloroform", "CHLOROFORM-d"], "formula": "CDCl3",
                    "smiles": "[2H]C(Cl)(Cl)Cl"},
                   {"name": "benzene-d6", "formula": "C6D6", "smiles": "C1([2H])=C([2H])C([2H])=C([2H])C([2H])=C1[2H]"}
                   ]
    for possible_solvent in nmrSolvents:
        for key, value in possible_solvent.items():
            if key == "name":
                if solvent_name in value:
                    return key
            elif value == solvent_name:
                return key


print(get_solvent_details(solvent_name))

"""# TODO: get the solvent details from some API like ChEBI or PubChem
if solvent_formula == "CDCl3":
    id = "chebi:85365"
    name = "deuterated chloroform"
    iupac_name = "trichloro((2)H)methane"
    smiles = "[2H]C(Cl)(Cl)Cl"
solvent = NmrSolvent(id=id, formula=SolventFormula(has_representation=solvent_formula),
                     iupac_name=IUPACname(has_representation=iupac_name), name=name,
                     smiles=SMILES(has_representation=smiles))

#print(yaml_dumper.dumps(solvent, allow_unicode=True))"""
