from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING, List

from pydantic import (
    Field,
    HttpUrl,
    computed_field,
    field_validator,
    model_serializer,
    model_validator,
)

from contentctl.objects.story_tags import StoryTags

if TYPE_CHECKING:
    from contentctl.objects.baseline import Baseline
    from contentctl.objects.config import CustomApp
    from contentctl.objects.data_source import DataSource
    from contentctl.objects.detection import Detection
    from contentctl.objects.investigation import Investigation

import pathlib

from contentctl.objects.enums import ContentStatus
from contentctl.objects.security_content_object import SecurityContentObject


class Story(SecurityContentObject):
    narrative: str = Field(...)
    tags: StoryTags = Field(...)
    status: ContentStatus
    # These are updated when detection and investigation objects are created.
    # Specifically in the model_post_init functions
    detections: List[Detection] = []
    investigations: List[Investigation] = []
    baselines: List[Baseline] = []

    @field_validator("status", mode="after")
    @classmethod
    def NarrowStatus(cls, status: ContentStatus) -> ContentStatus:
        return cls.NarrowStatusTemplate(
            status, [ContentStatus.production, ContentStatus.deprecated]
        )

    @classmethod
    def containing_folder(cls) -> pathlib.Path:
        return pathlib.Path("stories")

    @computed_field
