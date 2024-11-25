# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .feedback_score_compare_source import FeedbackScoreCompareSource
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class FeedbackScoreCompare(UniversalBaseModel):
    name: str
    category_name: typing.Optional[str] = None
    value: float
    reason: typing.Optional[str] = None
    source: FeedbackScoreCompareSource
    created_at: typing.Optional[dt.datetime] = None
    last_updated_at: typing.Optional[dt.datetime] = None
    created_by: typing.Optional[str] = None
    last_updated_by: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
