# =================================================================
# PROJECT: Version Control Workflow Simulation
# DESCRIPTION: Simulating Branching, Merging, and Conflict Resolution.
# DELIVERABLE: Documentation of Git commands and conflict handling.
# =================================================================

class GitSimulation:
    def __init__(self):
        self.repository = "Aditya_Internship_Project"
        self.history = []
        print(f"📁 Initialized Empty Git Repository: {self.repository}")

    def commit(self, message, branch="main"):
        """Simulates 'git commit -m'."""
        entry = {"branch": branch, "message": message, "id": len(self.history) + 101}
        self.history.append(entry)
        print(f"   [Branch: {branch}] Commit: {message} (SHA: {entry['id']})")

    def demonstrate_conflict(self):
        """Step-by-step simulation of a Merge Conflict."""
        print("\n--- 🛠️  SIMULATING MERGE CONFLICT ---")
        
        # 1. Main branch update
        print("1. [main] Developer A updates line 10 to 'Blue Theme'.")
        self.commit("Updated theme to Blue", "main")

        # 2. Feature branch update
        print("2. [feature] Developer B updates same line 10 to 'Red Theme'.")
        self.commit("Updated theme to Red", "feature_v1")

        # 3. Merging
        print("\n⚡ Command: git merge feature_v1")
        print("⚠️  CONFLICT (content): Merge conflict in style.css")
        print("📢 Automatic merge failed; fix conflicts and then commit the result.")

    def resolve_conflict(self, choice):
        """Logic for manual resolution of a conflict."""
        print("\n--- 🔧 RESOLVING CONFLICT ---")
        print(f"Decision: Keeping {choice}'s changes.")
        print("<<<<<<< HEAD (Current Change)")
        print("background: blue;")
        print("=======")
        print("background: red;")
        print(">>>>>>> feature_v1 (Incoming Change)")
        
        self.commit(f"Merged branch feature_v1 - Resolved conflict in favor of {choice}", "main")
        print("✅ Conflict Resolved. Repository is clean.")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    git = GitSimulation()

    # 1. Initial Setup
    git.commit("Initial project structure")

    # 2. Demonstrate Branching and Conflict (Deliverable)
    git.demonstrate_conflict()

    # 3. Resolve Conflict (Deliverable)
    git.resolve_conflict("Developer A")

    # 4. Final Commit History
    print("\n📜 FINAL COMMIT HISTORY:")
    for c in git.history:
        print(f"[{c['branch']}] {c['message']}")

    print("\n✅ Task 49 Complete: Git Workflow Verified.")
