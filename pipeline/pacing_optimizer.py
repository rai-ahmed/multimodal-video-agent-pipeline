"""
Audio Pacing and Narration Timing Optimizer
Analyzes speech rate and aligns narration beats with visual cuts.
"""
from typing import Dict, Any, List


class PacingOptimizer:
    """Computes Words-Per-Minute (WPM) and optimizes retention timing."""

    def __init__(self, target_wpm_min: float = 145.0, target_wpm_max: float = 165.0):
        self.target_wpm_min = target_wpm_min
        self.target_wpm_max = target_wpm_max

    def analyze_script(self, script_text: str, allocated_duration_sec: float) -> Dict[str, Any]:
        words = script_text.split()
        word_count = len(words)
        duration_minutes = allocated_duration_sec / 60.0
        actual_wpm = word_count / duration_minutes if duration_minutes > 0 else 0.0

        is_balanced = self.target_wpm_min <= actual_wpm <= self.target_wpm_max
        recommended_duration = (word_count / ((self.target_wpm_min + self.target_wpm_max) / 2)) * 60.0

        return {
            "word_count": word_count,
            "actual_wpm": round(actual_wpm, 1),
            "is_balanced": is_balanced,
            "recommended_duration_sec": round(recommended_duration, 2),
            "suggested_cut_intervals": self._calculate_cut_intervals(allocated_duration_sec, word_count)
        }

    def _calculate_cut_intervals(self, duration_sec: float, word_count: int) -> List[float]:
        # Target cut frequency every 2.5 - 4.0 seconds for modern high-retention video
        num_cuts = max(1, int(duration_sec // 3.0))
        interval = duration_sec / num_cuts
        return [round((i + 1) * interval, 2) for i in range(num_cuts)]
