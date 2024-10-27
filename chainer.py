#!/bin/python3

with open("final_check-27-10_14-27.txt","r") as file:
    for line in file.readlines():
        if "socks5" in line:
            with open("chain.txt","a") as c:
                tmp = line.split("-")[0].strip().split(":")[0]
                tmp1 = line.split("-")[0].strip().split(":")[1]
                c.write(f"socks5 {tmp} {tmp1}\n")
