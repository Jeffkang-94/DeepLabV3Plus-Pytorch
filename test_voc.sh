python main.py --model best_deeplabv3plus_resnet101_voc_os16 \
--enable_vis --vis_port 28333 --gpu_id 0 --year 2012_aug \
--crop_val --lr 0.01 --crop_size 513 --batch_size 16 \
--output_stride 16 --ckpt checkpoints/best_deeplabv3plus_mobilenet_voc_os16.pth --test_only --save_val_results
