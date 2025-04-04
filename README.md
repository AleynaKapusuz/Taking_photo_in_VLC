# 📸 VLC RTSP Snapshot Script

This Python script launches VLC Media Player in Remote Control (RC) mode and automatically captures snapshots from an RTSP (Real-Time Streaming Protocol) stream at specified time intervals. The script starts VLC in a remotely controllable mode, sends commands via a telnet connection, and saves snapshots at regular intervals. This allows you to capture real-time images from an RTSP stream without any manual intervention and automatically save them to a specified directory.

📌 Requirements
VLC Media Player (must be installed)

Python 3.x

Telnetlib (included with Python)

🚀 Usage
Ensure that VLC is installed.

Update the vlc_path variable with the installation path of VLC.

Set the rtsp_url variable to your RTSP stream address.

Specify the screenshot_path where the snapshots will be saved.

The script captures a snapshot every 2 seconds. To stop it, press CTRL + C.

🛠 To-Do List
📌 Implement an automatic file naming system

📌 Handle RTSP connection errors

📌 Save snapshots in a specific format


The output of the python code is as follows :
![Image](https://github.com/user-attachments/assets/d747914e-3b7e-49af-87b5-83499f53ac76)
