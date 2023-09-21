from scrapy.crawler import CrawlerProcess
from kimin.core_scraping import Scraping_Data
from kimin.core_db_web import DB_Core
import json

def main():
	process = CrawlerProcess()
	process.crawl(Scraping_Data)
	process.start()

if __name__ == "__main__":
	main()
	sin = DB_Core()
	data = sin.Get_Data('data_text')
	hasil = {"total_data":data['total_data'], "data":[]}
	for i in data['data']:
		i['created_at'] = str(i['created_at'])
		i['update_at'] = str(i['update_at'])
		hasil['data'].append(i)
	with open("datasetv1.min", "w", encoding="UTF-8") as dataku:
		json.dump(hasil, dataku, indent=4)
