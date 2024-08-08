import dns.resolver

website_list = ["google.com", "beardung.com","JMO.com", "gg.com"]

def check_dns(domain):
    try:
        dns.resolver.resolve(domain, 'A')
        return True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return False

for website in website_list:
    if check_dns(website):
        print(f"Legitimate site (valid DNS): {website}")
    #else:
    #    print(f"Invalid DNS or not reachable: {website}")
