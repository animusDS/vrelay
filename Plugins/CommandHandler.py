
from Plugins.AutoNexus import AutoNexus
from Plugins.DamageBoost import DamageBoost
from Plugins.Godmode import Godmode
from Plugins.NoDebuff import NoDebuff
from Plugins.NoProjectile import NoProjectile
from Plugins.Panic import Panic
from Plugins.PluginInterface import PluginInterface
from Plugins.Speedy import Speedy
from Plugins.Swiftness import Swiftness
from Plugins.TQ import TQ
from valorlib.Packets.Packet import *
from client import Client


class CommandHandler(PluginInterface):

    hooks = {PacketTypes.PlayerText}
    load = True  # always true because why wouldn't you want to activate them
    defaultState = True

    # add your own plugins / remove the ones you don't have
    plugins = {"an": AutoNexus, "db": DamageBoost, "gm": Godmode, "nb": NoDebuff,
               "np": NoProjectile, "pn": Panic, "sp": Speedy, "sw": Swiftness, "tq": TQ}

    def getAuthor(self) -> str:
        return "animus"

    def onPlayerText(self, client: Client, packet: PlayerText, send: bool) -> (PlayerText, bool):
        if packet.text[0:1] == "/" and packet.text[1:3] in self.plugins:
            p = self.plugins[packet.text[1:3]]
            p.defaultState = not p.defaultState
            client.createNotification(
                "CommandHandler", "Set to {}".format(p.defaultState))
            send = False
        elif packet.text[0:1] == "/help":
            client.createNotification(
                "CommandHandler", "Use the following command '/an' (AutoNexus), '/db' (DamageBoost), '/gm' (GodMode), '/nb' (NoDebuff), '/np' (NoProjectile), '/pn' (Panic), '/sp' (Speedy), '/sw' (Swiftness),")
            send = False
        return (packet, send)
