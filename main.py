import json
import os

def load_config():
    # config.json 파일 읽기
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config

def main():
    config = load_config()
    print(f"[{config['app_name']}] 프로그램을 시작합니다. (v{config['version']})")
    
    # GitHub Secrets 환경변수 가져오기 (설정되어 있지 않으면 기본값 사용)
    api_key = os.environ.get('MY_API_KEY', 'Local-Test-Key')
    print(f"사용 중인 API 키: {api_key[:4]}****")

if __name__ == "__main__":
    main()
