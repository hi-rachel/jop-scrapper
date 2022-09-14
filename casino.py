from random import randint

print("Welcome to Python Casino")

pc_choice = randint(1, 50)

playing = True

while playing:
  user_choice = int(input("Choose number:"))
  if user_choice == pc_choice:
    print("You won!")
    playing = False
  elif user_choice > pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher!")

# data structure : list [] = mutable / tuple () = immutable / dictionary {} key-value = mutable

from requests import get

websites = (
  "google.com",
  "naver.com",
  "airbnb.com",
  "twitter.com",
  "nomadcoders.co",
)

results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if response.status_code < 300:
    results[website] = "OK"
  elif status_code >= 300 and status_code < 400:
    results[website] = "OK"
  elif status_code >= 400:
    results[website] = "FAILED"
  
print(results)
  