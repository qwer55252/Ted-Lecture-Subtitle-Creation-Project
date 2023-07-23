### 환경 설정

`git clone https://github.com/qwer55252/Ted-Lecture-Subtitle-Creation-Project.git`

`cd Ted-Lecture-Subtitle-Creation-Project`

`python3 -m venv make_srt_env`

`source make_srt_env/bin/activate`

`pip install -r requirements.txt`

### 실행 방법

1. 작성해 놓은 쉘 스크립트를 이용하는 방법
    
    ```bash
    sh make_srt.sh
    ```
    
2. 터미널에 직접 python 명령어를 작성하여 실행하는 방법
    
    ```bash
    python3 make_srt.py --url https://www.ted.com/talks/young_ha_kim_be_an_artist_right_now/transcript?language=ko
    ```