#!/usr/bin/env python3

import psutil

print(f"Number CPU: {psutil.os.cpu_count()}")
print(f"Available Memory: {psutil.virtual_memory().total/2**30} GB")
print(f"Disk space: {psutil.disk_usage('/').total/2**30} GB")


