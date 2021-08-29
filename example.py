import function_checkpointing as ckpt
import time
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    print(f"filename: {filename}")
    try:
        ckpt.resume_from_checkpoint(filename)
    except FileNotFoundError:
        pass
for step_i in range(5):
    print(f"""step_i = {step_i}""")
    ckpt.save_checkpoint(f"step_i-{step_i}")  
    time.sleep(1)
for step_j in range(5):
    print(f"""step_j = {step_j}""")
    ckpt.save_checkpoint(f"step_j-{step_j}")  
    time.sleep(1)
for step_k in range(5):
    print(f"""step_k = {step_k}""")
    ckpt.save_checkpoint(f"step_k-{step_k}")  
    time.sleep(1)