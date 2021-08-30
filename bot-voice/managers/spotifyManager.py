import sys
sys.path.append(sys.path[0] + "/..")
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import talkBot as talk

device = "eadee7bd33e90ea24b0173baef7140db2999ef6a"
deviceNOTETrabajo = "eadee7bd33e90ea24b0173baef7140db2999ef6a"
deviceCeluNao = "add0b31febd5f331912ba458a79f7d1484694217"


def spotifyAction(scopeAction, action, query=""):
    global device
    cid = '8ac30afb6fe3457db697712e48804337'
    secret = '4c071e2c7179449b983882f6b0f69ae6'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,
                                                   client_secret=secret,
                                                   redirect_uri="http://localhost:2020",
                                                   scope=scopeAction))
    query = query.lstrip().rstrip()
    if action == "start":
        sp.start_playback(device_id=device)
    elif action == "stop":
        sp.pause_playback(device_id=device)
    elif action == "next":
        sp.next_track(device_id=device)
    elif action == "search":
        spAux = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,
                                                          client_secret=secret,
                                                          redirect_uri="http://localhost:2020",
                                                          scope="user-read-private"))
        search = spAux.search(q=query, type="playlist")
        idPlayList = search["playlists"]["items"][0]["id"]
        stringFullUri = "spotify:playlist:"+str(idPlayList)
        #talkBot("Reproduciendo "+query)
        sp.start_playback(device_id=device, context_uri=stringFullUri)
    elif action == "devices":
        devices = sp.devices()
        print(devices)
    elif action == "change":
        sp.transfer_playback(device_id=device, force_play=True)

def spotifyController(option , query):
    if(option == "buscar"):
        spotifyAction("user-modify-playback-state", "search", query)
        talk.talkBot("Reproduciendo en spotify a "+query)
    elif(option == "iniciar"):
        spotifyAction("user-modify-playback-state", "start")
        talk.talkBot("Reproduciendo en spotify a "+query)
    elif(option == "pausar"):
        spotifyAction("user-modify-playback-state", "stop")
    elif(option == "siguiente"):
        spotifyAction("user-modify-playback-state", "next")