from utils import find_common_subnet

def test(ip_addresses, expected_status, expected_result):
    status, value = find_common_subnet(ip_addresses)
    
    assert status == expected_status, f"Expected: {expected_status} | Actual: {status}"
    assert value == expected_result, f"Expected: {expected_result} | Actual: {value}"    
# Duplicated scenario
ip_addresses = [
    '192.168.1.1',
    '192.168.1.1',
    '192.168.1.1',
] # 192.168.1.1/32
test(ip_addresses, True, '192.168.1.1/32')

# Same host scenario
ip_addresses = [
    '192.168.1.1',
    '192.168.1.5',
    '192.168.1.254',
] # 192.168.1.0/24
test(ip_addresses, True, '192.168.1.0/24')

# Different host scenario
ip_addresses = [
    '192.168.1.1',
    '192.168.1.10',
    '192.168.2.254',
    '192.168.3.46',
] # 192.168.0.0/16
test(ip_addresses, True, '192.168.0.0/16')

# Different network scenario
ip_addresses = [
    '192.168.1.1',
    '192.100.5.50',
] # 192.0.0.0/8
test(ip_addresses, True, '192.0.0.0/8')

# Different network scenario 2
ip_addresses = [
    '10.1.0.1',
    '192.100.1.1',
    '1.1.1.1',
] # 0.0.0.0/0
test(ip_addresses, True, '0.0.0.0/0')

# Empty List
ip_addresses = [] 
test(ip_addresses, True, [])

# Wrong Data in list
ip_addresses = [
    '11111',
    '192.100.1.1',
] 
test(ip_addresses, False, None)
