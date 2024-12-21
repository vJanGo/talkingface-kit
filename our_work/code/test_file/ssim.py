import os
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import argparse

def get_ssim_score(path):
    full_frame_path = os.path.join(path,'full_frame')
    fin_out_path = os.path.join(path,'fin_out')
    full_frame_files = [f for f in os.listdir(full_frame_path) if f.endswith('.png')]
    fin_out_files = [f for f in os.listdir(fin_out_path) if f.endswith('.png')]

    count = 0
    SSIM_sum = 0

    for full_frame_file,fin_out_file in zip(full_frame_files,fin_out_files):
        img1_path = os.path.join(full_frame_path,full_frame_file)
        img2_path = os.path.join(fin_out_path,fin_out_file)
        img1 = np.array(Image.open(img1_path))
        img2 = np.array(Image.open(img2_path))
        count = count+1
        SSIM_sum = SSIM_sum + ssim(img1,img2,multichannel=True, channel_axis=-1)

    SSIM_mean = SSIM_sum/count
    return SSIM_mean

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str)
    args = parser.parse_args()
    path = args.path
    ssim_score = get_ssim_score(path)
    name = os.path.basename(path)
    print(f'Average SSIM score of {name}:{ssim_score}')
