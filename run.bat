SET dic=%cd%
cd ./letrot_scraper
python %dic%\letrot_scraper\letrot_scraper\spiders\letrot_spider_meetings.py
python %dic%\letrot_scraper\letrot_scraper\spiders\letrot_spider_courses.py
python %dic%\letrot_scraper\devScripts\file_prettify.py
python %dic%\letrot_scraper\devScripts\to_uploadable.py
python %dic%\letrot_scraper\devScripts\csv_writer.py