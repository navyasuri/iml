source activate styletransferml5
cd /home/u24235/train_style_transfer_devCloud/

export PYTHONUNBUFFERED=0
python style.py --style images/fire.jpg \
  --checkpoint-dir checkpoints/ \
  --model-dir models/ \
  --test images/violetaparra.jpg \
  --test-dir tests/ \
  --content-weight 1.5e1 \
  --checkpoint-iterations 1000 \
  --batch-size 32

