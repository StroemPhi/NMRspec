# Auto generated from Provenance.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-03-17T17:18:06
# Schema: Provenance
#
# id: https://raw.githubusercontent.com/StroemPhi/NMRspec/main/model/schema/Provenance.yaml
# description: Provenance mixin
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
DCE = CurieNamespace('dce', 'http://purl.org/dc/elements/1.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SDO = CurieNamespace('sdo', 'https://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://raw.githubusercontent.com/StroemPhi/NMRspec/main/model/schema/Provenance.yaml/')


# Types

# Class references



@dataclass
class Provenance(YAMLRoot):
    """
    This is a mixin to be used by any class that is needed as part of an audit trail to ensure the provenance of the
    metadata.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://raw.githubusercontent.com/StroemPhi/NMRspec/main/model/schema/Provenance.yaml/Provenance")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Provenance"
    class_model_uri: ClassVar[URIRef] = URIRef("https://raw.githubusercontent.com/StroemPhi/NMRspec/main/model/schema/Provenance.yaml/Provenance")

    source: str = None
    description: Optional[str] = None
    source_uri: Optional[Union[str, URIorCURIE]] = None
    date_created: Optional[Union[str, XSDDateTime]] = None
    licence_str: Optional[str] = None
    licence_url: Optional[Union[str, URIorCURIE]] = None
    created_by: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        super().__post_init__(**kwargs)


# Enumerations


# Slots

