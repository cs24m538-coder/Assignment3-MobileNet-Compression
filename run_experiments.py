# Script to run all compression experiments
import subprocess
import time

print("Running Assignment 3 Compression Experiments")
print("="*50)

bit_configs = [32, 16, 12, 8, 6, 4, 3, 2]

for bits in bit_configs:
    print(f"\nTesting {bits}-bit quantization...")
    print("-" * 30)
    
    cmd = f"python test.py --bits {bits}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    print(result.stdout)
    
    time.sleep(1)

print("\n" + "="*50)
print("All experiments completed!")
