import requests  # Импорт библиотеки Requests
from bs4 import BeautifulSoup
import json


def main():
    entireManga = []
    actualPage = 0

    while True:
        page = actualPage
        if 0 <= page <= 5 or page > 44:
            page = pageHandler(page)

        url = 'https://mangajar.com/manga/bastard-hwang-youngchan-abs3gYV/chapter/' + str(page)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        imgs = soup.findAll('img', {"data-src": True})
        if imgs:
            urls = [img['data-src'] for img in imgs]
            for i in soup.select(".chapter-container > .chapter-images"):
                firstImg = i.find('img', class_='img-fluid page-image')['src']
                urls.insert(0, firstImg)
            urls_json = {
                'chapter': actualPage,
                'imgs': urls
            }
            entireManga.append(urls_json)
            print(actualPage)
            actualPage += 1
        else:
            break
    # end while

    entireManga_json = json.dumps(entireManga)
    with open("manga.json", "w") as my_file:
        my_file.write(entireManga_json)


def pageHandler(page):
    if page == 0:
        return '0_abs34Ek'
    elif page == 1:
        return '1_abs347j'
    elif page == 2:
        return '2_abs3eKO'
    elif page == 3:
        return '3_abs3ybk'
    elif page == 4:
        return '4_abs3859'
    elif page == 5:
        return '5_abs38wV'
    elif page == 45:
        return '45_abs3L4M'
    elif page == 46:
        return '46_abs3dBd'
    elif page == 47:
        return '47_abs30G5'
    elif page == 48:
        return '48_abs3caI'
    elif page == 49:
        return '49_abs3rs0'
    elif page == 50:
        return '50_abs3MWc'
    elif page == 51:
        return '51_abs3FIC'
    elif page == 52:
        return '52_abs31xk'
    elif page == 53:
        return '53_abs3oEp'
    elif page == 54:
        return '54_abs39Jp'
    elif page == 55:
        return '55_abs3OYe'
    elif page == 56:
        return '56_abs3kaD'
    elif page == 57:
        return '57_abs3HjP'
    elif page == 58:
        return '58_abs3fsQ'
    elif page == 59:
        return '59_abs3pfu'
    elif page == 60:
        return '60_abs3Opc'
    elif page == 61:
        return '61_abs3iwR'
    elif page == 62:
        return '62_abs34hG'
    elif page == 63:
        return '63_abs3duk'
    elif page == 64:
        return '64_abs3HCP'
    elif page == 65:
        return '65_abs36e3'
    elif page == 66:
        return '66_abs3WN0'
    elif page == 67:
        return '67_abs3vIv'
    elif page == 68:
        return '68_abs3e91'
    elif page == 69:
        return '69_abs3gTa'
    elif page == 70:
        return '70_abs38th'
    elif page == 71:
        return '71_abs3eSL'
    elif page == 72:
        return '72_abs3P6o'
    elif page == 73:
        return '73_abs32xL'
    elif page == 74:
        return '74_abs3hUv'
    elif page == 75:
        return '75_abs3llD'
    elif page == 76:
        return '76_abs3jXK'
    elif page == 77:
        return '77_abs36QM'
    elif page == 78:
        return '78_abs3C6s'
    elif page == 79:
        return '79_abs3ywk'
    elif page == 80:
        return '80_abs3KSS'
    elif page == 81:
        return '81_abs37PR'
    elif page == 82:
        return '82_abs34oZ'
    elif page == 83:
        return '83_abs3qBd'
    elif page == 84:
        return '84_abs3WxC'
    elif page == 85:
        return '85_abs3o5f'
    elif page == 86:
        return '86_abs3ujn'
    elif page == 87:
        return '87_abs3Zp5'
    elif page == 88:
        return '88_abs3ute'
    elif page == 89:
        return '89_abs3fQO'
    elif page == 90:
        return '90_abs3Cvy'
    elif page == 91:
        return '91_abs3qhe'
    elif page == 92:
        return '92_abs3DSw'
    elif page == 93:
        return '93_abs3Xdw'
    elif page == 94:
        return '94_abs3v99'
    else:
        return page


if __name__ == '__main__':
    main()
