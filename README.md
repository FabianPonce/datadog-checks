# custom datadog checks

## aws subnet ip utilization
* `aws.ec2.subnet.available_addresses`: number of ips free
* `aws.ec2.subnet.total_addresses`: maximum # of ips in subnet

these metrics have their id tagged under the key `subnet`. 
they also inherit the aws tags of the individual subnet measured.