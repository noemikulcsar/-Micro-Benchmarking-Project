import os
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

JAVA_PROGRAMS_DIR = "./java_programs"
PYTHON_PROGRAMS_DIR = "./python_programs"

PROGRAMS = {
    "Static Allocation": {
        "Java": "StaticAllocation.java",
        "Python": "static_allocation.py",
    },
    "Dynamic Allocation": {
        "Java": "DynamicAllocation.java",
        "Python": "dynamic_allocation.py",
    },
    "Thread Creation": {
        "Java": "ThreadCreation.java",
        "Python": "thread_creation.py",
    },
    "Thread Context Switch": {
        "Java": "ThreadContextSwitch.java",
        "Python": "thread_context_switch.py",
    },
    "Thread Migration":{
        "Java": "ThreadMigration.java",
        "Python": "thread_migration.py",
    },
}
def read_results_from_file(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {file_path} not found!")
        return None

def run_program(file_path, language):
    try:
        if language == "Java":
            class_name = os.path.basename(file_path).replace(".java", "")
            subprocess.run(["javac", file_path], check=True)
            result = subprocess.run(["java", "-cp", JAVA_PROGRAMS_DIR, class_name], capture_output=True, text=True, check=True)
        
        elif language == "Python":
            result = subprocess.run(["python", file_path], capture_output=True, text=True, check=True)
        
        else:
            raise ValueError("Unsupported language")
        
        return result.stdout
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to execute {file_path}: {e}")
        return None

def measure_operation(operation):
    if not os.path.exists("./results"):
        os.makedirs("./results")
    
    results = {}
    
    for language, file_name in PROGRAMS[operation].items():
        folder = {"Java": JAVA_PROGRAMS_DIR, "Python": PYTHON_PROGRAMS_DIR}[language]
        file_path = os.path.join(folder, file_name)
        result_file = f"./results/{language.lower()}_{operation.lower().replace(' ', '_')}_results.txt"
        try:
            run_program(file_path, language)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run {language} program: {e}")
            continue
        output = read_results_from_file(result_file)
        if output:
            try:
                avg_time = float(output.split("Average:")[1].strip().split()[0])
                results[language] = avg_time
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected output in {result_file}: {e}")
    
    if not results:
        messagebox.showwarning("Warning", "No valid results were obtained!")
    return results

def plot_results(results):
    languages = list(results.keys())
    times = list(results.values())
    plt.bar(languages, times, color=['pink', 'lightcoral', 'hotpink'])
    plt.title("Execution Time Comparison", color="deeppink")
    plt.xlabel("Language", color="deeppink")
    plt.ylabel("Average Time (ns)", color="deeppink")
    plt.show()

def on_run_clicked():
    operation = operation_selector.get()
    if not operation:
        messagebox.showwarning("Warning", "Please select an operation to measure!")
        return
    
    results = measure_operation(operation)
    if results:
        plot_results(results)

root = tk.Tk()
root.title("Execution Time Measurement")
root.geometry("400x300")
root.configure(bg="pink")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="pink", foreground="deeppink", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 10))
style.configure("TButton", background="hotpink", foreground="white", font=("Arial", 10, "bold"))

ttk.Label(root, text="Select Operation:").pack(pady=10)
operation_selector = ttk.Combobox(root, values=list(PROGRAMS.keys()), state="readonly")
operation_selector.pack()

run_button = ttk.Button(root, text="Run Tests", command=on_run_clicked)
run_button.pack(pady=20)

root.mainloop()
