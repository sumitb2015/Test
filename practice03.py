from datetime import datetime
from pathlib import Path

dirpath = Path.home() / "Desktop"

for file in dirpath.iterdir():
    if file.suffix == ".xlsx":
        name = file.stem
        c = name.split(" ")
        print(c)
        d = f'{datetime.now().date()}_{c[1]}_{c[2]}{file.suffix}'
        new_path = dirpath.joinpath(datetime.strftime(datetime.now().date(),"%B"))    
        print(new_path)
        if not new_path.exists():
            new_path.mkdir()
        new_path = new_path / d
        file.rename(new_path)
print("Hello World")
print("Sumit Bandyopadhyay")
        
        