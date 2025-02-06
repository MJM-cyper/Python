# TCP Web Server

This project implements a simple TCP web server in Python. It listens for incoming connections and processes client requests using defined handlers.

## Project Structure

```
tcp-web-server
├── src
│   ├── server.py          # Entry point of the TCP web server
│   └── handlers
│       └── __init__.py    # Contains request handler functions
├── requirements.txt       # Lists project dependencies
└── README.md              # Project documentation
```

## Requirements

To run this project, you need to install the required dependencies listed in `requirements.txt`.

## Running the Server

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Start the server:
   ```
   python src/server.py
   ```

3. The server will listen for incoming TCP connections. You can connect to it using a TCP client.

## Configuration

You may need to adjust the server settings in `src/server.py` to change the host and port on which the server listens.