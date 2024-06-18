# 🌐Website Data Scraper - 100

## 📖Description
This script scrapes data from a list of websites and extracts the following information:
- Social Media Links
- Tech Stack (MVC, CMS, JS type, etc.)
- Meta Title
- Meta Description
- Payment Gateways (e.g., PayPal, Stripe, Razorpay)
- Website Language
- Category of Website

The extracted data is stored in a MySQL database. Moreover, 1.cvs is the exported data of MySQL database. 

## ⚙️Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `lxml` library
- `mysql-connector-python` library
- `python-Wappalyzer` library

## 🔍Setup Instructions
1. Clone the repository.  
   ```sh
   git clone https://github.com/smileagain6698/scrappy_100.git
2. Create the virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate
3. Install the required Python libraries:
   ```sh
   pip install requests beautifulsoup4 lxml mysql-connector-python python-Wappalyzer
4. Set-up your MySQL database
5. Add extensions to your vscode - SQLTools database management && SQLTools MySQL/MariaDB/TiDB Driver
6. Open SQLTools, select MySQL database and update `Connection Settings` with similar to the `settings.json` file and as per your database.
![image](https://github.com/smileagain6698/scrappy_100/assets/63532914/0827677d-0a01-4619-a9a3-3da734326500)
![image](https://github.com/smileagain6698/scrappy_100/assets/63532914/15715f43-5424-432e-ba57-2f8b627f03d3)
*(select MySQL)
![image](https://github.com/smileagain6698/scrappy_100/assets/63532914/aed7bd06-2397-4a39-b68d-04653b9909f2)
(password is your MySQL database password)
![image](https://github.com/smileagain6698/scrappy_100/assets/63532914/768dc1c1-f3d2-45fd-8618-ea81a583ae66)
8. Test your connection and Save Connection.
9. Run in terminal
   ```sh
   python main.py ```
![image](https://github.com/smileagain6698/scrappy_100/assets/63532914/9bf63773-a949-4bbf-a7b3-67ccf98f674f)
  
10. To open your database table, click on the plus icon in SQLTools
![image](https://github.com/smileagain6698/scrappy_100/assets/63532914/1fd2c923-084b-4809-b06f-13d5a1f7b491)

