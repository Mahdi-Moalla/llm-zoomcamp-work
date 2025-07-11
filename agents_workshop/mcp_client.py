from fastmcp import Client

import mcp_server
import asyncio

import json

async def main():
    async with Client(mcp_server.mcp) as mcp_client:
        tools = await mcp_client.list_tools()
        print(f"Available tools: {tools }")

        print("######################################################################")
        
        result = await mcp_client.call_tool("get_weather", {"city": "berlin"})
        print(f"Result: {result.structured_content }")



if __name__ == "__main__":
    test = asyncio.run(main())