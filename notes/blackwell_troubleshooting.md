# Blackwell (RTX 5090) Troubleshooting Notes

## Common Issues & Fixes

| Error                        | Cause                  | Fix                                                        |
| ---------------------------- | ---------------------- | ---------------------------------------------------------- |
| `no kernel image for device` | cu126 wheel installed  | Re‑install cu128 wheel as in README                        |
| Torch/vision mismatch        | Mixed nightly & stable | Pin exact versions (`torch==2.7.1`, `torchvision==0.22.1`) |
| bitsandbytes RuntimeError    | Incompatible wheel     | Upgrade or compile with `TORCH_CUDA_ARCH_LIST="12.0"`      |
| Tokenizer crash in CPU mode  | Old transformers       | `pip install --upgrade transformers accelerate`            |

## General Advice
- Always use cu128 wheels for PyTorch on RTX 5090 (Blackwell)
- Check CUDA version: must be 12.8+
- Pin all package versions for reproducibility
- If using containers, prefer official PyTorch or NGC images with CUDA 12.8+

## Quick Verification
```python
import torch
print(torch.__version__, torch.version.cuda)  # expect 2.7.1 / 12.8
print(torch.cuda.get_device_name())           # RTX 5090
torch.ones(1).cuda()                          # no errors
```

---
*See README.md and Blackwell_reqs.md for full details.* 