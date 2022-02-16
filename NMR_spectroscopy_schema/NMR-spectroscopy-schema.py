# Auto generated from NMR-spectroscopy-schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-17T00:30:36
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
class NmrSpecRecordId(extended_str):
    pass


class NmrBufferId(extended_str):
    pass


@dataclass
class HasProvenanceData(YAMLRoot):
    """
    This is a mixin to be used by any class that is needed as part of an audit trail to ensure the provenance of the
    metadata.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.HasProvenanceData
    class_class_curie: ClassVar[str] = "NMRspec:HasProvenanceData"
    class_name: ClassVar[str] = "HasProvenanceData"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.HasProvenanceData

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

    has_specified_input: Union[Union[dict, "NmrAssayInput"], List[Union[dict, "NmrAssayInput"]]] = None
    type: Union[str, "NmrAssayType"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.has_specified_input):
            self.MissingRequiredField("has_specified_input")
        self._normalize_inlined_as_dict(slot_name="has_specified_input", slot_type=NmrAssayInput, key_name="sample", keyed=False)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, NmrAssayType):
            self.type = NmrAssayType(self.type)

        super().__post_init__(**kwargs)


@dataclass
class NmrAssayInput(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrAssayInput
    class_class_curie: ClassVar[str] = "NMRspec:NmrAssayInput"
    class_name: ClassVar[str] = "NmrAssayInput"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrAssayInput

    sample: Union[dict, "NmrSample"] = None
    buffer: Optional[Union[str, NmrBufferId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sample):
            self.MissingRequiredField("sample")
        if not isinstance(self.sample, NmrSample):
            self.sample = NmrSample(**as_dict(self.sample))

        if self.buffer is not None and not isinstance(self.buffer, NmrBufferId):
            self.buffer = NmrBufferId(self.buffer)

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
    is_specified_output_of: Union[dict, PulsedNmrAssay] = None
    source: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    date_retrieved: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrSpecRecordId):
            self.id = NmrSpecRecordId(self.id)

        if self._is_empty(self.is_specified_output_of):
            self.MissingRequiredField("is_specified_output_of")
        if not isinstance(self.is_specified_output_of, PulsedNmrAssay):
            self.is_specified_output_of = PulsedNmrAssay(**as_dict(self.is_specified_output_of))

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if self.date_retrieved is not None and not isinstance(self.date_retrieved, XSDDateTime):
            self.date_retrieved = XSDDateTime(self.date_retrieved)

        super().__post_init__(**kwargs)


@dataclass
class NmrSample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NmrSample
    class_class_curie: ClassVar[str] = "NMRspec:NmrSample"
    class_name: ClassVar[str] = "NmrSample"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NmrSample

    local_id: Optional[str] = None
    name: Optional[str] = None
    formula: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.local_id is not None and not isinstance(self.local_id, str):
            self.local_id = str(self.local_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

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
    name: Optional[str] = None
    formula: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NmrBufferId):
            self.id = NmrBufferId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

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

# Slots

