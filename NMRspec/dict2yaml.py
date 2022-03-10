from NMRspec import *
from Provenance import *
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.loaders import yaml_loader
from datetime import date
from jdx import jdx2dict, in_dict
import os
import re

today_str = str(date.today())

def get_assay_data(jdx_dict) -> PulsedNmrAssay:
    def get_solvent() -> NmrSolvent:
        """A function to get the detail infos on the solvent bases on looking up the value provided in the JCAMP-DX file
        in the dictionary "nmrSolvents" defined here. As the value in the .jdx could be a synonym of the name,
        we need to include synonyms as a list of possible names in this dictionary"""
        nmr_solvents = [
            {"name": ["chloroform-d", "CHLOROFORM-d", "CDCl3", "methanol-d4", "CD3OD", "deuterated chloroform"],
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
            {"name": ["dimethyl sulfoxide-d6", "d6-DMSO", "DMSO-d6", "DMSO-D6", "C2H6OS",
                      "Dimethylsulfoxide-D6",
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
             "id": "https://pubchem.ncbi.nlm.nih.gov/compound/160586", "smiles": "[2H]C([2H])(Cl)Cl"},
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
        for possible_solvent in nmr_solvents:
            for key, value in possible_solvent.items():
                if key == "name":
                    if solvent_name in value:
                        solvent_dict = possible_solvent
                elif value == solvent_name:
                    solvent_dict = possible_solvent
        parsed_solvent = NmrSolvent(id=solvent_dict['id'],
                                    name=solvent_dict['name'][0],
                                    inchi=InCHI(has_representation=solvent_dict['inchi']),
                                    inchikey=InCHIKey(has_representation=solvent_dict['inchikey']),
                                    iupac_name=IUPACname(has_representation=solvent_dict['iupac_name']),
                                    smiles=SMILES(has_representation=solvent_dict['smiles']))
        if debug is True:
            print(f"----\nparsed_solvent: {parsed_solvent}")
        return parsed_solvent

    def get_assay_date() -> str:
        if 'long date' in jdx_dict.keys():
            assay_date = str(jdx_dict['long date'])
        elif 'longdate' in jdx_dict.keys():
            assay_date = str(jdx_dict['longdate'])
        return assay_date
    print(f"----\nassay_date: {get_assay_date()}")

    # parse the manufacturer in the jdx, by looking for its name in any of the jdx fields
    # TODO: make the list a list of dicts by adding websites to each manufacturer as default values,
    #  analog to nmr_solvents and nmr_pulse_programs
    def get_manufacturer() -> Manufacturer:
        nmr_manufacturers = ["Acorn NMR Inc", "Agilent Technologies", "Applied Biosystems", "Bruker", "Doty Scientific",
                            "FOSS", "General Electric", "JEOL", "JS Research", "Jasco", "Kimble Chase", "MR Resources",
                            "OceanOptics", "Oxford Instruments", "Perkin Elmer", "Phillips", "Siemens AG",
                            "Spinlock SRL",
                            "TX", "ThermoFinnigan", "ThermoMattson", "ThermoNicolet", "Varian", "Waters", "Wilmad",
                            "acdlabs", "micromass", "tecmag"]
        for possible_manufacturer in nmr_manufacturers:
            if in_dict(jdx_dict, possible_manufacturer):
                manufacturer = Manufacturer(name=possible_manufacturer)
        return manufacturer
    print(f"-----\nparsed manufacturer: {get_manufacturer()}")

    # parse the aquisition nuclei
    def get_aquisition_nuclei() -> list:
        acuisition_nuclei = []
        if '$nuc1' in jdx_dict:
            if jdx_dict['$nuc1'] != '<off>':
                acuisition_nuclei.append(jdx_dict['$nuc1'].replace('<', '').replace('>', ''))
            if jdx_dict['$nuc2'] != '<off>':
                acuisition_nuclei.append(jdx_dict['$nuc2'].replace('<', '').replace('>', ''))
            if jdx_dict['$nuc3'] != '<off>':
                acuisition_nuclei.append(jdx_dict['$nuc3'].replace('<', '').replace('>', ''))
            if jdx_dict['$nuc4'] != '<off>':
                acuisition_nuclei.append(jdx_dict['$nuc4'].replace('<', '').replace('>', ''))
            if jdx_dict['$nuc5'] != '<off>':
                acuisition_nuclei.append(jdx_dict['$nuc5'].replace('<', '').replace('>', ''))
            if jdx_dict['$nuc6'] != '<off>':
                acuisition_nuclei.append(jdx_dict['$nuc6'].replace('<', '').replace('>', ''))
            if jdx_dict['$nuc7'] != '<off>':
                acuisition_nuclei.append(jdx_dict['$nuc7'].replace('<', '').replace('>', ''))
            if jdx_dict['$nuc8'] != '<off>':
                acuisition_nuclei.append(jdx_dict['$nuc8'].replace('<', '').replace('>', ''))
        elif '.nucleus' in jdx_dict:
            nuclei = jdx_dict['.nucleus'].split(',')
            nuclei[1] = nuclei[1].strip()
            acuisition_nuclei.extend(nuclei)
        else:
            acuisition_nuclei.append(jdx_dict['.observe nucleus'].replace('^', ''))
        return acuisition_nuclei
    print(f"-----\naquisition nuclei: {get_aquisition_nuclei()}")


    # parse pulse program
    def get_pulse_program() -> str:
        # pulse program as stored in jdx
        pulse_program_jdx = jdx_dict['.pulse sequence'].lower()
        # controlled list of dicts for looking up and normalizing possible pulse programs = Enums of schema
        # TODO: document better how this is needed, in order to ground all possible vendor specific pulse programs to a
        #  certain standard. See also https://github.com/StroemPhi/NMRspec/issues/5
        nmr_pulse_program_cv = [{"name": "NMR", "bruker": "zg", "jeol_h": "proton", "jeol_c": "carbon"},
                              {"name": "Inverse NMR"},
                              {"name": "COSY"},
                              {"name": "SECSY"},
                              {"name": "RELAY"},
                              {"name": "TOCSY"},
                              {"name": "ROESY"},
                              {"name": "NOESY"},
                              {"name": "J_Resolved", "bruker": "jres"},
                              {"name": "DEPT"},
                              {"name": "INEPT"},
                              {"name": "HECTOR"},
                              {"name": "COLOC"},
                              {"name": "HOESY"},
                              {"name": "INADEQUATE"},
                              {"name": "HMQC"},
                              {"name": "DEPT-HMQC"},
                              {"name": "HSQC"},
                              {"name": "Inverse-INEPT"},
                              {"name": "TROSY"},
                              {"name": "CRINEPT"},
                              {"name": "HMQC-COSY"},
                              {"name": "H2BC"},
                              {"name": "HQMC-TOSCY"},
                              {"name": "HMQC-ROESY"},
                              {"name": "HMQC-NOESY"},
                              {"name": "HSQC-TOSCY"},
                              {"name": "HSQC-ROESY"},
                              {"name": "HSQC-NOESY"},
                              {"name": "HMBC"},
                              {"name": "HSQMBC"},
                              {"name": "EXSIDE"},
                              {"name": "HETLOC"},
                              {"name": "HSQC-HECADE"},
                              {"name": "ADEQUATE"},
                              {"name": "DOSY"},
                              {"name": "STE"},
                              {"name": "STEBP"},
                              {"name": "DSTE"},
                              {"name": "DSTEBP"},
                              {"name": "COSY-DOSY"},
                              {"name": "DOSY-TOCSY"},
                              {"name": "DOSY-NOESY"},
                              {"name": "DOSY-HMQC"},
                              {"name": "STD-TOSCY"},
                              {"name": "STD-NOESY"},
                              {"name": "STD-HSQC"},
                              {"name": "CLEANEX"},
                              {"name": "CLEANEX-HSQC"},
                              {"name": "CLEANEX-TROSY"}
                              ]
        pulse_program = None  # return variable
        for possible_pulse_program in nmr_pulse_program_cv:
            for key, value in possible_pulse_program.items():
                # normalize controlled terms to be able to match to manufacturer codes
                value = value.lower()
                # split controlled term of combined pulse programs, as the order might be different in Bruker & JEOl
                # (e.g. DOSY-COSY vs cosy-dosy)
                if '-' in value:
                    value = value.split('-')
                    # return controlled term if the combined pulse program could be matched
                    if value[0] in pulse_program_jdx and value[1] in pulse_program_jdx:
                        pulse_program = possible_pulse_program["name"]
                # return controlled term if there is a pulse program match
                else:
                    if re.match(rf"(^{value})", pulse_program_jdx):
                        pulse_program = possible_pulse_program["name"]
        # return initial
        if not pulse_program:
            pulse_program = pulse_program_jdx
        return pulse_program
    print(f"-----\npulse program: {get_pulse_program()}")



if __name__ == '__main__':
    # loading provenance metadata provided in manually generated files
    assay_info = yaml_loader.loads(source="./jdx_files/SG-V3259 (41-52)_10.yaml", target_class=Provenance)
    #print(f"-----\nloaded assay_info:\n{yaml_dumper.dumps(assay_info)}")
    dataset_info = yaml_loader.loads(source="./jdx_files/dataset_info.yaml", target_class=Provenance)
    #print(f"-----\nloaded dataset_info:\n{yaml_dumper.dumps(dataset_info)}")

    # loading sample metadata provided in manually generated file
    # TODO: get further sample infos from some API like ChEBI or PubChem
    sample = yaml_loader.loads(source="./jdx_files/sample_info.yaml", target_class=NmrSample)

    # parse the jdx file into Python dict
    jdx_dict = jdx2dict(filepath="./jdx_files/SG-V3259 (41-52)_10.dx")
    print(f"-----\nloading '{os.path.basename(jdx_dict['filename'])}' into dict:\n{jdx_dict}")

    # get solvent from jdx_dict
    solvent = get_solvent(jdx_dict)
    #print(f"-----\nparsed solvent:\n{yaml_dumper.dumps(solvent)}")

    # declare assayed solution
    solution = NmrSolution(solvent=solvent, sample=sample)
    print(f"-----\ndeclared solution:\n{yaml_dumper.dumps(solution)}")

    #get assay metadata from jdx_dict
    get_assay_data(jdx_dict)

