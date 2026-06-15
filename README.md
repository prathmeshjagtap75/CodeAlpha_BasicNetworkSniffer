# CodeAlpha_BasicNetworkSniffer

## 📌 Project Overview
This repository contains a production-ready **Basic Network Sniffer** developed in Python using the `Scapy` packet manipulation library. Built as part of the **CodeAlpha Cybersecurity Internship**, this tool interfaces directly with network hardware to intercept, decode, and analyze live network traffic passing through the host system's interface card.

The sniffer dynamically parses data starting from the Network Layer (Layer 3) down through the Transport Layer (Layer 4), exposing crucial packet anatomy and protocol telemetry directly onto the console in real-time.

---

## 🛠️ Features & Technical Capabilities
* **Live Packet Capture:** Establishes a raw socket interface loop to intercept high-velocity network traffic on active local interfaces.
* **Multi-Protocol Dissection:** Programmatically detects and classifies fundamental internet protocols, including:
  * **IP** (Internet Protocol)
  * **TCP** (Transmission Control Protocol)
  * **UDP** (User Datagram Protocol)
  * **ICMP** (Internet Control Message Protocol / Ping)
* **Granular Telemetry Extraction:** Dissects packet headers to extract critical architectural endpoints:
  * Source & Destination IPv4 Addresses
  * Source & Destination Port Numbers (Application tracking)
  * Protocol Layer Identifiers
* **Deep Packet Inspection (DPI):** Isolates and displays raw binary and textual payloads moving within non-encrypted or truncated secure data frames.
* **Resource Optimization:** Engine utilizes zero-storage packet looping (`store=0`) to process data on-the-fly, completely preventing RAM exhaustion and memory leaks during continuous execution.

---

## 🧠 Skills & Domains Covered

### 🌐 1. Advanced Network Architecture & Protocol Dissection
* **OSI Model Mapping:** Hands-on operational experience routing data flows from Layer 3 up to Layer 4.
* **Network Telemetry Tracking:** Monitoring active system services and remote connections through localized port mapping (e.g., verifying encrypted HTTPS data on Port 443).

### 🛡️ 2. Penetration Testing & Defensive Security Mechanics
* **Promiscuous Mode Operations:** Leveraging low-level kernel packet capture drivers (**Npcap/WinPcap**) to audit local network segments.
* **Cryptographic Evaluation:** Analyzing how modern security protocols (TLS/HTTPS) protect user privacy by verifying how encryption successfully obfuscates plain-text payloads from network eavesdroppers.

### 🐍 3. Production-Level Python Software Engineering
* **Low-Level Socket Interfacing:** Utilizing the **Scapy** framework to manipulate underlying hardware communication sockets.
* **Asynchronous Event Handling:** Architecting event-driven execution loops that pass runtime objects to custom callback threads (`packet_callback`) seamlessly.

---

## ⚙️ Technical Stack
* **Language:** Python 3.x
* **Core Framework:** Scapy
* **Packet Capture Driver:** Npcap (WinPcap API-Compatible Mode)

---

## 🚀 Execution Guide

### Prerequisites
1. Ensure Python 3.x is installed.
2. Install the Scapy framework:
   ```bash
   pip install scapy
