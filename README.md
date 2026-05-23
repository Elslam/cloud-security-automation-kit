# Cloud Security Automation Toolkit 🛡️

Hello there! This repo is my personal sandbox where I’m building out production-ready Python tools to automate threat detection and clean up messy network logs.

Instead of just writing basic scripts, I'm focusing heavily on writing secure code that blocks hacker evasion tricks and keeps cloud data safe in memory.

---

## 📁 What's Inside
* **network-log-parsers/**
  * `threat_parser.py`: Slices through massive, multi-layered cloud JSON logs at rapid speed using memory-optimized comprehensions to catch malicious actors during an incident response.
  * `http_threat_extractor.py`: Keeps production data safe in RAM using deep memory copying, splits open nested tuples, and strips out hidden spaces/caps to hunt down unencrypted web traffic.
  * `endpoint_cleaner.py`: Takes raw, messy URL strings, slices away unwanted subdomains/parameters, and flags unencrypted endpoints so they can be audited.

---

## 🚀 The Featured Tools

### 1. CloudTrail Incident Response Threat Parser ('threat_parser.py')
#### The Problem
During an active cyber attack on cloud infrastructure, security operations teams are hit with a tidal wave of massive, heavily nested JSON log streams (like AWS CloudTrail or Azure Activity logs). Standard loops ('for' loops inside 'for' loops) are incredibly slow and can hog system memory, delaying critical incident response times when every second counts. Furthermore, pulling target IP addresses or usernames out of deeply buried metadata arrays can be a total headache.

#### How I Fixed It
The `threat_parser.py` utility solves this bottleneck with an optimized, elite data pipeline:
* **Memory-Optimized Speed:** Built entirely using a highly efficient dictionary comprehension, bypassing clunky, multi-layered nested loops to parse massive streams instantly.
* **Deep Structural Unpacking:** Uses advanced Python unpacking to dive straight through mixed arrays, tuples, lists, and metadata blocks all at once, extracting actionable threat intel in a single pass.

### 2. HTTP Threat Extractor ('http_threat_extractor.py')
#### The Problem
Attackers love using tricks like adding extra spaces ("HTTP ") or mixing up capitalization ("hTtP") to slip right past lazy security rules. On top of that, if you mess with nested data configurations in a big cloud app using standard Python copies ('=' or '.copy()'), you can accidentally overwrite or leak your real production settings due to memory aliasing.

#### How I Fixed It
The 'http_threat_extractor.py' script shuts that down using two defense-in-depth moves:
* **Memory Isolation:** Uses 'copy.deepcopy()' to clone nested configs into fresh, isolated sandboxes in memory. No production data corruption allowed.
* **Anti-Evasion Gate:** Uses a single-line list comprehension to unpack raw data on the go while forcing '.strip().lower()' onto the protocols so hackers can't sneak past.

### 3. Endpoint Security Auditor ('endpoint_cleaner.py')
#### The Problem
When you pull raw API endpoints or URL logs from a cloud application, they are usually a total mess. They come packed with random subdomains, tracking parameters, and messy formatting. If you just try to run a basic string match on raw URLs, you’ll miss dangerous patterns, or worse, your automation will break entirely because the data isn't standardized.

#### How I Fixed It
The 'endpoint_cleaner.py' script cleans up the noise and isolates the real risk using two main techniques:
* **String Slicing & Sanitization:** Uses Python’s string manipulation methods to slice away useless parameters, strip out bad formatting, and isolate the core URL domain.
* **Security Flagging Stream:** Once the URLs are perfectly uniform, the script automatically parses the protocol header to flag any unencrypted, raw http traffic trying to talk to our cloud APIs.

---
