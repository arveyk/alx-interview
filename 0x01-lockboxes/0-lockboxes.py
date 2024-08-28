#!/usr/bin/python3
""" Module for lockBox task
"""


def canUnlockAll(boxes):
    """Function to determine if all boxes can be unlocked
    Args:
        boxes: a list of lists to be assessed
    Returns: true if all can be unlocked, false if otherwise
    """
    unlocked = []
    allBoxes = []

    noOfboxes = len(boxes)
    for box in range(noOfboxes):
        allBoxes.append(box)
    if (isinstance(boxes, list)):
        unlocked = boxes[0] + [0]
        for index in range(1, len(boxes)):
            if index in unlocked:
                unlocked += boxes[index]
                unlocked = list(set(unlocked))
                unlocked2 = []
                for elem in unlocked:
                    if elem < noOfboxes:
                        unlocked2 += boxes[elem]
                unlocked += unlocked2
    unlocked = list(set(unlocked))
    for key in allBoxes:
        if key not in unlocked:
            return False
    return True
