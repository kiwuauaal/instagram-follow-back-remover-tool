# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-07

### Added
- Initial release of Instagram Mutual-Follow Analyzer
- Cross-platform support (Windows/Termux/Unix)
- Analysis of followers vs following relationships
- Identification of:
  - Accounts you follow who don't follow you back
  - Accounts who follow you but you don't follow back
  - Mutual followers
- Command-line interface with multiple options
- Automatic file detection feature
- Save results to text file capability
- Sample data for testing
- Setup scripts for Windows and Termux
- Comprehensive documentation
- Git repository structure with proper .gitignore
- MIT License

### Changed
- Improved JSON parsing to handle various Instagram export formats
- Enhanced error handling and user feedback

### Fixed
- JSON parsing issues with different Instagram data formats
- File path handling across platforms

## [Unreleased]

### Planned
- Add support for more Instagram data export formats
- Implement web interface option
- Add statistical analysis features
- Include visualization options
- Add batch processing capabilities