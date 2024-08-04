#!/usr/bin/env python3
import json

inventory = {
    "all": {
        "hosts": {
            "debian_host": {
                "ansible_host": "54.91.199.248",
                "ansible_ssh_private_key_file": "/home/ubuntu/aws.pem",
                "ansible_user": "ubuntu"
            }
        }
    }
}

print(json.dumps(inventory, indent=2))
