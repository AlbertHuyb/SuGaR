town=$1
seq=$2
port=$3

data_root="/data/huyb/siggraph24/SuGaR/data/ss3dm"

# train
python gaussian_splatting/train.py -s ${data_root}/${town}/${seq} --iterations 7000 -m ./logs/${town}/${seq} --port ${port}

python train.py -s ${data_root}/${town}/${seq} -c ./logs/${town}/${seq}/ -r "sdf" --sugar_path ./sugar_logs/${town}/${seq}/

