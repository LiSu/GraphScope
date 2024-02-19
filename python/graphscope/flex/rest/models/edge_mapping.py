# coding: utf-8

"""
    GraphScope FLEX HTTP SERVICE API

    This is a specification for GraphScope FLEX HTTP service based on the OpenAPI 3.0 specification. You can find out more details about specification at [doc](https://swagger.io/specification/v3/).  Some useful links: - [GraphScope Repository](https://github.com/alibaba/GraphScope) - [The Source API definition for GraphScope Interactive](https://github.com/GraphScope/portal/tree/main/httpservice)

    The version of the OpenAPI document: 0.9.1
    Contact: graphscope@alibaba-inc.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from graphscope.flex.rest.models.column_mapping import ColumnMapping
from graphscope.flex.rest.models.edge_mapping_destination_vertex_mappings_inner import EdgeMappingDestinationVertexMappingsInner
from graphscope.flex.rest.models.edge_mapping_source_vertex_mappings_inner import EdgeMappingSourceVertexMappingsInner
from graphscope.flex.rest.models.edge_mapping_type_triplet import EdgeMappingTypeTriplet
from typing import Optional, Set
from typing_extensions import Self

class EdgeMapping(BaseModel):
    """
    EdgeMapping
    """ # noqa: E501
    type_triplet: Optional[EdgeMappingTypeTriplet] = None
    inputs: Optional[List[StrictStr]] = None
    source_vertex_mappings: Optional[List[EdgeMappingSourceVertexMappingsInner]] = None
    destination_vertex_mappings: Optional[List[EdgeMappingDestinationVertexMappingsInner]] = None
    column_mappings: Optional[List[ColumnMapping]] = None
    __properties: ClassVar[List[str]] = ["type_triplet", "inputs", "source_vertex_mappings", "destination_vertex_mappings", "column_mappings"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EdgeMapping from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of type_triplet
        if self.type_triplet:
            _dict['type_triplet'] = self.type_triplet.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in source_vertex_mappings (list)
        _items = []
        if self.source_vertex_mappings:
            for _item in self.source_vertex_mappings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['source_vertex_mappings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in destination_vertex_mappings (list)
        _items = []
        if self.destination_vertex_mappings:
            for _item in self.destination_vertex_mappings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['destination_vertex_mappings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in column_mappings (list)
        _items = []
        if self.column_mappings:
            for _item in self.column_mappings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['column_mappings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EdgeMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type_triplet": EdgeMappingTypeTriplet.from_dict(obj["type_triplet"]) if obj.get("type_triplet") is not None else None,
            "inputs": obj.get("inputs"),
            "source_vertex_mappings": [EdgeMappingSourceVertexMappingsInner.from_dict(_item) for _item in obj["source_vertex_mappings"]] if obj.get("source_vertex_mappings") is not None else None,
            "destination_vertex_mappings": [EdgeMappingDestinationVertexMappingsInner.from_dict(_item) for _item in obj["destination_vertex_mappings"]] if obj.get("destination_vertex_mappings") is not None else None,
            "column_mappings": [ColumnMapping.from_dict(_item) for _item in obj["column_mappings"]] if obj.get("column_mappings") is not None else None
        })
        return _obj


