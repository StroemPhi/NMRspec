# Auto generated from NMR-spectroscopy-schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-22T15:54:07
# Schema: NMR-spectroscopy-schema
#
# id: https://git.tib.eu/lab-linked-scientific-knowledge/nmr-research-data-semantification/-/blob/main/nmr_assay_schema.yaml
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
from linkml_runtime.linkml_model.types import Datetime, Float, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
FAIRSPEC = CurieNamespace('FAIRspec', 'https://github.com/IUPAC/IUPAC-FAIRSpec/blob/main/src/main/java/org/iupac/fairspec/core/')
NMRSPEC = CurieNamespace('NMRspec', 'https://nfdi4chem/nmr/data/')
BFO = CurieNamespace('bfo', 'http://purl.obolibrary.org/obo/BFO_')
CHEBI = CurieNamespace('chebi', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMINF = CurieNamespace('cheminf', 'http://purl.obolibrary.org/obo/CHEMINF_')
CHEMOTION = CurieNamespace('chemotion', 'https://chemotion.de/')
CHMO = CurieNamespace('chmo', 'http://purl.obolibrary.org/obo/CHMO_')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://doi.org/')
IAO = CurieNamespace('iao', 'http://purl.obolibrary.org/obo/IAO_')
ISA = CurieNamespace('isa', 'https://isa-specs.readthedocs.io/en/latest/isamodel.html#')
JDX = CurieNamespace('jdx', 'http://www.jcamp-dx.org/protocols/dxnmr01.pdf/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMRCV = CurieNamespace('nmrCV', 'http://nmrML.org/nmrCV#')
OBI = CurieNamespace('obi', 'http://purl.obolibrary.org/obo/OBI_')
OM = CurieNamespace('om', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
PATO = CurieNamespace('pato', 'http://purl.obolibrary.org/obo/PATO_')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
PUBCHEM = CurieNamespace('pubchem', 'https://pubchem.com/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RO = CurieNamespace('ro', 'http://purl.obolibrary.org/obo/RO_')
SDO = CurieNamespace('sdo', 'https://schema.org/')
DEFAULT_ = NMRSPEC


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class PulsedNmrAssayId(URIorCURIE):
    pass


class NmrSampleId(URIorCURIE):
    pass


class NmrSolventId(URIorCURIE):
    pass


class NmrBufferId(URIorCURIE):
    pass


class NmrSpectrometerId(URIorCURIE):
    pass


class NmrSpecRecordId(URIorCURIE):
    pass


@dataclass
class ProvenanceData(YAMLRoot):
    """
    This is a mixin to be used by any class that is needed as part of an audit trail to ensure the provenance of the
    metadata.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.ProvenanceData
    class_class_curie: ClassVar[str] = "NMRspec:ProvenanceData"
    class_name: ClassVar[str] = "ProvenanceData"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.ProvenanceData

    source: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    date_retrieved: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if self.date_retrieved is not None and not isinstance(self.date_retrieved, XSDDateTime):
            self.date_retrieved = XSDDateTime(self.date_retrieved)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalMetadata(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.ChemicalMetadata
    class_class_curie: ClassVar[str] = "NMRspec:ChemicalMetadata"
    class_name: ClassVar[str] = "ChemicalMetadata"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.ChemicalMetadata

    formula: Optional[str] = None
    inchi: Optional[str] = None
    inchikey: Optional[str] = None
    smiles: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

        if self.inchi is not None and not isinstance(self.inchi, str):
            self.inchi = str(self.inchi)

        if self.inchikey is not None and not isinstance(self.inchikey, str):
            self.inchikey = str(self.inchikey)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
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

    id: Union[str, PulsedNmrAssayId] = None
    assayed_solution: Union[dict, "NmrSolution"] = None
    spectrometer: Union[dict, "NmrSpectrometer"] = None
    has_dimension: Union[str, "Dimension"] = None
    pulse_program: Union[str, "PulseProgram"] = None
    acuisition_nuclei: Union[str, List[str]] = None
    name: Optional[str] = None
    assay_date: Optional[Union[str, XSDDateTime]] = None
    observed_frequencies: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PulsedNmrAssayId):
            self.id = PulsedNmrAssayId(self.id)

        if self._is_empty(self.assayed_solution):
            self.MissingRequiredField("assayed_solution")
        if not isinstance(self.assayed_solution, NmrSolution):
            self.assayed_solution = NmrSolution(**as_dict(self.assayed_solution))

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

        if self._is_empty(self.acuisition_nuclei):
            self.MissingRequiredField("acuisition_nuclei")
        if not isinstance(self.acuisition_nuclei, list):
            self.acuisition_nuclei = [self.acuisition_nuclei] if self.acuisition_nuclei is not None else []
        self.acuisition_nuclei = [v if isinstance(v, str) else str(v) for v in self.acuisition_nuclei]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.assay_date is not None and not isinstance(self.assay_date, XSDDateTime):
            self.assay_date = XSDDateTime(self.assay_date)

        if not isinstance(self.observed_frequencies, list):
            self.observed_frequencies = [self.observed_frequencies] if self.observed_frequencies is not None else []
        self.observed_frequencies = [v if isinstance(v, float) else float(v) for v in self.observed_frequencies]

        super().__post_init__(**kwargs)


@dataclass
class NmrSolution(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["75958"]
    class_class_curie: ClassVar[str] = "chebi:75958"
    class_name: ClassVar[str] = "NmrSolution"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSolution

    solvent: Union[dict, "NmrSolvent"] = None
    sample: Union[dict, "NmrSample"] = None
    buffer: Optional[Union[dict, "NmrBuffer"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        super().__post_init__(**kwargs)


@dataclass
class NmrSample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrSample
    class_class_curie: ClassVar[str] = "NMRspec:NmrSample"
    class_name: ClassVar[str] = "NmrSample"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSample

    id: Union[str, NmrSampleId] = None
    local_id: Optional[str] = None
    formula: Optional[str] = None
    inchi: Optional[str] = None
    inchikey: Optional[str] = None
    smiles: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSampleId):
            self.id = NmrSampleId(self.id)

        if self.local_id is not None and not isinstance(self.local_id, str):
            self.local_id = str(self.local_id)

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

        if self.inchi is not None and not isinstance(self.inchi, str):
            self.inchi = str(self.inchi)

        if self.inchikey is not None and not isinstance(self.inchikey, str):
            self.inchikey = str(self.inchikey)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

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

    id: Union[str, NmrSolventId] = None
    name: Optional[str] = None
    formula: Optional[str] = None
    inchi: Optional[str] = None
    inchikey: Optional[str] = None
    smiles: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSolventId):
            self.id = NmrSolventId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

        if self.inchi is not None and not isinstance(self.inchi, str):
            self.inchi = str(self.inchi)

        if self.inchikey is not None and not isinstance(self.inchikey, str):
            self.inchikey = str(self.inchikey)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        super().__post_init__(**kwargs)


@dataclass
class NmrBuffer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrBuffer
    class_class_curie: ClassVar[str] = "NMRspec:NmrBuffer"
    class_name: ClassVar[str] = "NmrBuffer"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrBuffer

    id: Union[str, NmrBufferId] = None
    formula: Optional[str] = None
    inchi: Optional[str] = None
    inchikey: Optional[str] = None
    smiles: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrBufferId):
            self.id = NmrBufferId(self.id)

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

        if self.inchi is not None and not isinstance(self.inchi, str):
            self.inchi = str(self.inchi)

        if self.inchikey is not None and not isinstance(self.inchikey, str):
            self.inchikey = str(self.inchikey)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class NmrSpectrometer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrSpectrometer
    class_class_curie: ClassVar[str] = "NMRspec:NmrSpectrometer"
    class_name: ClassVar[str] = "NmrSpectrometer"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSpectrometer

    id: Union[str, NmrSpectrometerId] = None
    manufactured_by: Optional[Union[dict, "Manufacturer"]] = None
    type: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSpectrometerId):
            self.id = NmrSpectrometerId(self.id)

        if self.manufactured_by is not None and not isinstance(self.manufactured_by, Manufacturer):
            self.manufactured_by = Manufacturer(**as_dict(self.manufactured_by))

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Manufacturer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000835"]
    class_class_curie: ClassVar[str] = "obi:0000835"
    class_name: ClassVar[str] = "Manufacturer"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.Manufacturer

    name: Optional[Union[str, "NmrManufacturers"]] = None
    website: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, NmrManufacturers):
            self.name = NmrManufacturers(self.name)

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        super().__post_init__(**kwargs)


@dataclass
class NmrSpecRecord(YAMLRoot):
    """
    This is the tree root node of the schema. It is a data item that serves as a container for all relevant
    information about one NMR spectroscopy assay record. The properties of this class represent the required metadata
    of an NMR assay, such as: * what kind of assay was performed (e.g. 2D 13C COSY) and what devices where used for
    that (e.g. spectrometer, magnet, solvent, buffer, ...) * what are the detail infos of the assayed sample (name,
    formula, structure, concentration, preperation process, ...)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrSpecRecord
    class_class_curie: ClassVar[str] = "NMRspec:NmrSpecRecord"
    class_name: ClassVar[str] = "NmrSpecRecord"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSpecRecord

    id: Union[str, NmrSpecRecordId] = None
    output_of_nmr_assay: Union[dict, PulsedNmrAssay] = None
    source: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    date_retrieved: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSpecRecordId):
            self.id = NmrSpecRecordId(self.id)

        if self._is_empty(self.output_of_nmr_assay):
            self.MissingRequiredField("output_of_nmr_assay")
        if not isinstance(self.output_of_nmr_assay, PulsedNmrAssay):
            self.output_of_nmr_assay = PulsedNmrAssay(**as_dict(self.output_of_nmr_assay))

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if self.date_retrieved is not None and not isinstance(self.date_retrieved, XSDDateTime):
            self.date_retrieved = XSDDateTime(self.date_retrieved)

        super().__post_init__(**kwargs)


# Enumerations
class PulseProgram(EnumDefinitionImpl):

    NMR = PermissibleValue(text="NMR")
    COSY = PermissibleValue(text="COSY")
    DOSY = PermissibleValue(text="DOSY")
    SECSY = PermissibleValue(text="SECSY")
    RELAY = PermissibleValue(text="RELAY")
    TOCSY = PermissibleValue(text="TOCSY")
    ROESY = PermissibleValue(text="ROESY")
    NOESY = PermissibleValue(text="NOESY")
    HECTOR = PermissibleValue(text="HECTOR")
    COLOC = PermissibleValue(text="COLOC")
    HOESY = PermissibleValue(text="HOESY")
    INADEQUATE = PermissibleValue(text="INADEQUATE")
    HMQC = PermissibleValue(text="HMQC")
    TROSY = PermissibleValue(text="TROSY")
    CRINEPT = PermissibleValue(text="CRINEPT")
    H2BC = PermissibleValue(text="H2BC")
    HMBC = PermissibleValue(text="HMBC")
    EXSIDE = PermissibleValue(text="EXSIDE")
    HETLOC = PermissibleValue(text="HETLOC")
    ADEQUATE = PermissibleValue(text="ADEQUATE")
    STE = PermissibleValue(text="STE")
    STEBP = PermissibleValue(text="STEBP")
    CLEANEX = PermissibleValue(text="CLEANEX")
    DSTE = PermissibleValue(text="DSTE")
    DSTEBP = PermissibleValue(text="DSTEBP")

    _defn = EnumDefinition(
        name="PulseProgram",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "COSY-DQF",
                PermissibleValue(text="COSY-DQF") )
        setattr(cls, "COSY-DOSY",
                PermissibleValue(text="COSY-DOSY") )
        setattr(cls, "Double-Quantum",
                PermissibleValue(text="Double-Quantum") )
        setattr(cls, "J-Resolved",
                PermissibleValue(text="J-Resolved") )
        setattr(cls, "DEPT & INEPT",
                PermissibleValue(text="DEPT & INEPT") )
        setattr(cls, "Heteronuclear J-resolved",
                PermissibleValue(text="Heteronuclear J-resolved") )
        setattr(cls, "Inverse 1H-NMR",
                PermissibleValue(text="Inverse 1H-NMR") )
        setattr(cls, "DEPT-HMQC",
                PermissibleValue(text="DEPT-HMQC") )
        setattr(cls, "Multiplicity-edited HSQC",
                PermissibleValue(text="Multiplicity-edited HSQC") )
        setattr(cls, "CT-HSQC",
                PermissibleValue(text="CT-HSQC") )
        setattr(cls, "CT-HMBC",
                PermissibleValue(text="CT-HMBC") )
        setattr(cls, "Inverse-INEPT",
                PermissibleValue(text="Inverse-INEPT") )
        setattr(cls, "2D HSQC-α,β",
                PermissibleValue(text="2D HSQC-α,β") )
        setattr(cls, "2D IPAP-HSQC",
                PermissibleValue(text="2D IPAP-HSQC") )
        setattr(cls, "2D J-modulated CT-HSQC",
                PermissibleValue(text="2D J-modulated CT-HSQC") )
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
        setattr(cls, "Phase-sensitive HMBC",
                PermissibleValue(text="Phase-sensitive HMBC") )
        setattr(cls, "J-HMBC",
                PermissibleValue(text="J-HMBC") )
        setattr(cls, "Long-range HSQC (HSQMBC)",
                PermissibleValue(text="Long-range HSQC (HSQMBC)") )
        setattr(cls, "HSQC-HECADE",
                PermissibleValue(text="HSQC-HECADE") )
        setattr(cls, "1,1-ADEQUATE",
                PermissibleValue(text="1,1-ADEQUATE") )
        setattr(cls, "1,n-ADEQUATE",
                PermissibleValue(text="1,n-ADEQUATE") )
        setattr(cls, "n,1-ADEQUATE",
                PermissibleValue(text="n,1-ADEQUATE") )
        setattr(cls, "n,n-ADEQUATE",
                PermissibleValue(text="n,n-ADEQUATE") )
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
        setattr(cls, "DOSY-TOCSY",
                PermissibleValue(text="DOSY-TOCSY") )
        setattr(cls, "DOSY-NOESY",
                PermissibleValue(text="DOSY-NOESY") )
        setattr(cls, "DOSY-HMQC",
                PermissibleValue(text="DOSY-HMQC") )

class NmrManufacturers(EnumDefinitionImpl):

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

    _defn = EnumDefinition(
        name="Dimension",
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

# Slots

