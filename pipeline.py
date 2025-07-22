import subprocess

print("🚀 Running Full COVID-19 Pipeline...\n")

subprocess.run(["python", "scripts/fetch_data.py"])
subprocess.run(["python", "scripts/clean_data.py"])
subprocess.run(["python", "scripts/load_data.py"])
subprocess.run(["python", "scripts/visualize.py"])  # Optional

print("\n✅ Pipeline completed!")
