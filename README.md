
# NLP Project By Python Newbie

Ini Adalah Project NLP (Natural Language Processing) Untuk Bahasa Indonesia Yang Bersifat Open Source Yang Digagas Oleh Anggota Grup Python Newbie.

Project Ini Bertujuan Untuk Mengembangkan NLP Khusus Bahasa Indonesia Agar Bisa Lebih Akurat dan Presisi Guna Mendapatkan Hasil Yang Maksimal

## Roadmap
- [Sumber Dataset](#Sumber_Dataset)
- [Dataset](#Dataset)
- [Model Pretained](#model)
- [Training Dataset](#training_dataset) 


# Sumber_Dataset
Dataset Dikumpulkan Menggunakan Teknik Scraping Dari Bebagai Artikel Berita Nasional Yang Meliputi :

- [Antara News](https://www.antaranews.com/)
# Dataset

Dataset Disimpan Dalam Format JSON dan Memiliki Beberapa Parameter Antara Lain

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `integer` | ID Dari Dataset |
| `id_sumber` | `integer` | ID Dari Sumber Dataset |
| `link_sumber` | `text` | Link Dari Artikel |
| `judul` | `text` | Judul Dari Artikel |
| `raw_text` | `text` | Isi Content / Artikel Tersebut |
| `publised_date` | `text` | Tanggal Publish Artikel |



## Instalasi & Runing Program

Instalasi Modul Yang Di perlukan
```python
pip install -r modul.min
```
Untuk Melakukan Scraping Data

```python
python scaping.py
```
