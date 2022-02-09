# Auto generated from NMR-assay-schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-09T17:21:55
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
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"

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
NMRCV = CurieNamespace('nmrcv', 'http://nmrML.org/nmrCV#')
OBI = CurieNamespace('obi', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('pato', 'http://purl.obolibrary.org/obo/PATO_')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RO = CurieNamespace('ro', 'http://purl.obolibrary.org/obo/RO_')
SDO = CurieNamespace('sdo', 'https://schema.org/')
DEFAULT_ = NMRSPEC


# Types

# Class references



@dataclass
class HasProvenance(YAMLRoot):
    """
    This is a mixin to be used by any class that is needed a part of an audit trail to ensure the provenance of the
    metadata.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.HasProvenance
    class_class_curie: ClassVar[str] = "NMRspec:HasProvenance"
    class_name: ClassVar[str] = "HasProvenance"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.HasProvenance

    source: Optional[str] = None
    source_uri: Optional[str] = None
    creator: Optional[str] = None
    publisher: Optional[str] = None
    date_retrieved: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.source_uri is not None and not isinstance(self.source_uri, str):
            self.source_uri = str(self.source_uri)

        if self.creator is not None and not isinstance(self.creator, str):
            self.creator = str(self.creator)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.date_retrieved is not None and not isinstance(self.date_retrieved, str):
            self.date_retrieved = str(self.date_retrieved)

        super().__post_init__(**kwargs)


class Assay(YAMLRoot):
    """
    A planned process with the objective to produce information about the material entity that is the evaluant, by
    physically examining it or its proxies.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000070"]
    class_class_curie: ClassVar[str] = "obi:0000070"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.Assay


class NMRspectroscopy(Assay):
    """
    An assay that exploits the magnetic properties of certain nuclei (those with a spin) to resonate when placed in
    particular magnetic field conditions. Instruments recording NMR spectrum and sets of analysis can be used to
    deduce identity of chemical as well as composition of complex chemical mixtures.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000623"]
    class_class_curie: ClassVar[str] = "obi:0000623"
    class_name: ClassVar[str] = "NMRspectroscopy"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NMRspectroscopy


class PulsedNMRspectroscopy(NMRspectroscopy):
    """
    Spectroscopy where the energy states of spin-active nuclei placed in a static magnetic field are interrogated by
    inducing transitions between the states via radio frequency irradiation. Each experiment consists of a sequence of
    radio frequency pulses with delay periods in between them. [ rsc:pr ]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000613"]
    class_class_curie: ClassVar[str] = "chmo:0000613"
    class_name: ClassVar[str] = "PulsedNMRspectroscopy"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.PulsedNMRspectroscopy


class AssayOutput(YAMLRoot):
    """
    A data item that is the specified output of an assay. May be a file, dataset etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000793"]
    class_class_curie: ClassVar[str] = "chmo:0000793"
    class_name: ClassVar[str] = "AssayOutput"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.AssayOutput


@dataclass
class NMRspecRecord(AssayOutput):
    """
    A data item that is an NMR assay output which represents the data produced by an NMR assay of a studied sample
    compound.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.NMRspecRecord
    class_class_curie: ClassVar[str] = "NMRspec:NMRspecRecord"
    class_name: ClassVar[str] = "NMRspecRecord"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.NMRspecRecord

    records_nmr_spec: Union[Union[dict, NMRspectroscopy], List[Union[dict, NMRspectroscopy]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.records_nmr_spec):
            self.MissingRequiredField("records_nmr_spec")
        if not isinstance(self.records_nmr_spec, list):
            self.records_nmr_spec = [self.records_nmr_spec] if self.records_nmr_spec is not None else []
        self.records_nmr_spec = [v if isinstance(v, NMRspectroscopy) else NMRspectroscopy(**as_dict(v)) for v in self.records_nmr_spec]

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

    nmr_spec_records: Optional[Union[Union[dict, NMRspecRecord], List[Union[dict, NMRspecRecord]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.nmr_spec_records, list):
            self.nmr_spec_records = [self.nmr_spec_records] if self.nmr_spec_records is not None else []
        self.nmr_spec_records = [v if isinstance(v, NMRspecRecord) else NMRspecRecord(**as_dict(v)) for v in self.nmr_spec_records]

        super().__post_init__(**kwargs)


# Enumerations


# Slots

