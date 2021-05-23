python main.py --model deeplabv3plus_mobilenet \
    --dataset cityscapes --gpu_id 0  --test_only \
    --batch_size 16 --output_stride 16 --data_root /mnt2/datasets/cityscapes \
    --ckpt ./checkpoints/best_deeplabv3plus_mobilenet_cityscapes_os16.pth \
    --save_val_results 