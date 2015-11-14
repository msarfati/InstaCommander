# InstaCommander
By Michael Sarfati (michael.sarfati@utoronto.ca), 2015

## Installation
### Make Virtual Environment
```bash
mkvirtualenv -p `which python3` -a . instacommander
```
```bash
make install
```

## Application Screenshot

![alt text](docs/screenshots/Screenshot_2015-11-13_18-05-35.png "InstaCommander prototype")

## Roadmap

### Towards version 1 (Current)
* Use of modular, clean and maintainable design pattern, and standardization of InstaCommander widgets and user conventions
* Graceful decay support - InstaCommander should be able to gracefully decay its color and unicode support in terminals with less and less color range, without losing user functionality

### Future plans

## Contributing

### Toolchain
* [python-instagram](https://github.com/Instagram/python-instagram) - Tumblr API wrapper compatible for Python 3
* [urwid](http://urwid.org/) - Console interface toolkit
* [Pillow](https://python-pillow.github.io/) - Python imaging library, to render images into ASCII/ANSI art
* [libcaca](http://caca.zoy.org/wiki/libcaca) - Another imaging library

## Kudos
* [img2txt](https://github.com/hit9/img2txt)
* 