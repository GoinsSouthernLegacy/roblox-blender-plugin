# Copyright © 2023 Roblox Corporation
# Modified by: *ARERPS* DEVELOPMENT @ARERPS

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# SPDX-License-Identifier: MIT

# ╔═══════════════════════════════════════╗
# ║      ARERPS DEVELOPMENT SYSTEMS       ║
# ║      Version Update Automation        ║
# ╚═══════════════════════════════════════╝

"""
Used in Github Actions workflow to automatically update the version number of the plugin to match the tag version.

This script takes a version tag (e.g., v1.2.3) and updates the version tuple in a Python file.
It includes robust error handling and validation to ensure reliable automation.
"""

import re
import sys
from pathlib import Path


def update_version(new_version: str, file_path: str) -> None:
    """
    Update the version string in a Python file.
    
    Args:
        new_version: Version tag in format 'vX.X.X' (e.g., 'v1.2.3')
        file_path: Path to the file to update
        
    Raises:
        ValueError: If version format is invalid or pattern not found
        FileNotFoundError: If file doesn't exist
    """
    # Validate version format
    version_match = re.match(r"v(\d+)\.(\d+)\.(\d+)", new_version)
    if not version_match:
        raise ValueError(f"Invalid version format: {new_version}. Expected 'vX.X.X'")
    
    # Convert version tag to tuple format
    new_version_line = re.sub(
        r"v(\d+)\.(\d+)\.(\d+)",
        r'"version": (\1, \2, \3),',
        new_version
    )
    
    version_line_pattern = (
        r'"version": \(\d+, \d+, \d+\),  # Gets updated by Github Actions. See README for info'
    )
    
    # Read file
    try:
        file_content = Path(file_path).read_text()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Update version
    updated_content = re.sub(version_line_pattern, new_version_line, file_content, count=1)
    
    # Check if replacement was made
    if updated_content == file_content:
        raise ValueError(f"Version pattern not found in {file_path}")
    
    # Write file
    Path(file_path).write_text(updated_content)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: update_version.py <version> <file_path>")
        print("Example: update_version.py v1.2.3 __init__.py")
        sys.exit(1)
    
    try:
        update_version(sys.argv[1], sys.argv[2])
        print(f"✓ Successfully updated version to {sys.argv[1]}")
    except (ValueError, FileNotFoundError) as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)
