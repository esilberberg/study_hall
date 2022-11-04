#!/usr/bin/env python3
"""
Author : esilberberg
Contact: ericsilberberg.com
Date   : 2022-11-04
Purpose: Rename Study Hall NFT files
"""
import argparse
import os
import random
import pandas as pd

# --------------------------------------------------

def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Rename Study Hall NFT files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
   
    parser.add_argument('directory',
                        metavar='directory',
                        help='Path to Study Hall photos directory.')
    
    return parser.parse_args()

# --------------------------------------------------

def main():
    """Make a jazz noise here"""
    args = get_args()
    path = args.directory
    
    if os.path.isdir(path):
        file_names = os.listdir(path)
        first_selection_files = file_names[0:3]
        second_selection_files = file_names[3:]

        random.shuffle(first_selection_files)
        random.shuffle(second_selection_files)
        randomized_files = first_selection_files + second_selection_files

        new_names = []
        for n in range(1,9):
            count = '{:d}'.format(n).zfill(3)
            new_name = f'Study_Hall_{count}'
            new_names.append(new_name)

        extensions = []
        for file in randomized_files:
            basename = os.path.basename(file)
            ext = os.path.splitext(basename)[1]
            extensions.append(ext)

        data = {'Old_Name': randomized_files,
                'Extension': extensions,
                'New_Name': new_names}

        df = pd.DataFrame(data)
        df['New_Name'] = (df['New_Name'] + df['Extension'])

        names_dict = dict(zip(df['New_Name'], df['Old_Name']))

        for new_name, old_name in names_dict.items():
            os.rename(os.path.join(path, old_name), os.path.join(path, new_name))

# --------------------------------------------------

if __name__ == '__main__':
    main()