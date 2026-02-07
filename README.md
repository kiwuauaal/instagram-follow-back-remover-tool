# Instagram Mutual-Follow Analyzer

A cross-platform tool (Windows/Termux) that analyzes your Instagram follow relationships to identify:
- Accounts you follow who don't follow you back ❌
- Accounts who follow you but you don't follow back ↩️
- Mutual followers ✅

## Features

- Works on Windows and Termux (Android)
- No external dependencies (uses only built-in Python libraries)
- Clean, readable output
- Option to save results to file
- Automatic file detection
- Detailed statistics

## How to Get Your Instagram Data

1. Open Instagram app
2. Go to **Settings** > **Security** > **Download Data**
3. Enter your email and password
4. Wait for email (usually takes a few hours)
5. Download and extract the ZIP file
6. Locate these files:
   - `followers.json` (or in `followers_and_following/followers.json`)
   - `following.json` (or in `followers_and_following/following.json`)

## Installation

### Windows

```cmd
# Run the setup script
setup_windows.bat

# Or manually:
python instagram_analyzer.py
```

### Termux (Android)

```bash
# Make setup script executable
chmod +x setup_termux.sh

# Run setup
./setup_termux.sh

# Or manually:
python3 instagram_analyzer.py
```

## Usage

### Basic Usage

```bash
# Interactive mode - will prompt for file paths
python instagram_analyzer.py

# Specify files directly
python instagram_analyzer.py -f followers.json -w following.json

# Auto-find files in common locations
python instagram_analyzer.py --auto-find

# Show detailed lists of all accounts
python instagram_analyzer.py --show-all

# Save results to file
python instagram_analyzer.py --save results.txt

# Combine options
python instagram_analyzer.py -f followers.json -w following.json --show-all --save results.txt
```

### Command Line Options

```
-h, --help          Show help message
-f, --followers     Path to followers JSON file
-w, --following     Path to following JSON file
-s, --save          Save results to file
--show-all          Show detailed lists of all accounts
--auto-find         Automatically search for Instagram files
```

## Example Output

```
============================================================
INSTAGRAM MUTUAL-FOLLOW ANALYSIS RESULTS
============================================================

📊 STATISTICS:
  Total Followers: 1,250
  Total Following: 800
  Mutual Followers: 750
  Following who don't follow back: 50
  Followers you don't follow back: 500

❌ FOLLOWING WHO DON'T FOLLOW YOU BACK (50 accounts):
--------------------------------------------------
    1. @example_user1
    2. @example_user2
    3. @example_user3
    ...

↩️  FOLLOWERS YOU DON'T FOLLOW BACK (500 accounts):
--------------------------------------------------
    1. @another_user1
    2. @another_user2
    ...
```

## How It Works

1. Loads your followers and following data from Instagram's JSON export
2. Compares the two lists to find:
   - Mutual followers (intersection)
   - People you follow who don't follow you back (following - followers)
   - People who follow you but you don't follow back (followers - following)
3. Displays statistics and optionally detailed lists
4. Can save results to a text file for later reference

## Requirements

- Python 3.6 or higher
- Instagram data export (JSON files)

## Troubleshooting

**File not found error:**
- Make sure you've extracted the Instagram ZIP file
- Check the file paths are correct
- Use absolute paths if relative paths don't work

**Invalid JSON error:**
- Ensure you're using the original JSON files from Instagram
- Don't modify the files before processing

**No data loaded:**
- Check that your JSON files contain the expected structure
- Recent Instagram exports may have different formats

## License

MIT License - Feel free to use and modify!

## Contributing

Pull requests are welcome! For major changes, please open an issue first.