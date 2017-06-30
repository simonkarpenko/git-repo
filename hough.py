from enum import Enum
class Skew(Enum):
	LEFT = 1
	RIGHT = 2

def hough_transform(image, skew = Skew.LEFT):
	level = 0
	stripe_height = 2 ** level
	stripe_count = image.height // stripe_height 
	assert (stripe_count * stripe_height == image.height)
	