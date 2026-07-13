#!/bin/bash

# Run the profile generator script
python generate_profile.py

# Check if profile.svg was created successfully
if [ -f "profile.svg" ]; then
    echo "✅ Success! profile.svg has been created."
else
    echo "❌ Error: profile.svg was not created."
    exit 1
fi
