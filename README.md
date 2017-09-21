# py-TensorRT

A demo for TensorRT running on Ubuntu sys with CUDA, cuDNN ... setup, (say, TX1/TX2/TK1).

# Simple Run

### 1. Environment

Ensure the env (Sys, GPUs, CUDA, cuDNN, TensorRT, ...) are all installed and here we are not going to document that.

Say, for TX1/TX2/TK1, you can follow my another [repo](https://github.com/KleinYuan/tx2-flash).

### 2. Setup

```
# Setup
bash setup.sh
```

And, that's it. (note, it may pop up requiring password for root access tho)


### 3. Run

```
python app.py
```

