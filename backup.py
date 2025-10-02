import os
import sys
import shutil
import time

def backup_files(source_dir, dest_dir):
    # Check if source and destination directories exist
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    if not os.path.exists(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return

    for filename in os.listdir(source_dir):
        src_file = os.path.join(source_dir, filename)
        if os.path.isfile(src_file):
            dst_file = os.path.join(dest_dir, filename)
            if os.path.exists(dst_file):
                base, ext = os.path.splitext(filename)
                timestamp = time.strftime("%Y%m%d%H%M%S")
                new_filename = f"{base}_{timestamp}{ext}"
                dst_file = os.path.join(dest_dir, new_filename)
            try:
                shutil.copy2(src_file, dst_file)
                print(f"Backed up: {src_file} -> {dst_file}")
            except Exception as e:
                print(f"Error copying '{filename}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        source = sys.argv[1]
        destination = sys.argv[2]
        backup_files(source, destination)
