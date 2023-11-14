# libBuffer
 Library for Python to help with storing shit in memory (will reset after user has closed program)

# Demo code
```
from libBuffer import *
import time

print("Current buffers")
print("b1: "+buff1)
print("b2: "+buff2)
print("switching")
time.sleep(3)
flipBuffers()
print("new values:")
print("b1: "+buff1)
print("b2: "+buff2)
```
