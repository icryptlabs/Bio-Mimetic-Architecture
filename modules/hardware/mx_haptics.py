import logitech_actions_sdk

# SENSORY PROPRIOCEPTION: Haptic Feedback
def signal_fixation_event(is_successful):
    # Uses MX Master 4 customizable haptics for tactile precision [Source 868].
    # Anchors the human user to the agent's 'Metabolic State' [Source 916].
    if is_successful:
        # Subtle vibration for 'Epigenetic Fixation' (ledger write) successful.
        logitech_actions_sdk.trigger_haptic('MX_MASTER_4', pattern='success_pulse')
    else:
        # Jolt for 'Validation Failure' or 'Pathogen Detected' [Source 868].
        logitech_actions_sdk.trigger_haptic('MX_MASTER_4', pattern='warning_jolt')
