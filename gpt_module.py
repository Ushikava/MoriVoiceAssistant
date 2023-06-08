import gpt_2_simple as gpt2
import os
import requests

# ----- variables -----
model_name = "124M"                             # may be: "124M" // "355M" // "774M" // "1550M"
file_name = "comments_in_txt.txt"                   # txt data file
training_steps = 100
sample_every = training_steps
save_every = training_steps
print_every = 10
batch_size = 1

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

gpt2.generate(sess)



# downloading model if needed
#if not os.path.isdir(os.path.join("models", model_name)):
#	print(f"Downloading {model_name} model...")
#	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/
#
#if not os.path.isfile(file_name):
#	print("(!) File not found, using default script...")
#	url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
#	data = requests.get(url)
#
#	with open(file_name, 'w') as f:
#		f.write(data.text)
#
#sess = gpt2.start_tf_sess()
#gpt2.finetune(sess, file_name, model_name=model_name, steps=training_steps, sample_every=sample_every, save_every=save_every, print_every=print_every, batch_size=batch_size, multi_gpu=True)  # steps is max number of training steps
#gpt2.generate(sess)