#!/usr/bin/python3


def canUnlockAll(boxes):
    """Unlock array of boxes of keys with indices"""

    if boxes is None or len(boxes) == 0:
        return False
    
    status = ["T"]
    
    for box in range(1, len(boxes)):
        status.append("F")
    
    for box in range(0, len(boxes)):
        if (status[box] == "T" or box == 0):
            for key in boxes[box]:
                if int(key) < len(boxes) and status[key] == "F":
                    for k in boxes[key]:
                        if k < len(boxes):
                            status[k] = "T"
                if key < len(boxes):
                    status[key] = "T"
                                
        if "F" in status:
            return False
        return True
                    
