# Install uv for sovereign dependency management [Source 968]
curl -LsSf https://astral.sh/uv/install.sh | sh

# Deploy local models for Mitochondrial Sovereignty
uv pip install whisperspeech gemma-3n-sdk

# Configure NVIDIA SDK for Jetson endpoints [Source 874]
sdkmanager --cli install --product Jetson --target OS
