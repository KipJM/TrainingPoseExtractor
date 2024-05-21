import pickle
from pathlib import Path


def serialize_and_save_multiple(file_paths, poses):
    output_file_paths = []
    for index, file_path in enumerate(file_paths):
        try:
            poses[file_path].pose_world_landmarks.landmark
        except:
            print(f"ERROR {index + 1}/{len(file_paths)}: No detections")
            continue

        # Create file
        p = Path(file_path)
        target_path = p.with_suffix('.pose')
        # "wb" argument opens the file in binary mode
        with open(target_path, "wb") as outfile:
            # Reparse since pickle can't do anything apparently
            data_for_serialization = []
            for landmark in poses[file_path].pose_world_landmarks.landmark:
                data_for_serialization.append(
                    {'x': landmark.x, 'y': landmark.y, 'z': landmark.z, 'visibility': landmark.visibility}
                )

            pickle.dump(data_for_serialization, outfile)
            output_file_paths.append(target_path)

        print(f"Saving... {index + 1}/{len(file_paths)}: {file_path}")
    return output_file_paths
