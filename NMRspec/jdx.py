"""in here are methods to read JCAMP-DX files from a folder and to convert each into a pythin dictionary"""
import os, re
from jcamp import JCAMP_reader

def capture_keys_regex(filename):
    """A function to get the JCAMP-DX keys"""
    with open(filename, "r") as jdx:
        jdx_content = jdx.read()
    exp_jdx_keys = re.compile(r'^##(?P<key>.*?)=', re.M)
    found_keys = set(re.findall(exp_jdx_keys, jdx_content))
    found_keys = [key.lower() for key in found_keys]
    return found_keys


def read_jdx_files_from_folder(filepath="NMRspec\jdx_files"):
    """A function to parse JCAMP files contained in the passed filepath"""
    for fn in os.listdir(f".\{filepath}\\"):
        if ".dx" or ".jdx" in fn:
            jdx2dict(f"{filepath}\\{fn}")


def jdx2dict(filepath="NMRspec\jdx_files\\000000012.jdx"):
    print(f"-----\nprocessing file: '{filepath}'")
    jcamp_dict = JCAMP_reader(f"{filepath}")
    # pprint(jcamp_dict)
    #print(f"test output: SOLVENT --> '{jcamp_dict['.solvent name']}'")

# NOTE: I don't know if we really need to look for keys in den jdx file that are not recognized by the JCAMP_reader
    jcamp_keys = sorted(list(jcamp_dict.keys()))  # jcamp_keys are the jcamp lib captured keys var from cell above
    found_keys_regex = capture_keys_regex(f"{filepath}")
    missing_jcamp_keys = [k for k in found_keys_regex if k not in jcamp_keys]
    #print(f'\nMissing keys: {missing_jcamp_keys}\n')

    return jcamp_dict


def in_dict(myDict, lookup):
    for key, value in myDict.items():
        if lookup in str(value):
            return True