import pickle
from pathlib import Path
import plotly.graph_objs as go
import mediapipe as mp

mp_pose = mp.solutions.pose


# From an image, find the corresponding pose file and displays the pose

def check_img(target_img):
    # find pose file
    p = Path(target_img)
    pose_path = p.with_suffix('.pose')
    # deserialize
    with open(pose_path, 'rb') as f:
        pose = pickle.load(f)
    # Show image
    # Visualize Pose
    fig = go.Figure()

    for index, point in enumerate(pose):
        fig.add_scatter3d(x=[point['x']], y=[point['y']], z=[point['z']], name=f"JOINT {index}")

    for index, connection in enumerate(mp_pose.POSE_CONNECTIONS):
        connections_x = [pose[connection[0]]['x'], pose[connection[1]]['x']]
        connections_y = [pose[connection[0]]['y'], pose[connection[1]]['y']]
        connections_z = [pose[connection[0]]['z'], pose[connection[1]]['z']]
        # default value init, to make python happy with null refs
        fig.add_scatter3d(x=connections_x, y=connections_y, z=connections_z, mode='lines', name=f"line {index}")
    fig.show()
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    img = mpimg.imread(target_img)
    imgplot = plt.imshow(img)
    plt.show()


check_img(r"D:\Code_Projects\UPenn\dataset\knees inward\knees_inward_9.png")
# check_img(r"D:\Code_Projects\UPenn\dataset\knees inward\knees_inward_1.png")
# check_img(r"D:\Code_Projects\UPenn\dataset\knees inward\knees_inward_5.png")
# check_img(r"D:\Code_Projects\UPenn\dataset\knees inward\knees_inward_53.png")
# check_img(r"D:\Code_Projects\UPenn\dataset\not deep enough\not_deep_enough_56.png")
