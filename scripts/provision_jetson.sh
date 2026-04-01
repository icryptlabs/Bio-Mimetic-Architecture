#!/bin/bash
# SFA-One Jetson Provisioning [Source 876, 1069]

# 1. Install uv for fast, sovereign dependency management [Source 1068]
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Deploy local models for the Reflex Arc
uv pip install gemma-3n-sdk whisperspeech # [Source 651, 939]

# 3. Configure local SDK targets
# Note: sdkmanager must be run from a host to flash or install target components [Source 880, 884]
sdkmanager --cli install --product Jetson --target OS --version 6.2
