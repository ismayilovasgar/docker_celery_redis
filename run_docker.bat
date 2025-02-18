@echo off
echo Docker ortamı başlatılıyor...

rem Eğer WSL yüklü ise, chmod komutunu çalıştır
rem wsl chmod +x ./entrypoint.sh xeta alsan bundan olacak !

rem Docker Compose ile uygulamayı başlat
docker-compose up -d --build

rem Django uygulamasını aç
start http://0.0.0.0:8000

echo İşlem tamamlandı!
