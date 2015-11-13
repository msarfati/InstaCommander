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

## Roadmap

### Towards version 1 (Current)
* Use of modular, clean and maintainable design pattern, and standardization of InstaCommander widgets and user conventions
* Graceful decay support - InstaCommander should be able to gracefully decay its color and unicode support in terminals with less and less color range, without losing user functionality
* 

### Future plans

## Contributing

### Toolchain
* [python-instagram](https://github.com/Instagram/python-instagram) - Tumblr API wrapper compatible for Python 3
* [ObjectPath](https://pypi.python.org/pypi/objectpath/) - a specification for sanely querying JSON and Python objects
    - [ObjectPath](https://github.com/adriank/ObjectPath) Python library
* [urwid](http://urwid.org/) - Console interface toolkit
* [Requests](http://docs.python-requests.org/en/latest/) - handles other web requests
* [lxml](http://lxml.de/) - For the occasional scraping

### Tools still requiring research
* Rendering images into ANSI/ASCII art
* Rendering videos into ANSI/ASCII
* Render audio into 8bit
