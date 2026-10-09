# 🔥 Adaptive AI Socket Flooding Engine

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Socket Layer](https://img.shields.io/badge/socket-raw-red.svg)](https://man7.org/linux/man-pages/man7/socket.7.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

An advanced, high-concurrency low-level socket stressing core equipped with an **Epsilon-Greedy Multi-Armed Bandit heuristic loop**. Designed to dynamically mutate packet signatures, rotate evasion strategies on the fly, and punch through rate-limiter walls without breaking a sweat.

---

## 🚀 Core Features

* **Low-Level Socket Architecture:** Bypasses high-level HTTP abstractions entirely using raw TCP sockets with custom `TCP_NODELAY` flags.
* **AI-Driven Evasion Loop:** Implements real-time reward feedback adjustments to pick optimal payload mutation arms dynamically.
* **Dynamic Header Mutation:** Randomizes User-Agents, IP spoof headers, cache-bypass parameters, and chunked transfer encodings automatically.
* **Terminal Dashboard:** Real-time state monitoring tracking total operations, successful bypasses, blocked counts, and live adaptive strategy weights.

---

## ⚙️ Installation & Setup (Termux / Linux)

Clone or transfer the script into your working directory, then make sure dependencies are natively satisfied (uses Python standard library only for maximum portability).

# Update package repositories and install python if not present
pkg update && pkg install python -y
# Verify python installation
python3 --version

💻 Usage Instructions 

​Execute the script from your terminal providing the target IP, target port, and desired thread count:python3 ai_engine.py <target_ip> <port> <threads>

📊 Live Metrics & Strategy Weights 

​The engine renders a real-time terminal output displaying operational stats and current multi-armed bandit weights:



=== AI ADAPTIVE BYPASS ENGINE ===
Total Operations : 142580
Bypassed / Active: 139102
Blocked / Refused: 3478

Adaptive Strategy Weights:
 - random_cache_bypass     : 8.412
 - chunked_encoding_spoof  : 6.204
 - user_agent_rotation     : 7.915
 - pipeline_flooding       : 9.241

