import pathlib
import shutil
from pathlib import Path

# Create output directories
base_dir = Path("collected_pdfs")
slides_dir = base_dir / "slides"
chapters_dir = base_dir / "chapters"
other_dir = base_dir / "other"

# Create all directories
for dir in [slides_dir, chapters_dir, other_dir]:
    dir.mkdir(parents=True, exist_ok=True)

# Get current directory
current_dir = Path(".")

# Find all PDF files recursively, excluding certain directories
def should_exclude(path):
    exclude_dirs = [".venv", "collected_pdfs", "all_pdfs"]
    return any(d in str(path) for d in exclude_dirs)

pdf_files = [f for f in current_dir.rglob("*.pdf") if not should_exclude(f)]

# Copy each PDF to the appropriate directory
used_names = {
    "slides": set(),
    "chapters": set(),
    "other": set()
}

for pdf_file in pdf_files:
    # Get base name and determine target directory
    base_name = pdf_file.name
    
    if "Slides" in base_name:
        target_dir = slides_dir
        used_set = used_names["slides"]
    elif "Chapter" in base_name:
        target_dir = chapters_dir
        used_set = used_names["chapters"]
    else:
        target_dir = other_dir
        used_set = used_names["other"]
    
    # Create unique filename if needed
    new_name = base_name
    counter = 1
    
    while new_name in used_set:
        name_part = base_name.rsplit('.', 1)[0]
        ext_part = base_name.rsplit('.', 1)[1]
        new_name = f"{name_part}_{counter}.{ext_part}"
        counter += 1
    
    used_set.add(new_name)
    dest = target_dir / new_name
    
    # Copy file
    shutil.copy2(pdf_file, dest)
    rel_path = pdf_file.relative_to(current_dir)
    target_folder = target_dir.name
    print(f"Copied to {target_folder}: {rel_path}")

print("\nPDFs have been organized into:")
print(f"- Slides: {slides_dir}")
print(f"- Chapters: {chapters_dir}")
print(f"- Other: {other_dir}")
