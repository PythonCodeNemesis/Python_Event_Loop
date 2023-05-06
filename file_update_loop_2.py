import asyncio
import aiofiles

# Define an async function to write data to a file
async def write_to_file(filename, data):
    # Open the file for writing using async with, which ensures the file is closed
    # when we're done with it
    async with aiofiles.open(filename, 'w') as f:
        # Write the data to the file using the await keyword
        await f.write(data)

# Define an async function to read data from a file
async def read_from_file(filename):
    # Open the file for reading using async with, which ensures the file is closed
    # when we're done with it
    async with aiofiles.open(filename, 'r') as f:
        # Read the contents of the file using the await keyword
        data = await f.read()
        # Return the data as a string
        return data

# Define the main coroutine, which will run when we execute the script
async def main():
    # Set up a filename and some data to write to the file
    filename = 'example.txt'
    data = 'Hello, world!'

    # Create tasks to write and read the file concurrently
    write_task = asyncio.create_task(write_to_file(filename, data))
    read_task = asyncio.create_task(read_from_file(filename))

    # Wait for both tasks to complete
    await asyncio.gather(write_task, read_task)

    # Print the contents of the file to the console
    print(read_task.result())

# Run the main coroutine using asyncio.run, which creates and manages the event loop
if __name__ == '__main__':
    asyncio.run(main())
