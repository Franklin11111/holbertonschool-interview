#!/usr/bin/python3
from collections import deque

def canUnlockAll(boxes):
    num_boxes = len(boxes) # 7
    unlocked_boxes = {0}
    keys_to_process = deque(boxes[0])

    while keys_to_process:
        # print("Keys to process: ", keys_to_process)
        key = keys_to_process.popleft() # 1
        # print("Key: ", key)
        if 0 <= key < num_boxes and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            # print("Number of unlocked boxes: ", len(unlocked_boxes))
            # print("Unlocked boxes: ", unlocked_boxes)
            for new_key in boxes[key]:
                keys_to_process.append(new_key)
        # print("Updated keys to process: ", keys_to_process)
        # print("/------------------------------/")
    return len(unlocked_boxes) == num_boxes

# boxes_1 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
#
# print(canUnlockAll(boxes_1))

# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes))
#
# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes))
#
# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes))