from cv2 import cv2

def detectTrash():
    pass

# calculates the distance from the camera to a centered object
# assumes camera moved back, and so adds that additional distance
# to the result
# returned distance will be in whatever units the moved_amount is in
def detectDistanceToTrash(moved_amount, orig_perim, new_perim):
    dist = moved_amount / (1-(orig_perim/new_perim))
    return dist + moved_amount

# bbox should be a provided bounding box
# frame should be the current image
# tracker should be the already initiated tracker, if there is one
# returns x, y, w, h, tracker
# where x, y, w, h is the new bounding box for the trash
def trackTrash(bbox, frame, tracker=None):
    ok = True
    if not tracker:
        tracker = cv2.TrackerCSRT_create()
        ok = tracker.init(frame,bbox)
    if not ok:
        return None
    ok, bbox = tracker.update(frame)
    if ok:
        (x,y,w,h)=[int(v) for v in bbox]
        return x, y, w, h, tracker
    else:
        return None

def centerTrash(trash_center_x, image_center_x):
    # turn robot right if trash is to the right of the image center ( trash center x is > than image center x )
    if trash_center_x > image_center_x:
        #robot.turn_right(trash_center_x - image_center_x) or something
        pass
    # turn robot left if trash is to the left ( trash center x is < than image center x )
    elif trash_center_x < image_center_x:
        #robot.turn_left(image_center_x - trash_center_x) or something
        pass
    # trash should now be centered

# assumes we are getting a single frame from the camera as an image
def doSteps():
    # for now
    image = None
    # this should return a bounding rectangle around the trash
    trash_width, trash_height, trash_x, _ = detectTrash()

    trash_center_x = trash_x + (trash_width / 2)

    trash_area = trash_width * trash_height
    trash_perim = (trash_width * 2) + (trash_height * 2)

    # assumes the image is an opencv image
    _, width = image.shape[:2]

    image_center_x = width / 2

    centerTrash(trash_center_x, image_center_x)

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

