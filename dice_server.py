#!/usr/bin/env python3
"""Simple Dice MCP Server - Roll dice with configurable sides and quantities."""

import os
import sys
import logging
import random
from mcp.server.fastmcp import FastMCP

# Configure logging to stderr
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger("dice-server")

# Initialize MCP server - NO PROMPT PARAMETER!
mcp = FastMCP("dice")


# === MCP TOOLS ===

@mcp.tool()
async def roll_dice(sides: str = "6") -> str:
    """Roll a single dice with the specified number of sides (default: 6)."""
    logger.info(f"Rolling dice with sides={sides}")
    
    try:
        sides_int = int(sides.strip()) if sides.strip() else 6
        
        if sides_int < 2:
            return "❌ Error: Dice must have at least 2 sides"
        if sides_int > 1000:
            return "❌ Error: Maximum 1000 sides allowed"
        
        result = random.randint(1, sides_int)
        return f"🎲 Rolled a d{sides_int}: **{result}**"
    
    except ValueError:
        return f"❌ Error: Invalid sides value: {sides}"
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"❌ Error: {str(e)}"


@mcp.tool()
async def roll_multiple(count: str = "2", sides: str = "6") -> str:
    """Roll multiple dice at once and return individual results plus total."""
    logger.info(f"Rolling {count} dice with {sides} sides")
    
    try:
        count_int = int(count.strip()) if count.strip() else 2
        sides_int = int(sides.strip()) if sides.strip() else 6
        
        if count_int < 1:
            return "❌ Error: Must roll at least 1 die"
        if count_int > 100:
            return "❌ Error: Maximum 100 dice allowed"
        if sides_int < 2:
            return "❌ Error: Dice must have at least 2 sides"
        if sides_int > 1000:
            return "❌ Error: Maximum 1000 sides allowed"
        
        rolls = [random.randint(1, sides_int) for _ in range(count_int)]
        total = sum(rolls)
        rolls_str = ", ".join(str(r) for r in rolls)
        
        return f"🎲 Rolled {count_int}d{sides_int}: [{rolls_str}]\n📊 Total: **{total}**"
    
    except ValueError:
        return f"❌ Error: Invalid count or sides value"
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"❌ Error: {str(e)}"


@mcp.tool()
async def coin_flip() -> str:
    """Flip a coin and return heads or tails."""
    logger.info("Flipping coin")
    
    try:
        result = random.choice(["Heads", "Tails"])
        emoji = "🪙" if result == "Heads" else "🪙"
        return f"{emoji} Coin flip: **{result}**"
    
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"❌ Error: {str(e)}"


# === SERVER STARTUP ===

if __name__ == "__main__":
    logger.info("Starting Dice MCP server...")
    
    try:
        mcp.run(transport='stdio')
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)