import os
import time

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

print(R"""
░█████╗░░██████╗░░░░░░████████╗░█████╗░███╗░░██╗
██╔══██╗██╔════╝░░░░░░╚══██╔══╝██╔══██╗████╗░██║
██║░░██║╚█████╗░█████╗░░░██║░░░███████║██╔██╗██║
██║░░██║░╚═══██╗╚════╝░░░██║░░░██╔══██║██║╚████║
╚█████╔╝██████╔╝░░░░░░░░░██║░░░██║░░██║██║░╚███║
░╚════╝░╚═════╝░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝ Generator""")

o = input("\ninput your OS-Tan: ")
print("Generating...")
time.sleep(2)
print("Done.")

# Windows-Tans
if o == "1.0-tan":
    os.system("feh windows/1-tan.jpg")

elif o == "3.1-tan":
    os.system("feh windows/3.1.jpg")

elif o == "95-tan":
    os.system("feh windows/95.png")

elif o == "98-tan":
    os.system("feh windows/98.png")

elif o == "98SE-tan":
    os.system("feh windows/98SE.png")

elif o == "2K-tan":
    os.system("feh windows/2K.png")

elif o == "ME-tan":
    os.system("feh windows/ME.jpg")

elif o == "XP-tan":
    os.system("feh windows/XP.png")

elif o == "Nanami Madobe":
    os.system("feh windows/7.png")

elif o == "Ai Madobe" or o == "Yu Madobe" or o == "Ai & Yu Madobe":
    os.system("feh windows/8.png")

elif o == "Touko Madobe":
    os.system("feh windows/10.png")

# MacOS-Tans

elif o == "MacOS 9-tan":
    os.system("feh macos/macos9.png")

elif o == "MacOS-tan":
    os.system("feh macos/macos.png")

# Unix-tan

elif o == "freebsd-tan":
    os.system("feh unix/freebsd.png")

elif o == "linux-tan":
    os.system("feh unix/linux.jpg")

elif o == "openbsd-tan":
    os.system("feh unix/openbsd.png")

