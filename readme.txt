### File 4: readme.txt
```
# Dice MCP Server

A Model Context Protocol (MCP) server that provides dice rolling and coin flipping functionality for AI assistants.

## Purpose

This MCP server provides a fun interface for AI assistants to roll dice and flip coins with customizable options.

## Features

### Current Implementation

- **`roll_dice`** - Roll a single die with configurable sides (default: 6-sided)
- **`roll_multiple`** - Roll multiple dice at once and get individual results plus total
- **`coin_flip`** - Flip a coin for heads or tails

## Prerequisites

- Docker Desktop with MCP Toolkit enabled
- Docker MCP CLI plugin (`docker mcp` command)

## Installation

See the step-by-step instructions provided with the files.

## Usage Examples

In Claude Desktop, you can ask:

- "Roll a dice"
- "Roll a d20"
- "Roll 4 six-sided dice"
- "Roll 2d8"
- "Flip a coin"
- "I need to roll for initiative - roll a d20 for me"

## Architecture

Claude Desktop → MCP Gateway → Dice MCP Server
                                    ↓
                              Random Number Generator

## Development

### Local Testing
```bash
# Run directly
python dice_server.py

# Test MCP protocol
echo '{"jsonrpc":"2.0","method":"tools/list","id":1}' | python dice_server.py
```

### Adding New Tools

1. Add the function to dice_server.py
2. Decorate with @mcp.tool()
3. Update the catalog entry with the new tool name
4. Rebuild the Docker image

## Troubleshooting

### Tools Not Appearing

- Verify Docker image built successfully
- Check catalog and registry files
- Ensure Claude Desktop config includes custom catalog
- Restart Claude Desktop

## Security Considerations

- Running as non-root user
- No external API calls
- No sensitive data handling

## License

MIT License