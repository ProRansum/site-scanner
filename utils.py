import os
import socket
import codecs
import urllib3
from urllib.parse import urlparse


def __process__(command):
	try:
		process = os.popen(command)
		results = str(process.read())
		return results
	except Exception as e:
		raise e
		

def create_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
		print("[+] Directory created")
	else:
		# print("[!] Directory exists")
		pass


def write_file(filepath, data=''):
	f = open(filepath, 'w')
	f.write('' if not data else data)
	f.close()
	return


def get_domain_name(url):
	print("[+] Resolving Domain Name")
	try:
		parsed = urlparse(url)
		if not parsed.scheme:
			print("[!] No protocol scheme not found, default to https.")
			url = 'https://%s' % url
			parsed = urlparse(url)
		
		domain_name = parsed.netloc
		return domain_name, url
	except:
		print("[!] Failed to resolve Domain Name.")


def get_whois(domain_name):
	print("[+] Fetching WhoIs Data.")
	
	result = None
	command = "whois %s" % domain_name
	try:
		return __process__(command)
	except:
		print("[!] Failed to get Whois Data.")
	
	return result


def get_ip_address(domain_name):
	print("[+] Fetching IP Address of Domain")
	try:

		ip_address = socket.gethostbyname(domain_name)
		return ip_address
	except:
		print("[!] Failed to resolve IP Address.")


def get_nmap(options, ip):
	print("[+] Retrieving Nmap Data.")
	
	command = "nmap %s %s" % (options, ip)
	try:
		return __process__(command)
	except:
		print("[!] Failed to retrieve Nmap Data.")

def get_robots_txt(url):
	print("[+] Fetching robots.txt.")
	
	if url.endswith('/'):
		path = url[:-1]
		
	try:
		req = urllib2.Request('%s/robots.txt' % path, data=None)
		response = urllib2.urlopen(req)
		page = response.read()
		page = page.encode('utf8')
		
		return page
	except:
		print("[+] Failed to retrieve robots.txt.")

