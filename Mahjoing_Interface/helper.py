import os

folder_name = "mahjong_tiles"

if os.path.exists(folder_name):
    files = os.listdir(folder_name)
    print("")
    for f in files:
        if f.endswith(".png"):
            print(f"        <file alias='{f}'>{folder_name}/{f}</file>")
else:
    print(f"Folder '{folder_name}' not found!")