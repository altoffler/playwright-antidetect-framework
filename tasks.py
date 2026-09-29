import time

def verifica_whoer(page):
    print("Navighez către whoer.net pentru verificare...")
    # Folosim 'domcontentloaded' pentru a fi mai toleranți cu scripturile externe de pe pagină
    page.goto("https://whoer.net", timeout=60000, wait_until="domcontentloaded")
    
    time.sleep(5)
    
    screenshot_path = "rezultat_verificare.png"
    page.screenshot(path=screenshot_path)
    print(f"Acțiune finalizată! Screenshot salvat ca '{screenshot_path}'.")

def verifica_sannysoft(page):
    print("Navighez către bot.sannysoft.com pentru testul de amprentă...")
    page.goto("https://bot.sannysoft.com", timeout=60000, wait_until="domcontentloaded")
    
    time.sleep(5)
    
    screenshot_path = "rezultat_sannysoft.png"
    page.screenshot(path=screenshot_path)
    print(f"Testul Sannysoft finalizat! Screenshot salvat ca '{screenshot_path}'.")