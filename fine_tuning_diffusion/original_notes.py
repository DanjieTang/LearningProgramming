# git clone https://github.com/huggingface/diffusers
# cd diffusers
# pip install .

# cd examples
# cd text_to_image

# pip install -r requirements.txt
# pip install wandb

# export MODEL_NAME="CompVis/stable-diffusion-v1-4"
# export DATASET_NAME="lambdalabs/pokemon-blip-captions"

# Enter huggingface token
# huggingface-cli login

accelerate launch train_text_to_image_lora.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --dataset_name=$DATASET_NAME --caption_column="text" \
  --resolution=512 --random_flip \
  --train_batch_size=4 \
  --num_train_epochs=100 --checkpointing_steps=5000 \
  --learning_rate=1e-04 --lr_scheduler="constant" --lr_warmup_steps=0 \
  --seed=42 \
  --output_dir="sd-pokemon-model-lora" \
  --validation_prompt="cute dragon creature" --report_to="wandb"
