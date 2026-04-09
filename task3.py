# =================================================================
# PROJECT: Kubernetes Microservices Orchestration
# DESCRIPTION: YAML configuration for Scalable Microservices.
# DELIVERABLE: Deployment and Service configs with Cluster simulation.
# =================================================================

# --- PART 1: KUBERNETES YAML CONFIG (For your Deliverable) ---
"""
# 1. Deployment Configuration (app-deployment.yaml)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: aditya-microservice
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web-container
        image: adityatripathi/microservice:v1.0
        ports:
        - containerPort: 80

---
# 2. Service Configuration (app-service.yaml)
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  type: LoadBalancer
  selector:
    app: web-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
"""

# --- PART 2: K8S CLUSTER SIMULATOR ---

class KubernetesCluster:
    def __init__(self, node_count):
        self.nodes = node_count
        self.pods = []
        print(f"☸️  Connecting to Kubernetes Cluster with {self.nodes} Nodes...")

    def apply_config(self, replicas):
        """Simulating 'kubectl apply -f' command."""
        print(f"\n🚀 Applying Deployment Config: Scaling to {replicas} replicas...")
        for i in range(1, replicas + 1):
            pod_id = f"pod-web-app-{i}"
            self.pods.append({"id": pod_id, "status": "Running"})
            print(f"   [+] Pod created: {pod_id} on Node { (i % self.nodes) + 1 }")
        print("✅ Deployment Successful. All pods are healthy.")

    def monitor_cluster(self):
        print("\n" + "="*45)
        print("📊 KUBERNETES CLUSTER DASHBOARD")
        print("="*45)
        print(f"{'POD ID':<20} | {'STATUS':<10} | {'HEALTH'}")
        print("-" * 45)
        for pod in self.pods:
            print(f"{pod['id']:<20} | {pod['status']:<10}
