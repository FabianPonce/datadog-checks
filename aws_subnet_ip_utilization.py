try:
    from datadog_checks.base import AgentCheck
except ImportError:
    # agent version < 6.6.0
    from checks import AgentCheck

import boto3
import math

# calculate total addresses in an ipv4 subnet
def subnet_size(block: str) -> int:
    cidr_size = int(block[block.find('/')+1:])
    return math.pow(2, 32-cidr_size)

def tag_value(s: str) -> str:
    s = s.lower()
    s = s.replace(" ", "_")
    s = s.replace(":", "_")
    return s

def subnet_aws_tags(subnet):
        if subnet.tags is None:
            return []
        else:
            return [ f"{tag_value(d['Key'])}:{tag_value(d['Value'])}" for d in subnet.tags ]

class AWSSubnetIPUtilizationCheck(AgentCheck):
    def __init__(self, name, init_config, agentConfig, instances=None):
        super(AWSSubnetIPUtilizationCheck, self).__init__(name, init_config, agentConfig, instances)
        self.client = boto3.resource('ec2')      

    def check(self, instance):
        for subnet in self.client.subnets.all():
            if subnet.ipv6_native:
                continue

            remaining = subnet.available_ip_address_count
            total = subnet_size(subnet.cidr_block)

            tags = [f"subnet:{subnet.id}"] + subnet_aws_tags(subnet) + self.instance.get('tags', [])

            self.gauge('aws.ec2.subnet.available_addresses', remaining, tags=tags)
            self.gauge('aws.ec2.subnet.total_addresses', total, tags=tags)