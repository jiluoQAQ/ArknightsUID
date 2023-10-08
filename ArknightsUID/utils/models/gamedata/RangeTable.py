from typing import Dict, List, Union

from ..common import BaseStruct

from msgspec import field


class GridPosition(BaseStruct):
    row: int
    col: int


class ObscuredRect(BaseStruct):
    m_xMin: float
    m_yMin: float
    m_width: float
    m_height: float


class Stage(BaseStruct):
    id_: str = field(name='id')
    direction: int
    grids: List[GridPosition]
    boundingBoxes: Union[List[ObscuredRect], None] = None


class RangeTable(BaseStruct):
    __version__ = '23-09-29-15-41-03-569cae'

    range_: Dict[str, Stage]
