#!/usr/bin/python

import argparse
import atexit
import signal
from time import sleep

from toolkit import stat, verbo
import globals
from webs import *
import mopidy

parser = argparse.ArgumentParser(description="Flex FM Radio Automation Backend")
parser.add_argument('--soundcard',  type=int, dest="card", help="Which sound card to use", choices=[0, 1], default=1);
parser.add_argument('--playlist', type=str, help="Spotify playlist to use (uri)", default="spotify:user:superconductor42:playlist:27Jbqg9tqkI9K8p8deNdu1")
parser.add_argument("--listen-port", dest="lport", type=int, help="Port for the websocket server to listen on.", default=8000)
parser.add_argument("--mopidy-port", dest="mport", type=int, help="Port for connecting to the MPD WebSocket API", default=6680)
parser.add_argument("--mopidy-host", dest="mhost", type=str, help="The Mopidy (MPD) host. Usually localhost.", default="localhost")
parser.add_argument('--cert', type=str, help="SSL/TLS Certificate file", default="/etc/letsencrypt/live/www.flexfm.org/fullchain.pem")
parser.add_argument("--key", type=str, help="SSL/TLS key file", default="/etc/letsencrypt/live/www.flexfm.org/privkey.pem")
parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", help="Be verbose")
parser.add_argument("-d", "--debug", dest="debug", action="store_true", help="Debug mode")
parser.add_argument("-e", "--existing", dest="existing", action="store_true", help="Don't start mopidy, run on an existing mopidy process")
args = parser.parse_args()
globals.args = args

def exit_handler():
    stat("Will now exit")
    if (globals.args.existing == False):
        mopidy.stop_music_server()

atexit.register(exit_handler)

if (globals.args.existing == False):
    verbo("Calling for start of mopidy")
    mopidy.start_music_server()
    verbo("Call completed")
verbo("Calling for start of WebSocket server")
server.start_websocket_server(args.cert, args.key, args.lport)
verbo("Call completed")
verbo("Calling for start of websocket client")
verbo("Root will now hand off control to websocket client.")
client.start_websocket_client(args.mhost, args.mport)
verbo("Call completed")
