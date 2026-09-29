import sys
import time
from engine import ruleaza_profil, incarca_configuratie
from tasks import verifica_whoer, verifica_sannysoft

TASKS_MAP = {
    "whoer": verifica_whoer,
    "sannysoft": verifica_sannysoft
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Eroare: Utilizare incorectă!")
        print("Mod de utilizare: python batch_run.py <task_name> [delay_seconds]")
        print("Exemplu: python batch_run.py sannysoft 5")
        sys.exit(1)
        
    task_name = sys.argv[1].lower()
    if task_name not in TASKS_MAP:
        print(f"Eroare: Task-ul '{task_name}' nu există!")
        print(f"Task-uri disponibile: {list(TASKS_MAP.keys())}")
        sys.exit(1)
        
    delay = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    selected_task = TASKS_MAP[task_name]
    
    config = incarca_configuratie()
    profiles = config.get("profiles", [])
    
    if not profiles:
        print("Eroare: Nu s-au găsit profile în config.json!")
        sys.exit(1)
        
    print(f"=== Pornesc rularea în serie pentru {len(profiles)} profile cu task-ul '{task_name}' ===")
    
    for i, profile in enumerate(profiles, start=1):
        profile_id = profile["id"]
        print(f"\n--- [Profil {i}/{len(profiles)}] Se procesează ID: {profile_id} ({profile['name']}) ---")
        
        try:
            ruleaza_profil(profile_id=profile_id, task_func=selected_task)
        except Exception as e:
            print(f"Eroare critică la rularea profilului {profile_id}: {e}")
            
        if i < len(profiles):
            print(f"Aștept {delay} secunde înainte de următorul profil...")
            time.sleep(delay)
            
    print("\n=== Rularea în serie a fost finalizată cu succes! ===")