# Auto generated from NMR-spectroscopy-schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-17T23:40:30
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
from linkml_runtime.linkml_model.types import Datetime, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NMRSPEC = CurieNamespace('NMRspec', 'https://nfdi4chem/nmr/data/')
BFO = CurieNamespace('bfo', 'http://purl.obolibrary.org/obo/BFO_')
CHEBI = CurieNamespace('chebi', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMINF = CurieNamespace('cheminf', 'http://purl.obolibrary.org/obo/CHEMINF_')
CHEMOTION = CurieNamespace('chemotion', 'https://chemotion.de/')
CHMO = CurieNamespace('chmo', 'http://purl.obolibrary.org/obo/CHMO_')
DOI = CurieNamespace('doi', 'https://doi.org/')
IAO = CurieNamespace('iao', 'http://purl.obolibrary.org/obo/IAO_')
ISA = CurieNamespace('isa', 'https://isa-specs.readthedocs.io/en/latest/isamodel.html#')
IUPAC = CurieNamespace('iupac', 'https://github.com/IUPAC/IUPAC-FAIRSpec/blob/main/src/main/java/org/iupac/fairspec/core/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMRCV = CurieNamespace('nmrCV', 'http://nmrML.org/nmrCV#')
OBI = CurieNamespace('obi', 'http://purl.obolibrary.org/obo/OBI_')
OM = CurieNamespace('om', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
PATO = CurieNamespace('pato', 'http://purl.obolibrary.org/obo/PATO_')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
PUBCHEM = CurieNamespace('pubchem', 'https://pubchem.com/')
RO = CurieNamespace('ro', 'http://purl.obolibrary.org/obo/RO_')
SDO = CurieNamespace('sdo', 'https://schema.org/')
DEFAULT_ = NMRSPEC


# Types

# Class references
class PulsedNmrAssayId(extended_str):
    pass


class NmrSampleId(extended_str):
    pass


class NmrSolventId(extended_str):
    pass


class NmrSpectrometerId(extended_str):
    pass


class NmrSpecRecordId(extended_str):
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
class PulsedNmrAssay(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000613"]
    class_class_curie: ClassVar[str] = "chmo:0000613"
    class_name: ClassVar[str] = "PulsedNmrAssay"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.PulsedNmrAssay

    id: Union[str, PulsedNmrAssayId] = None
    pulse_program: Union[str, "PulseProgram"] = None
    has_dimension: Union[str, "Dimension"] = None
    acuisition_nucleus: Union[str, List[str]] = None
    sample: Union[dict, "NmrSample"] = None
    solvent: Union[dict, "NmrSolvent"] = None
    spectrometer: Union[dict, "NmrSpectrometer"] = None
    name: Optional[str] = None
    assay_date: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PulsedNmrAssayId):
            self.id = PulsedNmrAssayId(self.id)

        if self._is_empty(self.pulse_program):
            self.MissingRequiredField("pulse_program")
        if not isinstance(self.pulse_program, PulseProgram):
            self.pulse_program = PulseProgram(self.pulse_program)

        if self._is_empty(self.has_dimension):
            self.MissingRequiredField("has_dimension")
        if not isinstance(self.has_dimension, Dimension):
            self.has_dimension = Dimension(self.has_dimension)

        if self._is_empty(self.acuisition_nucleus):
            self.MissingRequiredField("acuisition_nucleus")
        if not isinstance(self.acuisition_nucleus, list):
            self.acuisition_nucleus = [self.acuisition_nucleus] if self.acuisition_nucleus is not None else []
        self.acuisition_nucleus = [v if isinstance(v, str) else str(v) for v in self.acuisition_nucleus]

        if self._is_empty(self.sample):
            self.MissingRequiredField("sample")
        if not isinstance(self.sample, NmrSample):
            self.sample = NmrSample(**as_dict(self.sample))

        if self._is_empty(self.solvent):
            self.MissingRequiredField("solvent")
        if not isinstance(self.solvent, NmrSolvent):
            self.solvent = NmrSolvent(**as_dict(self.solvent))

        if self._is_empty(self.spectrometer):
            self.MissingRequiredField("spectrometer")
        if not isinstance(self.spectrometer, NmrSpectrometer):
            self.spectrometer = NmrSpectrometer(**as_dict(self.spectrometer))

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.assay_date is not None and not isinstance(self.assay_date, XSDDateTime):
            self.assay_date = XSDDateTime(self.assay_date)

        super().__post_init__(**kwargs)


@dataclass
class NmrSample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrSample
    class_class_curie: ClassVar[str] = "NMRspec:NmrSample"
    class_name: ClassVar[str] = "NmrSample"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSample

    id: Union[str, NmrSampleId] = None
    name: Optional[str] = None
    local_id: Optional[str] = None
    formula: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSampleId):
            self.id = NmrSampleId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.local_id is not None and not isinstance(self.local_id, str):
            self.local_id = str(self.local_id)

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

        super().__post_init__(**kwargs)


@dataclass
class NmrSolvent(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrSolvent
    class_class_curie: ClassVar[str] = "NMRspec:NmrSolvent"
    class_name: ClassVar[str] = "NmrSolvent"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSolvent

    id: Union[str, NmrSolventId] = None
    formula: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSolventId):
            self.id = NmrSolventId(self.id)

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

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
    manufacturered_by: Optional[Union[dict, "Manufacturer"]] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSpectrometerId):
            self.id = NmrSpectrometerId(self.id)

        if self.manufacturered_by is not None and not isinstance(self.manufacturered_by, Manufacturer):
            self.manufacturered_by = Manufacturer(**as_dict(self.manufacturered_by))

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

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
    A data item that is an NMR assay output which represents the data produced by an NMR assay of a studied sample
    compound.
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
        setattr(cls, "COSY-DOSY",
                PermissibleValue(text="COSY-DOSY") )
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

