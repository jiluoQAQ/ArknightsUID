from typing import Dict, List, Union

from msgspec import field

from ..common import BaseStruct


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class StoryDataConditionStageCondition(BaseStruct):
    stageId: str
    minState: int
    maxState: int


class StoryReviewInfoClientData(BaseStruct):
    storyReviewType: int
    storyId: str
    storyGroup: str
    storySort: int
    storyDependence: Union[str, None]
    storyCanShow: int
    storyCode: Union[str, None]
    storyName: str
    storyPic: Union[str, None]
    storyInfo: str
    storyCanEnter: int
    storyTxt: str
    avgTag: str
    unLockType: str
    costItemType: str
    costItemId: Union[str, None]
    costItemCount: int
    stageCount: int
    requiredStages: Union[List[StoryDataConditionStageCondition], None]


class StoryReviewGroupClientData(BaseStruct):
    id_: str = field(name='id')
    name: str
    entryType: str
    actType: str
    startTime: int
    endTime: int
    startShowTime: int
    endShowTime: int
    remakeStartTime: int
    remakeEndTime: int
    storyEntryPicId: Union[str, None]
    storyPicId: Union[str, None]
    storyMainColor: Union[str, None]
    customType: int
    storyCompleteMedalId: Union[str, None]
    rewards: Union[List[ItemBundle], None]
    infoUnlockDatas: List[StoryReviewInfoClientData]


class StoryReviewTable(BaseStruct):
    __version__ = '23-10-08-17-52-18-288259'

    storyreviewtable: Dict[str, StoryReviewGroupClientData]
