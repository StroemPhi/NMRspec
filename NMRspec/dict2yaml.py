from NMRspec import *
from Provenance import *
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.loaders import yaml_loader
from datetime import date
from jdx import jdx2dict

today_str = str(date.today())
debug = True

# Setting provenance metadata values from manually pre generated files
assay_info = yaml_loader.loads(source="NMRspec/jdx_files/SG-V3259 (41-52)_10.yaml", target_class=Provenance)
dataset_info = yaml_loader.loads(source="NMRspec/jdx_files/dataset_info.yaml", target_class=Provenance)
# TODO: get sample info from some API like ChEBI or PubChem
sample = yaml_loader.loads(source="NMRspec/jdx_files/sample_info.yaml", target_class=NmrSample)

# load the jdx data into a dict
jdx_dict = jdx2dict(filepath="NMRspec/jdx_files/SG-V3259 (41-52)_10.dx")

# get solvent from jdx_dict
def get_solvent(jdx_dict) -> NmrSolvent:
    """A function to get the detail infos on the solvent bases on looking up the value provided in the JCAMP-DX file
    in the dictionary "nmrSolvents" defined here. As the value in the .jdx could be a synonym of the name,
    we need to include synonyms as a list of possible names in this dictionary"""
    nmrSolvents = [{"name": ["chloroform-d", "CHLOROFORM-d", "CDCl3", "methanol-d4", "CD3OD", "deuterated chloroform"],
                    "id": "chebi:85365",
                    "smiles": "[2H]C(Cl)(Cl)Cl",
                    "iupac_name": "trichloro(deuterio)methane",
                    "inchi": "InChI=1S/CHCl3/c2-1(3)4/h1H/i1D",
                    "inchikey": "HEDRZPFGACZZDS-MICDWDOJSA-N"},
                   {"name": ["acetone-d6", "Acetone-D6", "CD3COCD3"],
                    "id": "chebi:78217",
                    "smiles": "[2H]C([2H])([2H])C(=O)C([2H])([2H])[2H]",
                    "iupac_name": "1,1,1,3,3,3-hexadeuteriopropan-2-one",
                    "inchi": "InChI=1S/C3H6O/c1-3(2)4/h1-2H3/i1D3,2D3",
                   "inchikey": "CSCPPACGZOOCGX-WFGJKAKNSA-N"},
                   {"name": ["dimethyl sulfoxide-d6","d6-DMSO", "DMSO-d6", "C2H6OS", "Dimethylsulfoxide-D6",
                             "deuterated dmso"],
                    "id": "https://pubchem.ncbi.nlm.nih.gov/compound/75151",
                    "smiles": "[2H]C([2H])([2H])S(=O)C([2H])([2H])[2H]",
                    "iupac_name": "trideuterio(trideuteriomethylsulfinyl)methane",
                    "inchi": "InChI=1S/C2H6OS/c1-4(2)3/h1-2H3/i1D3,2D3",
                    "inchikey": "IAZDPXIOMUYVGZ-WFGJKAKNSA-N"},
                   {"name": ["acetonitrile-d3", "CD3CN"],
                    "id": "https://pubchem.ncbi.nlm.nih.gov/compound/123151",
                    "smiles": "[2H]C([2H])([2H])C#N"},
                   {"name": ["deuterium oxide", "D2O"],
                    "id": "https://pubchem.ncbi.nlm.nih.gov/compound/24602",
                    "smiles": "[2H]O[2H]"},
                   {"name": ["dichloromethane-d2", "CD2Cl2"],
                    "id": "https://pubchem.ncbi.nlm.nih.gov/compound/160586","smiles": "[2H]C([2H])(Cl)Cl"},
                   {"name": ["ethanol-d6", "CD3CD2OD"],
                    "id": "https://pubchem.ncbi.nlm.nih.gov/compound/102138",
                    "smiles": "[2H]C([2H])([2H])C([2H])([2H])O[2H]"},
                   {"name": ["methanol-d4", "CD3COD", "MeOD"],
                    "id": "https://pubchem.ncbi.nlm.nih.gov/compound/71568",
                    "smiles": "[2H]C([2H])([2H])O[2H]"},
                   {"name": ["nitrobenzene-d5", "C6D5NO2"],
                    "id": "https://pubchem.ncbi.nlm.nih.gov/compound/123210",
                    "smiles": "[2H]C1=C(C(=C(C(=C1[2H])[2H])[N+](=O)[O-])[2H])[2H]"},
                   {"name": ["nitromethane-d3", "CD3NO2"],
                    "id": "https://pubchem.ncbi.nlm.nih.gov/compound/123293",
                    "smiles": "[2H]C([2H])([2H])[N+](=O)[O-]",
                   "inchikey": "LYGJENNIWJXYER-FIBGUPNXSA-N"},
                   {"name": ["pyridine-d5", "C5D5N"],
                    "id": "https://pubchem.ncbi.nlm.nih.gov/compound/558519",
                    "smiles": "[2H]C1=NC([2H])=C([2H])C([2H])=C1[2H]"},
                   {"name": ["toluene-d8", "C6D5CD3"],
                    "id": "https://pubchem.ncbi.nlm.nih.gov/compound/74861",
                    "smiles": "[2H]C([2H])([2H])C1=C([2H])C([2H])=C([2H])C([2H])=C1[2H]"},
                   {"name": ["benzene-d6", "C6D6"],
                    "id": "https://pubchem.ncbi.nlm.nih.gov/compound/71601",
                    "smiles": "C1([2H])=C([2H])C([2H])=C([2H])C([2H])=C1[2H]"}
                   ]
    solvent_name = jdx_dict['.solvent name']
    solvent_dict = {}
    for possible_solvent in nmrSolvents:
        for key, value in possible_solvent.items():
            if key == "name":
                if solvent_name in value:
                    solvent_dict = possible_solvent
            elif value == solvent_name:
                solvent_dict = possible_solvent

    solvent = NmrSolvent(id=solvent_dict['id'],
                         name=solvent_dict['name'][0],
                         inchi=InCHI(has_representation=solvent_dict['inchi']),
                         inchikey=InCHIKey(has_representation=solvent_dict['inchikey']),
                         iupac_name=IUPACname(has_representation=solvent_dict['iupac_name']),
                         smiles=SMILES(has_representation=solvent_dict['smiles']))
    if debug is True:
        print(f"parsed solvent:\n{solvent}")

    return solvent
solvent = get_solvent(jdx_dict)


