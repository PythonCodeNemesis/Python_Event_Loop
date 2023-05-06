import asyncio

async def handle_request(reader, writer):
    request = (await reader.read()).decode('utf-8')
    print("Handling request")
    print(request)
    
    headers = (
        b'HTTP/1.1 200 OK\r\n'
        b'Content-Type: text/plain\r\n'
        b'Access-Control-Allow-Origin: *\r\n'
        b'Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS\r\n'
        b'Access-Control-Allow-Headers: Content-Type\r\n\r\n'
    )

    response = b'Hello, world!'
    writer.write(headers + response)
    await writer.drain()
    writer.close()
    print("done!")

async def main():
    server = await asyncio.start_server(handle_request, 'localhost', 8000)
    print(f'Server running on {server.sockets[0].getsockname()}')
    async with server:
        await server.serve_forever()

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
