import re
import sys
import os
import getpass
import requests

def input_nonempty(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val

def main():
    print("Введите данные для скачивания дистрибутива 1С")

    username = input_nonempty("Логин: ")
    password = getpass.getpass("Пароль: ")
    version = input_nonempty("Версия (например, 8.3.23.1688): ")

    session = requests.Session()
    r = session.get('https://releases.1c.ru')
    r.raise_for_status()
    html = r.text
    action_match = re.search(r'<form method="post" id="loginForm" action="([^"]+)"', html)
    execution_match = re.search(r'<input type="hidden" name="execution" value="([^"]+)"', html)

    if not action_match or not execution_match:
        print("Не удалось получить форму входа")
        sys.exit(1)

    action = action_match.group(1)
    execution = execution_match.group(1)

    login_url = 'https://login.1c.ru' + action

    login_data = {
        "inviteCode": "",       
        "execution": execution, 
        "_eventId": "submit",   
        "username": username,   
        "password": password    
    }

    resp = session.post(login_url, data=login_data)
    resp.raise_for_status()

    if 'TGC' not in session.cookies:
        print("Ошибка авторизации, проверьте логин и пароль")
        sys.exit(1)

    version_underscored = version.replace('.', '_')
    
    files = [
        (f"windows64full_{version_underscored}.rar", f"Platform\\{version_underscored}\\windows64full_{version_underscored}.rar"),
        (f"server32_{version_underscored}.zip", f"Platform\\{version_underscored}\\server32_{version_underscored}.zip"),
        (f"server64_{version_underscored}.zip", f"Platform\\{version_underscored}\\server64_{version_underscored}.zip"),
        (f"setuptc64_{version_underscored}.rar", f"Platform\\{version_underscored}\\setuptc64_{version_underscored}.rar"),
        (f"setuptc_{version_underscored}.rar", f"Platform\\{version_underscored}\\setuptc_{version_underscored}.rar"),
        (f"macos.thin.client_{version_underscored}.dmg", f"Platform\\{version_underscored}\\macos.thin.client_{version_underscored}.dmg")
    ]

    target_dir = os.path.join("W:\\1CDistr\\8.3", version)
    os.makedirs(target_dir, exist_ok=True)

    def get_direct_link(path):
        encoded_path = path.replace('\\', '%5c')  # Экранируем путь
        url = f"https://releases.1c.ru/version_file?nick=Platform83&ver={version}&path={encoded_path}"
        r = session.get(url)
        r.raise_for_status()
        match = re.search(r'href="([^"]+)">Скачать дистрибутив<', r.text)
        if not match:
            print(f"Не удалось получить прямую ссылку для: {path}")
            return None
        return match.group(1)

    def download_file(url, local_path):
        print(f"Скачивание: {local_path}")
        with session.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Файл сохранён: {local_path}")

    for filename, path in files:
        direct_url = get_direct_link(path)
        if direct_url:
            full_path = os.path.join(target_dir, filename)
            download_file(direct_url, full_path)

if __name__ == "__main__":
    main()
