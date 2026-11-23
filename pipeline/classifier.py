"""
Shot Classification Agent
Routes production shots between deterministic 3D blocking and generative video diffusion.
"""
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Any


class ShotCategory(str, Enum):
    DETERMINISTIC_3D = "DETERMINISTIC_3D"      # Close facial contact, lip sync, precise choreography
    GENERATIVE_ENHANCED = "GENERATIVE_ENHANCED"  # 3D base geometry enhanced by diffusion models
    GENERATIVE_FIRST = "GENERATIVE_FIRST"        # Atmospheric landscapes, macro environmental shots


@dataclass
class ShotDescriptor:
    shot_id: str
    description: str
    has_named_characters: bool
    requires_lip_sync: bool
    has_precise_interaction: bool
    environment_focus: bool
    target_duration_sec: float


class ShotClassifier:
    """Categorizes shots deterministically to prevent generative drift."""

    @staticmethod
    def classify(shot: ShotDescriptor) -> ShotCategory:
        if shot.requires_lip_sync or shot.has_precise_interaction:
            return ShotCategory.DETERMINISTIC_3D
        if shot.has_named_characters and not shot.environment_focus:
            return ShotCategory.DETERMINISTIC_3D
        if shot.has_named_characters and shot.environment_focus:
            return ShotCategory.GENERATIVE_ENHANCED
        return ShotCategory.GENERATIVE_FIRST

    def classify_manifest(self, shots: List[ShotDescriptor]) -> Dict[str, ShotCategory]:
        return {shot.shot_id: self.classify(shot) for shot in shots}
