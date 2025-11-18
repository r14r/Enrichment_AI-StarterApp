"""Utility functions for the Streamlit app."""

import os
import re
from pathlib import Path
from collections import defaultdict
import streamlit as st


def build_navigation():
    """
    Scan all files in the 'pages' directory and group them by topic.
    
    This function reads all Python files from the pages directory,
    extracts topics from filenames (based on emoji and topic name),
    and returns a navigation structure suitable for st.navigation.
    
    File naming convention: {number}_{emoji}_{Topic}_{Details}.py
    Example: 100_🐍_Python_Basics_Data_Types.py
    
    Returns:
        dict: A dictionary where keys are section headers (topic names)
              and values are lists of st.Page objects for that topic.
              Format: {"Topic Name": [st.Page(...), st.Page(...), ...]}
    """
    # Get the pages directory path
    pages_dir = Path("pages")
    
    if not pages_dir.exists():
        return {}
    
    # Pattern to match: number_emoji_Topic_Name_...
    # Group 1: number, Group 2: emoji, Group 3: topic word, Group 4: rest of filename
    pattern = r'^(\d+)_(.+?)_(.+?)(?:_(.+?))?\.py$'
    
    # Dictionary to store pages grouped by topic
    topics = defaultdict(list)
    
    # Get all Python files in pages directory (not in subdirectories)
    files = [f for f in os.listdir(pages_dir) if f.endswith('.py')]
    
    for filename in sorted(files):  # Sort to maintain consistent order
        match = re.match(pattern, filename)
        
        if match:
            number, emoji, topic, rest = match.groups()
            
            # Create a readable topic key
            # Format: "emoji Topic"
            # Example: "🐍 Python" or "📊 Streamlit"
            topic_key = f"{emoji} {topic.replace('_', ' ')}"
            
            # Create the page path
            page_path = pages_dir / filename
            
            # Create title from the filename (remove number and first parts)
            # Keep the details part if it exists
            # Prepend the page number to make titles unique
            if rest:
                # Remove .py extension if present in rest
                title_base = rest.replace('_', ' ').replace('.py', '')
                title = f"{number}. {title_base}"
            else:
                title_base = topic.replace('_', ' ')
                title = f"{number}. {title_base}"
            
            # Create a unique URL path using the entire filename (without extension)
            # Remove emojis from URL path as they might cause issues
            # This ensures no duplicate URL pathnames
            url_path = filename[:-3]  # Remove .py extension
            # Remove emoji from url_path (emojis can be multi-byte)
            url_path_clean = ''.join(c for c in url_path if ord(c) < 128 or c.isalnum() or c in '_-')
            if not url_path_clean:
                url_path_clean = f"page_{number}"
            
            # Add page to the appropriate topic group
            topics[topic_key].append(
                st.Page(
                    str(page_path),
                    title=title,
                    icon=emoji,
                    url_path=url_path_clean
                )
            )
    
    # Convert defaultdict to regular dict for cleaner output
    return dict(topics)
