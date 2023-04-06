import os

def rename_video_files(directory_path):
    # loop through each file in the directory
    for file_name in os.listdir(directory_path):
        # check if the file is a video file (and not a directory) and the extension is .mov
        if os.path.isfile(os.path.join(directory_path, file_name)):
            try:
                if file_name.endswith(".mov") or file_name.endswith(".MOV"):
                    # construct the old and new file paths
                    old_file_path = os.path.join(directory_path, file_name)
                    new_file_path = os.path.join(directory_path, os.path.splitext(file_name)[0] + ".mp4")
                    # rename the file
                    os.rename(old_file_path, new_file_path)
                    print(f'|-- {file_name} -> {file_name.split(".")[0]}.mp4 --|')
            except Exception as e:
                print(f"An error occurred while renaming {file_name}: {str(e)}")

def remove_heic_files(directory_path):
    # loop through each file in the directory
    for file_name in os.listdir(directory_path):
        # check if the file is a HEIC file (and not a directory)
        if os.path.isfile(os.path.join(directory_path, file_name)):
            try:
                if file_name.endswith(".HEIC") or file_name.endswith(".heic"):
                    # remove the file
                    os.remove(os.path.join(directory_path, file_name))
                    print(f'|-- Deleted {file_name} successfully --|')
            except Exception as e:
                print(f"An error occurred while deleting {file_name}: {str(e)}")
                
# replace this with the absolute path to the directory containing the video files
directory_path = "/Users/cajeeeeeeee/Desktop/Tere Bina"

# call the functions to rename the video files and remove the HEIC files
rename_video_files(directory_path)
remove_heic_files(directory_path)
