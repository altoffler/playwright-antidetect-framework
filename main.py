import sys
from engine import ruleaza_profil
from tasks import verifica_whoer, verifica_sannysoft

# Dicționar cu sarcinile disponibile în proiect
TASKS_MAP = {
    "whoer": verifica_whoer,
    "sannysoft": verifica_sannysoft
}

if __name__ == "__main__":
    # Verificăm dacă avem cel puțin ID-ul profilului și numele task-ului
    if len(sys.argv) < 3:
        print("Eroare: Utilizare incorectă!")
        print("Mod de utilizare: python main.py <profile_id> <task_name>")
        print("Task-uri disponibile: whoer, sannysoft")
        print("Exemplu: python main.py 1 whoer")
        sys.exit(1)
        
    try:
        profile_id = int(sys.argv[1])
    except ValueError:
        print("Eroare: ID-ul profilului trebuie să fie un număr întreg!")
        sys.exit(1)
        
    task_name = sys.argv[2].lower()
    if task_name not in TASKS_MAP:
        print(f"Eroare: Task-ul '{task_name}' nu există!")
        print(f"Task-uri disponibile: {list(TASKS_MAP.keys())}")
        sys.exit(1)
        
    selected_task = TASKS_MAP[task_name]
    
    print(f"Pornesc execuția pentru Profilul #{profile_id} cu task-ul '{task_name}'...")
    ruleaza_profil(profile_id=profile_id, task_func=selected_task)