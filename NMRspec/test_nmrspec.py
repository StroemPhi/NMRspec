from linkml_runtime.dumpers import yaml_dumper
from NMRspec import *

sample_formula = MolecularFormula(has_representation="C17H17NO2S")
sample_name = IUPACname(has_representation="2-(2,6-dimethoxy-4-methylphenyl)-6-methyl-1,3-benzothiazole")
sample1 = NmrSample(id="doi:10.14272/QXXCRBSWGPRILJ-UHFFFAOYSA-N.1", local_id="SG-V3259 (41-52)",
                            formula=sample_formula, iupac_name=sample_name)

solvent_formula = SolventFormula(has_representation="CDCL3")
if solvent_formula.has_representation == "CDCL3":
    solvent_id = "chebi:85365"
    solvent_iupac_name = IUPACname(has_representation="trichloro((2)H)methane")
    solvent_name = "deuterated chloroform"
solvent1 = NmrSolvent(id=solvent_id, formula=solvent_formula, iupac_name=solvent_iupac_name, name=solvent_name)

print("##################################################")
print(yaml_dumper.dumps(solvent1))