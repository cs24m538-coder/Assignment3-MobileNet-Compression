# Assignment 3: MobileNet-v2 Compression

## Results
- Baseline: 92.17% accuracy
- 8-bit: 92.03% accuracy, 4.06x compression
- Best: 8-bit quantization

## Run
```bash
pip install -r requirements.txt
python train.py
python test.py --bits 8
