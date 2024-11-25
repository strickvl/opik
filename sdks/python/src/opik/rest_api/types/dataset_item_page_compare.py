# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .dataset_item_compare import DatasetItemCompare
from .column_compare import ColumnCompare
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class DatasetItemPageCompare(UniversalBaseModel):
    content: typing.Optional[typing.List[DatasetItemCompare]] = None
    page: typing.Optional[int] = None
    size: typing.Optional[int] = None
    total: typing.Optional[int] = None
    columns: typing.Optional[typing.List[ColumnCompare]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
