"""
CLI Runner for Multimodal Video Generation Pipeline
"""
from pipeline import MultimodalVideoPipeline, ShotDescriptor


def main():
    pipeline = MultimodalVideoPipeline()

    sample_shots = [
        ShotDescriptor(
            shot_id="SHOT_001",
            description="Character close-up speaking dialogue",
            has_named_characters=True,
            requires_lip_sync=True,
            has_precise_interaction=False,
            environment_focus=False,
            target_duration_sec=3.5
        ),
        ShotDescriptor(
            shot_id="SHOT_002",
            description="Wide panoramic landscape of ancient city",
            has_named_characters=False,
            requires_lip_sync=False,
            has_precise_interaction=False,
            environment_focus=True,
            target_duration_sec=4.0
        ),
        ShotDescriptor(
            shot_id="SHOT_003",
            description="Character walking through misty forest",
            has_named_characters=True,
            requires_lip_sync=False,
            has_precise_interaction=False,
            environment_focus=True,
            target_duration_sec=3.0
        )
    ]

    sample_script = "In the heart of the ancient city, mysteries lay dormant waiting to be discovered."
    plan = pipeline.plan_production("Pilot Episode", sample_script, sample_shots)

    print("=== Production Plan Generated ===")
    print(f"Title: {plan['title']}")
    print(f"Pacing: {plan['pacing_analysis']['actual_wpm']} WPM (Balanced: {plan['pacing_analysis']['is_balanced']})")
    print("Shot Routing:")
    for shot_id, route in plan["shot_routing"].items():
        print(f"  {shot_id} -> {route}")


if __name__ == "__main__":
    main()
