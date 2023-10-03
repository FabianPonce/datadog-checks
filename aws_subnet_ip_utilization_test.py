import unittest
from unittest.mock import Mock
import aws_subnet_ip_utilization


class TestAWSSubnetIPUtilization(unittest.TestCase):
    def test_subnet_size(self):
        self.assertEqual(aws_subnet_ip_utilization.subnet_size("10.0.0.0/24"), 256)
        self.assertEqual(aws_subnet_ip_utilization.subnet_size("10.0.0.0/8"), 16777216)

    def test_subnet_tags(self):
        # empty tags on subnet should return empty list
        emptytags = Mock()
        emptytags.tags = None        
        self.assertEqual(aws_subnet_ip_utilization.subnet_aws_tags(emptytags), [])

if __name__ == '__main__':
    unittest.main()
