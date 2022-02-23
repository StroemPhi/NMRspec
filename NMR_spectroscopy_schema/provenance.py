# Auto generated from provenance.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-23T15:21:57
# Schema: provenance
#
# id: https://github.com/StroemPhi/NMR-spectroscopy-schema/provenance
# description: provenance mixin
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
NMRSPEC = CurieNamespace('NMRspec', 'https://github.com/StroemPhi/NMR-spectroscopy-schema/')
DCT = CurieNamespace('dct', 'http://example.org/UNKNOWN/dct/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = NMRSPEC


# Types

# Class references



@dataclass
class Provenance(YAMLRoot):
    """
    This is a mixin to be used by any class that is needed as part of an audit trail to ensure the provenance of the
    metadata.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMRSPEC.Provenance
    class_class_curie: ClassVar[str] = "NMRspec:Provenance"
    class_name: ClassVar[str] = "provenance"
    class_model_uri: ClassVar[URIRef] = NMRSPEC.Provenance

    source: str = None
    source_file: str = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    date_retrieved: Optional[Union[str, XSDDateTime]] = None
    licence_str: Optional[str] = None
    licence_url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.source_file):
            self.MissingRequiredField("source_file")
        if not isinstance(self.source_file, str):
            self.source_file = str(self.source_file)

        if self.source_uri is not None and not isinstance(self.source_uri, URIorCURIE):
            self.source_uri = URIorCURIE(self.source_uri)

        if self.date_retrieved is not None and not isinstance(self.date_retrieved, XSDDateTime):
            self.date_retrieved = XSDDateTime(self.date_retrieved)

        if self.licence_str is not None and not isinstance(self.licence_str, str):
            self.licence_str = str(self.licence_str)

        if self.licence_url is not None and not isinstance(self.licence_url, URIorCURIE):
            self.licence_url = URIorCURIE(self.licence_url)

        super().__post_init__(**kwargs)


# Enumerations


# Slots

