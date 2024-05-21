import cv2
import mediapipe as mp
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def process_single(img_filepath):
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        # Make detection
        img = cv2.imread(img_filepath)

        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # show original image
        plt.imshow(image)
        plt.title(f"Original {img_filepath}")
        plt.show()

        # Make detection
        results = pose.process(image)

        # Add tracked pose
        image.flags.writeable = True

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )
        print("done!")

        plt.imshow(image)
        plt.title(f"Tracked {img_filepath}")
        plt.show()
    return results


def process_multiple(img_filepaths, process_preview = False):
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        output_poses = {}
        for index, img_filepath in enumerate(img_filepaths):
            # Make detection
            img = cv2.imread(img_filepath)

            image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            if process_preview:
                # show original image
                plt.imshow(image)
                plt.title(f"Original {img_filepath}")
                plt.show()

            # Make detection
            results = pose.process(image)

            # Add tracked pose
            image.flags.writeable = True

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                      )
            print(f"Processed {index+1}/{len(img_filepaths)}: {img_filepath}")

            if process_preview:
                plt.imshow(image)
                plt.title(f"Tracked {img_filepath}")
                plt.show()

            output_poses[img_filepath] = results

    return output_poses
