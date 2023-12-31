import requests
import re
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)

file_name = 'config.yaml'
config = yaml.load(open(file_name))

# Cập nhật địa chỉ IP trong phần 'proxies'clear

for proxy in config['proxies']:
    domain_name = proxy['server']
    try:
        print(domain_name)
        response = requests.get(f"https://checkip.com.vn/locator?host={domain_name}")
        content = response.text
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', content)
        try:
            proxy['server'] = str(ip[1])
            print(ip[1])
        except IndexError:
            print(f"Insufficient IP addresses found for {domain_name}")
    except requests.exceptions.RequestException:
        pass
        
with open('output.yaml', 'w') as fp:
    yaml.dump(config, fp)
