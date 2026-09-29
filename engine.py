import os
import json
import time
from playwright.sync_api import sync_playwright

def incarca_configuratie():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def ruleaza_profil(profile_id, task_func):
    config = incarca_configuratie()
    profile_data = next((p for p in config["profiles"] if p["id"] == profile_id), None)
    
    if not profile_data:
        print(f"Eroare: Profilul #{profile_id} nu a fost găsit în config.json!")
        return

    # Directorul dedicat pentru persistența datelor profilului (cookie-uri, cache, local storage)
    user_data_dir = os.path.abspath(f"./profiles/profile_{profile_id}")
    os.makedirs(user_data_dir, exist_ok=True)

    print(f"Pornesc profilul: {profile_data['name']} (ID: {profile_id})...")

    with sync_playwright() as p:
        launch_options = {
            "headless": False,  # Vizibil pentru a urmări execuția în timp real
            "args": [
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-infobars",
                "--start-maximized"
            ]
        }

        # Verificăm dacă profilul are configurat un proxy valid
        proxy_url = profile_data.get("proxy")
        if proxy_url:
            launch_options["proxy"] = {"server": proxy_url}
            print(f"Profilul {profile_id} folosește proxy: {proxy_url}")

        # Creăm contextul persistent specific acestui profil
        context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            user_agent=profile_data["user_agent"],
            **launch_options,
            viewport={"width": 1920, "height": 1080}
        )

        # Injectăm scripturi de eludare a detecției anti-bot
        context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            window.navigator.chrome = {
                runtime: {}
            };
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en']
            });
        """)

        page = context.new_page()
        
        # Mecanism de reîncercare (Retry) în caz de erori pasagere de rețea
        max_retries = 3
        success = False
        
        for attempt in range(1, max_retries + 1):
            try:
                # Apelăm funcția de automatizare trimisă ca parametru
                task_func(page)
                success = True
                break
            except Exception as e:
                print(f"Încercarea {attempt}/{max_retries} a eșuat pentru profilul {profile_id}: {e}")
                if attempt < max_retries:
                    print("Aștept 3 secunde înainte de a reîncerca...")
                    time.sleep(3)
                else:
                    print(f"Toate cele {max_retries} încercări au eșuat pentru profilul {profile_id}.")

        context.close()
        print(f"Profilul {profile_id} a fost închis și sesiunea salvată cu succes.\n")