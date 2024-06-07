#!/usr/bin/python3


def canUnlockAll(boxes):
    """Function to determine if all boxes can be unlocked
    Args:
        boxes: a list of lists to be assessed
    Returns: true if all can be unlocked, false if otherwise
    """
    keys = []
    count = 0
    for item in boxes:
        if (item isinstance list):
            for index in range(len(item)):
                if len(item) == 0 and count < len(boxes):
                    return False

        count += 1

    return True

