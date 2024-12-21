from niqe import get_niqe_score
from fid import get_fid_score
from psnr import get_psnr_score
from ssim import get_ssim_score
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str)
    args = parser.parse_args()
    name = os.path.basename(args.path)
    path = args.path
    print('begin fid')
    FID_score = get_fid_score(path)
    print(f'Average FID score of {name}:{FID_score}')
    print('begin ssim')
    ssim_score = get_ssim_score(path)
    print(f'Average SSIM score of {name}:{ssim_score}')
    print('begin psnr')
    psnr_score = get_psnr_score(path)
    print(f'Average PSNR score of {name}:{psnr_score}')
    print('begin niqe')
    full_frame_niqe_score, fin_out_niqe_score = get_niqe_score(path)
    print(f'Average NIQE score of full_frame {name}:{full_frame_niqe_score}')
    print(f'Average NIQE score of fin_out {name}:{fin_out_niqe_score}')
    print('finish')