# Auto generated from NMR-spectroscopy-schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-10T15:57:41
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
class PlannedProcessId(extended_str):
    pass


class AssayId(PlannedProcessId):
    pass


class NMRspectroscopyId(AssayId):
    pass


class PulsedNMRspectroscopyId(NMRspectroscopyId):
    pass


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
    source_uri: Optional[Union[str, URIorCURIE]] = None
    creator: Optional[Union[str, List[str]]] = empty_list()
    publisher: Optional[str] = None
    date_retrieved: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if not isinstance(self.creator, list):
            self.creator = [self.creator] if self.creator is not None else []
        self.creator = [v if isinstance(v, str) else str(v) for v in self.creator]

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.date_retrieved is not None and not isinstance(self.date_retrieved, XSDDateTime):
            self.date_retrieved = XSDDateTime(self.date_retrieved)

        super().__post_init__(**kwargs)


@dataclass
class PlannedProcess(YAMLRoot):
    """
    A process that realizes a plan which is the concretization of a plan specification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000011"]
    class_class_curie: ClassVar[str] = "obi:0000011"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.PlannedProcess

    id: Union[str, PlannedProcessId] = None
    title: Optional[str] = None
    type: Optional[str] = None
    achieves_planned_objective: Optional[str] = None
    source: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    creator: Optional[Union[str, List[str]]] = empty_list()
    publisher: Optional[str] = None
    date_retrieved: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlannedProcessId):
            self.id = PlannedProcessId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.achieves_planned_objective is not None and not isinstance(self.achieves_planned_objective, str):
            self.achieves_planned_objective = str(self.achieves_planned_objective)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if not isinstance(self.creator, list):
            self.creator = [self.creator] if self.creator is not None else []
        self.creator = [v if isinstance(v, str) else str(v) for v in self.creator]

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.date_retrieved is not None and not isinstance(self.date_retrieved, XSDDateTime):
            self.date_retrieved = XSDDateTime(self.date_retrieved)

        super().__post_init__(**kwargs)


@dataclass
class Assay(PlannedProcess):
    """
    A planned process with the objective to produce information about the material entity that is the evaluant, by
    physically examining it or its proxies.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000070"]
    class_class_curie: ClassVar[str] = "obi:0000070"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.Assay

    id: Union[str, AssayId] = None
    has_specified_input: Optional[str] = None
    has_specified_output: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssayId):
            self.id = AssayId(self.id)

        if self.has_specified_input is not None and not isinstance(self.has_specified_input, str):
            self.has_specified_input = str(self.has_specified_input)

        if self.has_specified_output is not None and not isinstance(self.has_specified_output, str):
            self.has_specified_output = str(self.has_specified_output)

        super().__post_init__(**kwargs)


@dataclass
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

    id: Union[str, NMRspectroscopyId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NMRspectroscopyId):
            self.id = NMRspectroscopyId(self.id)

        super().__post_init__(**kwargs)


@dataclass
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

    id: Union[str, PulsedNMRspectroscopyId] = None
    pulse_sequence: Optional[Union[dict, "PulseSequenceSpecification"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PulsedNMRspectroscopyId):
            self.id = PulsedNMRspectroscopyId(self.id)

        if self.pulse_sequence is not None and not isinstance(self.pulse_sequence, PulseSequenceSpecification):
            self.pulse_sequence = PulseSequenceSpecification(**as_dict(self.pulse_sequence))

        super().__post_init__(**kwargs)


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

    records_nmr_spec: Union[Dict[Union[str, NMRspectroscopyId], Union[dict, NMRspectroscopy]], List[Union[dict, NMRspectroscopy]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.records_nmr_spec):
            self.MissingRequiredField("records_nmr_spec")
        self._normalize_inlined_as_list(slot_name="records_nmr_spec", slot_type=NMRspectroscopy, key_name="id", keyed=True)

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


@dataclass
class CategoricalValueSpecification(YAMLRoot):
    """
    A value specification that is specifies one category out of a fixed number of nominal categories
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0001930"]
    class_class_curie: ClassVar[str] = "obi:0001930"
    class_name: ClassVar[str] = "CategoricalValueSpecification"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.CategoricalValueSpecification

    specifies_value_of: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.specifies_value_of is not None and not isinstance(self.specifies_value_of, str):
            self.specifies_value_of = str(self.specifies_value_of)

        super().__post_init__(**kwargs)


@dataclass
class PulseSequenceSpecification(CategoricalValueSpecification):
    """
    A categorical specification that is used to specify which pulse sequence has been used in a pulsed NMR
    spectroscopy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.PulseSequenceSpecification
    class_class_curie: ClassVar[str] = "NMRspec:PulseSequenceSpecification"
    class_name: ClassVar[str] = "PulseSequenceSpecification"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.PulseSequenceSpecification

    specifies_value_of: Optional[Union[str, PulsedNMRspectroscopyId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.specifies_value_of is not None and not isinstance(self.specifies_value_of, PulsedNMRspectroscopyId):
            self.specifies_value_of = PulsedNMRspectroscopyId(self.specifies_value_of)

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

