import img_loader
import pose_extractor
import serializer_saver

FILE_PATH = '..\\dataset\\'

# load files
file_paths = img_loader.get_all_files(FILE_PATH)

# Process
poses = pose_extractor.process_multiple(file_paths)
print(poses)

# Serialize and Save
output_files = serializer_saver.serialize_and_save_multiple(file_paths, poses)
print(f"SAVING DONE.\n{output_files}")
