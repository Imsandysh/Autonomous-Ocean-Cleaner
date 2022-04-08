def detectTrash():
    pass

def detectDistanceToTrash():
    pass

def doSteps():
    # this should return a bounding rectangle around the trash
    trash_width, trash_height, trash_x, trash_y = detectTrash()

    trash_center_x = trash_x + (trash_width / 2)
    trash_center_y = trash_y + (trash_height / 2)

    trash_area = trash_width * trash_height

    # turn robot right if trash is to the right of the image center ( trash center x is > than image center x )

    # turn robot left if trash is to the left ( trash center x is < than image center x )

    # trash should now be centered

    dist = detectDistanceToTrash()

    # move robot forward while dist < amount

    # repeat steps until robot has hit desired trash

    # grab trash

