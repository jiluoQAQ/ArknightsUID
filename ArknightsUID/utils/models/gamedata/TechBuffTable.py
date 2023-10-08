from typing import List, Union

from ..common import BaseStruct

from msgspec import field


class RuneDataSelector(BaseStruct):
    professionMask: int
    buildableMask: int
    charIdFilter: Union[List[str], None]
    enemyIdFilter: Union[List[str], None]
    skillIdFilter: Union[List[str], None]
    tileKeyFilter: Union[List[str], None]


class Blackboard(BaseStruct):
    key: str
    value: Union[float, None] = None
    valueStr: Union[str, None] = None


class RuneData(BaseStruct):
    key: str
    selector: RuneDataSelector
    blackboard: List[Blackboard]


class PackedRuneData(BaseStruct):
    id_: str = field(name='id')
    points: float
    mutexGroupKey: Union[str, None]
    description: str
    runes: List[RuneData]


class TechBuffTable(BaseStruct):
    __version__ = '23-09-29-15-41-03-569cae'

    runes: List[PackedRuneData]
