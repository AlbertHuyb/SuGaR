import os
import numpy as np
import argparse

import glob

parser = argparse.ArgumentParser()
parser.add_argument('--town', type=str, default=None)
parser.add_argument('--seq', type=str, default=None)
parser.add_argument('--update', action='store_true')

args = parser.parse_args()

data_root = '/data/huyb/siggraph24/SuGaR/data/ss3dm'

if args.town is not None:
    town_list = [args.town]
elif args.seq is not None:
    town_list = [args.seq.split('_')[0]]
else:
    town_list = ['Town01',  'Town02',  'Town03',  'Town04',  'Town05',  'Town06',  'Town07',  'Town10']

for town in town_list:
    town_dir = os.path.join(data_root, town)
    
    if args.seq is not None:
        seq_list = [args.seq]
    else:
        seq_list = os.listdir(town_dir)
    for seq in seq_list:
        if os.path.isdir(os.path.join(town_dir, seq)):
            sugar_output_dir = './sugar_logs/%s/%s/'%(town, seq)
            output_obj_path = os.path.join(sugar_output_dir, 'refined_mesh/%s/*.obj'%seq)
            if len(glob.glob(output_obj_path)) == 0:
                train_cmd = "bash train.sh %s %s"%(town, seq)
                # os.system(train_cmd)
                print(train_cmd)