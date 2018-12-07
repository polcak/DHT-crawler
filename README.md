# DHT-crawler

This project was created as part of the TARZAN project and the bacherol thesis of Martin Vaško.
DHT-crawler is supposed to monitor
BitTorrent traffic with use of DHT tables. Tool has variety of usage and plenty
of space to expand.

### Getting Started
To run this program you are supposed to install prerequisites. When you do not want to
use it on your machine, there is a docker image to make container which is created for
safety. Setup.py installs script with sudo privileges to /usr/env/python. From there
you have to execute it from this repository with sudo privileges. There is only 1
file which is executable found at ./dht_crawler/exec.py.

### Prerequisites

To run this application you need python 3 and more. Bencoder and bencoder.pyx package.
```
pip3 install -r requirements.txt
or
pip3 install bencoder bencoder.pyx
```

### Outputs

Program has 3 types of output.
1. print IP addresses of detected peers.
2. db_format, which creates a JSON object carrying the detected peers, it can be send to server.
3. print_as_country format, which have translate IP-addresses to geolocation.
4. without formatting, which has every 5 seconds tells you about current status of crawling.

For example, to search for Debian netinst ISO torrent peers use the following command:

./dht\_crawler/exec.py --file debian-9.6.0-amd64-netinst.iso.torrent

If you know the info hash, you can also use the following command:

./dht\_crawler/exec.py --hash f71e7defc014563fc7d8ffe26f759b2518c30f34

### Tests

There are unit tests which are supposed to rely on application, that is still runnable.

### Contribution

There is possiblity to contribute, when something is not working or something should be
done better even refactor some part of library. Project is not well modularized so
there is probably good call to get better structure of this property.

## Built With

* [Fedora 26](https://getfedora.org/) - Distribution on which was tool developed.
* [Python3/3.6](https://www.python.org/) - Programming language which is used to run exec.py program.
