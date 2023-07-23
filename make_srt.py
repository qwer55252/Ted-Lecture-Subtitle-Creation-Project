import argparse
import json
import requests
from bs4 import BeautifulSoup



def time_conversion(time: int):
    '''
        시간 변환 함수
        (예시) 971226(int) -> "00:16:11,226"(str)
    '''
    sec, ms = divmod(time, 1000)
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)

    time_format = '%02d'%(h) + ':%02d'%(m) + ':%02d'%(s) + ',%03d'%(ms)
    return time_format # str

def make_srt(url: str):
    response = requests.get(url)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        data = soup.select("#__NEXT_DATA__")
        dict_str = data[0].text
        dict_data = json.loads(dict_str)
        paragraphs = dict_data['props']['pageProps']['transcriptData']['translation']['paragraphs']
        
        text_list = []
        time_list = []
        for paragraph in paragraphs:
            cues = paragraph['cues']
            for cue in cues:
                text_list.append(cue["text"])
                time_list.append(cue["time"])

        # 길이 다를 경우 예외 처리
        if len(text_list) != len(time_list):
            raise Exception('text 수와 time 수가 다릅니다!')   
        else:
            list_len = len(time_list)
        
        # 자막(.srt) 포맷으로 가공
        srt_data = ""
        for i, (text, time) in enumerate(zip(text_list, time_list)):
            start_time = time
            if i != list_len - 1:
                end_time = time_list[i+1] - 24
            else:
                end_time = start_time + 24
            start_time = time_conversion(start_time)
            end_time = time_conversion(end_time)
            # print(f'start_time : {start_time}')
            # print(f'end_time : {end_time}')

            srt_data += f"{i+1}\n{start_time} --> {end_time}\n{text}\n\n"
            # print(srt_data)
        
        # 자막(.srt) 파일 생성
        with open("ted_talk_subtitle.srt", "w", encoding="utf-8") as file:
            file.write(srt_data)
    else:
        print(f'Status Code : {response.status_code}')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, default='https://www.ted.com/talks/young_ha_kim_be_an_artist_right_now/transcript?language=ko')
    args = parser.parse_args()
    
    # 크롤링할 TED 영상 링크
    url = args.url

    # 자막 생성
    make_srt(url)
    