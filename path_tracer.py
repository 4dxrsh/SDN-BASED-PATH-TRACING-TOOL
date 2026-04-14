from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet.ipv4 import ipv4
log = core.getLogger()

mac_to_port = {}

def _handle_PacketIn(event):
    packet = event.parsed
    dpid = event.connection.dpid

    src = packet.src
    dst = packet.dst
    # 🔴 BLOCK h1 USING IP (FINAL FIX)
    ip_packet = packet.find('ipv4')

#UNCOMMENT THIS BLOCK FOR THE BLOCKING VERSION
    #if ip_packet and ip_packet.srcip == "10.0.0.1":
    	#log.info("Blocked traffic from h1")

    	#msg = of.ofp_packet_out()
    	#msg.data = event.ofp
    	#msg.in_port = event.port
    	#msg.actions = []   # DROP
    	#event.connection.send(msg)

    	#return

    # Normal learning switch logic
    if dpid not in mac_to_port:
        mac_to_port[dpid] = {}

    mac_to_port[dpid][src] = event.port

    log.info(f"Packet at switch s{dpid}: {src} -> {dst}")
    log.info(f"Path Trace: Host {src} → s{dpid}")

    if dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][dst]
    else:
        out_port = of.OFPP_FLOOD

    # Install flow rule ONLY for allowed traffic
    msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet, event.port)
    msg.actions.append(of.ofp_action_output(port=out_port))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Path Tracing Controller Started 🚀")
