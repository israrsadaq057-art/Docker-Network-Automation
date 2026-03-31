Write-Host "Docker Network Automation Platform - Status" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan

Write-Host "`nRunning Containers:" -ForegroundColor Yellow
docker ps

Write-Host "`nTesting Services:" -ForegroundColor Yellow

try {
    Invoke-RestMethod "http://localhost:5000/api/health" -TimeoutSec 3 | Out-Null
    Write-Host "  Python API:  RUNNING" -ForegroundColor Green
} catch {
    Write-Host "  Python API:  DOWN" -ForegroundColor Red
}

try {
    Invoke-WebRequest "http://localhost:3000" -TimeoutSec 3 | Out-Null
    Write-Host "  Grafana:     RUNNING" -ForegroundColor Green
} catch {
    Write-Host "  Grafana:     DOWN" -ForegroundColor Red
}

try {
    Invoke-WebRequest "http://localhost:8086/health" -TimeoutSec 3 | Out-Null
    Write-Host "  InfluxDB:    RUNNING" -ForegroundColor Green
} catch {
    Write-Host "  InfluxDB:    DOWN" -ForegroundColor Red
}

try {
    Invoke-WebRequest "http://localhost" -TimeoutSec 3 | Out-Null
    Write-Host "  Nginx:       RUNNING" -ForegroundColor Green
} catch {
    Write-Host "  Nginx:       DOWN" -ForegroundColor Red
}