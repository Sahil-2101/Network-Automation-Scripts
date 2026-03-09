import yaml
from jinja2 import Environment, FileSystemLoader
import glob
from netmiko import ConnectHandler

# Load Jinja2 template folder
env = Environment(loader=FileSystemLoader("templates"))

# Loop through all YAML device files
for device_file in glob.glob("devices/*.yml"):
    with open(device_file) as f:
        data = yaml.safe_load(f)
    
    # pull the required template according to YAML File
    template_name = data["j2_template"]
    template = env.get_template(template_name)

    # Render template
    config = template.render(data)
    
    # push config to device via netmiko
    net_connect = ConnectHandler(device_type='cisco_ios', host=data['svi']['ip'], username='admin', password='password123')
    output = net_connect.send_config_set(config.splitlines())
    print(output)