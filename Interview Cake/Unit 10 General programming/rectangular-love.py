# A crack team of love scientists from OkEros (a hot new dating site) have devised a way to represent dating profiles as rectangles on a two-dimensional plane.

# Write a function to find the rectangular intersection of two given love rectangles.
# love rectangles are always "straight" and never "diagonal"

'''
my_rectangle = {

    # Coordinates of bottom-left corner
    'left_x'   : 1,
    'bottom_y' : 1,

    # Width and height
    'width'    : 6,
    'height'   : 3,
}
'''

'''
- ranges can partially overlap
- one range can be in other
- ranges don't overlap
- ranges touch at a point
'''

def find_x_overlap(x1, width1, x2, width2):
    # Find the highest ("rightmost") start point and
    # lowest ("leftmost") end point
    highest_start_point = max(x1, x2)
    lowest_end_point = min(x1 + width1, x2 + width2)

    # Return null overlap if there is no overlap
    if highest_start_point >= lowest_end_point:
        return (None, None)

    # Compute the overlap width
    overlap_width = lowest_end_point - highest_start_point

    return (highest_start_point, overlap_width)

def find_range_overlap(point1, length1, point2, length2):
    # Find the highest start point and lowest end point.
    # The highest ("rightmost" or "upmost") start point is
    # the start point of the overlap.
    # The lowest end point is the end point of the overlap.
    highest_start_point = max(point1, point2)
    lowest_end_point = min(point1 + length1, point2 + length2)

    # Return null overlap if there is no overlap
    if highest_start_point >= lowest_end_point:
        return (None, None)

    # Compute the overlap length
    overlap_length = lowest_end_point - highest_start_point

    return (highest_start_point, overlap_length)

def find_rectangular_overlap(rect1, rect2):
    # Get the x and y overlap points and lengths
    x_overlap_point, overlap_width  = find_range_overlap(rect1['left_x'],
                                                         rect1['width'],
                                                         rect2['left_x'],
                                                         rect2['width'])
    y_overlap_point, overlap_height = find_range_overlap(rect1['bottom_y'],
                                                         rect1['height'],
                                                         rect2['bottom_y'],
                                                         rect2['height'])

    # Return null rectangle if there is no overlap
    if not overlap_width or not overlap_height:
        return {
            'left_x'   : None,
            'bottom_y' : None,
            'width'    : None,
            'height'   : None,
        }

    return {
        'left_x'   : x_overlap_point,
        'bottom_y' : y_overlap_point,
        'width'    : overlap_width,
        'height'   : overlap_height,
    }

# O(1) time and O(1) space

'''
Draw out all possible cases - ranges overlap
Use specific and descriptive variable names
'''