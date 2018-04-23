#!/usr/bin/env python3
import subprocess

for i in range(1, 100):
    with open("../../logs/lifo_less/logU{}.out".format(i), "w") as f:
        subprocess.Popen(["../../src/exec.py",
                          "--duration=900".format(i),
                          "--bind_port={}".format(i+26000),
                          "--hash=59066769B9AD42DA2E508611C33D7C4480B3857B"],
                          stdout=f)

