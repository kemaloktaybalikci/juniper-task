import ipaddress

def find_common_subnet(ip_list:list)-> tuple:
    ip_blocks = [set() for k in range(4)]
    
    if not ip_list:
        return True, []

    for ip in ip_list:
        
        try:
            ipaddress.IPv4Address(ip)
        except Exception as e:
            return False, None
               
        blocks = ip.split('.')
        for i in range(4):
            ip_blocks[i].add(blocks[i])
            
    if len(ip_blocks[0]) > 1:
        return True, '0.0.0.0/0'
    
    if len(ip_blocks[1]) > 1:
        return True, ip_blocks[0].pop() + '.0.0.0/8'
    
    if len(ip_blocks[2]) > 1:
        return True, ip_blocks[0].pop() + '.' + ip_blocks[1].pop() + '.0.0/16'
    
    if len(ip_blocks[3]) > 1:
        return True, ip_blocks[0].pop() + '.' + ip_blocks[1].pop() + '.' + ip_blocks[2].pop() + '.0/24'
    else:
        return True, ip_blocks[0].pop() + '.' + ip_blocks[1].pop() + '.' + ip_blocks[2].pop() + '.' + ip_blocks[3].pop() + '/32'