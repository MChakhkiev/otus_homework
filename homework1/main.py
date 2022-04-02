import requests
from bs4 import BeautifulSoup
from requests import *
from urllib.parse import urlparse

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def parse_a(html):
    soup = BeautifulSoup(html, "html.parser")
    all_a = soup.findAll('a', href=True)
    return all_a


def get_all_a(url):
    print('Начало обработки')
    response = request('GET', url)
    if response.status_code == requests.codes.ok:
        parsed = parse_a(response.text)
        a_dict_main = {}
        a_dict_main[url] = []
        for a in parsed:
            a_dict_main[url].append(a['href'])
        a_dict_hrefs = {}
        for href in a_dict_main[url]:
            if href in ('/', '#'):
                pass
            else:
                if href[0] == '/':
                    href = urlparse(url).scheme+'://'+urlparse(url).netloc + href
                parsed2 = parse_a(request('GET', url).text)
                a_dict_hrefs[href] = []
                if len(parsed2) > 0:
                    for a2 in parsed2:
                        a_dict_hrefs[href].append(a2['href'])
        a_dict = a_dict_main | a_dict_hrefs
        return a_dict


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        url = input('Введите url (https://yandex.ru/): ')
        if url == '':
            pass
        else:
            print(urlparse(url))
            if urlparse(url).scheme and urlparse(url).netloc:
                break
    a_dict = get_all_a(url)
    print('парсинг закончен')
    while True:
        command = input('вывести результат:\nв терминале-1\nв файл-2\nВведите значение: ')
        if command == '1':
            for key, val in a_dict.items():
                print(f"{key}:\n")
                for i in val:
                    print(f"\t{i}")
            break
        elif command == '2':
            with open('parser.txt', 'w') as out:
                for key, val in a_dict.items():
                    out.write(f"{key}:\n")
                    for i in val:
                        out.write(f"\t{i}\n")
            break
