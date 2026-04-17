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

    # =========================
    # 🔴 BLOCKING LOGIC (COMMENTED FOR DEMO)
    # =========================
    ip_packet = packet.find('ipv4')

    # Uncomment this block to enable blocking
    # if ip_packet and ip_packet.srcip == "10.0.0.1":
    #     log.info("Blocked traffic from h1")
    #
    #     msg = of.ofp_packet_out()
    #     msg.data = event.ofp
    #     msg.in_port = event.port
    #     msg.actions = []   # DROP PACKET
    #     event.connection.send(msg)
    #
    #     return

    # =========================
    # 🟢 NORMAL LEARNING SWITCH LOGIC
    # =========================
    if dpid not in mac_to_port:
        mac_to_port[dpid] = {}

    # Learn source MAC → port
    mac_to_port[dpid][src] = event.port

    # Logging (Path Tracing)
    log.info(f"Packet at switch s{dpid}: {src} -> {dst}")
    log.info(f"Path Trace: Host {src} → s{dpid}")

    # Decide output port
    if dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][dst]
    else:
        out_port = of.OFPP_FLOOD

    # =========================
    # 🔥 STEP 1: FORWARD CURRENT PACKET
    # =========================
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.in_port = event.port
    msg.actions.append(of.ofp_action_output(port=out_port))
    event.connection.send(msg)

    # =========================
    # 🔥 STEP 2: INSTALL FLOW RULE
    # =========================
    flow_mod = of.ofp_flow_mod()
    flow_mod.match = of.ofp_match.from_packet(packet, event.port)
    flow_mod.actions.append(of.ofp_action_output(port=out_port))
    event.connection.send(flow_mod)


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Path Tracing Controller Started 🚀")
