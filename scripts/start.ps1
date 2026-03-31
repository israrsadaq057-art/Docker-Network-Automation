Write-Host "Starting Docker Network Automation Platform..." -ForegroundColor Yellow

try {
    docker version | Out-Null
    Write-Host "Docker is running" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Docker is not running. Please start Docker Desktop." -ForegroundColor Red
    exit 1
}

docker-compose up -d

Write-Host "Waiting for services to start..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

docker ps

Write-Host "`nAll services started!" -ForegroundColor Green
Write-Host "Dashboard:  http://localhost" -ForegroundColor Yellow
Write-Host "Grafana:    http://localhost:3000" -ForegroundColor Yellow
Write-Host "InfluxDB:   http://localhost:8086" -ForegroundColor Yellow
Write-Host "Python API: http://localhost:5000" -ForegroundColor Yellow