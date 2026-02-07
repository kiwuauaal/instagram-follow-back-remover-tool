#!/usr/bin/env python3
"""
Installation Verification Script
Checks if all required components are properly installed and working.
"""

import sys
import os
import json

def check_python_version():
    """Check if Python version is compatible."""
    print("🔍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 6:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Upgrade needed (3.6+ required)")
        return False

def check_required_files():
    """Check if all required files exist."""
    print("\n🔍 Checking required files...")
    required_files = [
        'instagram_analyzer.py',
        'README.md',
        'LICENSE',
        'requirements.txt',
        '.gitignore'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - Missing")
            missing_files.append(file)
    
    return len(missing_files) == 0

def check_sample_data():
    """Check if sample data files exist and are valid."""
    print("\n🔍 Checking sample data...")
    sample_files = ['sample_followers.json', 'sample_following.json']
    
    for file in sample_files:
        if os.path.exists(file):
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                print(f"✅ {file} - Valid JSON")
            except json.JSONDecodeError:
                print(f"❌ {file} - Invalid JSON")
                return False
            except Exception as e:
                print(f"❌ {file} - Error: {e}")
                return False
        else:
            print(f"⚠️  {file} - Not found (optional for testing)")
    
    return True

def test_imports():
    """Test if all required imports work."""
    print("\n🔍 Testing imports...")
    try:
        import json
        print("✅ json module")
        
        import os
        print("✅ os module")
        
        import sys
        print("✅ sys module")
        
        import time
        print("✅ time module")
        
        import argparse
        print("✅ argparse module")
        
        from typing import Dict, List, Set, Tuple
        print("✅ typing module")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def run_sample_test():
    """Run a quick test with sample data."""
    print("\n🔍 Running sample test...")
    try:
        # Import the analyzer
        sys.path.insert(0, '.')
        from instagram_analyzer import InstagramAnalyzer
        
        # Create analyzer instance
        analyzer = InstagramAnalyzer()
        
        # Load sample data
        if not analyzer.load_data_from_files('sample_followers.json', 'sample_following.json'):
            print("❌ Failed to load sample data")
            return False
        
        # Analyze relationships
        analyzer.analyze_relationships()
        
        # Check results
        if len(analyzer.followers) > 0 and len(analyzer.following) > 0:
            print("✅ Sample analysis completed successfully")
            print(f"   Followers: {len(analyzer.followers)}")
            print(f"   Following: {len(analyzer.following)}")
            print(f"   Not following back: {len(analyzer.not_following_back)}")
            return True
        else:
            print("❌ No data loaded from sample files")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    print("🔧 Instagram Analyzer - Installation Verification")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python_version),
        ("Required Files", check_required_files),
        ("Sample Data", check_sample_data),
        ("Module Imports", test_imports),
        ("Functionality Test", run_sample_test)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ {name} check failed with exception: {e}")
            results.append((name, False))
    
    print("\n" + "=" * 50)
    print("📋 VERIFICATION SUMMARY")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {name}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n🎉 Installation verified successfully!")
        print("You're ready to use the Instagram Analyzer!")
        return 0
    else:
        print("\n⚠️  Some checks failed. Please review the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())