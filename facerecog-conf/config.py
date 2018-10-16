# -*- coding: utf-8 -*-
u"""File cấu hình cho toàn bộ project."""

import os


thrift_emb_service_host = 'localhost'
# thrift_emb_service_host = 'gpu'
thrift_emb_service_port = 9991
emb_type = 'FACENET'
if "EMB_HOST_THRIFT" in os.environ:
    thrift_emb_service_host = os.environ["EMB_HOST_THRIFT"]
if "EMB_PORT_THRIFT" in os.environ:
    thrift_emb_service_port = os.environ["EMB_PORT_THRIFT"]
if "EMB_TYPE" in os.environ:
    emb_type = os.environ["EMB_TYPE"]

# predict_model_path = '/root/data/models/predict.pkl_nofinetune'
# id2name_map_path = '/root/data/models/id2name_map.pkl_nofinetune'

model_path = '/root/data/models'
predict_model_path = '/root/data/models/predict.pkl'
id2name_map_path = '/root/data/models/id2name_map.pkl'

facenet_model_dir = '/root/data/20170512-110547'
facenet_model_dir = '/root/data/facenet_model'
# facenet_model_dir = '/root/data/facenet_finetune'

face_cluster_dir = '/root/data/face_label_good_resplit'
face_cluster_old_dir = '/root/data/face_cluster_old'
old_vectors_dir = '/root/data/old_vectors'

use_motion_detection = False
if 'ENABLE_MOTION_DETECTION' in os.environ:
    use_motion_detection = os.environ["ENABLE_MOTION_DETECTION"]

camera_id = 'DEFAULT_CAMID'
if 'CFG_CAMERA_ID' in os.environ:
    camera_id = os.environ['CFG_CAMERA_ID']

list_people_file = '/root/data/people.txt'

feature_model = 'resnet'  #  'resnet' or 'facenet'

if feature_model == 'resnet':
    use_pca = True
    MODEL_INPUT_SHAPE = 224
elif feature_model == 'facenet':
    use_pca = False
    MODEL_INPUT_SHAPE = 160

N_COMPONENTS_PCA = 256
DIVERSITY_SCORE = 40

MAX_IMAGE_SIZE = 1200

MTCNN_THRESHOLD = [0.8, 0.85, 0.9]  # three steps's threshold
MTCNN_FACTOR = 0.72  # scale factor

DISPLAY_WIDTH = 1280
FACE_MIN_SIZE = (120, 120)
FACE_MAX_SIZE = (1000, 1000)

FACE_MIN_SIZE_COLLECTING = (100, 100)
FACE_MAX_SIZE_COLLECTING = (800, 800)

face_collecting_sequence_facedetector = 'mtcnn'  # 'mtcnn' or 'stack' or 'hibrid'
camera_surveillance_facedetector = 'mtcnn'  # 'mtcnn' or 'stack' or 'hibrid'

vector_dir = '/root/data/vectors'
face_review_dir = '/root/data/static'
failed_images_dir = '/root/data/failed_images'
camera_surveillance_data_dir = '/root/data/surveillance_data'
tagged_data_dir = '/root/data/tagged_data'
collected_sequence_dir = '/root/data/face_sequences'
collected_face_dir = '/root/data/face_collected'

wsconfig_url = 'wss://godeyes.mobilelab.vn/ws/camcc'
dbEnv = '/root/data/db/eventlog'

zmq_port = 9992
zmq_log = True
