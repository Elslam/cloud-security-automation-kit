"""
CloudTrail Threat Parser
Author: yagizcan_simsir
Description: Minimalist forensic script running a high-performance 
             dictionary comprehension to isolate compromised accounts.
"""

# The raw security intelligence stream (SIEM simulation)
cloudtrail_stream = [
    [
        "evt_001", 
        ("us-east-1", "12345"), 
        ["admin_jack", "Owner", "192.168.1.10"], 
        {"action": "CreateUser", "severity": 9, "impact_score": 95}
    ],
    [
        "evt_002", 
        ("eu-west-1", "12345"), 
        ["sec_engine_alex", "Analyst", "10.0.0.5"], 
        {"action": "DescribeInstances", "severity": 1, "impact_score": 5}
    ],
    [
        "evt_003", 
        ("us-east-1", "12345"), 
        ["admin_jack", "Owner", "192.168.1.10"], 
        {"action": "StopLogging", "severity": 10, "impact_score": 100}
    ],
    [
        "evt_004", 
        ("us-west-2", "67890"), 
        ["dev_billy", "Developer", "172.16.0.4"], 
        {"action": "RunInstances", "severity": 8, "impact_score": 88}
    ]
]

urgent = {
    name: (payload["action"], server) 
    for event, (server, data), [name, title, ip], payload in cloudtrail_stream 
    if payload["impact_score"] > 90
}

# Output the final isolated attack surface map
print(urgent)
