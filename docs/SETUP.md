\# Docker Network Automation Platform



\## About



A complete Network Automation and Monitoring Platform built with Docker containers.

This project demonstrates modern DevOps practices applied to network engineering.



\*\*Built by:\*\* Israr Sadaq | Network Engineer | CCNA | CCNP

\*\*Location:\*\* Berlin, Germany

\*\*Email:\*\* israrsadaq057@gmail.com



\## Architecture

TELEGRAF (Collector) --> INFLUXDB (Database) --> GRAFANA (Dashboard) | NGINX (Web Server) PYTHON API (Automation) <----+



\## Services



| Service    | Port | Description                          |

|------------|------|--------------------------------------|

| Grafana    | 3000 | Monitoring dashboards                |

| InfluxDB   | 8086 | Time-series database                 |

| Telegraf   | -    | Metrics collector                    |

| Nginx      | 80   | Web server landing page              |

| Python API | 5000 | Network automation REST API          |



\## Quick Start



```powershell

git clone https://github.com/yourusername/Docker-Network-Automation.git

cd Docker-Network-Automation

docker-compose up -d

docker ps

Access Services

Service	URL

Dashboard	http://localhost

Grafana	http://localhost:3000

InfluxDB	http://localhost:8086

Python API	http://localhost:5000

Default Credentials

Service	Username	Password

Grafana	admin	Grafana2026

API Endpoints

Method	Endpoint	Description

GET	/	API information

GET	/api/health	Health check

GET	/api/devices	List network devices

GET	/api/devices/status	Check device status

GET	/api/devices//backup	Backup device config

GET	/api/metrics	Network metrics

GET	/api/network/scan	Scan network

Technologies Used

Docker \& Docker Compose

Python 3.11 \& Flask

Telegraf

InfluxDB

Grafana

Nginx

Netmiko

Skills Demonstrated

Network Engineering (CCNA/CCNP)

DevOps \& Docker

Python API Development

Real-time Monitoring

Network Automation

Author

Israr Sadaq Network Engineer | CCNA | CCNP Berlin, Germany israrsadaq057@gmail.com

License

MIT License - see LICENSE file



\---



\#### Step 5: Create docs/SETUP.md



```powershell

notepad docs\\SETUP.md

Paste this in Notepad, Save, Close:

\# Setup Guide



\## Prerequisites

1\. Docker Desktop - https://www.docker.com/products/docker-desktop/

2\. Git - https://git-scm.com/downloads

3\. Windows 10/11 with PowerShell



\## Installation



\### 1. Clone Repository



```powershell

git clone https://github.com/yourusername/Docker-Network-Automation.git

cd Docker-Network-Automation

