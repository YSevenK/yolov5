# yolov5 for Tianchi

## run
python train.py --data tianchi/street_yolo.yaml --cfg tianchi/street_yolov5s.yaml --epochs 1 --batch-size -1

## test
python detect.py --weights runs/train/exp/weights/best.pt --source  tianchi/images/test/ --save-txt
