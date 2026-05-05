╔═══════════════════════════════════════╗
║      ARERPS DEVELOPMENT SYSTEMS       ║
║      Professional Code Solutions      ║
╚═══════════════════════════════════════╝

# 📚 Update Version Script - Beginner's Guide

> **Modified & Enhanced by:** *ARERPS* DEVELOPMENT @ARERPS  
> **Original Creator:** Roblox Corporation  
> **Purpose:** Automated version management for the Roblox Blender Plugin

---

## 🎯 What is This Script?

The `update_version.py` script is a **helper tool** that automatically updates your plugin's version number. Instead of manually editing files every time you release a new version, this script does it for you automatically!

Think of it like a **smart find-and-replace tool** that:
- Takes your new version number (like `v1.2.3`)
- Finds the old version in your code
- Replaces it with the new one
- Saves the file automatically

---

## 🚀 How to Use It

### Basic Usage

```bash
python update_version.py v1.2.3 /path/to/your/file.py
```

### Breaking It Down

| Part | Meaning | Example |
|------|---------|---------|
| `python` | Tells your computer to run Python | Always the same |
| `update_version.py` | The script name | File in `.github/scripts/` |
| `v1.2.3` | Your new version number | Use format: `vX.X.X` |
| `/path/to/file.py` | File to update | Path to your Python file |

### Example in Action

```bash
python .github/scripts/update_version.py v2.5.1 src/__init__.py
```

✓ **Output:** `Successfully updated version to v2.5.1`

---

## 🔧 What Was Improved?

### Original Issues ❌
- No error checking - script would silently fail
- No way to know if update actually worked
- Crashes with unclear error messages
- Hard to understand what went wrong
- No validation of version format

### ARERPS Enhancements ✅

#### 1. **Error Handling**
- Validates version format before running
- Confirms file exists
- Checks if the pattern was actually found and replaced
- Clear error messages telling you what went wrong

#### 2. **Better Code Organization**
- Wrapped logic in a reusable function
- Added type hints (tells you what data types are expected)
- Added comprehensive documentation

#### 3. **User-Friendly Messages**
- Shows success with checkmark: `✓ Successfully updated version to v1.2.3`
- Shows errors with cross: `✗ Error: Invalid version format`
- Provides usage instructions if run incorrectly

#### 4. **Modern Python Standards**
- Uses `pathlib.Path` (cleaner file handling)
- Proper exit codes (0 = success, 1 = failure)
- Errors go to stderr (standard error output)

---

## 📋 Requirements

### What You Need
- **Python 3.6 or higher** installed on your computer
- A file to update with a version line in this format:

```python
"version": (1, 2, 3),  # Gets updated by Github Actions. See README for info
```

### Checking Your Python Version

```bash
python --version
```

Should show something like: `Python 3.9.0` or higher ✓

---

## ⚠️ Common Issues & Solutions

### Issue: "Invalid version format"
```
Error: Invalid version format: 1.2.3. Expected 'vX.X.X'
```
**Solution:** Add the `v` prefix. Use `v1.2.3` not `1.2.3`

### Issue: "File not found"
```
Error: File not found: /path/to/file.py
```
**Solution:** Check that the file path is correct. Use full path or relative path from where you run the command.

### Issue: "Version pattern not found"
```
Error: Version pattern not found in __init__.py
```
**Solution:** Make sure your file has the exact version line:
```python
"version": (X, X, X),  # Gets updated by Github Actions. See README for info
```

---

## 🔄 How It's Used in GitHub Actions

This script runs **automatically** when you create a release. You don't need to run it manually!

**What happens:**
1. You create a release with tag `v2.0.0`
2. GitHub Actions automatically triggers
3. The script runs: `python update_version.py v2.0.0 src/__init__.py`
4. Your version is updated
5. Changes are committed back to your repository

---

## 📝 The Version Format

### Valid Formats ✓
- `v0.0.1` (small version)
- `v1.0.0` (major version)
- `v10.25.99` (large numbers)

### Invalid Formats ❌
- `1.0.0` (missing `v`)
- `v1.0` (missing third number)
- `v1.0.0.0` (too many numbers)
- `version-1.0.0` (wrong format)

---

## 🎓 For Developers

### Understanding the Code

**Version Pattern Regex:**
```python
r"v(\d+)\.(\d+)\.(\d+)"
```

Translation:
- `v` = literal letter "v"
- `(\d+)` = capture one or more digits (major version)
- `\.` = literal dot (escaped)
- `(\d+)` = capture digits (minor version)
- `\.` = literal dot
- `(\d+)` = capture digits (patch version)

**Replacement Pattern:**
```python
r'"version": (\1, \2, \3),'
```

Translation:
- Takes captured groups `\1`, `\2`, `\3`
- Formats them as Python tuple: `(major, minor, patch)`

---

## 🏆 Key Takeaways

| Feature | Benefit |
|---------|---------|
| **Automatic Updates** | No manual editing needed |
| **Error Checking** | Catches mistakes before they happen |
| **Clear Messages** | Tells you exactly what went wrong |
| **GitHub Integration** | Works seamlessly in CI/CD pipelines |
| **Reliable** | Ensures version consistency |

---

## 📞 Need Help?

If something doesn't work:
1. Read the error message carefully
2. Check the table above for your issue
3. Verify file paths are correct
4. Make sure version format is `vX.X.X`
5. Confirm file contains the required version line

---

## 📄 License

Original: © 2023 Roblox Corporation (MIT License)  
Modifications: © 2026 ARERPS Development (MIT License)

---

**Last Updated:** May 5, 2026  
**Enhanced by:** ARERPS Development Systems  
**Status:** ✓ Production Ready

╔═══════════════════════════════════════╗
║      ARERPS DEVELOPMENT SYSTEMS       ║
║      Making Code Better, Every Day    ║
╚═══════════════════════════════════════╝
