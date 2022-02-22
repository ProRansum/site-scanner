import os
from utils import create_dir, write_file
from utils import get_whois, get_domain_name, get_ip_address, get_nmap, get_robots_txt


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
DIR_PATH = os.path.join(ROOT_PATH, 'Sites')


def gather_info(url):
	domain_name, url = get_domain_name(url)
	ip_address = get_ip_address(domain_name)
	nmap = get_nmap('-F', ip_address)
	robots_txt = get_robots_txt(url)
	whois = get_whois(domain_name)
	
	create_report(url, domain_name, ip_address, nmap, robots_txt, whois)
	return

def create_report(url, domain_name, ip_address, nmap, robots_txt, whois):
	directory = '%s/%s' % (DIR_PATH, domain_name)
	create_dir(directory)
	
	write_file('%s/full_url.txt' % directory, url)
	write_file('%s/domain_name.txt' % directory, domain_name)
	write_file('%s/ip_address.txt' % directory, ip_address)
	write_file('%s/nmap.txt' % directory, nmap)
	write_file('%s/robots.txt' % directory, robots_txt)
	write_file('%s/whois.txt' % directory, whois)
	
	return


create_dir(DIR_PATH)
url = input("Enter url: ")
gather_info(url)

