
# 🌌 Star Wars API Fetcher

A simple Python command-line application that interacts with a REST API to fetch and display data from the Star Wars universe. 

This is my **5th Python learning project**, built to practice fundamental programming concepts like making HTTP requests, handling JSON data, and implementing basic error handling. As someone highly interested in data, this project serves as my first hands-on experience with the **Data Extraction** phase.

---

## ✨ Features
- **Interactive Prompt:** Asks the user which Star Wars category they want to explore (e.g., people, planets, starships).
- **Data Fetching:** Communicates with the SWAPI (Star Wars API) to retrieve live data.
- **Error Handling:** Safely manages network errors or invalid requests using `try-except` blocks so the program doesn't crash abruptly.
- **Data Parsing:** Extracts and displays specific information (like character names) from complex JSON structures.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x  
- **Library:** `requests` (for handling HTTP requests)

---

## 🚀 How to Run the Project

1.  **Clone this repository**
      ```bash
      git clone https://github.com/USERNAME_KAMU/star-wars-api-fetcher.git
2.  **Navigate to the project directory**
      ``bash
       cd star-wars-api-fetcher
3.  **Make sure you have the requests library installed**
      ```bash
       pip install requests
4.  **Run the script**
      ```bash
      python main.py
(Note: Change main.py to whatever you named your Python file).

---

## 🧠 What I Learned
Through building this project, I gained practical understanding of:
* **APIs (Application Programming Interfaces):** How client applications communicate with web servers to get data.
* **JSON Formatting:** How to navigate and extract values from nested dictionaries and lists returned by the API.
* **The requests Module:** Using requests.get() and validating responses with .raise_for_status().
* **Resilient Code:** Using try-except blocks (specifically catching requests.exceptions.HTTPError) to handle situations where a URL might be wrong or the server is down.
* **String Manipulation:** Using .strip().lower() to clean user input before passing it into a URL string.

## 🔮 Future Upgrades
While this script perfectly serves its current purpose, here are some features I plan to add as my Python skills progress:
* **Data Export:** Implementing pandas to convert the extracted JSON data into a clean .csv file for further analysis.
* **Dynamic Key Handling:** Using the .get() method to handle categories that don't have a "name" attribute (like "films" which uses "title").
* **Input Validation:** Adding a while loop to ensure the user only types valid categories.
* **Pagination:** Writing logic to fetch all pages of the API data, not just the first page.
