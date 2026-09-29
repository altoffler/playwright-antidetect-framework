Playwright Anti-Detect Browser Automation Framework (Demo)
A modular, lightweight Python framework built on top of Playwright and WSL2, designed for multi-profile browser isolation, anti-bot fingerprint handling, and batch task execution.

Looking for the full production-ready framework?
Get the complete, unconstrained source code (including advanced stealth arguments, batch execution controllers, persistent session management, and proxy rotation tools) on Gumroad ($24.99).

What's in the Full Version?
engine.py: Fully configured stealth browser launch engine with custom fingerprint masking and retry logic.

batch_run.py: Production-grade batch controller to execute tasks across multiple profiles sequentially with custom delays.

tasks.py: Extended automation task templates for browser verification and scraping.

Persistent Contexts: Clean profile isolation without cross-contamination.

Quick Start (Demo Preview)
Clone the repository:

Bash
git clone https://github.com/altoffler/playwright-antidetect-framework.git
cd playwright-antidetect-framework
Set up a virtual environment and install dependencies:

Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
Run the demo script:

Bash
python main.py
License & Commercial Distribution
This repository serves as a public preview and structural demo. The core production framework is distributed commercially via Gumroad.