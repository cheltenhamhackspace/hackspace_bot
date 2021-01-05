#!/usr/bin/env python3
from discord.ext import commands
from datetime import datetime as dt

class Hackspace(commands.Cog):
    """
    The Hackspace command wraps all info questions about the space.
    """
    def __init__(self, bot):
        """
        Takes bot object
        
        Args:
            bot (class)
        """
        self.bot = bot
     
    @commands.command()
    async def opennight(self, ctx):
        "Returns open-night information"
        response_text = f"""```Hey {ctx.author}!

The Hackspace is currently doing virtual open nights
on the first and third Thursday of every month at 7pm.

The jitsi chat link goes up 30min in advance on Twitter
and the WhatsApp group.

```"""
        await ctx.send(response_text)
