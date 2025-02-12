from typing import Dict, List, Union

from msgspec import field

from ..common import BaseStruct


class BGMBank(BaseStruct):
    name: str
    intro: Union[str, None]
    loop: Union[str, None]
    volume: float
    crossfade: float
    delay: float


class SoundFXBankSoundFX(BaseStruct):
    asset: str
    weight: float
    important: bool
    is2D: bool
    delay: float
    minPitch: float
    maxPitch: float
    minVolume: float
    maxVolume: float
    ignoreTimeScale: bool


class SoundFXBank(BaseStruct):
    name: str
    sounds: Union[List[SoundFXBankSoundFX], None]
    maxSoundAllowed: int
    popOldest: bool
    customMixerGroup: Union[str, None]
    loop: bool


class SoundFXCtrlBank(BaseStruct):
    name: str
    targetBank: str
    ctrlStop: bool
    ctrlStopFadetime: float


class SnapshotBank(BaseStruct):
    name: str
    targetSnapshot: str
    hookSoundFxBank: str
    delay: float
    duration: float
    targetFxBank: Union[str, None] = None


class BattleVoiceOption(BaseStruct):
    voiceType: int
    priority: int
    overlapIfSamePriority: bool
    cooldown: float
    delay: float


class MusicData(BaseStruct):
    id_: str = field(name='id')
    name: str
    bank: str


class BattleVoiceData(BaseStruct):
    crossfade: float
    minTimeDeltaForEnemyEncounter: float
    minSpCostForImportantPassiveSkill: int
    voiceTypeOptions: List[BattleVoiceOption]


class AudioData(BaseStruct):
    __version__ = '23-10-08-17-52-18-288259'

    bgmBanks: List[BGMBank]
    soundFXBanks: List[SoundFXBank]
    soundFXCtrlBanks: List[SoundFXCtrlBank]
    snapshotBanks: List[SnapshotBank]
    battleVoice: BattleVoiceData
    musics: List[MusicData]
    soundFxVoiceLang: Dict[str, Dict[str, Dict[str, str]]]
    bankAlias: Dict[str, str]
