import subprocess


def main():
    subprocess.run(
        ['python3', 'sayari_scraper/sayari_scraper/spiders/Sayari_Spider_X_Entity_Capture.py'])
    subprocess.run(['python3', 'graph_generation.py'])


if __name__ == '__main__':
    main()
