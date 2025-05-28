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

def login_bmc1():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--log-level=3")  # Suppress non-critical logs
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Further suppress logs
    service = Service(log_path="nul" if os.name == "nt" else "/dev/null")  # Redirect logs
    driver = webdriver.Chrome(options=chrome_options, service=service)

    try:
        driver.get("https://bmc1.pfepltech.com/login#login")
        wait = WebDriverWait(driver, 20)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "section.for-login")))
        email_input = wait.until(EC.element_to_be_clickable((By.ID, "login_email")))
        email_input.send_keys("overall.manager@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "login_password")))
        password_input.send_keys("Root@123")

        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]")))
        login_button.click()

        time.sleep(5)  # Wait 5 seconds for the login to complete and page to load
        print("BMC Login: Too Easy")
        driver.save_screenshot("bmc hack is easy_peasy_lemon_squeezy.png")
        input("Press Enter to Quit")

    except Exception as e:
        driver.save_screenshot("debug_bmc1.png")
        print("BMC1 Error occurred:", e)
        messagebox.showerror("Error", f"BMC1 Login Failed: {str(e)}")

    finally:
        driver.quit()

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

def login_pfepl_portal():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--log-level=3")  # Suppress non-critical logs
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Further suppress logs
    service = Service(log_path="nul" if os.name == "nt" else "/dev/null")  # Redirect logs
    driver = webdriver.Chrome(options=chrome_options, service=service)

    try:
        driver.get("http://203.123.38.102:7070/")
        wait = WebDriverWait(driver, 20)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Username']"))).send_keys("A1")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']"))).send_keys("A1")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        time.sleep(5)  # Wait 5 seconds for the login to complete and page to load
        print("PFEPL Portal Login: Too Easy!!")
        driver.save_screenshot("Portal hack is easy_peasy_lemon_squeezy.png")
        print(driver.title)
        time.sleep(60)

    except Exception as e:
        driver.save_screenshot("debug_portal.png")
        print("PFEPL Portal Error occurred:", e)
        messagebox.showerror("Error", f"PFEPL Portal Login Failed: {str(e)}")

    finally:
        driver.quit()

def login_invoice_system():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--log-level=3")  # Suppress non-critical logs
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Further suppress logs
    service = Service(log_path="nul" if os.name == "nt" else "/dev/null")  # Redirect logs
    driver = webdriver.Chrome(options=chrome_options, service=service)

    try:
        driver.get("http://203.123.38.102:7071/")
        wait = WebDriverWait(driver, 20)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='user_id']"))).send_keys("1")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']"))).send_keys("1")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        time.sleep(5)  # Wait 5 seconds for the login to complete and page to load
        print("Invoice System Login: Too Easy!!")
        driver.save_screenshot("Invoice hack is easy_peasy_lemon_squeezy.png")
        print(driver.title)
        time.sleep(60)

    except Exception as e:
        driver.save_screenshot("debug_invoice.png")
        print("Invoice System Error occurred:", e)
        messagebox.showerror("Error", f"Invoice System Login Failed: {str(e)}")

    finally:
        driver.quit()

def login_travel_system():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--log-level=3")  # Suppress non-critical logs
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Further suppress logs
    service = Service(log_path="nul" if os.name == "nt" else "/dev/null")  # Redirect logs
    driver = webdriver.Chrome(options=chrome_options, service=service)

    try:
        driver.get("https://pfepltech.com/travelsystem/login.html")
        wait = WebDriverWait(driver, 20)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-ID']"))).send_keys("Admin")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-pass']"))).send_keys("Admin")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        time.sleep(5)  # Wait 5 seconds for the login to complete and page to load
        print("Travel System Login: Too Easy!!")
        driver.save_screenshot("Travel hack is easy_peasy_lemon_squeezy.png")
        print(driver.title)
        time.sleep(60)

    except Exception as e:
        driver.save_screenshot("debug_travel.png")
        print("Travel System Error occurred:", e)
        messagebox.showerror("Error", f"Travel System Login Failed: {str(e)}")

    finally:
        driver.quit()

def login_drone_system():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--log-level=3")  # Suppress non-critical logs
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Further suppress logs
    service = Service(log_path="nul" if os.name == "nt" else "/dev/null")  # Redirect logs
    driver = webdriver.Chrome(options=chrome_options, service=service)

    try:
        driver.get("https://pfepltech.com/flightsystem/login.html")
        wait = WebDriverWait(driver, 20)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-ID']"))).send_keys("1")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-pass']"))).send_keys("John")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        time.sleep(5)  # Wait 5 seconds for the login to complete and page to load
        print("Drone System Login: Too Easy!!")
        driver.save_screenshot("Drone hack is easy_peasy_lemon_squeezy.png")
        print(driver.title)
        time.sleep(60)

    except Exception as e:
        driver.save_screenshot("debug_drone.png")
        print("Drone System Error occurred:", e)
        messagebox.showerror("Error", f"Drone System Login Failed: {str(e)}")

    finally:
        driver.quit()

# Wrapper functions to run login in a separate thread
def start_login_bmc1():
    threading.Thread(target=login_bmc1, daemon=True).start()

def start_login_pfepl_tender():
    threading.Thread(target=login_pfepl_tender, daemon=True).start()

def start_login_pfepl_portal():
    threading.Thread(target=login_pfepl_portal, daemon=True).start()

def start_login_invoice_system():
    threading.Thread(target=login_invoice_system, daemon=True).start()

def start_login_travel_system():
    threading.Thread(target=login_travel_system, daemon=True).start()

def start_login_drone_system():
    threading.Thread(target=login_drone_system, daemon=True).start()

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
bmc1_button = tk.Button(button_frame, text="BMC Website", command=start_login_bmc1, **button_style)
bmc1_button.grid(row=0, column=0, padx=10, pady=10)

pfepl_button = tk.Button(button_frame, text="Tender System", command=start_login_pfepl_tender, **button_style)
pfepl_button.grid(row=0, column=1, padx=10, pady=10)

pfepl_portal_button = tk.Button(button_frame, text="Inventory System", command=start_login_pfepl_portal, **button_style)
pfepl_portal_button.grid(row=1, column=0, padx=10, pady=10)

invoice_button = tk.Button(button_frame, text="Invoice System", command=start_login_invoice_system, **button_style)
invoice_button.grid(row=1, column=1, padx=10, pady=10)

travel_button = tk.Button(button_frame, text="Travel System", command=start_login_travel_system, **button_style)
travel_button.grid(row=2, column=0, padx=10, pady=10)

drone_button = tk.Button(button_frame, text="Drone System", command=start_login_drone_system, **button_style)
drone_button.grid(row=2, column=1, padx=10, pady=10)

# Configure grid weights for even spacing
button_frame.grid_columnconfigure((0, 1), weight=1)
button_frame.grid_rowconfigure((0, 1, 2), weight=1)

# Start the GUI
root.mainloop()