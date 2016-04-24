# COS 720 Securities
# Assignment by Jason R. Evans 13032608 & Vivian L. Venter 13238435
# Project 14

from pytagcloud import create_tag_image, make_tags, LAYOUTS
from pytagcloud.lang.counter import get_tag_counts

'''
This class creates word cloud images from the data given.
'''
class WordCloud:
    def CreateWordcloud(data):
        tags = make_tags(get_tag_counts(data))
        create_tag_image(tags, 'image.png', size=(900, 600), background=(0, 0, 0, 0), fontname='Lobster')
