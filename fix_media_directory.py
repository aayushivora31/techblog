import os
import shutil
from pathlib import Path
from typing import Generator, TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pathlib import Path as PathType

def fix_media_directory() -> None:
    # Define paths
    current_media_dir = Path('media')  # This is where images are currently stored
    correct_media_dir = Path('../media')  # This is where they should be
    
    print(f"Current media directory: {current_media_dir.absolute()}")
    print(f"Correct media directory: {correct_media_dir.absolute()}")
    
    # Check if current media directory exists and has content
    # Explicitly type the generator to help Pyright
    if current_media_dir.exists():
        # Type ignore for unknown generator type
        items: Generator[Path, None, None] = current_media_dir.iterdir()  # type: ignore
        if any(items):
            print("Found images in current media directory")
            
            # Create the correct media directory if it doesn't exist
            correct_media_dir.mkdir(exist_ok=True)
            
            # Move all content from current to correct directory
            item: Path
            # Type ignore for unknown iterdir return type
            for item in current_media_dir.iterdir():  # type: ignore
                destination = correct_media_dir / item.name
                print(f"Moving {item} to {destination}")
                if destination.exists():
                    if destination.is_dir():
                        shutil.rmtree(destination)
                    else:
                        destination.unlink()
                # Type ignore for unknown return type of shutil.move
                _ = shutil.move(str(item), str(destination))  # type: ignore
            
            print("Moved all media files to correct directory")
        else:
            print("No images found in current media directory")
    else:
        print("Current media directory does not exist")
    
    # Clean up empty current media directory
    if current_media_dir.exists():
        # Use a simpler approach that Pyright can fully resolve
        # Type ignore for unknown iterdir return type
        remaining_items = list(current_media_dir.iterdir())  # type: ignore
        if not remaining_items:
            try:
                current_media_dir.rmdir()
                print("Removed empty current media directory")
            except OSError:
                print("Could not remove current media directory (might not be empty)")
        else:
            print("Current media directory is not empty, skipping removal")

if __name__ == '__main__':
    fix_media_directory()