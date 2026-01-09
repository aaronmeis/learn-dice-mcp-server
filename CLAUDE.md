# Dice MCP Server - Implementation Guide

## Overview

This is a simple MCP server that provides dice rolling functionality. It uses Python's `random` module for generating random numbers.

## Tools Available

| Tool | Parameters | Description |
|------|------------|-------------|
| `roll_dice` | `sides` (default: "6") | Roll a single die |
| `roll_multiple` | `count` (default: "2"), `sides` (default: "6") | Roll multiple dice |
| `coin_flip` | None | Flip a coin |

## Code Guidelines

- All parameters are strings with empty string defaults
- All tools return formatted strings
- Single-line docstrings only
- Error handling in every tool

## Common Dice Notation

- d4 = 4-sided die
- d6 = 6-sided die (standard)
- d8 = 8-sided die
- d10 = 10-sided die
- d12 = 12-sided die
- d20 = 20-sided die (common in D&D)
- d100 = 100-sided die (percentile)

## Rebuild Commands
```bash
docker build -t dice-mcp-server .
```