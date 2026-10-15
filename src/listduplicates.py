#!/usr/bin/env python3
import os
import sys
import hashlib
import tempfile

def get_sha256(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except (OSError, IOError):
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python listduplicates.py <directory_path>")
        sys.exit(1)

    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"Error: {root_dir} is not a valid directory.")
        sys.exit(1)

    # Use a temporary file to store the mapping of files and their hashes
    # We will store them as "hash path" per line
    with tempfile.NamedTemporaryFile(mode='w+', delete=True) as temp_store:
        for root, _, files in os.walk(root_dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_hash = get_sha256(file_path)
                if file_hash:
                    temp_store.write(f"{file_hash} {file_path}\n")
        
        temp_store.seek(0)
        
        hash_map = {}
        for line in temp_store:
            parts = line.strip().split(' ', 1)
            if len(parts) == 2:
                h, path = parts
                if h not in hash_map:
                    hash_map[h] = []
                hash_map[h].append(path)

    duplicate_count = 0
    for h, paths in hash_map.items():
        if len(paths) > 1:
            first_file = paths[0]
            for other_file in paths[1:]:
                print(f"{first_file} and {other_file} are duplicates")
                duplicate_count += 1

    print(f"Total duplicate files found: {duplicate_count}")

if __name__ == "__main__":
    main()

