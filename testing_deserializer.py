import pickle
from pathlib import Path
import plotly.graph_objs as go
import mediapipe as mp

mp_pose = mp.solutions.pose

# From an image, find the corresponding pose file and displays the pose
TARGET_IMG = "D:\\Code_Projects\\UPenn\\dataset\\knees too far forward\\knees_too_far_forward_47.png"

# find pose file
p = Path(TARGET_IMG)
pose_path = p.with_suffix('.pose')

# deserialize
with open(pose_path, 'rb') as f:
    pose = pickle.load(f)

# Show image

# Visualize Pose
fig = go.Figure()
for connection in mp_pose.POSE_CONNECTIONS:
    connections_x = [pose[connection[0]]['x'], pose[connection[1]]['x']]
    connections_y = [pose[connection[0]]['y'], pose[connection[1]]['y']]
    connections_z = [pose[connection[0]]['z'], pose[connection[1]]['z']]
    # default value init, to make python happy with null refs
    fig.add_scatter3d(x=connections_x, y=connections_y, z=connections_z, mode='lines')

fig.show()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread(TARGET_IMG)
imgplot = plt.imshow(img)
plt.show()