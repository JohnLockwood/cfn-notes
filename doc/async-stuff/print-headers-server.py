# My code, but based on print-headers.py, an asyncio example (q.v.)
# As well as https://medium.com/@pgjones/an-asyncio-socket-tutorial-5e6f3308b8b0

import asyncio

# Just print the
async def client_connected(reader, writer):
    while True:
        line = await reader.readline()
        if not line:
            break

        line = line.decode('latin1').rstrip()
        if line:
            print(f'HTTP header> {line}')
    writer.close()


async def print_http_headers():
    server = await asyncio.start_server(client_connected, host="127.0.0.1", port=8888)
    await server.serve_forever()


asyncio.run(print_http_headers())