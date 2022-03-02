from linkml_runtime.dumpers import yaml_dumper, rdf_dumper
from NMRspec import *


sample1 = NmrSample(id="doi:10.14272/QXXCRBSWGPRILJ-UHFFFAOYSA-N.1", local_id="SG-V3259 (41-52)",
                    formula=MolecularFormula(has_representation="C17H17NO2S"),
                    iupac_name=IUPACname(
                        has_representation="2-(2,6-dimethoxy-4-methylphenyl)-6-methyl-1,3-benzothiazole"))

solvent_formula = SolventFormula(has_representation="CDCL3")
if solvent_formula.has_representation == "CDCL3":
    solvent_id = "chebi:85365"
    solvent_iupac_name = IUPACname(has_representation="trichloro((2)H)methane")
    solvent_name = "deuterated chloroform"
solvent1 = NmrSolvent(id=solvent_id, formula=solvent_formula, iupac_name=solvent_iupac_name, name=solvent_name)


solution1 = NmrSolution(solvent=solvent1, sample=sample1,
                        measured_molarity=MolarConcentration(
                            is_quality_measured_as=MolarityMeasurementDatum(value=21.55, unit="molar")),
                        measured_pH=PhValue(is_quality_measured_as=PhMeasurementDatum(value=7.5, unit="pH")))

print("##################################################")
print(rdf_dumper.dumps(solution1))