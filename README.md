**Cyber-Intelligence Wing: Real-Time Threat Mapping**

Project Overview
The Cyber-Intelligence Wing is an advanced cybersecurity dashboard designed to bridge the gap between raw honeypot data and actionable threat intelligence. It utilizes a machine learning-driven approach to map incoming logs to the MITRE ATT&CK framework, providing digital forensics investigators with high-confidence technique identification.

Key Features
AI-Powered Mapping: Leverages a SciBERT-BiLSTM model to analyze the semantics of raw logs (e.g., Log4Shell, SSH Brute Force) and map them to specific MITRE techniques.

Azure-Native Deployment: Fully deployed on an Azure VM to ensure public accessibility and reliability.

Dual-Source Architecture: Features a high-speed inference engine that pivots between curated feature sets for real-time demo stability and a backend capable of handling 10 million alerts.

Automated Rule Generation: Integrated with the Sentinel API to automatically write Suricata rules based on detected patterns.

Technical Architecture
Ingestion: Raw logs are collected via a T-Pot honeypot node.

Processing: A Flask-based backend processes incoming POST requests through a dedicated ML pipeline.

Visualization: An interactive frontend displays the MITRE technique ID, description, and model confidence score.

Tech Stack
Languages: Python, SQL, C, Lex.

Frameworks: Flask, Flask-CORS.

Tools: Git, GitHub, Azure Cloud, Fortinet.

Data Science: Pandas, SciBERT-BiLSTM.

Installation & Deployment
To run the dashboard locally or on a cloud node:

Clone the repository:

Bash
git clone https://github.com/Ajayduddu/Cyber-Intelligence-Wing.git
Set up the environment:

Bash
source ~/ml_env/bin/activate
pip install -r requirements.txt
Launch the Application:

Bash
python app.py
The app will be available at http://<your-ip>:5000.

Future Work
Implementation of the Real-Time Autonomous Response (RTAR) framework.

Full integration of the 10M alert Elasticsearch backend into the live inference pipeline.

Author
Ajay Kumar Duddu
