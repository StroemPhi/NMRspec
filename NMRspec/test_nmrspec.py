from linkml_runtime.dumpers import yaml_dumper
from NMRspec import *
from Provenance import *
import os, re
from jcamp import JCAMP_reader
from pprint import pprint


def capture_keys_regex(filename):
    """A function to get the JCAMP-DX keys"""
    with open(filename, "r") as jdx:
        jdx_content = jdx.read()
    exp_jdx_keys = re.compile(r'^##(?P<key>.*?)=', re.M)
    found_keys = set(re.findall(exp_jdx_keys, jdx_content))
    found_keys = [key.lower() for key in found_keys]
    return found_keys


def read_files_from_folder(filepath="NMRspec\jdx_files"):
    """A function to parse JCAMP files contained in the passed filepath"""
    for fn in os.listdir(f".\{filepath}\\"):
        if ".dx" or ".jdx" in fn:
            parse_jdx(f"{filepath}\\{fn}")


def parse_jdx(filepath="NMRspec\jdx_files\SG-V3259 (41-52)_11.jdx"):
    print(f"\nprocessing file: '{filepath}'")
    jcamp_dict = JCAMP_reader(f"{filepath}")
    # pprint(jcamp_dict)
    print(f"test output: SOLVENT --> '{jcamp_dict['.solvent name']}'")

    # NOTE
    jcamp_keys = sorted(list(jcamp_dict.keys()))  # jcamp_keys are the jcamp lib captured keys var from cell above
    found_keys_regex = capture_keys_regex(f"{filepath}")
    missing_jcamp_keys = [k for k in found_keys_regex if k not in jcamp_keys]
    # print(f'\nMissing keys: {missing_jcamp_keys}\n')
    return jcamp_dict


def set_solvent_info(id=None, local_id=None, formula=None, iupac_name=None, name=None):
    """A function to set the metadata of the solvent of the assayed solution"""
    if formula == "CDCl3":
        id = "chebi:85365"
        iupac_name = "deuterated chloroform"
        name = "trichloro((2)H)methane"
    solvent = NmrSolvent(id=id, formula=SolventFormula(has_representation=formula),
                         iupac_name=IUPACname(has_representation=iupac_name), name=name)
    return solvent


def set_sample_info(id=None, local_id=None, formula=None, iupac_name=None):
    sample = NmrSample(id=id, local_id=local_id, formula=MolecularFormula(has_representation=formula),
                       iupac_name=IUPACname(has_representation=iupac_name))
    return sample


# parse jdx files into dict
jdx_data = parse_jdx()
# print(jdx_data['.solvent name'])

# Setting some test data values
provenance_info1 = Provenance(
    source_uri="https://www.chemotion-repository.net/home/publications/molecules/3366",
    source="Chemotion Repository",
    licence_str="Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
    licence_url="https://creativecommons.org/licenses/by-sa/4.0/",
    date_created="2022-01-10")

solvent1 = set_solvent_info(formula=jdx_data['.solvent name'])

sample1 = set_sample_info(id="doi:10.14272/QXXCRBSWGPRILJ-UHFFFAOYSA-N.1", local_id="SG-V3259 (41-52)",
                          formula="C17H17NO2S",
                          iupac_name="2-(2,6-dimethoxy-4-methylphenyl)-6-methyl-1,3-benzothiazole")

solution1 = NmrSolution(solvent=solvent1, sample=sample1,
                        measured_molarity=MolarConcentration(
                            measured_as=MolarityMeasurementDatum(value=21.55, unit="molar")),
                        measured_pH=PhValue(measured_as=PhMeasurementDatum(value=7.5, unit="pH")))

# print("##################################################")
# print(yaml_dumper.dumps(solution1))
