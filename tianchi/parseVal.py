import json

import cv2

val_json = json.load(open('mchar_val.json'))
for x in val_json:
    img = cv2.imread("images/mchar_val/" + x)
    width = img.shape[1]
    height = img.shape[0]
    val_label = list(map(int, val_json[x]['label']))
    val_height = list(map(int, val_json[x]['height']))
    val_left = list(map(int, val_json[x]['left']))
    val_width = list(map(int, val_json[x]['width']))
    val_top = list(map(int, val_json[x]['top']))
    loc_pic = "labels/val/" + x.split('.')[0] + '.txt'
    pic = open(loc_pic, "w")
    for i in range(len(val_label)):
        pic_label = val_label[i]
        pic_x = (val_left[i] + val_width[i] / 2) / width
        pic_y = (val_top[i] + val_height[i] / 2) / height
        pic_width = val_width[i] / width
        pic_height = val_height[i] / height
        pic.write(str(pic_label) + " " + str(pic_x) + " " + str(pic_y) + " " + str(pic_width) + " " + str(pic_height))
        pic.write("\n")
    pic.close()
