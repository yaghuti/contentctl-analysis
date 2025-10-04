from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, Any, List

if TYPE_CHECKING:
    from contentctl.input.director import DirectorOutputDto

import pathlib

from pydantic import (
    Field,
    ValidationInfo,
    computed_field,
    field_validator,
    model_serializer,
)

from contentctl.objects.baseline_tags import BaselineTags
from contentctl.objects.config import CustomApp
from contentctl.objects.constants import (
    CONTENTCTL_BASELINE_STANZA_NAME_FORMAT_TEMPLATE,
    CONTENTCTL_MAX_SEARCH_NAME_LENGTH,
)
from contentctl.objects.deployment import Deployment
from contentctl.objects.enums import ContentStatus, DataModel
from contentctl.objects.lookup import Lookup
from contentctl.objects.security_content_object import SecurityContentObject


class Baseline(SecurityContentObject):
    name: str = Field(..., max_length=CONTENTCTL_MAX_SEARCH_NAME_LENGTH)
    type: Annotated[str, Field(pattern="^Baseline$")] = Field(...)
    search: str = Field(..., min_length=4)
    how_to_implement: str = Field(..., min_length=4)
    known_false_positives: str = Field(..., min_length=4)
    tags: BaselineTags = Field(...)
    lookups: list[Lookup] = Field([], validate_default=True)
    # enrichment
