import sys

# Step 2: Automated Self-Validation Hook [Source 315, 332]
def validate_mandate_integrity(file_path):
    # Runs on 'stop hook' to ensure mandate contains mandatory cryptographic signatures
    with open(file_path, 'r') as f:
        content = f.read()
        if 'merchant_signature' not in content:
            print(f'VALIDATION FAILURE: {file_path} lacks signature [Source 316]')
            sys.exit(1)
    print('VALIDATION SUCCESS: Mandate is sterile and ready for fixation.')
