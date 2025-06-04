import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import threading

def login_pfepl_tender():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--log-level=3")  # Suppress non-critical logs
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Further suppress logs
    service = Service(log_path="nul" if os.name == "nt" else "/dev/null")  # Redirect logs
    driver = webdriver.Chrome(options=chrome_options, service=service)

    try:
        driver.get("https://pfepl-tender.vercel.app/")
        wait = WebDriverWait(driver, 20)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter your Login ID']"))).send_keys("Admin")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter your password']"))).send_keys("Admin")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))).click()

        time.sleep(5)  # Wait 5 seconds for the login to complete and page to load
        print("PFEPL Tender Login: Too Easy!!")
        driver.save_screenshot("Tender hack is easy_peasy_lemon_squeezy.png")
        print(driver.title)
        time.sleep(60)

    except Exception as e:
        driver.save_screenshot("debug.png")
        print("PFEPL Tender Error occurred:", e)
        messagebox.showerror("Error", f"PFEPL Tender Login Failed: {str(e)}")

    finally:
        driver.quit()

# Wrapper functions to run login in a separate thread
def start_login_pfepl_tender():
    threading.Thread(target=login_pfepl_tender, daemon=True).start()

# Create the GUI
root = tk.Tk()
root.title("Website Login Selector")
root.geometry("400x300")
root.configure(bg="#f0f2f5")

# Frame for Buttons, centered in the window
button_frame = tk.Frame(root, bg="#f0f2f5")
button_frame.pack(expand=True, fill="both", pady=20, anchor="center")

# Button Styling
button_style = {
    "font": ("Helvetica", 10, "bold"),
    "bg": "#4CAF50",
    "fg": "white",
    "activebackground": "#45a049",
    "activeforeground": "white",
    "width": 20,
    "height": 2,
    "relief": "flat",
    "cursor": "hand2"
}

# Buttons arranged in a 3x2 grid

pfepl_button = tk.Button(button_frame, text="Tender System", command=start_login_pfepl_tender, **button_style)
pfepl_button.grid(row=0, column=1, padx=10, pady=10)


# Start the GUI
root.mainloop()
