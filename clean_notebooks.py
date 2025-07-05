#!/usr/bin/env python3
import json
import os
import glob

def clean_notebook(notebook_path):
    """Remove output from a Jupyter notebook while keeping code cells."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Clean each cell
        for cell in notebook['cells']:
            if cell['cell_type'] == 'code':
                # Remove output and execution count
                if 'outputs' in cell:
                    cell['outputs'] = []
                if 'execution_count' in cell:
                    cell['execution_count'] = None
                if 'metadata' in cell:
                    # Keep only essential metadata
                    if 'execution' in cell['metadata']:
                        cell['metadata']['execution'] = {}
        
        # Write the cleaned notebook back
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)
        
        print(f"Cleaned: {notebook_path}")
        return True
    except Exception as e:
        print(f"Error processing {notebook_path}: {e}")
        return False

def main():
    """Process all .ipynb files in the project."""
    # Find all notebook files
    notebook_files = []
    
    # Search in current directory and subdirectories
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.ipynb'):
                notebook_files.append(os.path.join(root, file))
    
    print(f"Found {len(notebook_files)} notebook files:")
    for file in notebook_files:
        print(f"  - {file}")
    
    print("\nCleaning notebooks...")
    success_count = 0
    for notebook_file in notebook_files:
        if clean_notebook(notebook_file):
            success_count += 1
    
    print(f"\nCompleted! Successfully cleaned {success_count}/{len(notebook_files)} notebooks.")

if __name__ == "__main__":
    main()