#!/usr/bin/env python3
import json

inventory = {
    "all": {
        "hosts": ["debian_host"],
        "vars": {
            "ansible_user": "ubuntu"
        }
    },
    "_meta": {
        "hostvars": {
            "debian_host": {
                "ansible_host": "54.91.199.248",
                "ansible_ssh_private_key_file": "/home/ubuntu/aws.pem"
            }
        }
    }
}

print(json.dumps(inventory, indent=2))
