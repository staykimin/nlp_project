
# NLP Project By Python Newbie
<p align="center"><img width="33%" src="Untitled.jpeg"></p>

NLP (Natural Language Processing) adalah cabang dari kecerdasan buatan yang berhubungan dengan interaksi antara komputer dan manusia menggunakan bahasa alami, di project ini kita mengembangkan NLP yang menggunakan bahasa Indonesia Yang Bersifat Open Source Yang Digagas Oleh Anggota Grup Python Newbie.

Dalam project ini Kita bertujuan untuk mengembangkan NLP khusus bahasa Indonesia agar bisa lebih akurat dan presisi guna mendapatkan hasil yang maksimal dalam berinteraksi dengan komputer

## Index List
- [Sumber Dataset](#Sumber_Dataset)
- [Dataset](#Dataset)
- [Tokenizer](#Tokenizer)
- [Collabolator](#Collabolator)
- [Scraping](#Scraping)


## Sumber_Dataset
Pengumpulan dataset menggunakan teknik scraping dari bebagai artikel berita nasional yang meliputi :

- [Antara News](https://www.antaranews.com/)
## Dataset
- [Dataset Antara News](https://raw.githubusercontent.com/staykimin/nlp_project/kimin/Dataset/datasetv1.min)

Dataset Disimpan Dalam Format JSON dan Memiliki Beberapa Parameter Antara Lain

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `integer` | ID Dari Dataset |
| `id_sumber` | `integer` | ID Dari Sumber Dataset |
| `link_sumber` | `text` | Link Dari Artikel |
| `judul` | `text` | Judul Dari Artikel |
| `raw_text` | `text` | Isi Content / Artikel Tersebut |
| `publised_date` | `text` | Tanggal Publish Artikel |

| ID Sumber | Website Name     |
| :-------- | :------- |
| `1` | `Antara News` |




## Tokenizer
Tokenizer Dilakukan Menggunakan library Transformers Dengan Metode byte-level
## Instalasi & Runing Program

Instalasi Modul Yang Di perlukan
```python
pip install transformers
```
Import Library Ke Dalam Script Python
```python
from tokenizers.implementations import ByteLevelBPETokenizer
```
Import Model
```python
tokenizer = ByteLevelBPETokenizer.from_file("/model/kimin_tokenizer-vocab.json", "/model/kimin_tokenizer-merges.txt")
```
Proses tokenizer
```python
text= "iNI ADALAH CONTOH text yang Akan Di Tokenizer"
encoded = tokenizer.encode(text)
tokens = encoded.tokens
token_ids = encoded.ids
sub_tokens = encoded.tokens[1:-1]
```
Proses Decode Token
```python
decoded_text = tokenizer.decode(encoded.ids)
```
![Logo](hasil.png)


## Contact

Untuk Contact Person, Bisa Langsung Gabung Pada Link Grup WA Berikut

- [Belajar Python Newbie](https://chat.whatsapp.com/KVgG1OgRWJm14U3JpLqEhR)



