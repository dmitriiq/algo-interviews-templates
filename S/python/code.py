IPV4 = "IPv4"
IPV6 = "IPv6"
ERROR = "Error"

# return IPV4, IPV6 or ERROR constant
def check_ip_address(ip_to_check: str) -> str:
    try:
        str_num = ip_to_check.split('.')
        # if str_num[0] == 0:
        for s in str_num:
            if s[0] == '0' and len(s) != 1:
                raise Exception('leading 0')
        m = list(map(int, str_num))
        if len(m) != 4:
            # print('xcvxcv')
            raise Exception('xcvxcv')
        # print(m)
        for x in m:
            # print(x)
            if x > 255 or x < 0:
                # print('x > 255')
                raise Exception('x>255')
        return IPV4
    except Exception as e:
        # print(e)
        pass

    try:
        str_num = ip_to_check.split(':')
        for x in str_num:
            if len(x) > 4:
                raise Exception('>4')
        m = list(map(lambda x : int(x, base=16), str_num))
        if len(m) != 8:
            raise Exception('asdf')
        for x in m:
            # print(x)
            if x > 0XFFFF or x < 0:
                raise Exception('x>ffff')
        return IPV6
    except Exception as e:
        # print(e)
        pass
    return ERROR

ip_to_check = input()
print(check_ip_address(ip_to_check))