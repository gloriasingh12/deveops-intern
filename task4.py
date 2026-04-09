# =================================================================
# PROJECT: DevSecOps Pipeline Integration
# DESCRIPTION: Integrating SonarQube & OWASP ZAP for Automated Security.
# DELIVERABLE: Pipeline YAML logic and Security Audit Report.
# =================================================================

# --- PART 1: DEVSECOPS PIPELINE YAML (For your Deliverable) ---
"""
name: DevSecOps-Security-Scan

on: [push]

jobs:
  security-audit:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: SonarQube Scan (SAST)
        run: sonar-scanner -Dsonar.projectKey=Aditya_Project -Dsonar.sources=.
        
      - name: OWASP ZAP Scan (DAST)
        run: zap-baseline.py -t http://staging-app.soit.edu -r security-report.html

      - name: Quality Gate Check
        run: |
          if [ ${{ steps.sonar.outputs.status }} == 'FAILED' ]; then
            echo "❌ Security Quality Gate Failed!"
            exit 1
          fi
"""

# --- PART 2: SECURITY REPORT GENERATOR SIMULATOR ---

class DevSecOpsEngine:
    def __init__(self):
        self.vulnerabilities = []
        print("🛡️  DevSecOps Quality Gate: ACTIVE")

    def run_sonarqube_scan(self):
        print("\n🔍 [Step 1] Running SonarQube Static Analysis...")
        # Simulating identified issues
        self.vulnerabilities.append({"tool": "SonarQube", "issue": "Hardcoded API Key", "severity": "CRITICAL"})
        self.vulnerabilities.append({"tool": "SonarQube", "issue": "Code Smell: Deep Nesting", "severity": "MINOR"})
        print("✅ Static Scan Complete.")

    def run_owasp_zap_scan(self):
        print("\n🌐 [Step 2] Running OWASP ZAP Dynamic Analysis...")
        self.vulnerabilities.append({"tool": "OWASP ZAP", "issue": "Missing X-Frame-Options Header", "severity": "HIGH"})
        print("✅ Dynamic Scan Complete.")

    def generate_audit_report(self):
        print("\n" + "="*55)
        print("📋 DEVSECOPS SECURITY AUDIT REPORT - TASK 52")
        print("="*55)
        print(f"{'TOOL':<12} | {'IDENTIFIED VULNERABILITY':<30} | {'SEVERITY'}")
        print("-" * 55)
        for v in self.vulnerabilities:
            color = "🔴" if v['severity'] in ['CRITICAL', 'HIGH'] else "🟡"
            print(f"{v['tool']:<12} | {v['issue']:<30} | {color} {v['severity']}")
        print("-" * 55)
        print("📢 ACTION REQUIRED: 2 Critical/High issues must be fixed before Deploy.")
        print
