CS6886 Assignment 3: MobileNet-v2 Compression on CIFAR-10

GitHub Repository: https://github.com/cs24m538-coder/Assignment3-MobileNet-Compression

## Assignment Overview
This project implements custom model compression for MobileNet-v2 on CIFAR-10 using symmetric uniform quantization implemented from scratch. The assignment evaluates compression-accuracy trade-offs across 8 bit-width configurations (32-bit to 2-bit).

## 📊 Results Summary
- Baseline accuracy: 92.17%
- 8-bit quantization: 92.03% accuracy, 4.06x compression
- Final model size: 2.10 MB (reduced from 8.40 MB)
- Best configuration: 8-bit quantization

### Compression Results
| Bits | Accuracy | Compression Ratio | Model Size |
|------|----------|-------------------|------------|
| 32   | 92.00%   | 1.00x             | 8.40 MB    |
| 16   | 92.01%   | 2.03x             | 4.20 MB    |
| 12   | 92.03%   | 2.71x             | 3.15 MB    |
| 8    | 92.03%   | 4.06x             | 2.10 MB    |
| 6    | 91.71%   | 5.42x             | 1.58 MB    |
| 4    | 86.24%   | 8.12x             | 1.05 MB    |
| 3    | 5.35%    | 10.83x            | 0.79 MB    |
| 2    | 10.00%   | 16.24x            | 0.53 MB    |

## ⚠️ Important Note on Reproducibility
Due to GitHub's 100MB file size limit, the trained MobileNet-v2 model (89MB) is not included in this repository.

### To Test the Compression Pipeline:
```bash
# 1. Create placeholder model files (for testing only)
python create_model.py

# 2. Test 8-bit quantization (will show ~10% accuracy)
python test.py --bits 8

# 3. Run all experiments
python run_experiments.py
Expected Results with Placeholder Model:

Accuracy: ~10% (random guessing, CIFAR-10 has 10 classes)

Compression ratios: Correctly calculated

All 8 bit-widths tested successfully

Note: The results in the table above (92.17% accuracy, etc.) are from the actual trained model trained for 120 epochs. The placeholder model demonstrates the compression implementation works correctly.

🚀 Quick Start
1. Install Dependencies
bash
pip install -r requirements.txt
2. Train Baseline Model
bash
python train.py
3. Test Compression
bash
# Test 8-bit quantization
python test.py --bits 8

# Run all experiments
python run_experiments.py
📁 Repository Structure
text
Assignment3-MobileNet-Compression/
├── create_model.py                 # Placeholder model
├── models/mobilenetv2.py           # MobileNet-v2 for CIFAR-10
├── data/data_loader.py             # CIFAR-10 data loader
├── compression/quantizer.py        # Custom quantization
├── results/compression_results.json
├── train.py                        # Training script
├── test.py                         # Compression testing
├── run_experiments.py              # Run all experiments
├── requirements.txt                # Dependencies
├── README.md                       # This file
└── parallel_coordinates_plot.png   # Required plot
🔧 Implementation
Quantization: Symmetric uniform (implemented from scratch)

Method: Post-training quantization

Configurations: 8 bit-widths (32, 16, 12, 8, 6, 4, 3, 2)

No compression APIs used

📈 Key Findings
8-bit optimal: 4x compression with no accuracy loss

Critical threshold: Model collapses below 4-bit

Storage efficient: 75% size reduction with 8-bit

Quantization regularization: 12-bit slightly improved accuracy

📄 Report
Complete analysis with parallel coordinates plot available in the submitted PDF report.
