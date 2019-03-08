#!/usr/bin/python
import time
import socket
from selenium import webdriver


def main():
    links = grab_magnet_links()
    add_links(links)


def grab_magnet_links():
    links = []
    with open("torrents.state.txt", "r") as fi:
        for ln in fi:
            if ln.startswith("S'magnet:"):
                link = ln.strip()[2: -1]  # To remove the S' at the beginning and the trailing '.
                links.append(link)  # Append it in the array
    return links


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def add_links(links):
    driver = webdriver.Chrome('./chromedriver')

    address = 'http://' + get_ip() + ':9091/transmission/web/'
    time.sleep(3)  # Give the get_ip() method a little time to run...

    driver.get(address)  # Open the URL address we grabbed.

    # Allow the user to login themselves. Can't figure out a way to automate this part.
    # Set to sleep for 15 seconds while the user enters their username / pass. Not ideal, but oh well.
    time.sleep(15)

    for link in links:
        driver.find_element_by_id("toolbar-open").click()
        driver.find_element_by_id('torrent_upload_url').send_keys(link)
        driver.find_element_by_id('upload_confirm_button').click()


if __name__ == '__main__':
    main()
