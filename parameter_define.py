import os


TrainModel = False

img_dataset = 'training_dataset/HKU-IS/imgs/'  # train set
sal_dataset = 'training_dataset/HKU-IS/gt/'  # train set
# train_dataset = 'training_dataset/images_jpg/'  # train set
dirpath = 'RetargetMeAll/'  # test path
img_ext = '.png'
outpath = './test_result'  # test output path

grid_size = 8
grid_min = 3.0  #16*0.2

VGG_MEAN = [103.939, 116.779, 123.68]
SEED = 664  # Set to None for random seed.
batch_size = 4
img_height = 240
img_width = 320
learning_rate_ger = 1e-3
learning_rate_dis = 1e-3
device = '/gpu:0'


Citers = 5

# the upper bound and lower bound of parameters in critic
clamp_lower = -0.01
clamp_upper = 0.01

# whether to use adam for parameter update, if the flag is set False, use tf.train.RMSPropOptimizer
# as recommended in paper
is_adam = True

# directory to store log, including loss and grad_norm of generator and critic
log_dir = './log_wgan'
ckpt_dir = './ckpt_wgan'

if not os.path.exists(ckpt_dir):
    os.makedirs(ckpt_dir)

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

if not os.path.exists(outpath):
    os.makedirs(outpath)

num_epochs = 100