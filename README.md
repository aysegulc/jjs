
JJ-Times Scraping Project
-------------------------

This scrapy project is built to extract contact details of Jiu Jitsu schools.

School logos and images are saved into `\images` directory.

Scraped items can be saved as json or csv files.


```bash
# Save items to csv file
scrapy crawl jjs -o jjs_schools.csv
# save items to json file
scrapy crawl jjs -o jjs_schools.json
```
