# Auto generated from NMRspec.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-03-17T21:01:17
# Schema: NMRspec
#
# id: https://raw.githubusercontent.com/StroemPhi/NMRspec/main/model/schema/NMRspec.yaml
# description: This model is to be used to semantify NMR spectroscopy research data.
# license: https://creativecommons.org/licenses/by/4.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Datetime, Double, Float, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
FAIRSPEC = CurieNamespace('FAIRspec', 'https://github.com/IUPAC/IUPAC-FAIRSpec/blob/main/src/main/java/org/iupac/fairspec/core/')
NMRSPEC = CurieNamespace('NMRspec', 'https://raw.githubusercontent.com/StroemPhi/NMRspec/main/model/schema/')
BFO = CurieNamespace('bfo', 'http://purl.obolibrary.org/obo/BFO_')
CC = CurieNamespace('cc', 'https://creativecommons.org/licenses/')
CHEMINF = CurieNamespace('cheminf', 'http://purl.obolibrary.org/obo/CHEMINF_')
CHEMOTION = CurieNamespace('chemotion', 'https://www.chemotion-repository.net/home/publications/reactions/')
CHEMOTIONDATA = CurieNamespace('chemotionDATA', 'https://www.chemotion-repository.net/home/publications/datasets/')
CHEMOTIONPID = CurieNamespace('chemotionPID', 'https://www.chemotion-repository.net/pid/')
CHMO = CurieNamespace('chmo', 'http://purl.obolibrary.org/obo/CHMO_')
DOI = CurieNamespace('doi', 'https://doi.org/')
IAO = CurieNamespace('iao', 'http://purl.obolibrary.org/obo/IAO_')
ISA = CurieNamespace('isa', 'https://isa-specs.readthedocs.io/en/latest/isamodel.html#')
JDX = CurieNamespace('jdx', 'http://www.jcamp-dx.org/protocols/dxnmr01.pdf/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMRCV = CurieNamespace('nmrCV', 'http://nmrML.org/nmrCV#')
NMRSPARQL = CurieNamespace('nmrSPARQL', 'https://nfdi4chem/sparql/')
OBI = CurieNamespace('obi', 'http://purl.obolibrary.org/obo/OBI_')
OM = CurieNamespace('om', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
PATO = CurieNamespace('pato', 'http://purl.obolibrary.org/obo/PATO_')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
PUBCHEMCID = CurieNamespace('pubchemCID', 'https://pubchem.ncbi.nlm.nih.gov/compound/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RO = CurieNamespace('ro', 'http://purl.obolibrary.org/obo/RO_')
SDO = CurieNamespace('sdo', 'https://schema.org/')
UO = CurieNamespace('uo', 'http://purl.obolibrary.org/obo/')
DEFAULT_ = NMRSPEC


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class PulsedNmrAssayId(URIorCURIE):
    pass


class NmrSolutionId(URIorCURIE):
    pass


class NmrSampleId(URIorCURIE):
    pass


class NmrSolventId(URIorCURIE):
    pass


class NmrBufferId(URIorCURIE):
    pass


class NmrSpectrometerId(URIorCURIE):
    pass


class NmrSampleTubeId(URIorCURIE):
    pass


class ManufacturerId(URIorCURIE):
    pass


class MolarConcentrationId(URIorCURIE):
    pass


class PhValueId(URIorCURIE):
    pass


class TemperatureId(URIorCURIE):
    pass


class MOLfileId(URIorCURIE):
    pass


class NmrSpecRecordId(URIorCURIE):
    pass


class NmrSpecRecordCollectionId(URIorCURIE):
    pass


@dataclass
class ChemicalDescriptor(YAMLRoot):
    """
    A chemical descriptor is a data item (quantity or value) about a chemical entity that conforms to a specification
    for how it is calculated, measured or recorded.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000123"]
    class_class_curie: ClassVar[str] = "cheminf:000123"
    class_name: ClassVar[str] = "ChemicalDescriptor"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.ChemicalDescriptor

    inchi: Optional[str] = None
    inchikey: Optional[str] = None
    smiles: Optional[str] = None
    mol_file: Optional[Union[dict, "MOLfile"]] = None
    formula: Optional[str] = None
    iupac_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.inchi is not None and not isinstance(self.inchi, str):
            self.inchi = str(self.inchi)

        if self.inchikey is not None and not isinstance(self.inchikey, str):
            self.inchikey = str(self.inchikey)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        if self.mol_file is not None and not isinstance(self.mol_file, MOLfile):
            self.mol_file = MOLfile(**as_dict(self.mol_file))

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

        if self.iupac_name is not None and not isinstance(self.iupac_name, str):
            self.iupac_name = str(self.iupac_name)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    a mixin to be used by any class that has a name and unique id
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SDO.Thing
    class_class_curie: ClassVar[str] = "sdo:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class PulsedNmrAssay(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000613"]
    class_class_curie: ClassVar[str] = "chmo:0000613"
    class_name: ClassVar[str] = "PulsedNmrAssay"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.PulsedNmrAssay

    solution: Union[dict, "NmrSolution"] = None
    spectrometer: Union[dict, "NmrSpectrometer"] = None
    acquisition_nuclei: Union[str, List[str]] = None
    has_dimension: Union[str, "Dimension"] = "1D"
    pulse_program: Union[str, "PulseProgram"] = "not provided"
    id: Union[str, PulsedNmrAssayId] = NMRSPARQL.Assay
    assay_date: Optional[Union[str, XSDDateTime]] = None
    pulse_program_custom: Optional[str] = None
    observed_frequencies: Optional[Union[float, List[float]]] = empty_list()
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PulsedNmrAssayId):
            self.id = PulsedNmrAssayId(self.id)

        if self._is_empty(self.solution):
            self.MissingRequiredField("solution")
        if not isinstance(self.solution, NmrSolution):
            self.solution = NmrSolution(**as_dict(self.solution))

        if self._is_empty(self.spectrometer):
            self.MissingRequiredField("spectrometer")
        if not isinstance(self.spectrometer, NmrSpectrometer):
            self.spectrometer = NmrSpectrometer(**as_dict(self.spectrometer))

        if self._is_empty(self.has_dimension):
            self.MissingRequiredField("has_dimension")
        if not isinstance(self.has_dimension, Dimension):
            self.has_dimension = Dimension(self.has_dimension)

        if self._is_empty(self.pulse_program):
            self.MissingRequiredField("pulse_program")
        if not isinstance(self.pulse_program, PulseProgram):
            self.pulse_program = PulseProgram(self.pulse_program)

        if self._is_empty(self.acquisition_nuclei):
            self.MissingRequiredField("acquisition_nuclei")
        if not isinstance(self.acquisition_nuclei, list):
            self.acquisition_nuclei = [self.acquisition_nuclei] if self.acquisition_nuclei is not None else []
        self.acquisition_nuclei = [v if isinstance(v, str) else str(v) for v in self.acquisition_nuclei]

        if self.assay_date is not None and not isinstance(self.assay_date, XSDDateTime):
            self.assay_date = XSDDateTime(self.assay_date)

        if self.pulse_program_custom is not None and not isinstance(self.pulse_program_custom, str):
            self.pulse_program_custom = str(self.pulse_program_custom)

        if not isinstance(self.observed_frequencies, list):
            self.observed_frequencies = [self.observed_frequencies] if self.observed_frequencies is not None else []
        self.observed_frequencies = [v if isinstance(v, float) else float(v) for v in self.observed_frequencies]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class NmrSolution(YAMLRoot):
    """
    A NMR sollution is the solution made up of the solvent in which the evaluated sample is dissolved in as well as
    possibly the buffer needed to adjust the pH value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["75958"]
    class_class_curie: ClassVar[str] = "CHEBI:75958"
    class_name: ClassVar[str] = "NmrSolution"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSolution

    solvent: Union[dict, "NmrSolvent"] = None
    sample: Union[dict, "NmrSample"] = None
    id: Union[str, NmrSolutionId] = NMRSPARQL.Solution
    buffer: Optional[Union[dict, "NmrBuffer"]] = None
    measured_molarity: Optional[Union[dict, "MolarConcentration"]] = None
    measured_pH: Optional[Union[dict, "PhValue"]] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSolutionId):
            self.id = NmrSolutionId(self.id)

        if self._is_empty(self.solvent):
            self.MissingRequiredField("solvent")
        if not isinstance(self.solvent, NmrSolvent):
            self.solvent = NmrSolvent(**as_dict(self.solvent))

        if self._is_empty(self.sample):
            self.MissingRequiredField("sample")
        if not isinstance(self.sample, NmrSample):
            self.sample = NmrSample(**as_dict(self.sample))

        if self.buffer is not None and not isinstance(self.buffer, NmrBuffer):
            self.buffer = NmrBuffer(**as_dict(self.buffer))

        if self.measured_molarity is not None and not isinstance(self.measured_molarity, MolarConcentration):
            self.measured_molarity = MolarConcentration(**as_dict(self.measured_molarity))

        if self.measured_pH is not None and not isinstance(self.measured_pH, PhValue):
            self.measured_pH = PhValue(**as_dict(self.measured_pH))

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class NmrSample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrSample
    class_class_curie: ClassVar[str] = "NMRspec:NmrSample"
    class_name: ClassVar[str] = "NmrSample"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSample

    id: Union[str, NmrSampleId] = NMRSPARQL.Sample
    local_id: Optional[str] = None
    inchi: Optional[str] = None
    inchikey: Optional[str] = None
    smiles: Optional[str] = None
    mol_file: Optional[Union[dict, "MOLfile"]] = None
    formula: Optional[str] = None
    iupac_name: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSampleId):
            self.id = NmrSampleId(self.id)

        if self.local_id is not None and not isinstance(self.local_id, str):
            self.local_id = str(self.local_id)

        if self.inchi is not None and not isinstance(self.inchi, str):
            self.inchi = str(self.inchi)

        if self.inchikey is not None and not isinstance(self.inchikey, str):
            self.inchikey = str(self.inchikey)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        if self.mol_file is not None and not isinstance(self.mol_file, MOLfile):
            self.mol_file = MOLfile(**as_dict(self.mol_file))

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

        if self.iupac_name is not None and not isinstance(self.iupac_name, str):
            self.iupac_name = str(self.iupac_name)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class NmrSolvent(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrSolvent
    class_class_curie: ClassVar[str] = "NMRspec:NmrSolvent"
    class_name: ClassVar[str] = "NmrSolvent"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSolvent

    id: Union[str, NmrSolventId] = NMRSPARQL.Solvent
    name: Optional[str] = None
    inchi: Optional[str] = None
    inchikey: Optional[str] = None
    smiles: Optional[str] = None
    mol_file: Optional[Union[dict, "MOLfile"]] = None
    formula: Optional[str] = None
    iupac_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSolventId):
            self.id = NmrSolventId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.inchi is not None and not isinstance(self.inchi, str):
            self.inchi = str(self.inchi)

        if self.inchikey is not None and not isinstance(self.inchikey, str):
            self.inchikey = str(self.inchikey)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        if self.mol_file is not None and not isinstance(self.mol_file, MOLfile):
            self.mol_file = MOLfile(**as_dict(self.mol_file))

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

        if self.iupac_name is not None and not isinstance(self.iupac_name, str):
            self.iupac_name = str(self.iupac_name)

        super().__post_init__(**kwargs)


@dataclass
class NmrBuffer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrBuffer
    class_class_curie: ClassVar[str] = "NMRspec:NmrBuffer"
    class_name: ClassVar[str] = "NmrBuffer"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrBuffer

    id: Union[str, NmrBufferId] = NMRSPARQL.Buffer
    inchi: Optional[str] = None
    inchikey: Optional[str] = None
    smiles: Optional[str] = None
    mol_file: Optional[Union[dict, "MOLfile"]] = None
    formula: Optional[str] = None
    iupac_name: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrBufferId):
            self.id = NmrBufferId(self.id)

        if self.inchi is not None and not isinstance(self.inchi, str):
            self.inchi = str(self.inchi)

        if self.inchikey is not None and not isinstance(self.inchikey, str):
            self.inchikey = str(self.inchikey)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        if self.mol_file is not None and not isinstance(self.mol_file, MOLfile):
            self.mol_file = MOLfile(**as_dict(self.mol_file))

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

        if self.iupac_name is not None and not isinstance(self.iupac_name, str):
            self.iupac_name = str(self.iupac_name)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class NmrSpectrometer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000566"]
    class_class_curie: ClassVar[str] = "obi:0000566"
    class_name: ClassVar[str] = "NmrSpectrometer"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSpectrometer

    id: Union[str, NmrSpectrometerId] = NMRSPARQL.Spectrometer
    manufactured_by: Optional[Union[dict, "Manufacturer"]] = None
    type: Optional[str] = None
    sample_tube: Optional[Union[dict, "NmrSampleTube"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSpectrometerId):
            self.id = NmrSpectrometerId(self.id)

        if self.manufactured_by is not None and not isinstance(self.manufactured_by, Manufacturer):
            self.manufactured_by = Manufacturer(**as_dict(self.manufactured_by))

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.sample_tube is not None and not isinstance(self.sample_tube, NmrSampleTube):
            self.sample_tube = NmrSampleTube(**as_dict(self.sample_tube))

        super().__post_init__(**kwargs)


@dataclass
class NmrSampleTube(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000578"]
    class_class_curie: ClassVar[str] = "obi:0000578"
    class_name: ClassVar[str] = "NmrSampleTube"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSampleTube

    id: Union[str, NmrSampleTubeId] = NMRSPARQL.SampleTube
    manufactured_by: Optional[Union[dict, "Manufacturer"]] = None
    type: Optional[str] = None
    measured_temperature: Optional[Union[dict, "Temperature"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSampleTubeId):
            self.id = NmrSampleTubeId(self.id)

        if self.manufactured_by is not None and not isinstance(self.manufactured_by, Manufacturer):
            self.manufactured_by = Manufacturer(**as_dict(self.manufactured_by))

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.measured_temperature is not None and not isinstance(self.measured_temperature, Temperature):
            self.measured_temperature = Temperature(**as_dict(self.measured_temperature))

        super().__post_init__(**kwargs)


@dataclass
class Manufacturer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000835"]
    class_class_curie: ClassVar[str] = "obi:0000835"
    class_name: ClassVar[str] = "Manufacturer"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.Manufacturer

    id: Union[str, ManufacturerId] = NMRSPARQL.Manufacturer
    name: Optional[Union[str, "NmrManufacturers"]] = None
    website: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ManufacturerId):
            self.id = ManufacturerId(self.id)

        if self.name is not None and not isinstance(self.name, NmrManufacturers):
            self.name = NmrManufacturers(self.name)

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        super().__post_init__(**kwargs)


@dataclass
class MolarConcentration(YAMLRoot):
    """
    A quality inhering in a substance by virtue of the amount of the bearer's there is mixed with another substance.
    [Wikipedia:http://en.wikipedia.org/wiki/concentration]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATO["0000033"]
    class_class_curie: ClassVar[str] = "pato:0000033"
    class_name: ClassVar[str] = "MolarConcentration"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.MolarConcentration

    id: Union[str, MolarConcentrationId] = NMRSPARQL.Concentration
    measured_as: Optional[Union[dict, "MolarityMeasurementDatum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolarConcentrationId):
            self.id = MolarConcentrationId(self.id)

        if self.measured_as is not None and not isinstance(self.measured_as, MolarityMeasurementDatum):
            self.measured_as = MolarityMeasurementDatum(**as_dict(self.measured_as))

        super().__post_init__(**kwargs)


@dataclass
class PhValue(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATO["0001842"]
    class_class_curie: ClassVar[str] = "pato:0001842"
    class_name: ClassVar[str] = "PhValue"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.PhValue

    id: Union[str, PhValueId] = NMRSPARQL.PhValue
    measured_as: Optional[Union[dict, "PhMeasurementDatum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhValueId):
            self.id = PhValueId(self.id)

        if self.measured_as is not None and not isinstance(self.measured_as, PhMeasurementDatum):
            self.measured_as = PhMeasurementDatum(**as_dict(self.measured_as))

        super().__post_init__(**kwargs)


@dataclass
class Temperature(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATO["0000146"]
    class_class_curie: ClassVar[str] = "pato:0000146"
    class_name: ClassVar[str] = "Temperature"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.Temperature

    id: Union[str, TemperatureId] = NMRSPARQL.Temperature
    measured_as: Optional[Union[dict, "TemperatureMeasurementDatum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TemperatureId):
            self.id = TemperatureId(self.id)

        if self.measured_as is not None and not isinstance(self.measured_as, TemperatureMeasurementDatum):
            self.measured_as = TemperatureMeasurementDatum(**as_dict(self.measured_as))

        super().__post_init__(**kwargs)


@dataclass
class MolarityMeasurementDatum(YAMLRoot):
    """
    A scalar measurement datum that is the result of measuring the molarity (aka volume concentration) of a chemical
    solution.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IAO["0000032"]
    class_class_curie: ClassVar[str] = "iao:0000032"
    class_name: ClassVar[str] = "MolarityMeasurementDatum"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.MolarityMeasurementDatum

    value: Optional[float] = None
    unit: Optional[Union[str, "MolarityUnit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.unit is not None and not isinstance(self.unit, MolarityUnit):
            self.unit = MolarityUnit(self.unit)

        super().__post_init__(**kwargs)


@dataclass
class PhMeasurementDatum(YAMLRoot):
    """
    A scalar measurement datum that is the result of measuring the pH value of a chemical solution.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IAO["0000032"]
    class_class_curie: ClassVar[str] = "iao:0000032"
    class_name: ClassVar[str] = "PhMeasurementDatum"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.PhMeasurementDatum

    value: Optional[float] = None
    unit: Optional[Union[str, "PhValueUnit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.unit is not None and not isinstance(self.unit, PhValueUnit):
            self.unit = PhValueUnit(self.unit)

        super().__post_init__(**kwargs)


@dataclass
class TemperatureMeasurementDatum(YAMLRoot):
    """
    A scalar measurement datum that is the result of measuring temperature.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0003079"]
    class_class_curie: ClassVar[str] = "obi:0003079"
    class_name: ClassVar[str] = "TemperatureMeasurementDatum"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.TemperatureMeasurementDatum

    value: Optional[float] = None
    unit: Optional[Union[str, "TemperatureUnit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.unit is not None and not isinstance(self.unit, TemperatureUnit):
            self.unit = TemperatureUnit(self.unit)

        super().__post_init__(**kwargs)


@dataclass
class MOLfile(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000114"]
    class_class_curie: ClassVar[str] = "cheminf:000114"
    class_name: ClassVar[str] = "MOLfile"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.MOLfile

    id: Union[str, MOLfileId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MOLfileId):
            self.id = MOLfileId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class NmrSpecRecord(YAMLRoot):
    """
    This is the tree root node of the schema. It is a data item that serves as a container for all relevant
    information about *one* NMR spectroscopy assay record. The properties of this class represent the required
    metadata of an NMR assay, such as: * what kind of assay was performed (e.g. 2D 13C COSY) and what devices where
    used for that (e.g. spectrometer, magnet, solvent, buffer, ...) * what are the detail infos of the assayed sample
    (name, formula, structure, concentration, preperation process, ...)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrSpecRecord
    class_class_curie: ClassVar[str] = "NMRspec:NmrSpecRecord"
    class_name: ClassVar[str] = "NmrSpecRecord"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSpecRecord

    id: Union[str, NmrSpecRecordId] = None
    source: str = None
    output_of_nmr_assay: Optional[Union[dict, PulsedNmrAssay]] = None
    description: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    date_created: Optional[Union[str, XSDDateTime]] = None
    licence_str: Optional[str] = None
    licence_url: Optional[Union[str, URIorCURIE]] = None
    created_by: Optional[Union[str, List[str]]] = empty_list()
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSpecRecordId):
            self.id = NmrSpecRecordId(self.id)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self.output_of_nmr_assay is not None and not isinstance(self.output_of_nmr_assay, PulsedNmrAssay):
            self.output_of_nmr_assay = PulsedNmrAssay(**as_dict(self.output_of_nmr_assay))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if self.date_created is not None and not isinstance(self.date_created, XSDDateTime):
            self.date_created = XSDDateTime(self.date_created)

        if self.licence_str is not None and not isinstance(self.licence_str, str):
            self.licence_str = str(self.licence_str)

        if self.licence_url is not None and not isinstance(self.licence_url, URIorCURIE):
            self.licence_url = URIorCURIE(self.licence_url)

        if not isinstance(self.created_by, list):
            self.created_by = [self.created_by] if self.created_by is not None else []
        self.created_by = [v if isinstance(v, str) else str(v) for v in self.created_by]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class NmrSpecRecordCollection(YAMLRoot):
    """
    This class represents a collection of NMR spectroscopy records. It is to be used when multiple NMR assays were
    made in order to analyse a given sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrSpecRecordCollection
    class_class_curie: ClassVar[str] = "NMRspec:NmrSpecRecordCollection"
    class_name: ClassVar[str] = "NmrSpecRecordCollection"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSpecRecordCollection

    id: Union[str, NmrSpecRecordCollectionId] = None
    contains_assay_records: Union[Dict[Union[str, NmrSpecRecordId], Union[dict, NmrSpecRecord]], List[Union[dict, NmrSpecRecord]]] = empty_dict()
    assays_sample: Union[dict, NmrSample] = None
    source: str = None
    description: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    date_created: Optional[Union[str, XSDDateTime]] = None
    licence_str: Optional[str] = None
    licence_url: Optional[Union[str, URIorCURIE]] = None
    created_by: Optional[Union[str, List[str]]] = empty_list()
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSpecRecordCollectionId):
            self.id = NmrSpecRecordCollectionId(self.id)

        if self._is_empty(self.contains_assay_records):
            self.MissingRequiredField("contains_assay_records")
        self._normalize_inlined_as_list(slot_name="contains_assay_records", slot_type=NmrSpecRecord, key_name="id", keyed=True)

        if self._is_empty(self.assays_sample):
            self.MissingRequiredField("assays_sample")
        if not isinstance(self.assays_sample, NmrSample):
            self.assays_sample = NmrSample(**as_dict(self.assays_sample))

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if self.date_created is not None and not isinstance(self.date_created, XSDDateTime):
            self.date_created = XSDDateTime(self.date_created)

        if self.licence_str is not None and not isinstance(self.licence_str, str):
            self.licence_str = str(self.licence_str)

        if self.licence_url is not None and not isinstance(self.licence_url, URIorCURIE):
            self.licence_url = URIorCURIE(self.licence_url)

        if not isinstance(self.created_by, list):
            self.created_by = [self.created_by] if self.created_by is not None else []
        self.created_by = [v if isinstance(v, str) else str(v) for v in self.created_by]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


# Enumerations
class PulseProgram(EnumDefinitionImpl):
    """
    Enum of the most commonly used pulse sequences that specify the type of pulsed NMR. Based on a mix of Bruker specs
    (https://pharm.ucsf.edu/sites/pharm.ucsf.edu/files/Pulse%20Program%20Catalog%201%20%281D%20and%202D%20Experiments%29.pdf),
    IUPAC specs (http://www.jcamp-dx.org/protocols/NMR%20Pulse%20Sequences%20PAC%2079(11)%20pp1748-1764%202001.pdf)
    and JEOL specs (https://www.uh.edu/nsm/chemistry/resources/nmr/ECAXSII_Advanced_Mode_Tutorial_Manual.pdf)
    """
    NMR = PermissibleValue(text="NMR")
    COSY = PermissibleValue(text="COSY")
    SECSY = PermissibleValue(text="SECSY")
    RELAY = PermissibleValue(text="RELAY")
    TOCSY = PermissibleValue(text="TOCSY")
    ROESY = PermissibleValue(text="ROESY")
    NOESY = PermissibleValue(text="NOESY")
    DEPT = PermissibleValue(text="DEPT")
    INEPT = PermissibleValue(text="INEPT")
    HECTOR = PermissibleValue(text="HECTOR")
    COLOC = PermissibleValue(text="COLOC")
    HOESY = PermissibleValue(text="HOESY")
    INADEQUATE = PermissibleValue(text="INADEQUATE")
    HMQC = PermissibleValue(text="HMQC")
    HSQC = PermissibleValue(text="HSQC")
    TROSY = PermissibleValue(text="TROSY")
    CRINEPT = PermissibleValue(text="CRINEPT")
    H2BC = PermissibleValue(text="H2BC")
    HMBC = PermissibleValue(text="HMBC")
    HSQMBC = PermissibleValue(text="HSQMBC")
    EXSIDE = PermissibleValue(text="EXSIDE")
    HETLOC = PermissibleValue(text="HETLOC")
    ADEQUATE = PermissibleValue(text="ADEQUATE")
    DOSY = PermissibleValue(text="DOSY")
    STE = PermissibleValue(text="STE")
    STEBP = PermissibleValue(text="STEBP")
    DSTE = PermissibleValue(text="DSTE")
    DSTEBP = PermissibleValue(text="DSTEBP")
    CLEANEX = PermissibleValue(text="CLEANEX")
    Custom = PermissibleValue(text="Custom",
                                   description="To be used, if the pulse program is not in this list.")

    _defn = EnumDefinition(
        name="PulseProgram",
        description="Enum of the most commonly used pulse sequences that specify the type of pulsed NMR. Based on a mix of Bruker specs (https://pharm.ucsf.edu/sites/pharm.ucsf.edu/files/Pulse%20Program%20Catalog%201%20%281D%20and%202D%20Experiments%29.pdf), IUPAC specs (http://www.jcamp-dx.org/protocols/NMR%20Pulse%20Sequences%20PAC%2079(11)%20pp1748-1764%202001.pdf) and JEOL specs (https://www.uh.edu/nsm/chemistry/resources/nmr/ECAXSII_Advanced_Mode_Tutorial_Manual.pdf)",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Inverse NMR",
                PermissibleValue(text="Inverse NMR") )
        setattr(cls, "COSY-DQF",
                PermissibleValue(text="COSY-DQF") )
        setattr(cls, "J-Resolved",
                PermissibleValue(text="J-Resolved") )
        setattr(cls, "DEPT-HMQC",
                PermissibleValue(text="DEPT-HMQC") )
        setattr(cls, "Inverse-INEPT",
                PermissibleValue(text="Inverse-INEPT") )
        setattr(cls, "HMQC-COSY",
                PermissibleValue(text="HMQC-COSY") )
        setattr(cls, "HQMC-TOSCY",
                PermissibleValue(text="HQMC-TOSCY") )
        setattr(cls, "HMQC-ROESY",
                PermissibleValue(text="HMQC-ROESY") )
        setattr(cls, "HMQC-NOESY",
                PermissibleValue(text="HMQC-NOESY") )
        setattr(cls, "HSQC-TOSCY",
                PermissibleValue(text="HSQC-TOSCY") )
        setattr(cls, "HSQC-ROESY",
                PermissibleValue(text="HSQC-ROESY") )
        setattr(cls, "HSQC-NOESY",
                PermissibleValue(text="HSQC-NOESY") )
        setattr(cls, "HSQC-HECADE",
                PermissibleValue(text="HSQC-HECADE") )
        setattr(cls, "COSY-DOSY",
                PermissibleValue(text="COSY-DOSY") )
        setattr(cls, "DOSY-TOCSY",
                PermissibleValue(text="DOSY-TOCSY") )
        setattr(cls, "DOSY-NOESY",
                PermissibleValue(text="DOSY-NOESY") )
        setattr(cls, "DOSY-HMQC",
                PermissibleValue(text="DOSY-HMQC") )
        setattr(cls, "STD-TOSCY",
                PermissibleValue(text="STD-TOSCY") )
        setattr(cls, "STD-NOESY",
                PermissibleValue(text="STD-NOESY") )
        setattr(cls, "STD-HSQC",
                PermissibleValue(text="STD-HSQC") )
        setattr(cls, "CLEANEX-HSQC",
                PermissibleValue(text="CLEANEX-HSQC") )
        setattr(cls, "CLEANEX-TROSY",
                PermissibleValue(text="CLEANEX-TROSY") )
        setattr(cls, "not provided",
                PermissibleValue(text="not provided",
                                 description="This is only to be used, if there no way to derive which pulse program has been used.") )

class NmrManufacturers(EnumDefinitionImpl):
    """
    Controlled list of manufacturers of NMR lab devices.
    """
    Bruker = PermissibleValue(text="Bruker")
    FOSS = PermissibleValue(text="FOSS")
    JEOL = PermissibleValue(text="JEOL")
    Jasco = PermissibleValue(text="Jasco")
    OceanOptics = PermissibleValue(text="OceanOptics")
    Phillips = PermissibleValue(text="Phillips")
    TX = PermissibleValue(text="TX")
    ThermoFinnigan = PermissibleValue(text="ThermoFinnigan")
    ThermoMattson = PermissibleValue(text="ThermoMattson")
    ThermoNicolet = PermissibleValue(text="ThermoNicolet")
    Varian = PermissibleValue(text="Varian")
    Waters = PermissibleValue(text="Waters")
    Wilmad = PermissibleValue(text="Wilmad")
    acdlabs = PermissibleValue(text="acdlabs")
    micromass = PermissibleValue(text="micromass")
    tecmag = PermissibleValue(text="tecmag")

    _defn = EnumDefinition(
        name="NmrManufacturers",
        description="Controlled list of manufacturers of NMR lab devices.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Acorn NMR Inc",
                PermissibleValue(text="Acorn NMR Inc") )
        setattr(cls, "Agilent Technologies",
                PermissibleValue(text="Agilent Technologies") )
        setattr(cls, "Applied Biosystems",
                PermissibleValue(text="Applied Biosystems") )
        setattr(cls, "Doty Scientific",
                PermissibleValue(text="Doty Scientific") )
        setattr(cls, "General Electric",
                PermissibleValue(text="General Electric") )
        setattr(cls, "JS Research",
                PermissibleValue(text="JS Research") )
        setattr(cls, "Kimble Chase",
                PermissibleValue(text="Kimble Chase") )
        setattr(cls, "MR Resources",
                PermissibleValue(text="MR Resources") )
        setattr(cls, "Oxford Instruments",
                PermissibleValue(text="Oxford Instruments") )
        setattr(cls, "Perkin Elmer",
                PermissibleValue(text="Perkin Elmer") )
        setattr(cls, "Siemens AG",
                PermissibleValue(text="Siemens AG") )
        setattr(cls, "Spinlock SRL",
                PermissibleValue(text="Spinlock SRL") )

class Dimension(EnumDefinitionImpl):
    """
    The dimensionality of the produced spectrum.
    """
    _defn = EnumDefinition(
        name="Dimension",
        description="The dimensionality of the produced spectrum.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1D",
                PermissibleValue(text="1D") )
        setattr(cls, "2D",
                PermissibleValue(text="2D") )
        setattr(cls, "3D",
                PermissibleValue(text="3D") )
        setattr(cls, "4D",
                PermissibleValue(text="4D") )

class MolarityUnit(EnumDefinitionImpl):
    """
    Enums of needed units aligned with UO. *WIP:needs to be expanded*
    """
    femtomolar = PermissibleValue(text="femtomolar",
                                           meaning=UO["0000073"])
    micromolar = PermissibleValue(text="micromolar")
    millimolar = PermissibleValue(text="millimolar")
    molar = PermissibleValue(text="molar",
                                 meaning=UO["0000062"])
    nanomolar = PermissibleValue(text="nanomolar")
    picomolar = PermissibleValue(text="picomolar")

    _defn = EnumDefinition(
        name="MolarityUnit",
        description="Enums of needed units aligned with UO. *WIP:needs to be expanded*",
    )

class PhValueUnit(EnumDefinitionImpl):

    pH = PermissibleValue(text="pH",
                           meaning=UO["0000196"])

    _defn = EnumDefinition(
        name="PhValueUnit",
    )

class TemperatureUnit(EnumDefinitionImpl):

    Celsius = PermissibleValue(text="Celsius",
                                     meaning=UO["0000027"])
    Kelvin = PermissibleValue(text="Kelvin")

    _defn = EnumDefinition(
        name="TemperatureUnit",
    )

# Slots

