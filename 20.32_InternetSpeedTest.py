# How to do internet speed test with python code?
# https://pypi.org/project/speedtest-cli/

import speedtest
wifi = speedtest.Speedtest()
print("My wifi download speed = ", wifi.download())
print("My wifi Upload speed = ", wifi.upload())