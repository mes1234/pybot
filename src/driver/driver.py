import debugpy
print("debugger started")
debugpy.listen(("localhost", 5678))
print("listening to external")
breakpoint()
print("connected")
counter = 0
while True:
    print(f"yello {counter}")