# TCP Web Server

This project implements a simple TCP web server in Python. It listens for incoming connections and processes client requests using defined handlers.

## Project Structure

```
tcp-web-server
├── src
│   ├── server.py          # Entry point of the TCP web server
└── README.md              # Project documentation
```

## Running the Server

2. Start the server:
   ```
   python src/server.py
   ```

3. The server will listen for incoming TCP connections. You can connect to it using a TCP client.

## Configuration

You may need to adjust the server settings in `src/server.py` to change the host and port on which the server listens.