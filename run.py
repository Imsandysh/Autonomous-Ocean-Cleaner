def detectTrash():
    pass

# calculates the distance from the camera to a centered object
# assumes camera moved back, and so adds that additional distance
# to the result
def detectDistanceToTrash(moved_amount, orig_perim, new_perim):
    dist = moved_amount / (1-(orig_perim/new_perim))
    return dist + moved_amount


def doSteps():
    # this should return a bounding rectangle around the trash
    trash_width, trash_height, trash_x, trash_y = detectTrash()

    trash_center_x = trash_x + (trash_width / 2)
    trash_center_y = trash_y + (trash_height / 2)

    trash_area = trash_width * trash_height
    trash_perim = (trash_width * 2) + (trash_height * 2)

    # turn robot right if trash is to the right of the image center ( trash center x is > than image center x )

    # turn robot left if trash is to the left ( trash center x is < than image center x )

    # trash should now be centered

    # move robot backward x amount 
    # (this does not need to be in pixels, should be in meters or inches) 
    # and calculate trash growth in image
    # should go backward so we do not run into the trash on accident

    move_backward = 0

    #robot.move_backward(move_backward)

    trash_width_2, trash_height_2, _, _ = detectTrash()

    trash_perim_2 = (trash_width_2 * 2) + (trash_height_2 * 2)

    dist = detectDistanceToTrash(move_backward, trash_perim, trash_perim_2)

    # move robot forward while dist > desired_dist

    # repeat steps until robot has hit desired trash

    # grab trash

