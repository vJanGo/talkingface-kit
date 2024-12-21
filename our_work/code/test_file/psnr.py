import cv2
import os
from skimage.metrics import mean_squared_error
from skimage.metrics import peak_signal_noise_ratio
import argparse

def get_psnr_score(path):
    full_frame_path = os.path.join(path,'full_frame')
    fin_out_path = os.path.join(path,'fin_out')
    full_frame_files = [f for f in os.listdir(full_frame_path) if f.endswith('.png')]
    fin_out_files = [f for f in os.listdir(fin_out_path) if f.endswith('.png')]

    count = 0
    PSNR_sum = 0

    for full_frame_file,fin_out_file in zip(full_frame_files,fin_out_files):
        img1_path = os.path.join(full_frame_path,full_frame_file)
        img2_path = os.path.join(fin_out_path,fin_out_file)
        img1 = cv2.imread(img1_path)
        img2 = cv2.imread(img2_path)

        PSNR = peak_signal_noise_ratio(img1, img2)
        count = count+1
        PSNR_sum = PSNR_sum + PSNR

    PSNR_mean = PSNR_sum/count
    return PSNR_mean

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str)
    args = parser.parse_args()
    path = args.path
    psnr_score = get_psnr_score(path)
    name = os.path.basename(path)
    print(f'Average PSNR score of {name}:{psnr_score}')