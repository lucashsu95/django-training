# Django Day1

## 初始化專案
```bash
python -m django startproject <name>
```

## 新增網頁應用專案
```bash
python -m django startapp <name>
```

## How to Run
```bash
python manage.py runserver
```

## 介紹

### 設定tempaltes

用vscode打html的格式可能是Django HTML這樣會沒有提示，要記得改成HTML。

設定路徑
`setting.py`裡的`TEMPLATES` -> `DIRS` <br>然後在裡面打`os.path.join(BASE_DIR,'templates')` ~~記得import os~~