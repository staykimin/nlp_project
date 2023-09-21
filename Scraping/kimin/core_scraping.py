from kimin.core_db_web import DB_Core
from bs4 import BeautifulSoup
import scrapy, re, json

class Scraping_Data(scrapy.Spider):
	def __init__(kimin):
		kimin.config = kimin.Get_Config()
		kimin.name = "Kimin_Scraping"
		kimin.database = DB_Core()

	def Get_Config(kimin):
		with open("config.min", "r", encoding="UTF-8") as dataku:
			hasil = json.loads(dataku.read())
		return hasil

	def start_requests(kimin):
		if kimin.config is None:
			print("List URL Not Set")
		else:
			for i in kimin.config['list_sumber']:
				yield scrapy.Request(i['url'], callback=kimin.Parser, cb_kwargs={"id_sumber":i['id_sumber']})

	def Parser(kimin, response, id_sumber):
		kolom = ["id_sumber", "link_sumber", "judul", "publised_date"]
		for i in response.xpath("//item"):
			judul = i.xpath('title/text()').get()
			if id_sumber == 1:
				link = i.xpath("link/text()").get()
			elif id_sumber == 2:
				link = i.xpath("guid/text()").get()
			publised_date = i.xpath('pubDate/text()').get()
			value = [id_sumber, link, judul, publised_date]
			if link.find("video") == -1 and link.find("foto") == -1:
				if kimin.database.Check_Data('data_text', 'link_sumber', link) is False:
					kimin.database.Add_Data("data_text", kolom, value)
					yield scrapy.Request(link, callback=kimin.Get_Content, cb_kwargs={"id_sumber":id_sumber})

	def Clear_Text(kimin, data):
		# Membersihkan teks dari elemen HTML
		cleaned_text = re.sub(r'<.*?>', '', data)

		# Membersihkan spasi berlebih dan tanda tab
		cleaned_text = ' '.join(cleaned_text.split())

		# Membersihkan tanda yang dapat menyebabkan SQL error
		cleaned_text = re.sub(r'[\'";]', '', cleaned_text)
		return cleaned_text

	def Get_Content(kimin, response, id_sumber):

		# Mencari elemen <article> dengan class "post-wrapper clearfix"
		if id_sumber == 1:
			article = response.css('div.post-content.clearfix').extract_first()
		elif id_sumber == 2:
			detail_div = response.css('div.side-article.txt-article.multi-fontsize')
			p_elements = detail_div.css('p')
			for i in p_elements:
				print(kimin.Clear_Text(i.get))


		if article:
			# Membersihkan teks dari tag HTML, spasi berlebihan, dan tanda tab
			cleaned_article = ' '.join(article.split())

		post_content = response.css('div.post-content.clearfix').extract_first()
		if post_content:
			all_text = ''.join(response.css('div.post-content.clearfix::text').extract())
			cleaned_article = kimin.Clear_Text(cleaned_article)
			kimin.database.Update_Data('data_text', 'raw_text', cleaned_article, 'link_sumber', response.url)
			jam = kimin.database.Get_Time("%Y-%m-%d %H:%M:%S")
			kimin.database.Update_Data('data_text', 'update_at', jam, 'link_sumber', response.url)

