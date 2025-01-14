import requests
import schedule
import time

SITE_URLS = ["https://attendancetracker-uq2s.onrender.com/", "https://heythere-6yi0.onrender.com/"]

#function to access site
def keep_sites_alive():
    for url in SITE_URLS:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Accessed {url} successfully at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print(f"Site {url} returned status code {response.status_code} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        except requests.RequestException as e:
            print(f"Error accessing {url}: {e}")
        

# schedule every 15min(render time before inactivity keeps in)
schedule.every(15).minutes.do(keep_sites_alive)

# Run the scheduler
print("Starting the script to keep the sites alive...")
while True:
    schedule.run_pending()
    time.sleep(1)
