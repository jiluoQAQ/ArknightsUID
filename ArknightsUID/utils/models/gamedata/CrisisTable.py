from typing import Dict, List, Union

from msgspec import field

from ..common import BaseStruct


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class StringKeyFrames(BaseStruct):
    level: int
    data: str


class CrisisClientDataSeasonInfo(BaseStruct):
    seasonId: str
    startTs: int
    endTs: int
    name: str
    crisisRuneCoinUnlockItem: ItemBundle
    permBgm: str
    medalGroupId: Union[str, None]
    bgmHardPoint: int
    permBgmHard: Union[str, None]


class CrisisMapRankInfo(BaseStruct):
    rewards: List[ItemBundle]
    unlockPoint: int


class CrisisTable(BaseStruct):
    __version__ = '23-10-08-17-52-18-288259'

    seasonInfo: List[CrisisClientDataSeasonInfo]
    tempAppraise: List[StringKeyFrames]
    permAppraise: List[StringKeyFrames]
    mapRankInfo: Dict[str, CrisisMapRankInfo]
    meta: str
    unlockCoinLv3: int
    hardPointPerm: int
    hardPointTemp: int
    voiceGrade: int
    crisisRuneCoinUnlockItemTitle: str
    crisisRuneCoinUnlockItemDesc: str
