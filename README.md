# Path Tracing Tool using SDN (Mininet + POX)

## 👨‍💻 Author

Name: Adarsh Rajesh

SRN: PES1UG24CS020

Course: Computer Networks

University: PES University

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

screenshots:

1. Controller running
<img width="940" height="336" alt="image" src="https://github.com/user-attachments/assets/e4938ad6-7c0d-4179-a525-1e120ffbf646" />

2. Cleanup And Network topology 
<img width="940" height="329" alt="image" src="https://github.com/user-attachments/assets/0410685c-02d2-4096-8373-5df7bf7a5da9" />
<img width="940" height="283" alt="image" src="https://github.com/user-attachments/assets/73272719-2bdf-477f-b281-ff1df9bdc19d" />


3. Successful ping
<img width="653" height="223" alt="image" src="https://github.com/user-attachments/assets/54f55ff7-258a-4f6c-9899-90fae398b334" />

4. Path tracing logs
<img width="940" height="765" alt="image" src="https://github.com/user-attachments/assets/d3286370-1be8-4e40-8879-bc68382554c5" />
<img width="940" height="726" alt="image" src="https://github.com/user-attachments/assets/5604abee-f103-4bf8-95b2-e3225320cf62" />


5. Latency output
<img width="457" height="54" alt="image" src="https://github.com/user-attachments/assets/2f2daf6c-d8f9-453d-b047-ee70d8f4df51" />

6. Throughput (iperf)
<img width="822" height="153" alt="image" src="https://github.com/user-attachments/assets/65ad535b-acd7-4b58-91f3-41b6345ac931" />

7. Flow table
<img width="940" height="211" alt="image" src="https://github.com/user-attachments/assets/4bfbe76e-896f-4cf7-beef-316f65ab0e07" />

8. Blocked traffic case
<img width="817" height="342" alt="image" src="https://github.com/user-attachments/assets/d0adeefa-d7ce-482e-af02-f5e908f0acad" />
<img width="940" height="222" alt="image" src="https://github.com/user-attachments/assets/a7aa0ea4-c472-4982-b82a-2b1b0d94f78c" />


9. Wireshark Capture
<img width="1654" height="602" alt="image" src="https://github.com/user-attachments/assets/2735b4bd-23c2-4403-943e-3b6514dccb24" />
We can see the ARP protocol in work. Ping Request and Reply Packets.


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



---
