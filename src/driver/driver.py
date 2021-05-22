import debugpy
import time
print("debugger started")
debugpy.listen(("localhost", 5678))
print("listening to external")
breakpoint()
print("connected")
counter = 0
while True:
    time.sleep(1)
    print(f"yello {counter}")