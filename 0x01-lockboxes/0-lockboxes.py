#!/usr/bin/python3


def canUnlockAll(boxes):
    """Function to determine if all boxes can be unlocked
    Args:
        boxes: a list of lists to be assessed
    Returns: true if all can be unlocked, false if otherwise
    """
    unlocked = []
    allBoxes = []
    for box in range(len(boxes)):
        allBoxes.append(box)
    if (isinstance(boxes, list)):
        unlocked = boxes[0] + [0]
        for index in range(1, len(boxes)):
            if index in unlocked:
                unlocked += boxes[index]
                unlocked = list(set(unlocked))
                unlocked2 = []
                for elem in unlocked:
                    unlocked2 += boxes[elem]
                unlocked += unlocked2
                unlocked = list(set(unlocked))

    if allBoxes == unlocked:
        return True
    return False
