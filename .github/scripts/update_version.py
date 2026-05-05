╔════════════════════════════════════════════════════════════════════╗
║                  ARERPS DEVELOPMENT SYSTEMS                         ║
║              Professional Code Enhancement Solutions               ║
╚════════════════════════════════════════════════════════════════════╝

# Copyright © 2023 Roblox Corporation
# Modified & Enhanced by: *ARERPS* DEVELOPMENT @ARERPS (2026)

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


"""
Used in Github Actions workflow to automatically update the version number of the plugin to match the tag version.

This enhanced version includes:
  ✓ Comprehensive error handling
  ✓ Input validation
  ✓ Type hints for better code clarity
  ✓ User-friendly error messages
  ✓ Exit code handling for CI/CD integration
"""

import re
import sys
from pathlib import Path


def update_version(new_version: str, file_path: str) -> None:
    """
    Update the version string in a Python file.
    
    Replaces the version tuple in the target file with the new version
    extracted from the provided version tag.
    
    Args:
        new_version: Version tag in format 'vX.X.X' (e.g., 'v1.2.3')
        file_path: Path to the file to update (absolute or relative path)
        
    Raises:
        ValueError: If version format is invalid or pattern not found
        FileNotFoundError: If the target file doesn't exist
        
    Example:
        >>> update_version('v1.2.3', 'src/__init__.py')
        # Successfully updates version to (1, 2, 3)
    """
    # ✓ Validate version format
    version_match = re.match(r"v(\d+)\.(\d+)\.(\d+)", new_version)
    if not version_match:
        raise ValueError(
            f"✗ Invalid version format: {new_version}. Expected 'vX.X.X' (e.g., v1.2.3)"
        )
    
    # ✓ Convert version tag to tuple format
    # Example: v1.2.3 -> "version": (1, 2, 3),
    new_version_line = re.sub(
        r"v(\d+)\.(\d+)\.(\d+)",
        r'"version": (\1, \2, \3),',
        new_version
    )
    
    # ✓ Define the pattern to find and replace
    version_line_pattern = (
        r'"version": \(\d+, \d+, \d+\),  # Gets updated by Github Actions. See README for info'
    )
    
    # ✓ Read file with error handling
    try:
        file_content = Path(file_path).read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(
            f"✗ File not found: {file_path}\n"
            f"  Please verify the file path is correct."
        )
    except Exception as e:
        raise RuntimeError(
            f"✗ Error reading file {file_path}: {str(e)}"
        )
    
    # ✓ Update version in content
    updated_content = re.sub(version_line_pattern, new_version_line, file_content, count=1)
    
    # ✓ Check if replacement was actually made
    if updated_content == file_content:
        raise ValueError(
            f"✗ Version pattern not found in {file_path}\n"
            f"  Expected pattern: 'version': (X, X, X),  # Gets updated by Github Actions. See README for info\n"
            f"  See UPDATE_VERSION_README.md for more information."
        )
    
    # ✓ Write updated file with error handling
    try:
        Path(file_path).write_text(updated_content, encoding="utf-8")
    except Exception as e:
        raise RuntimeError(
            f"✗ Error writing to file {file_path}: {str(e)}"
        )


def main() -> int:
    """
    Main entry point for the script.
    
    Returns:
        0 on success, 1 on error
    """
    # ✓ Validate command line arguments
    if len(sys.argv) != 3:
        print("╔════════════════════════════════════════════════════════════╗")
        print("║           Version Update Script - ARERPS Enhanced           ║")
        print("╚════════════════════════════════════════════════════════════╝")
        print()
        print("Usage: update_version.py <version> <file_path>")
        print()
        print("Arguments:")
        print("  <version>    Version tag in format 'vX.X.X' (e.g., v1.2.3)")
        print("  <file_path>  Path to the Python file to update")
        print()
        print("Examples:")
        print("  python update_version.py v1.2.3 src/__init__.py")
        print("  python update_version.py v2.0.0 /full/path/to/plugin.py")
        print()
        print("For detailed help, see: UPDATE_VERSION_README.md")
        print()
        return 1
    
    try:
        new_version = sys.argv[1]
        file_path = sys.argv[2]
        
        update_version(new_version, file_path)
        
        # ✓ Success message
        print(f"✓ Successfully updated version to {new_version}")
        return 0
        
    except (ValueError, FileNotFoundError, RuntimeError) as e:
        print(str(e), file=sys.stderr)
        return 1
    except Exception as e:
        print(f"✗ Unexpected error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
