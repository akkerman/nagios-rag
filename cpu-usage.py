#!/usr/bin/python
import psutil

def cpu_rag():
    cpu = psutil.cpu_percent(interval=1)

    print cpu

    if cpu > 25:
        return "011"
    if cpu > 50:
        return "010"
    if cpu > 75:
        return "110"
    if cpu > 99:
        return "100"

    return "001"

if __name__ == '__main__':
    print cpu_rag()
