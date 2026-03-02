# Enterprise Campus Network Automation Labs

Welcome to my **Network Automation Labs** repository!  
This project demonstrates network automation using **Python, YAML, and Jinja2**, targeting Cisco routers and switches. It is designed to teach **structured, reusable, and scalable automation** for enterprise networks.

---

## 📌 Project Overview

Projects in this repo can include (but are not limited to):  

- Automating VLAN, interface, and SVI configurations  
- Routing protocols (OSPF, EIGRP, etc.)  
- DHCP and IP address management  
- Access control lists (ACLs) and security policies  
- Template-driven configuration using YAML + Jinja2  
- Multi-device automation and orchestration  
- Integration with Python scripts and/or Ansible  

Goals:

1. Automate repetitive network configuration tasks  
2. Demonstrate structured configuration using YAML + templates  
3. Show best practices in **enterprise-ready automation**  
4. Provide interview-ready examples of scalable network automation  

---

## 📂 Repository Structure

```text
enterprise-campus-network-automation/
├── deploy.py                    # Python automation script
├── templates/                     # J2 files for each device type
    ├── access-switch.j2
    ├── core-switch.j2
    └── edge-router.j2
└── devices/                     # YAML files for each device
    ├── switch0.yml
    ├── switch1.yml
    ├── switch2.yml
    └── router.yml
