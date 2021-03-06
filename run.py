#!/usr/bin/env python3
"bot.py"

import argparse
import logging
import sys
import hackspacebot.bot as hack_bot
import hackspacebot.cogs as cogs

def import_token():
    """
    Attempts to to get the discord token from auth file then env variable
    
    Returns:
        (string)
    """
    try:
        import auth
        return auth.DISCORD_HACKSPACE_TOKEN
    except ImportError:
        try:
            import os
            return os.environ["DISCORD_HACKSPACE_TOKEN"]
        except KeyError:
            print("""
ERROR: DISCORD_HACKSPACE_TOKEN neither provided by auth file or environmental variable!"
"""
            )
            
            sys.exit()

# logging file location
LOG_LOC = "/tmp/qbot.log"

# Quarantine date time example const
Q_START = "05/11/2020 00:01:00"

def setup_arguments():
    """
    Sets up command line arguments to allow for debug and optional log file
    location
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--debug", 
        action="store_true", 
        help="Sets debug mode"
        ) 
    parser.add_argument(
        "-f",
        "--filename",
        action="store",
        type=str,
        default=LOG_LOC,
        help="Location where the log file will be located"
        )
    return parser.parse_args()


def setup_logging(debug, file_name):
    "Sets defaults for logging."
    log_format = '%(asctime)s - %(message)s'
    if debug:
        severity = logging.DEBUG
    else:
        severity = logging.INFO
    logging.basicConfig(format=log_format, level=severity, filename=file_name)
     

if __name__  == "__main__":    
    args = setup_arguments()
    setup_logging(args.debug, args.filename)
    TOKEN = import_token()
    hack_bot.bot.add_cog(cogs.Hackspace(hack_bot))
    hack_bot.bot.run(TOKEN)
