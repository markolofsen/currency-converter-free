#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Package name for logging purposes
PACKAGE_NAME="currency_converter_free"

echo "============================================"
echo "Testing, Building, and Publishing $PACKAGE_NAME"
echo "============================================"

# Step 1: Run unit tests
echo "Running unit tests..."
python -m unittest discover tests

# Step 2: Clean up old build artifacts
echo "Cleaning up old build artifacts..."
rm -rf dist build *.egg-info

# Step 3: Build the package
echo "Building the package..."
python -m build

# Step 4: Upload to TestPyPI
echo "Uploading to TestPyPI..."
twine upload --repository testpypi dist/*
echo "Upload to TestPyPI successful."

# Step 5: Prompt user for uploading to PyPI
echo "Do you want to upload to PyPI? (yes/no)"
read -r UPLOAD_TO_PYPI

if [[ "$UPLOAD_TO_PYPI" =~ ^[Yy][Ee][Ss]$ || "$UPLOAD_TO_PYPI" =~ ^[Yy]$ ]]; then
    echo "Uploading to PyPI..."
    twine upload --repository pypi dist/*
    echo "Upload to PyPI completed successfully."
else
    echo "Skipping upload to PyPI."
fi

# Step 6: Git commit and push
echo "Committing and pushing changes to Git..."
git add .
git commit -m "fix: Updated package $PACKAGE_NAME"
git push
echo "Changes have been committed and pushed to the remote repository."

echo "============================================"
echo "Process completed."
echo "============================================"
