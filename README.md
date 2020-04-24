# Wattpad txt scraper

Based on [Wattpad Epub Scraper](https://github.com/de3sw2aq1/wattpad-ebook-scraper)

Scrape Wattpad stories into several txt files and images files for offline reading.

Please use this for personal use only.

## Usage

List one or more story or chapter URLs as command line arguments.

```
$ python3 scrape.py http://www.wattpad.com/story/9876543-example-story http://www.wattpad.com/story/9999999-example-story-2
```

Or feed it a list of URLs, one per line, via standard input.

```
$ python3 scrape.py < list_of_story_urls.txt
```

You may convert the epub to a mobi file with `kindlegen` or similar tools if desired.

## Details

This uses documented and undocumented portions of the Wattpad API. The undocumented portions of the API allow downloading story text, which conceivably could break in the future.

The story details API call is also undocumented and is from the internal v3 API used by the Android app. This would be a very useful API call to make public.

The chapters are assembled into an epub with epubbuilder, but nothing is really done to clean up the HTML. Epub files are supposed to be fully valid XHTML.

## Dependencies

Depends on [requests](http://python-requests.org), [python-dateutil](http://labix.org/python-dateutil) and [smartypants](https://pypi.python.org/pypi/smartypants/).

Install them with `pip`:

```
$ pip install requests python-dateutil smartypants bs4
```

## TODO

*   Verify the user input to actually be a valid story URL (regex).
*   Slow down downloads to comply with the requirement that "any automated system [...] that accesses the Website in a manner that sends more request messages to the Wattpad.com servers in a given period of time than a human can reasonably produce in the same period by using a conventional on-line web browser" from the [terms of service](http://www.wattpad.com/terms).
    -   That said, this probably violates the rest of the ToS everywhere else, but may as well be nice and not thrash sites with fast downloads.
*   Actually do error checking on API responses
