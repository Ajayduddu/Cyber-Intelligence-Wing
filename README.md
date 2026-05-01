# Cyber-Intelligence Wing: AI-Driven MITRE ATT&CK Mapping

## **Project Overview**
The **Cyber-Intelligence Wing** is an advanced cybersecurity infrastructure designed to bridge the gap between raw honeypot data and actionable threat intelligence. Hosted on an **Azure VM**, the system utilizes a custom **SciBERT-BiLSTM** neural network to automatically categorize incoming threats into the **MITRE ATT&CK** framework with high precision.

## **Key Features**
*   **AI-Powered Mapping**: Leverages a SciBERT-BiLSTM model to analyze the semantics of raw logs (e.g., Log4Shell, SSH Brute Force) and map them to specific MITRE techniques.
*   **Azure-Native Deployment**: Fully deployed on an Azure VM to ensure public accessibility and professional reliability.
*   **Dual-Source Architecture**: Features a high-speed inference engine that pivots between curated feature sets for real-time demo stability and a backend capable of handling **10 million alerts** collected via **T-Pot**.
*   **Forensic Verification**: Integrated logic to cross-reference identified exploits with live web intelligence for validated threat analysis.

## **Repository Structure & Logic**
This repository contains the full research and development pipeline:
*   **`app.py`**: The Flask-based core that serves the dashboard and handles real-time API requests.
*   **`model.py` & `retrain_model.py`**: The neural network architecture (BiLSTM) and the scripts used for continuous model optimization.
*   **`mitre_scraper.py`**: A dynamic scraper that ensures the system stays updated with the latest TTPs from the official MITRE ATT&CK matrix.
*   **`google_search.py`**: An automated verification script that pulls live security advisories to cross-validate model predictions.

## **Technical Architecture**
*   **Ingestion**: Raw logs are collected via a **T-Pot** honeypot node.
*   **Processing**: A Flask-backend processes incoming data through an ML pipeline involving **Python** and **Pandas**.
*   **Visualization**: An interactive frontend displays the MITRE technique ID, description, and model confidence score.

## **Tech Stack**
*   **Languages**: Python (Data Science/Backend), SQL (Database), C, Lex.
*   **Cloud & DevOps**: Azure Cloud, Git/GitHub, Fortinet (Secure Authentication).
*   **Data Science**: Pandas, SciBERT-BiLSTM, PyTorch (for the `.pth` model weights).

## **Installation & Deployment**
1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/Ajayduddu/Cyber-Intelligence-Wing.git](https://github.com/Ajayduddu/Cyber-Intelligence-Wing.git)
    ```
2.  **Set up the environment**:
    ```bash
    source ~/ml_env/bin/activate
    pip install -r requirements.txt
    ```
3.  **Launch the Application**:
    ```bash
    python app.py
    ```

## **Roadmap & Future Work**
*   **Sentinel API Integration**: Automating the generation of **Suricata rules** based on predicted threats.
*   **Real-Time Autonomous Response (RTAR)**: Transitioning from passive forensic detection to active network mitigation.
*   **Elasticsearch Integration**: Full live-streaming of the 10M alert backend into the inference engine.

---

### **Author**
**Ajay Kumar Duddu**  

