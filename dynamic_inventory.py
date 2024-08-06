#!/usr/bin/env python3
import json

inventory = {
    "all": {
        "hosts": {
            "ubuntu1": {
                "ansible_host": "10.1.3.51",
                "ansible_ssh_private_key_file": "/home/ubuntu/aws.pem",
                "ansible_user": "ubuntu"
            },
            "ubuntu2": {
                "ansible_host": "10.1.3.23",
                "ansible_ssh_private_key_file": "/home/ubuntu/aws.pem",
                "ansible_user": "ubuntu"
            },
            "ubuntu3": {
                "ansible_host": "10.1.3.138",
                "ansible_ssh_private_key_file": "/home/ubuntu/aws.pem",
                "ansible_user": "ubuntu"
            }
        }
    }
}

print(json.dumps(inventory, indent=2))
