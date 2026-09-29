Playwright Anti-Detect Browser Automation Framework
A modular, lightweight Python framework built on top of Playwright and WSL2, designed for multi-profile browser isolation, anti-bot fingerprint handling, and batch task execution.

Features
Profile Isolation: Persistent user contexts and independent sessions.

Modular Architecture: Clean separation between core engine (engine.py), task definitions (tasks.py), and execution controllers (main.py, batch_run.py).

CLI Control: Easily run single profiles or execute batch tasks sequentially.

Project Structure
engine.py - Core browser launch and stealth configuration.

tasks.py - Custom automation tasks and navigation logic.

main.py - CLI coordinator for single profile execution.

batch_run.py - Batch execution script for multiple profiles.

Installation & Setup
Clone the repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Create and activate a Python virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt
playwright install chromium

Configure your profiles:
Copy config.example.json to config.json and add your profile IDs and proxy settings.

Usage
Run a specific task for a single profile:
python main.py 1 sannysoft

Run a batch task across all configured profiles:
python batch_run.py sannysoft 5