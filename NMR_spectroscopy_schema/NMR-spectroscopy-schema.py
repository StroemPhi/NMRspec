# Auto generated from NMR-spectroscopy-schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-16T12:29:50
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
NMRSPEC = CurieNamespace('NMRspec', 'https://raw.githubusercontent.com/StroemPhi/NMR-spectroscopy-schema/main/model/schema/sample_model.yaml')
BFO = CurieNamespace('bfo', 'http://purl.obolibrary.org/obo/BFO_')
CHEBI = CurieNamespace('chebi', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMINF = CurieNamespace('cheminf', 'http://purl.obolibrary.org/obo/CHEMINF_')
CHMO = CurieNamespace('chmo', 'http://purl.obolibrary.org/obo/CHMO_')
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
class NMRspecRecordId(extended_str):
    pass


@dataclass
class HasProvenanceData(YAMLRoot):
    """
    This is a mixin to be used by any class that is needed a part of an audit trail to ensure the provenance of the
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
class NMRspecRecord(YAMLRoot):
    """
    A data item that is an NMR assay output which represents the data produced by an NMR assay of a studied sample
    compound.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NMRspecRecord
    class_class_curie: ClassVar[str] = "NMRspec:NMRspecRecord"
    class_name: ClassVar[str] = "NMRspecRecord"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NMRspecRecord

    id: Union[str, NMRspecRecordId] = None
    source: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    date_retrieved: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NMRspecRecordId):
            self.id = NMRspecRecordId(self.id)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if self.date_retrieved is not None and not isinstance(self.date_retrieved, XSDDateTime):
            self.date_retrieved = XSDDateTime(self.date_retrieved)

        super().__post_init__(**kwargs)


@dataclass
class NMRspecRecords(YAMLRoot):
    """
    A container for holding multiple NMR assay records.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NMRspecRecords
    class_class_curie: ClassVar[str] = "NMRspec:NMRspecRecords"
    class_name: ClassVar[str] = "NMRspecRecords"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NMRspecRecords

    nmr_spec_records: Optional[Union[Union[str, NMRspecRecordId], List[Union[str, NMRspecRecordId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.nmr_spec_records, list):
            self.nmr_spec_records = [self.nmr_spec_records] if self.nmr_spec_records is not None else []
        self.nmr_spec_records = [v if isinstance(v, NMRspecRecordId) else NMRspecRecordId(v) for v in self.nmr_spec_records]

        super().__post_init__(**kwargs)


# Enumerations
class PulsedNMRSpecTypes(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="PulsedNMRSpecTypes",
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

