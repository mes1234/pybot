import debugpy
import time
print("debugger started")
debugpy.listen(("0.0.0.0", 5678))
print("listening to external")
debugpy.wait_for_client()  # blocks execution until client is attached
print("connected")
counter = 0
while True:
    time.sleep(1)
    print(f"yello {counter}")