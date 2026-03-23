import logitech_actions_sdk

# THE 'METABOLIC THROTTLE' & 'STATUS PROPRIOCEPTION'
def sync_hardware_state(dial_value, agent_phase):
    # 1. MX Dial -> Velocity Controller [2, 7].
    # Turning Right increases transaction frequency (ATP burn rate) [1].
    velocity_delay = max(0.1, 2.0 - dial_value) 
    
    # 2. Actions Ring -> Digital Status Overlay [3, 8].
    # Updates the radial menu slices to reflect the agent's current phenotype.
    logitech_actions_sdk.update_actions_ring(
        slices=[
            {'id': 'status', 'label': f'Phase: {agent_phase}', 'icon': 'dna'},
            {'id': 'velocity', 'label': f'Rate: {1/velocity_delay:.1f} tx/s', 'icon': 'bolt'}
        ]
    )
    return velocity_delay
