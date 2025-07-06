# Math Equation Conversion Model Experiments

## Blackwell/RTX 5090 Requirements

This project is designed for research and experimentation on a workstation with:
- **GPU:** Nvidia RTX 5090 (Blackwell)
- **OS:** Ubuntu 22.04
- **Python:** 3.10–3.12

### CUDA & Driver
- **NVIDIA Driver:** ≥ 555.xx (ships with CUDA 12.8)
- **CUDA Toolkit:** 12.8+ (only if compiling extra libraries)

### PyTorch & Add-ons
- **PyTorch:** 2.7.1+cu128 (cu128 wheel required for Blackwell/`sm_120` support)
- **Add-ons:**
  - bitsandbytes >= 0.46.1
  - flash-attn == 2.5.6
  - xformers >= 0.0.28

### Installation
```bash
pip install torch==2.7.1+cu128 torchvision torchaudio \
  --index-url https://download.pytorch.org/whl/cu128
pip install bitsandbytes>=0.46.1 flash-attn==2.5.6 xformers>=0.0.28
```

### Container Option
```bash
docker run --gpus all -it --rm \
  pytorch/pytorch:2.7.1-cuda12.8-cudnn9-devel \
  bash
```

### Quick Verification
```python
import torch
print(torch.__version__, torch.version.cuda)  # expect 2.7.1 / 12.8
print(torch.cuda.get_device_name())           # RTX 5090
torch.ones(1).cuda()                          # no errors
```

### Troubleshooting
- Only use cu128 wheels (cu126 will fail on 5090)
- Pin exact versions for torch/vision
- For bitsandbytes errors, upgrade or compile with `TORCH_CUDA_ARCH_LIST="12.0"`
- Upgrade `transformers` and `accelerate` if tokenizer crashes in CPU mode

---

## Project Structure
See `experiment_roadmap.md` for experiment phases and directory layout.

## Getting Started
1. Ensure your system meets the above requirements
2. Install dependencies as above
3. Follow the experiment roadmap for next steps
