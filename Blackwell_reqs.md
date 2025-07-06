# RTX 5090 + PyTorch (Ubuntu 22.04)

> **Purpose**
> Quick reference for AI agent & developers to set up a Blackwell‑based RTX 5090 for LLM fine‑tuning with PyTorch.

---

## 1. Minimum versions

| Component     | Version                                 |
| ------------- | --------------------------------------- |
| NVIDIA driver | **≥ 555.xx** (ships with CUDA 12.8)     |
| CUDA toolkit  | 12.8 + (only if you compile extra libs) |
| Python        | 3.10 – 3.12                             |

---

## 2. Install PyTorch with CUDA 12.8

```bash
python -m pip install --upgrade \
  torch torchvision torchaudio \
  --index-url https://download.pytorch.org/whl/cu128
```

* Installs **torch 2.7.1+cu128** (first build with full Blackwell/`sm_120` kernels).
* Default PyPI wheels (cu126) will fail with `no kernel image available`.

### Quick verification

```python
import torch, platform
print(torch.__version__, torch.version.cuda)  # expect 2.7.1 / 12.8
print(torch.cuda.get_device_name())           # RTX 5090
torch.ones(1).cuda()                          # no errors
```

---

## 3. Container option

```bash
docker run --gpus all -it --rm \
  pytorch/pytorch:2.7.1-cuda12.8-cudnn9-devel \
  bash
```

NGC alternative: `nvcr.io/nvidia/pytorch:25.06-py3`

---

## 4. Essential add‑ons (cu128 wheels)

```bash
pip install bitsandbytes>=0.46.1 \
            flash-attn==2.5.6 \
            xformers>=0.0.28
```

---

## 5. Troubleshooting

| Error                        | Cause                  | Fix                                                        |
| ---------------------------- | ---------------------- | ---------------------------------------------------------- |
| `no kernel image for device` | cu126 wheel installed  | Re‑install cu128 wheel as above                            |
| Torch/vision mismatch        | Mixed nightly & stable | Pin exact versions (`torch==2.7.1`, `torchvision==0.22.1`) |
| bitsandbytes RuntimeError    | Incompatible wheel     | Upgrade or compile with `TORCH_CUDA_ARCH_LIST="12.0"`      |
| Tokenizer crash in CPU mode  | Old transformers       | `pip install --upgrade transformers accelerate`            |

---

## 6. One‑liner

```bash
pip install torch==2.7.1+cu128 torchvision torchaudio \
            --index-url https://download.pytorch.org/whl/cu128
```

---

*Last updated: 2025‑07‑06*
