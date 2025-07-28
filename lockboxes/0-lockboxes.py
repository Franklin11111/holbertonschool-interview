#!/usr/bin/python3
"""
This module includes function for solving lockboxes algorithm
"""
from collections import deque


def canUnlockAll(boxes):
    """ The function for solving lockboxes algorithm """
    num_boxes = len(boxes)
    unlocked_boxes = {0}
    keys_to_process = deque(boxes[0])

    while keys_to_process:
        key = keys_to_process.popleft() # 1
        if 0 <= key < num_boxes and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            for new_key in boxes[key]:
                keys_to_process.append(new_key)
    return len(unlocked_boxes) == num_boxes
