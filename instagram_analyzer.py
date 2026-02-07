#!/usr/bin/env python3
"""
Instagram Mutual-Follow Analyzer
Analyzes Instagram follow relationships to identify accounts that don't follow you back.
Works on Windows and Termux (Android).
"""

import json
import os
import sys
import time
from typing import Dict, List, Set, Tuple
import argparse

class InstagramAnalyzer:
    def __init__(self):
        self.followers = set()
        self.following = set()
        self.mutual_followers = set()
        self.not_following_back = set()  # People you follow who don't follow you
        self.you_dont_follow_back = set()  # People who follow you but you don't follow back
        
    def load_data_from_files(self, followers_file: str, following_file: str) -> bool:
        """
        Load Instagram data from JSON files downloaded from Instagram.
        
        Args:
            followers_file: Path to followers JSON file
            following_file: Path to following JSON file
            
        Returns:
            bool: True if data loaded successfully
        """
        try:
            # Load followers data
            print(f"Loading followers data from: {followers_file}")
            with open(followers_file, 'r', encoding='utf-8') as f:
                followers_data = json.load(f)
            
            # Extract follower usernames - handle various Instagram JSON formats
            if isinstance(followers_data, list):
                for item in followers_data:
                    # Format 1: {'string_list_data': [{'value': 'username'}]}
                    if 'string_list_data' in item and item['string_list_data']:
                        username = item['string_list_data'][0].get('value', '')
                        if username:
                            self.followers.add(username.lower())
                    # Format 2: {'value': 'username'}
                    elif 'value' in item:
                        self.followers.add(item['value'].lower())
                    # Format 3: Direct string in list
                    elif isinstance(item, str):
                        self.followers.add(item.lower())
            # Handle direct dictionary format
            elif isinstance(followers_data, dict):
                # Look for keys that might contain follower data
                for key in followers_data:
                    if 'follower' in key.lower() and isinstance(followers_data[key], list):
                        for item in followers_data[key]:
                            if isinstance(item, dict) and 'value' in item:
                                self.followers.add(item['value'].lower())
                            elif isinstance(item, str):
                                self.followers.add(item.lower())
                            # Handle string_list_data format within the list items
                            elif isinstance(item, dict) and 'string_list_data' in item and item['string_list_data']:
                                username = item['string_list_data'][0].get('value', '')
                                if username:
                                    self.followers.add(username.lower())
            
            print(f"Loaded {len(self.followers)} followers")
            
            # Load following data
            print(f"Loading following data from: {following_file}")
            with open(following_file, 'r', encoding='utf-8') as f:
                following_data = json.load(f)
            
            # Extract following usernames - handle various Instagram JSON formats
            if isinstance(following_data, list):
                for item in following_data:
                    # Format 1: {'string_list_data': [{'value': 'username'}]}
                    if 'string_list_data' in item and item['string_list_data']:
                        username = item['string_list_data'][0].get('value', '')
                        if username:
                            self.following.add(username.lower())
                    # Format 2: {'value': 'username'}
                    elif 'value' in item:
                        self.following.add(item['value'].lower())
                    # Format 3: Direct string in list
                    elif isinstance(item, str):
                        self.following.add(item.lower())
            # Handle direct dictionary format
            elif isinstance(following_data, dict):
                # Look for keys that might contain following data
                for key in following_data:
                    if 'following' in key.lower() and isinstance(following_data[key], list):
                        for item in following_data[key]:
                            if isinstance(item, dict) and 'value' in item:
                                self.following.add(item['value'].lower())
                            elif isinstance(item, str):
                                self.following.add(item.lower())
                            # Handle string_list_data format within the list items
                            elif isinstance(item, dict) and 'string_list_data' in item and item['string_list_data']:
                                username = item['string_list_data'][0].get('value', '')
                                if username:
                                    self.following.add(username.lower())
            
            print(f"Loaded {len(self.following)} following")
            
            return True
            
        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
            return False
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format - {e}")
            return False
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def analyze_relationships(self):
        """Analyze the follow relationships and populate result sets."""
        print("\nAnalyzing relationships...")
        
        # Find mutual followers (people who follow you AND you follow them)
        self.mutual_followers = self.followers.intersection(self.following)
        
        # Find people you follow who don't follow you back
        self.not_following_back = self.following.difference(self.followers)
        
        # Find people who follow you but you don't follow back
        self.you_dont_follow_back = self.followers.difference(self.following)
        
        print("Analysis complete!")
    
    def display_results(self, show_all: bool = False):
        """Display the analysis results."""
        print("\n" + "="*60)
        print("INSTAGRAM MUTUAL-FOLLOW ANALYSIS RESULTS")
        print("="*60)
        
        print(f"\n📊 STATISTICS:")
        print(f"  Total Followers: {len(self.followers):,}")
        print(f"  Total Following: {len(self.following):,}")
        print(f"  Mutual Followers: {len(self.mutual_followers):,}")
        print(f"  Following who don't follow back: {len(self.not_following_back):,}")
        print(f"  Followers you don't follow back: {len(self.you_dont_follow_back):,}")
        
        if show_all:
            self._display_detailed_lists()
    
    def _display_detailed_lists(self):
        """Display detailed lists of accounts."""
        if self.not_following_back:
            print(f"\n❌ FOLLOWING WHO DON'T FOLLOW YOU BACK ({len(self.not_following_back)} accounts):")
            print("-" * 50)
            for i, username in enumerate(sorted(self.not_following_back), 1):
                print(f"  {i:3d}. @{username}")
        
        if self.you_dont_follow_back:
            print(f"\n↩️  FOLLOWERS YOU DON'T FOLLOW BACK ({len(self.you_dont_follow_back)} accounts):")
            print("-" * 50)
            for i, username in enumerate(sorted(self.you_dont_follow_back), 1):
                print(f"  {i:3d}. @{username}")
        
        if len(self.mutual_followers) > 0:
            show_mutual = input(f"\nShow mutual followers list ({len(self.mutual_followers)} accounts)? (y/N): ").strip().lower()
            if show_mutual == 'y':
                print(f"\n✅ MUTUAL FOLLOWERS ({len(self.mutual_followers)} accounts):")
                print("-" * 40)
                for i, username in enumerate(sorted(self.mutual_followers), 1):
                    print(f"  {i:3d}. @{username}")

    def save_results(self, output_file: str = None):
        """Save results to a text file."""
        if not output_file:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_file = f"instagram_analysis_{timestamp}.txt"
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("INSTAGRAM MUTUAL-FOLLOW ANALYSIS RESULTS\n")
                f.write("="*50 + "\n\n")
                
                f.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Followers: {len(self.followers):,}\n")
                f.write(f"Total Following: {len(self.following):,}\n")
                f.write(f"Mutual Followers: {len(self.mutual_followers):,}\n")
                f.write(f"Following who don't follow back: {len(self.not_following_back):,}\n")
                f.write(f"Followers you don't follow back: {len(self.you_dont_follow_back):,}\n\n")
                
                if self.not_following_back:
                    f.write(f"FOLLOWING WHO DON'T FOLLOW YOU BACK ({len(self.not_following_back)} accounts):\n")
                    f.write("-" * 50 + "\n")
                    for username in sorted(self.not_following_back):
                        f.write(f"@{username}\n")
                    f.write("\n")
                
                if self.you_dont_follow_back:
                    f.write(f"FOLLOWERS YOU DON'T FOLLOW BACK ({len(self.you_dont_follow_back)} accounts):\n")
                    f.write("-" * 50 + "\n")
                    for username in sorted(self.you_dont_follow_back):
                        f.write(f"@{username}\n")
                    f.write("\n")
                
                if self.mutual_followers:
                    f.write(f"MUTUAL FOLLOWERS ({len(self.mutual_followers)} accounts):\n")
                    f.write("-" * 40 + "\n")
                    for username in sorted(self.mutual_followers):
                        f.write(f"@{username}\n")
            
            print(f"\nResults saved to: {output_file}")
            return True
            
        except Exception as e:
            print(f"Error saving results: {e}")
            return False

def get_instagram_files():
    """Helper function to find Instagram JSON files in common locations."""
    common_paths = [
        ".",  # Current directory
        "./followers_and_following",
        "../followers_and_following",
        "~/Downloads/followers_and_following",
        "/sdcard/Download/followers_and_following"  # Termux path
    ]
    
    followers_file = None
    following_file = None
    
    for path in common_paths:
        expanded_path = os.path.expanduser(path)
        if os.path.exists(expanded_path):
            files = os.listdir(expanded_path)
            for file in files:
                if 'follower' in file.lower() and file.endswith('.json'):
                    followers_file = os.path.join(expanded_path, file)
                elif 'following' in file.lower() and file.endswith('.json'):
                    following_file = os.path.join(expanded_path, file)
    
    return followers_file, following_file

def main():
    parser = argparse.ArgumentParser(
        description="Instagram Mutual-Follow Analyzer - Find accounts that don't follow you back",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python instagram_analyzer.py
  python instagram_analyzer.py -f followers.json -w following.json
  python instagram_analyzer.py --show-all --save results.txt
        """
    )
    
    parser.add_argument('-f', '--followers', help='Path to followers JSON file')
    parser.add_argument('-w', '--following', help='Path to following JSON file')
    parser.add_argument('-s', '--save', help='Save results to file')
    parser.add_argument('--show-all', action='store_true', help='Show detailed lists of all accounts')
    parser.add_argument('--auto-find', action='store_true', help='Automatically search for Instagram files')
    
    args = parser.parse_args()
    
    print("Instagram Mutual-Follow Analyzer")
    print("="*40)
    
    # Initialize analyzer
    analyzer = InstagramAnalyzer()
    
    # Get file paths
    followers_file = args.followers
    following_file = args.following
    
    if not followers_file or not following_file:
        if args.auto_find:
            print("Searching for Instagram files...")
            followers_file, following_file = get_instagram_files()
        else:
            # Interactive mode
            print("\nHow to get your Instagram data:")
            print("1. Go to Instagram Settings > Security > Download Data")
            print("2. Request your data (takes some hours to arrive via email)")
            print("3. Extract the ZIP file and locate:")
            print("   - followers.json (or followers_and_following/followers.json)")
            print("   - following.json (or followers_and_following/following.json)")
            print()
            
            followers_file = input("Enter path to followers JSON file: ").strip()
            following_file = input("Enter path to following JSON file: ").strip()
    
    if not followers_file or not following_file:
        print("Error: Both followers and following files are required!")
        sys.exit(1)
    
    # Load data
    if not analyzer.load_data_from_files(followers_file, following_file):
        sys.exit(1)
    
    # Analyze relationships
    analyzer.analyze_relationships()
    
    # Display results
    analyzer.display_results(show_all=args.show_all)
    
    # Save results if requested
    if args.save:
        analyzer.save_results(args.save)

if __name__ == "__main__":
    main()