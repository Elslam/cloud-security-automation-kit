import copy

# 1. THE RAW LOGS
# This is the messy data we got from the servers. 
# We have to be careful of the sneaky spacing and mixed caps.
master_config = [
    ["admin_panel", ("HTTPS", "443")],
    ["user_login",  ("HTTP ", "80")],      # <-- Threat 1 (sneaky space)
    ["ssh_gateway", ("ssh", "22")],
    ["backdoor_vln", ("http", "8080")],    # <-- Threat 2 (lowercase)
    ["file_transfer", ("FTP", "21")]
]

# 2. LOCKING DOWN THE MEMORY (No Aliasing Allowed)
# If we used '=' or '.copy()', the inner tuples would still share the same memory IDs.
# If a hacker messed with our test data, it would corrupt production. Bad news.
# copy.deepcopy() completely isolates the data in RAM so master_config is 100% safe.
secure_test_config = copy.deepcopy(master_config)

# 3. THE UNPACKING & CLEANUP FILTER
# We're matching the exact layout of our data: [label, (proto, port)].
# We run .strip().lower() inside the 'if' condition so spaces and caps can't sneak past.
# If it's a match, we pull ONLY the port number to the very front of the list.
flagged_ports = [port for label, (proto, port) in secure_test_config if proto.strip().lower() == "http"]

# 4. SEND IT TO THE FIREWALL
# This gives us the exact target ports we need to block at the network edge.
print(f"Actionable Firewall Targets Identified: {flagged_ports}")
# Output: ['80', '8080']
