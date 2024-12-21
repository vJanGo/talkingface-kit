import torch
import os
from pytorch_fid import fid_score
import argparse

def get_fid_score(path):
    full_frame_path = os.path.join(path,'full_frame')
    fin_out_path = os.path.join(path,'fin_out')
    FID_score = fid_score.calculate_fid_given_paths([full_frame_path, fin_out_path],batch_size=100, device=torch.device('cpu'), dims=2048,num_workers=0)
    return FID_score

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str)
    args = parser.parse_args()
    path = args.path
    path = 'test_result/Jae-in'
    FID_score = get_fid_score(path)
    name = os.path.basename(path)
    print(f'Average FID score of {name}:{FID_score}')