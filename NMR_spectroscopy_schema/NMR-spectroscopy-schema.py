# Auto generated from NMR-spectroscopy-schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-17T11:08:16
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
from linkml_runtime.linkml_model.types import Datetime, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NMRSPEC = CurieNamespace('NMRspec', 'https://nfdi4chem/nmr/data/')
NMRMANUFACTURERS = CurieNamespace('NmrManufacturers', 'http://example.org/UNKNOWN/NmrManufacturers/')
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
PATO = CurieNamespace('pato', 'http://purl.obolibrary.org/obo/PATO_')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RO = CurieNamespace('ro', 'http://purl.obolibrary.org/obo/RO_')
SDO = CurieNamespace('sdo', 'https://schema.org/')
DEFAULT_ = NMRSPEC


# Types

# Class references
class NmrBufferId(extended_str):
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

    sample: Union[dict, "NmrSample"] = None
    buffer: Union[dict, "NmrBuffer"] = None
    type: Union[str, "NmrAssayType"] = None
    spectrometer: Optional[Union[dict, "NmrSpectrometer"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sample):
            self.MissingRequiredField("sample")
        if not isinstance(self.sample, NmrSample):
            self.sample = NmrSample(**as_dict(self.sample))

        if self._is_empty(self.buffer):
            self.MissingRequiredField("buffer")
        if not isinstance(self.buffer, NmrBuffer):
            self.buffer = NmrBuffer(**as_dict(self.buffer))

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, NmrAssayType):
            self.type = NmrAssayType(self.type)

        if self.spectrometer is not None and not isinstance(self.spectrometer, NmrSpectrometer):
            self.spectrometer = NmrSpectrometer(**as_dict(self.spectrometer))

        super().__post_init__(**kwargs)


@dataclass
class NmrSample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrSample
    class_class_curie: ClassVar[str] = "NMRspec:NmrSample"
    class_name: ClassVar[str] = "NmrSample"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSample

    name: Optional[str] = None
    local_id: Optional[str] = None
    formula: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.local_id is not None and not isinstance(self.local_id, str):
            self.local_id = str(self.local_id)

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

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
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrBufferId):
            self.id = NmrBufferId(self.id)

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Instrument(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.Instrument
    class_class_curie: ClassVar[str] = "NMRspec:Instrument"
    class_name: ClassVar[str] = "Instrument"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.Instrument

    manufacturered_by: Optional[Union[dict, "Manufacturer"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.manufacturered_by is not None and not isinstance(self.manufacturered_by, Manufacturer):
            self.manufacturered_by = Manufacturer()

        super().__post_init__(**kwargs)


@dataclass
class NmrSpectrometer(Instrument):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrSpectrometer
    class_class_curie: ClassVar[str] = "NMRspec:NmrSpectrometer"
    class_name: ClassVar[str] = "NmrSpectrometer"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSpectrometer

    magnet: Optional[str] = None
    probe: Optional[str] = None
    sample_tube: Optional[str] = None
    manufacturered_by: Optional[Union[dict, "NmrManufacturer"]] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.magnet is not None and not isinstance(self.magnet, str):
            self.magnet = str(self.magnet)

        if self.probe is not None and not isinstance(self.probe, str):
            self.probe = str(self.probe)

        if self.sample_tube is not None and not isinstance(self.sample_tube, str):
            self.sample_tube = str(self.sample_tube)

        if self.manufacturered_by is not None and not isinstance(self.manufacturered_by, NmrManufacturer):
            self.manufacturered_by = NmrManufacturer(**as_dict(self.manufacturered_by))

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


class Manufacturer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.Manufacturer
    class_class_curie: ClassVar[str] = "NMRspec:Manufacturer"
    class_name: ClassVar[str] = "Manufacturer"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.Manufacturer


@dataclass
class NmrManufacturer(Manufacturer):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrManufacturer
    class_class_curie: ClassVar[str] = "NMRspec:NmrManufacturer"
    class_name: ClassVar[str] = "NmrManufacturer"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrManufacturer

    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

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
class NmrAssayType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="NmrAssayType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1D-1H-NMR",
                PermissibleValue(text="1D-1H-NMR",
                                 meaning=CHMO["0002442"]) )
        setattr(cls, "2DJ-DOSY",
                PermissibleValue(text="2DJ-DOSY",
                                 meaning=CHMO["0001953"]) )
        setattr(cls, "3D-COSY-DOSY",
                PermissibleValue(text="3D-COSY-DOSY",
                                 meaning=CHMO["0001951"]) )
        setattr(cls, "3D-DOSY-TOCSY",
                PermissibleValue(text="3D-DOSY-TOCSY",
                                 meaning=CHMO["0001950"]) )
        setattr(cls, "3D-DOSY-HMQC",
                PermissibleValue(text="3D-DOSY-HMQC",
                                 meaning=CHMO["0001952"]) )

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

# Slots

