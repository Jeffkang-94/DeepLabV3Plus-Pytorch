import argparse
import os
import shutil
from tqdm import tqdm

import json

def load_json(f):
    with open(f, 'r') as fp:
        return json.load(fp)


def save_json(obj, f, *args, **kwargs):
    with open(f, 'w') as fp:
        json.dump(obj, fp, *args, **kwargs)

def split_json(path, dataset_type):
    dirname = os.path.join(os.path.dirname(path), dataset_type)
    os.makedirs(dirname, exist_ok=True)

    labels = load_json(path)
    # /mnt/datasets/bdd100k
    for label in tqdm(labels):
        name = label['name']
        f = os.path.join(dirname, name.replace('.jpg', '.json')) # f : filename
        save_json(label, f, indent=4)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--root', type=str, default='/mnt2/datasets/bdd100k')
    args = parser.parse_args()

    root = args.root

    train_labels = os.path.join(root, 'labels/sem_seg/polygons/sem_seg_train.json')
    valid_labels = os.path.join(root, 'labels/sem_seg/polygons/sem_seg_val.json')

    split_json(train_labels, 'train') 
    split_json(valid_labels, 'val')


if __name__ == '__main__':
    main()
