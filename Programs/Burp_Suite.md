# Burp Suite

Burp Suite is an integrated platform for performing security testing of web applications. It's an essential tool for web application penetration testing.

## Installation
- Download from [PortSwigger](https://portswigger.net/burp/communitydownload)
- Free Community Edition is sufficient for most basic testing
- Requires Java Runtime Environment (JRE)

## Key Components

### 1. Proxy
- Intercepts HTTP/S traffic between browser and target application
- Allows inspection and modification of requests/responses
- Setup: Configure browser to use `127.0.0.1:8080` as proxy

### 2. Spider
- Crawls web applications to discover content
- Maps application structure
- Identifies hidden directories and endpoints

### 3. Repeater
- Manually modify and resend requests
- Test parameter variations
- Analyze server responses

### 4. Intruder
- Automated attack tool
- Useful for:
  - Fuzzing parameters
  - Brute force attacks
  - Testing for vulnerabilities
- Four attack types: Sniper, Battering ram, Pitchfork, Cluster bom

### Install Turbo intruder
- Good for parallell attempt when doing a brute-force attack
- Make sure to define what's "interesting"