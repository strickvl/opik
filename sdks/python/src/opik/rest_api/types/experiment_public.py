# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .json_node_public import JsonNodePublic
from .feedback_score_average_public import FeedbackScoreAveragePublic
from .comment_public import CommentPublic
import datetime as dt
from .prompt_version_link_public import PromptVersionLinkPublic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ExperimentPublic(UniversalBaseModel):
    id: typing.Optional[str] = None
    dataset_name: str
    dataset_id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    metadata: typing.Optional[JsonNodePublic] = None
    feedback_scores: typing.Optional[typing.List[FeedbackScoreAveragePublic]] = None
    comments: typing.Optional[typing.List[CommentPublic]] = None
    trace_count: typing.Optional[int] = None
    created_at: typing.Optional[dt.datetime] = None
    last_updated_at: typing.Optional[dt.datetime] = None
    created_by: typing.Optional[str] = None
    last_updated_by: typing.Optional[str] = None
    prompt_version: typing.Optional[PromptVersionLinkPublic] = None
    prompt_versions: typing.Optional[typing.List[PromptVersionLinkPublic]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
