import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os
import schedule
import time

def crawl_snackvideo(keywords):
    data = []
    
    for keyword in keywords:
        url = f"https://snackvideo.com/discover/{keyword}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Mengambil data dari script JSON-LD
        scripts = soup.find_all('script', type='application/ld+json')
        for script in scripts:
            json_data = script.string
            if json_data:
                video_data = json.loads(json_data)
                if 'itemListElement' in video_data:
                    for item in video_data['itemListElement']:
                        if item['@type'] == 'VideoObject':
                            video_info = {
                                'Keyword': keyword,
                                'Video ID': item['url'].split('/')[-1],
                                'Video URL': item['url'],
                                'Username': item['creator']['mainEntity']['alternateName'],
                                'Author': item['creator']['mainEntity']['name'],
                                'View': item['interactionStatistic'][0]['userInteractionCount'],
                                'Like': item['interactionStatistic'][1]['userInteractionCount'],
                                'Comment': item['commentCount'],
                                'Share': item['interactionStatistic'][2]['userInteractionCount'],
                                'Followers': item['creator']['mainEntity']['interactionStatistic'][1]['userInteractionCount'],
                                'Upload Date': item['uploadDate']
                            }
                            data.append(video_info)

    return data

def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

def main():
    keywords = ["kafe", "kopi"]
    data = crawl_snackvideo(keywords)
    
    # Menyimpan file Excel ke folder output
    output_folder = 'output'  # Ganti dengan path lengkap jika perlu
    os.makedirs(output_folder, exist_ok=True)  # Membuat folder jika belum ada
    output_file = os.path.join(output_folder, 'snackvideo_data.xlsx')
    
    save_to_excel(data, output_file)

# Scheduler
schedule.every().day.at("19:02").do(main)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)