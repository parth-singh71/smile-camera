import os


def is_smile_inside_face(smile_coords, face_coords):
    """Function to check if the smile detected is inside a face or not

    Args:
        smile_coords (list): list of smaile coordinates of form [x, y, (x+w), (y+h)]
        face_coords (list): list of face coordinates of form [x, y, (x+w), (y+h)]

    Returns:
        bool: True if smile is inside of face bounding box, else False
    """
    sx1, sy1, sx2, sy2 = smile_coords
    fx1, fy1, fx2, fy2 = face_coords
    # If top-left plate corner is inside the face
    if fx1 < sx1 and fy1 < sy1:
        # If bottom-right plate corner is inside the face
        if sx2 < fx2 and sy2 < fy2:
            # The entire smile is inside the face.
            return True
        else:
            # Some part of the smile is outside the face.
            return False
    else:
        # whole smile is outside the face.
        return False


def get_selfie_number():
    """Gives the last selfie number

    Returns:
        int: Last selfie number
    """
    data = os.listdir("selfies/")
    if not data == []:
        last_selfie = sorted(data)[-1]
        hiphen_index = last_selfie.rfind("-")
        extension_index = last_selfie.rfind(".png")
        return int(last_selfie[hiphen_index + 1:extension_index])
    return 0


def create_dir(dir):
    """Creates a directory if not already exists

    Args:
        dir (String): path of directory
    """
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print('Error: Cannot create directory named \"' + dir + '\"')
