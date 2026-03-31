from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

DEVICES = [
    {"id": 1, "hostname": "router-01", "ip": "192.168.1.1", "device_type": "cisco_ios", "location": "Berlin-DC1", "status": "online", "model": "Cisco ISR 4321"},
    {"id": 2, "hostname": "switch-01", "ip": "192.168.1.2", "device_type": "cisco_ios", "location": "Berlin-DC1", "status": "online", "model": "Cisco Catalyst 9300"},
    {"id": 3, "hostname": "switch-02", "ip": "192.168.1.3", "device_type": "cisco_ios", "location": "Berlin-DC2", "status": "online", "model": "Cisco Catalyst 3850"},
    {"id": 4, "hostname": "firewall-01", "ip": "192.168.1.4", "device_type": "cisco_asa", "location": "Berlin-DC1", "status": "online", "model": "Cisco ASA 5525-X"},
    {"id": 5, "hostname": "router-02", "ip": "192.168.1.5", "device_type": "cisco_ios", "location": "Berlin-DC2", "status": "offline", "model": "Cisco ISR 4431"}
]

CSS = """<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',Arial,sans-serif;background:#0a0e1a;color:#e0e0e0;min-height:100vh}
.nav{background:#1a1f2e;padding:15px 30px;display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #ffd700}
.nav h1{color:#ffd700;font-size:20px}
.nav a{color:#888;text-decoration:none;margin-left:20px;font-size:14px}
.nav a:hover,.nav a.on{color:#ffd700}
.wrap{max-width:1200px;margin:30px auto;padding:0 20px}
.hdr{text-align:center;margin-bottom:30px}
.hdr h2{color:#ffd700;font-size:28px;margin-bottom:5px}
.hdr p{color:#888;font-size:14px}
.row4{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-bottom:30px}
.row3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:30px}
.box{background:#1a1f2e;padding:20px;border-radius:10px;text-align:center;border:1px solid #333}
.box .num{font-size:36px;font-weight:bold;margin:10px 0}
.box .lbl{color:#888;font-size:14px}
.grn{color:#22c55e}.red{color:#ef4444}.ylw{color:#ffd700}.blu{color:#3b82f6}
table{width:100%;border-collapse:collapse;background:#1a1f2e;border-radius:10px;overflow:hidden}
th{background:#252b3b;color:#ffd700;padding:15px;text-align:left;font-size:14px;text-transform:uppercase}
td{padding:12px 15px;border-bottom:1px solid #2a2f3e;font-size:14px}
tr:hover{background:#252b3b}
.badge{padding:4px 12px;border-radius:20px;font-size:12px;font-weight:bold}
.b-on{background:#22c55e20;color:#22c55e;border:1px solid #22c55e}
.b-off{background:#ef444420;color:#ef4444;border:1px solid #ef4444}
.crd{background:#1a1f2e;padding:25px;border-radius:10px;border:1px solid #333}
.crd h3{color:#ffd700;margin-bottom:15px;font-size:16px}
.itm{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #2a2f3e;font-size:14px}
.itm:last-child{border-bottom:none}
.ft{text-align:center;padding:20px;color:#555;font-size:12px;margin-top:30px}
.btn{display:inline-block;padding:8px 16px;background:#ffd700;color:#0a0e1a;text-decoration:none;border-radius:5px;font-size:13px;font-weight:bold;margin:5px}
.btn:hover{background:#ffed4a}
.btn-g{background:#22c55e}.btn-b{background:#3b82f6;color:white}
code{background:#252b3b;padding:2px 8px;border-radius:4px;font-size:13px}
</style>"""

def nav(a=""):
    links = [("home","/","Home"),("dev","/api/devices","Devices"),("st","/api/devices/status","Status"),("met","/api/metrics","Metrics"),("sc","/api/network/scan","Scan")]
    h = '<div class="nav"><h1>Docker Network Automation</h1><div>'
    for k,u,t in links:
        c = ' class="on"' if k == a else ""
        h += f'<a href="{u}"{c}>{t}</a>'
    h += '<a href="http://localhost:3000" target="_blank">Grafana</a></div></div>'
    return h

FT = '<div class="ft"><p>Docker Network Automation v1.0 | Israr Sadaq | CCNA | CCNP | Berlin</p></div>'

@app.route("/")
def home():
    on = len([d for d in DEVICES if d["status"] == "online"])
    off = len([d for d in DEVICES if d["status"] == "offline"])
    return f"""<!DOCTYPE html><html><head><title>Network Automation</title>{CSS}</head><body>
{nav("home")}
<div class="wrap">
<div class="hdr"><h2>Network Automation Platform</h2><p>Real-time Monitoring and Automation | Israr Sadaq | CCNA | CCNP</p></div>
<div class="row4">
<div class="box"><div class="lbl">Total Devices</div><div class="num ylw">{len(DEVICES)}</div><div class="lbl">Managed</div></div>
<div class="box"><div class="lbl">Online</div><div class="num grn">{on}</div><div class="lbl">Healthy</div></div>
<div class="box"><div class="lbl">Offline</div><div class="num red">{off}</div><div class="lbl">Needs Attention</div></div>
<div class="box"><div class="lbl">API Status</div><div class="num grn">UP</div><div class="lbl">All Systems Go</div></div>
</div>
<div class="row3">
<div class="crd"><h3>Quick Links</h3>
<a href="/api/devices" class="btn">View Devices</a>
<a href="/api/devices/status" class="btn btn-g">Check Status</a>
<a href="/api/metrics" class="btn btn-b">Metrics</a>
<a href="/api/network/scan" class="btn">Network Scan</a></div>
<div class="crd"><h3>External Services</h3>
<a href="http://localhost:3000" target="_blank" class="btn">Grafana</a>
<a href="http://localhost:8086" target="_blank" class="btn btn-b">InfluxDB</a>
<a href="http://localhost" target="_blank" class="btn btn-g">Dashboard</a></div>
<div class="crd"><h3>API Endpoints</h3>
<div class="itm"><span>GET</span><span>/api/health</span></div>
<div class="itm"><span>GET</span><span>/api/devices</span></div>
<div class="itm"><span>GET</span><span>/api/devices/status</span></div>
<div class="itm"><span>GET</span><span>/api/metrics</span></div>
<div class="itm"><span>GET</span><span>/api/network/scan</span></div></div>
</div></div>{FT}</body></html>"""

@app.route("/api/health")
def health():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.route("/api/devices")
def get_devices():
    rows = ""
    for d in DEVICES:
        bc = "b-on" if d["status"] == "online" else "b-off"
        bt = "ONLINE" if d["status"] == "online" else "OFFLINE"
        rows += f'<tr><td>{d["id"]}</td><td><b>{d["hostname"]}</b></td><td>{d["ip"]}</td><td>{d["model"]}</td><td>{d["device_type"]}</td><td>{d["location"]}</td><td><span class="badge {bc}">{bt}</span></td><td><a href="/api/devices/{d["id"]}/backup" class="btn" style="padding:4px 10px;font-size:11px">Backup</a></td></tr>'
    on = len([d for d in DEVICES if d["status"] == "online"])
    off = len([d for d in DEVICES if d["status"] == "offline"])
    locs = len(set(d["location"] for d in DEVICES))
    return f"""<!DOCTYPE html><html><head><title>Devices</title>{CSS}</head><body>
{nav("dev")}
<div class="wrap">
<div class="hdr"><h2>Network Devices</h2><p>All managed network devices</p></div>
<div class="row4">
<div class="box"><div class="lbl">Total</div><div class="num ylw">{len(DEVICES)}</div></div>
<div class="box"><div class="lbl">Online</div><div class="num grn">{on}</div></div>
<div class="box"><div class="lbl">Offline</div><div class="num red">{off}</div></div>
<div class="box"><div class="lbl">Locations</div><div class="num blu">{locs}</div></div>
</div>
<table><thead><tr><th>ID</th><th>Hostname</th><th>IP Address</th><th>Model</th><th>Type</th><th>Location</th><th>Status</th><th>Action</th></tr></thead><tbody>{rows}</tbody></table>
</div>{FT}</body></html>"""

@app.route("/api/devices/status")
def device_status():
    rows = ""
    for d in DEVICES:
        bc = "b-on" if d["status"] == "online" else "b-off"
        bt = "ONLINE" if d["status"] == "online" else "OFFLINE"
        dot = "&#9679;" if d["status"] == "online" else "&#9679;"
        dc = "grn" if d["status"] == "online" else "red"
        rt = "12 ms" if d["status"] == "online" else "Timeout"
        rc = "grn" if d["status"] == "online" else "red"
        rows += f'<tr><td><span class="{dc}">{dot}</span> <b>{d["hostname"]}</b></td><td>{d["ip"]}</td><td><span class="badge {bc}">{bt}</span></td><td class="{rc}">{rt}</td><td>{d["location"]}</td><td>{datetime.now().strftime("%H:%M:%S")}</td></tr>'
    return f"""<!DOCTYPE html><html><head><title>Status</title>{CSS}</head><body>
{nav("st")}
<div class="wrap">
<div class="hdr"><h2>Device Status Monitor</h2><p>Real-time status of all devices</p></div>
<table><thead><tr><th>Device</th><th>IP Address</th><th>Status</th><th>Response</th><th>Location</th><th>Last Check</th></tr></thead><tbody>{rows}</tbody></table>
</div>{FT}</body></html>"""

@app.route("/api/devices/<int:did>/backup")
def backup_device(did):
    dev = next((d for d in DEVICES if d["id"] == did), None)
    if not dev:
        return jsonify({"error": "Device not found"}), 404
    ok = dev["status"] == "online"
    sc = "grn" if ok else "red"
    st = "SUCCESS" if ok else "FAILED"
    return f"""<!DOCTYPE html><html><head><title>Backup</title>{CSS}</head><body>
{nav("")}
<div class="wrap">
<div class="hdr"><h2>Configuration Backup</h2><p>Backup result for {dev["hostname"]}</p></div>
<div class="crd" style="max-width:600px;margin:0 auto">
<h3>Backup Details</h3>
<div class="itm"><span>Device</span><span><b>{dev["hostname"]}</b></span></div>
<div class="itm"><span>IP Address</span><span>{dev["ip"]}</span></div>
<div class="itm"><span>Model</span><span>{dev["model"]}</span></div>
<div class="itm"><span>Status</span><span class="{sc}"><b>{st}</b></span></div>
<div class="itm"><span>Time</span><span>{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</span></div>
<div class="itm"><span>Config Lines</span><span>{"245" if ok else "0"}</span></div>
<div class="itm"><span>Size</span><span>{"12.5 KB" if ok else "0 KB"}</span></div>
<div style="margin-top:20px;text-align:center"><a href="/api/devices" class="btn">Back to Devices</a></div>
</div></div>{FT}</body></html>"""

@app.route("/api/metrics")
def get_metrics():
    on = len([d for d in DEVICES if d["status"] == "online"])
    off = len([d for d in DEVICES if d["status"] == "offline"])
    return f"""<!DOCTYPE html><html><head><title>Metrics</title>{CSS}</head><body>
{nav("met")}
<div class="wrap">
<div class="hdr"><h2>Network Metrics</h2><p>Real-time network performance</p></div>
<div class="row4">
<div class="box"><div class="lbl">Devices</div><div class="num ylw">{len(DEVICES)}</div></div>
<div class="box"><div class="lbl">Online</div><div class="num grn">{on}</div></div>
<div class="box"><div class="lbl">Offline</div><div class="num red">{off}</div></div>
<div class="box"><div class="lbl">Uptime</div><div class="num grn">99.8%</div></div>
</div>
<div class="row3">
<div class="crd"><h3>Interfaces</h3>
<div class="itm"><span>Total</span><span class="ylw">48</span></div>
<div class="itm"><span>Active</span><span class="grn">42</span></div>
<div class="itm"><span>Down</span><span class="red">6</span></div>
<div class="itm"><span>Errors</span><span class="grn">0</span></div></div>
<div class="crd"><h3>Bandwidth</h3>
<div class="itm"><span>Usage</span><span class="ylw">67.5%</span></div>
<div class="itm"><span>Inbound</span><span class="grn">150 Mbps</span></div>
<div class="itm"><span>Outbound</span><span class="blu">89 Mbps</span></div>
<div class="itm"><span>Peak</span><span class="red">245 Mbps</span></div></div>
<div class="crd"><h3>Performance</h3>
<div class="itm"><span>Latency</span><span class="grn">8.5 ms</span></div>
<div class="itm"><span>Packet Loss</span><span class="grn">0.02%</span></div>
<div class="itm"><span>Jitter</span><span class="grn">1.2 ms</span></div>
<div class="itm"><span>Throughput</span><span class="ylw">892 Mbps</span></div></div>
</div></div>{FT}</body></html>"""

@app.route("/api/network/scan")
def network_scan():
    hosts = [
        {"ip": "192.168.1.1", "hostname": "router-01", "mac": "AA:BB:CC:DD:EE:01", "status": "up", "type": "Router"},
        {"ip": "192.168.1.2", "hostname": "switch-01", "mac": "AA:BB:CC:DD:EE:02", "status": "up", "type": "Switch"},
        {"ip": "192.168.1.3", "hostname": "switch-02", "mac": "AA:BB:CC:DD:EE:03", "status": "up", "type": "Switch"},
        {"ip": "192.168.1.4", "hostname": "firewall-01", "mac": "AA:BB:CC:DD:EE:04", "status": "up", "type": "Firewall"},
        {"ip": "192.168.1.5", "hostname": "router-02", "mac": "AA:BB:CC:DD:EE:05", "status": "down", "type": "Router"}
    ]
    rows = ""
    for h in hosts:
        bc = "b-on" if h["status"] == "up" else "b-off"
        dc = "grn" if h["status"] == "up" else "red"
        rows += f'<tr><td><span class="{dc}">&#9679;</span> {h["ip"]}</td><td><b>{h["hostname"]}</b></td><td><code>{h["mac"]}</code></td><td>{h["type"]}</td><td><span class="badge {bc}">{h["status"].upper()}</span></td></tr>'
    up = len([h for h in hosts if h["status"] == "up"])
    dn = len([h for h in hosts if h["status"] == "down"])
    return f"""<!DOCTYPE html><html><head><title>Network Scan</title>{CSS}</head><body>
{nav("sc")}
<div class="wrap">
<div class="hdr"><h2>Network Scan Results</h2><p>Scan of 192.168.1.0/24 | {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p></div>
<div class="row4">
<div class="box"><div class="lbl">Network</div><div class="num ylw" style="font-size:20px">192.168.1.0/24</div></div>
<div class="box"><div class="lbl">Found</div><div class="num blu">{len(hosts)}</div></div>
<div class="box"><div class="lbl">Up</div><div class="num grn">{up}</div></div>
<div class="box"><div class="lbl">Down</div><div class="num red">{dn}</div></div>
</div>
<table><thead><tr><th>IP Address</th><th>Hostname</th><th>MAC Address</th><th>Type</th><th>Status</th></tr></thead><tbody>{rows}</tbody></table>
</div>{FT}</body></html>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
