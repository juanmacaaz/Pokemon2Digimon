import requests

FILE_NORMAL = 'links_normal.txt'
FILE_SHINY = 'links_shiny.txt'

DOWNLOADED_FOLDER = '../dataset/'

def downloader(file_name):
    lines = open(file_name, 'r').read().split('\n')
    for line in lines:
        if line == '': continue
        url = line.split('/')
        name_img = DOWNLOADED_FOLDER + url[-2] + "/" + url[-1]
        print(f'Downloading {name_img}...')
        r = requests.get(line)
        open(f'{name_img}', 'wb').write(r.content)
        
if __name__ == '__main__':
    downloader(FILE_NORMAL)
    downloader(FILE_SHINY)