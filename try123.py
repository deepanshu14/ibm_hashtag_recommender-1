from watson_developer_cloud import VisualRecognitionV3
import os
import json
from os.path import join, dirname
from os import environ
#Set up credentials


def get_image_info(img_url):
	visual_recognition = VisualRecognitionV3('2016-05-20', api_key='c19caa73754b7dd23158f48033309ad362cc3816')
	str_dict =  json.dumps(visual_recognition.classify(images_url=img_url), indent=2)
	obj_dict =  json.loads(str_dict)
	return str_dict,obj_dict