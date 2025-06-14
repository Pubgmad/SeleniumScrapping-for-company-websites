### Website Content Scraper using Selenium
This Python script scrapes all readable text from the <main> or <body> section of a website and its internal links, then prints them in a structured format.

### Project Structure


selenium-scrap/
│
├── chromedriver-win64/
│   └── chromedriver.exe
│
├── main.py
├── scraped_output.txt
└── README.md


 Requirements
Python 3.7+

Google Chrome (any recent version)

ChromeDriver matching your Chrome version

### Installation
Clone the repository:
git clone https://github.com/your-username/selenium-scraper.git
cd selenium-scraper


### Install dependencies:
pip install selenium
Download ChromeDriver:

Visit: https://googlechromelabs.github.io/chrome-for-testing/

Select your Chrome version (e.g., 137.0.7151.104)

Download chromedriver-win64.zip, extract it, and place chromedriver.exe in the project folder or somewhere in your system PATH.

### How to Run
python main.py
Enter a website URL when prompted (e.g., https://axtr.in)

The script will:

Open the page using headless Chrome

Extract readable text from the main content

Visit internal links recursively

Print each page’s content with a ===== PAGE: <url> ===== header

Save everything to scraped_output.txt

### Example Output

===== PAGE: https://axtr.in/ =====
About
Services
Transform Your SaaS to AgenticSaaS
...

===== PAGE: https://axtr.in/services =====
What we do
Face Recognition
...
### Customization
You can modify the script to:

Save each page to separate .txt files

Output content as JSON

Filter specific HTML tags

### License
MIT License