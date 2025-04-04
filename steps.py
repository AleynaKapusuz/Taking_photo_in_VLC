import subprocess
import time
import telnetlib

vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
rtsp_url = r"rtsp://..."
screenshot_path = r"C:\Users\YapayZeka\Desktop\Aleyna\.."

# VLC'yi RC (Remote Control) modunda başlat
process = subprocess.Popen([
    vlc_path,
    rtsp_url,
    "--extraintf", "rc",         # RC (Remote Control) arayüzünü aktif et
    "--rc-host", "localhost:4212",  # Telnet bağlantısı için port belirle
    "--snapshot-path", screenshot_path,  # Ekran görüntüsünün kaydedileceği klasör
    "--snapshot-format", "png"  # PNG formatında kaydet
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# VLC'nin açılması için bekleme süresi
time.sleep(5)

try:
    # VLC'nin RC arayüzüne bağlan
    tn = telnetlib.Telnet("localhost", 4212)

    # Sonsuz döngü ile her 2 saniyede bir fotoğraf çek
    while True:
        tn.write(b"snapshot\n")  # VLC'ye fotoğraf çekme komutu gönder
        print(f"📸 Fotoğraf çekildi ve şu klasöre kaydedildi: {screenshot_path}")
        time.sleep(2)  # 2 saniye bekle

except Exception as e:
    print(f"Hata oluştu: {e}")


