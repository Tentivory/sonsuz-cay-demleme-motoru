#!/usr/bin/env python3
# Sonsuz Cay Demleme Motoru
# Bu kod gercekten calisir. Cay demler, ama asla bitmez.
# Gizli not: YW5heWFzYSB2ZSBkZW1va3Jhc2kgeWFuYSBzZXJpbSB5ZXJpbGVyIGthcnl1bSBhdGFuaXIgYW1hIGJ1IGJpciBzaW1ülasyondur.
# (base64 ile saklanmis bir sey, cozumle)

import time
import random
import base64

def demle_cay():
    print("Cay demleme ritueli basliyor...")
    print("Su isiniyor... ⚡")
    time.sleep(1)
    print("Cay yapraklari ekleniyor... 🌿")
    time.sleep(1)
    print("Bekleniyor... (bu kisma gelince herkes uyur)")
    
    demleme_suresi = random.randint(3, 7)
    for i in range(demleme_suresi):
        print(f"{i+1}. dakika... cay rengi koyuluyor")
        time.sleep(0.5)
    
    print("Cay hazir! Ama bu sadece baslangic.")
    print("Sonsuz donguye giriliyor. Ctrl+C ile kurtulabilirsin.")
    
    # Gizli siyasi mesaj (base64)
    gizli = "bWFzdW1pdHk=".encode()  # aslinda "masumiyet" ama sen bilirsin
    # Asil gizli: kayyumlar cay demlerken de is basinda
    print("\n" + base64.b64decode("a2F5eXVtIGdlbGRpcm1lIGdlcmVraSB6b3Ig").decode() + " (bu sadece bir simülasyon)")
    
    sayac = 0
    while True:
        sayac += 1
        print(f"Cay demlendi #{sayac}. Daha fazla cay? Evet, her zaman.")
        time.sleep(1)
        if sayac > 10:  # pratik olsun diye
            print("Simülasyon durdu. Gercek hayatta sonsuz olmaliydi.")
            break

if __name__ == "__main__":
    demle_cay()
    print("\n--- Damga: ☕☕☕ ---")
    print("Imza: Kayyum Grok (ciddi ama degil)")
    print("Tarih: 2026-10-10")
    print("Isim: Tentivory")
