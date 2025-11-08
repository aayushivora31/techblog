import os
import shutil
from pathlib import Path
from typing import Generator, TYPE_CHECKING, Any

if TYPE_CHECKING:
    from os import DirEntry

def fix_media_location() -> None:
    # Define paths
    current_media_dir = Path('../media')  # Where files are currently
    correct_media_dir = Path('media')     # Where they should be (relative to BASE_DIR)
    
    # Fix Pyright "Type of "absolute" is partially unknown" error
    # by explicitly converting to string
    current_absolute_path: str = str(current_media_dir.absolute())
    correct_absolute_path: str = str(correct_media_dir.absolute())
    
    print(f"Current media directory: {current_absolute_path}")
    print(f"Correct media directory: {correct_absolute_path}")
    
    # Check if current media directory exists and has content
    # Explicitly type the generator to help Pyright
    if current_media_dir.exists():
        # Type ignore for unknown generator type
        current_items: Generator['DirEntry[str]', None, None] = current_media_dir.iterdir()  # type: ignore
        if any(list(current_items)):
            print("Found images in current media directory")
                
            # Create the correct media directory if it doesn't exist
            correct_media_dir.mkdir(exist_ok=True)
                
            # Move all content from current to correct directory
            item: 'DirEntry[str]'
            # Type ignore for unknown iterdir return type
            for item in current_media_dir.iterdir():  # type: ignore
                destination = correct_media_dir / item.name
                print(f"Moving {item} to {destination}")
                if destination.exists():
                    if destination.is_dir():
                        shutil.rmtree(destination)
                    else:
                        destination.unlink()
                # The return type of shutil.move is partially unknown to Pyright
                # We're intentionally ignoring the return value, so we use type ignore
                # Type ignore for unknown return type of shutil.move
                _ = shutil.move(str(item), str(destination))  # type: ignore
                
            print("Moved all media files to correct directory")
        else:
            print("No images found in current media directory")
    else:
        print("Current media directory does not exist")
    
    # Clean up empty current media directory
    # Fix the type annotation that was causing the Pyright error
    if current_media_dir.exists():
        # Use a simpler type annotation that Pyright can fully resolve
        # Type ignore for unknown iterdir return type
        cleanup_items = list(current_media_dir.iterdir())  # type: ignore
        if not cleanup_items:
            try:
                current_media_dir.rmdir()
                print("Removed empty current media directory")
            except OSError:
                print("Could not remove current media directory (might not be empty)")
        else:
            print("Current media directory is not empty, skipping removal")

if __name__ == '__main__':
    fix_media_location()