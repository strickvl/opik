# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class DatasetPublic(UniversalBaseModel):
    id: typing.Optional[str] = None
    name: str
    description: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    created_by: typing.Optional[str] = None
    last_updated_at: typing.Optional[dt.datetime] = None
    last_updated_by: typing.Optional[str] = None
    experiment_count: typing.Optional[int] = None
    dataset_items_count: typing.Optional[int] = None
    most_recent_experiment_at: typing.Optional[dt.datetime] = None
    last_created_experiment_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
