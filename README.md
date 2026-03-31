# 🐳 Docker Network Automation Platform

## Complete Containerized Network Monitoring Stack

<div align="center">

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![InfluxDB](https://img.shields.io/badge/InfluxDB-22ADF6?style=for-the-badge&logo=influxdb&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)

**[📊 Live Demo](#)** | **[🐳 Docker Hub](#)** | **[📁 GitHub](https://github.com/israrsadaq057-art/Docker-Network-Automation)**

</div>

---

## 👨‍💻 Network Automation Specialist

**Israr Sadaq** | CCNA | CCNP | Network Automation Specialist

📍 Berlin, Germany | 📧 israrsadaq057@gmail.com | 📱 +49 152525267799

<div align="center">
  
[![GitHub](https://img.shields.io/badge/GitHub-israrsadaq057--art-black)](https://github.com/israrsadaq057-art)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/israr-sadaq)

</div>

---

## 📋 Project Overview

This project is a **complete containerized network monitoring platform** built with Docker. It provides real-time system metrics collection, time-series data storage, and beautiful visualization dashboards - all running in containers.

 
---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| **📡 Real-time Metrics** | Collects CPU, Memory, Disk, Network stats via Telegraf |
| **💾 Time-Series Database** | InfluxDB for efficient metric storage |
| **📊 Beautiful Dashboards** | Grafana with pre-configured panels |
| **🐳 Containerized** | All services run in Docker containers |
| **🔧 Easy Deployment** | Single command to start everything |
| **🌐 Web Dashboard** | Custom HTML dashboard for quick overview |

---

## 🛠️ Technologies Used

| Component | Technology | Purpose | Port |
|-----------|------------|---------|------|
| **Metrics Collector** | Telegraf | Collects system metrics | - |
| **Time-Series DB** | InfluxDB 1.8 | Stores metrics data | 8086 |
| **Visualization** | Grafana 10.2 | Creates dashboards | 3000 |
| **Web Server** | Nginx Alpine | Serves dashboard | 80 |
| **Automation** | Python 3.11 | API and automation | 5000 |

---

## 📁 Project Structure
Docker-Network-Automation/
│
├── docker-compose.yml # Main Docker Compose configuration
├── .gitignore # Git ignore rules
├── LICENSE.txt # MIT License
│
├── telegraf/
│ └── telegraf.conf # Telegraf configuration
│
├── dashboard/
│ └── index.html # Custom web dashboard
│
├── learning/
│ └── docker_explained.html # Interactive learning diagram
│
├── python-api/
│ ├── Dockerfile # Python API Dockerfile
│ ├── requirements.txt # Python dependencies
│ └── app/ # Flask application
│
├── docker/
│ └── telegraf/
│ └── telegraf.conf # Telegraf config (backup)
│
├── scripts/
│ ├── start.ps1 # PowerShell start script
│ ├── stop.ps1 # PowerShell stop script
│ └── status.ps1 # PowerShell status script
│
└── docs/
├── API.md # API documentation
└── SETUP.md # Setup instructions

---

## 🚀 Quick Start

### Prerequisites
- Docker Desktop installed and running
- 4GB+ RAM available
- Git (optional, for cloning)

 ## 🚀 Step 1: Start All Services

```bash
# Start all containers
docker-compose up -d

# Check status
docker-compose ps
```

---

## 🌐 Step 2: Access Services

| Service     | URL                   | Credentials          |
|------------|------------------------|----------------------|
| Dashboard  | http://localhost       | -                    |
| Grafana    | http://localhost:3000  | admin / Grafana@2026 |
| InfluxDB   | http://localhost:8086  | -                    |
| Python API | http://localhost:5000  | -                    |

---

## 📊 Step 3: View Metrics in Grafana

Open in your browser:

http://localhost:3000

Login credentials:
- **Username:** admin  
- **Password:** Grafana@2026  

Navigate to:
- Dashboards → General → Network Monitoring  

---

## 📈 Grafana Dashboard

| Panel           | Description                          |
|-----------------|--------------------------------------|
| CPU Usage       | Real-time CPU utilization per core   |
| Memory Usage    | RAM usage percentage and total       |
| Disk Usage      | Storage utilization                  |
| Network Traffic | In/Out bytes per interface           |
| System Load     | Load average (1, 5, 15 minutes)      |

---

## 📥 Import Custom Dashboard

1. Download JSON file from `dashboards/` folder  
2. Open Grafana  
3. Go to **Dashboards → Import**  
4. Upload the JSON file  

---

## 🔧 Configuration

### Telegraf Configuration

```bash
nano telegraf/telegraf.conf
```

```ini
[agent]
  interval = "10s"

[[inputs.exec]]
  commands = ["/path/to/script.sh"]
```

---

### InfluxDB Configuration

```bash
nano docker-compose.yml
```

```yaml
environment:
  - INFLUXDB_DB=network_metrics
  - INFLUXDB_HTTP_AUTH_ENABLED=false
```

---

### Grafana Configuration

- Username: `admin`  
- Password: `Grafana@2026`  
- Data source: `http://influxdb:8086`  

---

## 🛠️ Management Commands

### PowerShell

```bash
.\scripts\start.ps1
.\scripts\stop.ps1
.\scripts\status.ps1
```

---

### Docker Commands

```bash
# View logs
docker-compose logs -f

# Restart Grafana
docker-compose restart grafana

# Stop services
docker-compose down

# Remove volumes
docker-compose down -v
```

---

## 📊 Performance Metrics

| Metric          | Value              |
|-----------------|--------------------|
| CPU Usage       | Every 10 seconds   |
| Memory Usage    | Real-time          |
| Disk Usage      | Every 15 minutes   |
| Network Traffic | Live monitoring    |
| Data Retention  | Configurable       |

---

## 🔌 TSN Telemetry Integration

- Python API collects TSN metrics  
- Data stored in InfluxDB  
- Visualized in Grafana (latency, jitter, packet loss)  

Example loop:

```bash
while true; do
  python fetch_tsn_metrics.py
  sleep 10
done
```

---

## 📚 Learning Resources

```bash
learning/docker_explained.html
```

---

## 🧪 Testing

```bash
# Check running containers
docker ps

# Test InfluxDB
curl http://localhost:8086/query?q=SHOW+DATABASES

# Test Grafana
curl http://localhost:3000/api/health
```

---

## 🐛 Troubleshooting

```bash
# View logs
docker-compose logs <service-name>

# Restart service
docker-compose restart <service-name>
```

---

### Port Conflict Fix

```yaml
ports:
  - "8081:8086"
```

---

### Fix Permissions

```bash
sudo chown -R $USER:$USER data/
```

---

## 🎯 Next Steps

- Add TSN telemetry integration  
- Create more Grafana dashboards  
- Add alerting rules  
- Implement data retention policies  
- Add Prometheus support  
- Deploy to cloud (AWS / Kubernetes)  

---

## 🤝 Contributing

```bash
git checkout -b feature-name
git commit -m "Add feature"
git push origin feature-name
```

---

## 📄 License

MIT License — see `LICENSE.txt`

---

## 📞 Contact

**Israr Sadaq**  
Network Automation Specialist (CCNA, CCNP)

- Email: israrsadaq057@gmail.com  
- Phone: +49 152525267799  
- Location: Berlin, Germany  
- GitHub: https://github.com/israrsadaq057-art  
- LinkedIn: https://linkedin.com/in/israr-sadaq  

---

## ⭐ Support

If you found this project useful, give it a ⭐

---

**Built with ❤️ for Docker & Network Monitoring**  
© 2026 Israr Sadaq
---

**Copy everything above and paste it into your README.md!** 🚀
