&#x20;# API Documentation



\## Base URL



http://localhost:5000



\## GET /



Returns API information.



\## GET /api/health



Health check endpoint.



Response:

{

&#x20;   "status": "healthy",

&#x20;   "timestamp": "2026-03-31T10:00:00"

}



\## GET /api/devices



List all network devices.



Response:

{

&#x20;   "total\_devices": 5,

&#x20;   "online": 4,

&#x20;   "offline": 1,

&#x20;   "devices": \[...]

}



\## GET /api/devices/status



Check status of all devices.



\## GET /api/devices/<id>/backup



Backup configuration of a specific device.



\## GET /api/metrics



Get network metrics summary.



\## GET /api/network/scan



Scan network for devices.

