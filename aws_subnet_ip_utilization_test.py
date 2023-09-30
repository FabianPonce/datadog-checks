import unittest
import aws_subnet_ip_utilization

class TestAWSSubnetIPUtilization(unittest.TestCase):
    def test_subnet_size(self):
        self.assertEqual(aws_subnet_ip_utilization.subnet_size("10.0.0.0/24"), 256)
        self.assertEqual(aws_subnet_ip_utilization.subnet_size("10.0.0.0/8"), 16777216)

if __name__ == '__main__':
    unittest.main()
