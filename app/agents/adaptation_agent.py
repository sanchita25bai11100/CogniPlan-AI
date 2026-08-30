"""
Schedule Adaptation Agent
=========================

Dynamically modifies future learning sessions based on
student performance and retention risk.

This creates CogniPlan's continuous feedback loop:

PLAN → STUDY → EVALUATE → ADAPT → REPLAN
"""


class AdaptationAgent:
    """
    Adapts future study sessions using learning signals.
    """

    def adapt(
        self,
        accuracy: float,
        retention_risk: float,
        current_duration: int,
    ) -> dict:
        """
        Determine how the next study session should change.
        """

        # Keep incoming values within sensible ranges.
        accuracy = max(0.0, min(1.0, accuracy))
        retention_risk = max(
            0.0,
            min(1.0, retention_risk),
        )

        # Case 1:
        # Very poor performance means the learner needs
        # focused revision before progressing.
        if accuracy < 0.50:

            return {
                "action": "increase_revision",
                "next_duration": min(
                    current_duration + 15,
                    90,
                ),
                "strategy": "focused_revision",
                "reason": (
                    "Low accuracy detected. "
                    "Additional revision is recommended."
                ),
            }

        # Case 2:
        # Moderate performance means more active practice.
        if accuracy < 0.75:

            return {
                "action": "increase_practice",
                "next_duration": min(
                    current_duration + 10,
                    75,
                ),
                "strategy": "active_recall",
                "reason": (
                    "Moderate accuracy detected. "
                    "More active practice is recommended."
                ),
            }

        # Case 3:
        # Good performance but high retention risk means
        # the learner should revisit the material later.
        if retention_risk > 0.60:

            return {
                "action": "schedule_review",
                "next_duration": current_duration,
                "strategy": "spaced_repetition",
                "reason": (
                    "Knowledge appears strong, but "
                    "retention risk is elevated."
                ),
            }

        # Case 4:
        # Strong performance and low retention risk means
        # the learner can progress.
        return {
            "action": "advance",
            "next_duration": max(
                current_duration - 5,
                20,
            ),
            "strategy": "progressive_learning",
            "reason": (
                "Strong performance detected. "
                "The learner is ready to progress."
            ),
        }
