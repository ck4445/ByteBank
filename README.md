# ByteBank

ByteBank is a Scratch-based project that implements a virtual currency with no real world value. You can interact with the project here: [ByteBank on Scratch](https://scratch.mit.edu/projects/1026899140/).

## Versioning

The version scheme uses three numbers:

1. **Major** – breaking changes that may require replacing your scripts completely.
2. **Client** – updates for the Scratch project. Update your Scratch client.
3. **Scripts** – updates for the Python helper scripts.

## Installation

The project currently supports Raspberry Pi and Windows. Instructions for other platforms will be added in the future.

### Required Python Modules

- `py7zr`
- `numpy`
- `scratchattach==1.4.7`

The modules `smtplib`, `re`, and `heapq` are included with Python and do not need to be installed separately.

### Setup on Raspberry Pi

1. Create a virtual environment and install the required modules.
2. Configure `crontab` to run the maintenance scripts:

   ```cron
   0 0 * * * /home/pi/bytebank/bin/python3.11 /home/pi/Python_Projects/ByteBank/auto_sort.py && /home/pi/bytebank/bin/python3.11 /home/pi/Python_Projects/ByteBank/backups/Main_Scripts.py
   ```
3. Set up the cloud request service for automatic start:

   ```bash
   sudo nano /etc/systemd/system/cloud_requests.service
   ```

   Paste the following configuration:

   ```ini
   [Unit]
   Description=Cloud Requests Script
   After=network-online.target
   Wants=network-online.target

   [Service]
   ExecStart=/home/pi/bytebank/bin/python3.11 /home/pi/Python_Projects/ByteBank/cloud_requests.py
   WorkingDirectory=/home/pi/Python_Projects/ByteBank/
   StandardOutput=append:/home/pi/cloud_requests.log
   StandardError=append:/home/pi/cloud_requests.err
   Restart=on-failure
   RestartSec=10
   User=pi

   [Install]
   WantedBy=multi-user.target
   ```

   Save and close, then enable the service:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable cloud_requests.service
   sudo systemctl start cloud_requests.service
   ```

### Setup on Windows

1. Install **Python 3.11** from [python.org](https://www.python.org/downloads/windows/) and ensure it is added to your `PATH`.
2. Open **Command Prompt** or **PowerShell** and navigate to the project directory.
3. Create and activate a virtual environment:

   ```powershell
   python -m venv env
   .\env\Scripts\activate
   ```
4. Install the required modules:

   ```powershell
   pip install py7zr numpy scratchattach==1.4.7
   ```
5. Run the main script:

   ```powershell
   python ByteBank/main.py
   ```

## Notes

Documentation will continue to improve over time.
