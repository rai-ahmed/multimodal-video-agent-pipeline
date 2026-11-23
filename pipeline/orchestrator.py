"""
Video Pipeline Orchestrator
Coordinates shot classification, timing allocation, and composite rendering.
"""
from typing import List, Dict, Any
from .classifier import ShotClassifier, ShotDescriptor, ShotCategory
from .pacing_optimizer import PacingOptimizer


class MultimodalVideoPipeline:
    def __init__(self):
        self.classifier = ShotClassifier()
        self.pacing = PacingOptimizer()

    def plan_production(self, title: str, script: str, shots: List[ShotDescriptor]) -> Dict[str, Any]:
        total_duration = sum(s.target_duration_sec for s in shots)
        pacing_report = self.pacing.analyze_script(script, total_duration)
        classification = self.classifier.classify_manifest(shots)

        return {
            "title": title,
            "total_shots": len(shots),
            "total_duration_sec": total_duration,
            "pacing_analysis": pacing_report,
            "shot_routing": {k: v.value for k, v in classification.items()}
        }
