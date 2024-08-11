# import moduels
import requests 
import tkinter as tk
from tkinter import ttk, messagebox

# fetch data function from api
def fetch_prayer_times(city,country):
  url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
  try:
    response = requests.get(url)
    info = response.json()
    if "data" in info:
      timings = info["data"]["timings"]
      return timings
    else:
      return None

  except Exception as e:
    return f"an unexpeted error occured: {e}"

# the gui fuction
def gui_fetch_prayer_times():
  city = city_entry.get()
  country = country_entry.get()
  if city and country:
    prayer_timings = fetch_prayer_times(city,country)
    for name,time in prayer_timings.items():
      result.insert(tk.END,f"{name}: {time}")
  else:
   messagebox.showerror("error","unable to fetch prayer times")
  

# the gui frame
app = tk.Tk()
app.title("Prayer Times")

frame = ttk.Frame(app,padding = 20)
frame.grid(row= 0,column=0)
# city label
city_label = ttk.Label(frame,text = "City Name")
city_label.grid(row = 0,column =0,pady=10,padx=4)
# city entry
city_entry = ttk.Entry(frame,width = 20)
city_entry.grid(row = 0,column = 1,pady=10,padx=4)
# country label
country_label = ttk.Label(frame,text = "Country Name")
country_label.grid(row = 1,column = 0,pady=10,padx=4)
# country entry
country_entry = ttk.Entry(frame,width = 20)
country_entry.grid(row = 1,column = 1,pady=10,padx=4)
# button
fetch_botton = ttk.Button(frame,text = "get prayer times",command=gui_fetch_prayer_times)
fetch_botton.grid(row = 2,column = 0,columnspan=2,pady=10)
# box results
result = tk.Listbox(frame,height = 20,width = 30)
result.grid(row = 3,column =0 ,columnspan=2,pady=10)
# to keep the app running