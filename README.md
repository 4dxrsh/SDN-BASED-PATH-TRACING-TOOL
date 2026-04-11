# Path Tracing Tool using SDN (Mininet + POX)

## 📌 Project Overview

This project implements a Software Defined Networking (SDN)-based path tracing tool using Mininet and the POX controller. The controller monitors packet flow in the network, logs the path taken by packets, and enforces simple policies such as blocking traffic from specific hosts.

---

## 🎯 Objectives

* Simulate a network using Mininet
* Implement a custom SDN controller using POX
* Track and display packet paths
* Apply flow rules using OpenFlow
* Measure performance (latency & throughput)
* Validate behavior using test cases

---

## 🛠️ Technologies Used

* Mininet (Network Emulator)
* POX Controller (Python-based SDN controller)
* OpenFlow Protocol (v1.0)
* Ubuntu Linux (VM)

---

## 🏗️ Network Topology

Simple topology with:

* 2 Hosts: h1, h2
* 1 Switch: s1

```
h1 ---- s1 ---- h2
```

---

## ⚙️ Implementation Details

### 1. Controller Logic

The controller performs:

* MAC learning
* Packet forwarding
* Path tracing (logs packet movement)
* Flow rule installation
* Traffic blocking based on IP

### 2. Path Tracing

Logs are generated for each packet:

```
Packet at switch s1: <src_mac> -> <dst_mac>
Path Trace: Host <src_mac> → s1
```

### 3. Flow Rules

Flow rules are installed using OpenFlow:

* Matches packet fields
* Defines forwarding action
* Reduces controller load

---

## 🧪 Test Cases

### ✅ Test Case 1: Normal Communication

* Command: `h1 ping h2`
* Result: Successful communication (0% packet loss)

### ❌ Test Case 2: Blocked Traffic

* Condition: Traffic from h1 (IP: 10.0.0.1) blocked
* Result: No response (packets dropped)
* Controller Log:

```
Blocked traffic from h1
```

---

## 📊 Performance Analysis

### 1. Latency

Measured using ping:

* Average latency observed: few milliseconds

### 2. Throughput

Measured using iperf:

* Output in Mbps indicating bandwidth

---

## 📋 Flow Table Verification

Flow entries observed using:

```
sudo ovs-ofctl dump-flows s1
```

This confirms:

* OpenFlow rules are installed correctly
* Switch forwards packets based on rules

---

## 📸 Proof of Execution

Include the following screenshots:

1. Controller running
2. Network topology
3. Successful ping
4. Path tracing logs
5. Latency output
6. Throughput (iperf)
7. Flow table
8. Blocked traffic case

---

## 🧠 Key Concepts Used

* Software Defined Networking (SDN)
* Control Plane vs Data Plane
* OpenFlow Protocol
* Packet-In events
* Flow table management

---

## 🚀 Conclusion

This project demonstrates how SDN enables centralized control of network behavior. The controller successfully tracks packet paths, enforces policies, and manages flow rules dynamically.

---

## 📚 Future Improvements

* Multi-switch topology support
* GUI visualization of paths
* Dynamic policy updates
* Integration with Ryu controller

---

## 👨‍💻 Author

Name: [Your Name]
Course: Computer Networks
University: PES University

---
