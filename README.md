# Wattpad txt or fb2 scraper

[Russian instruction - Русская инструкция](https://github.com/Hell13Cat/WPD/blob/master/README-ru.md)

Based on [Wattpad Epub Scraper](https://github.com/de3sw2aq1/wattpad-ebook-scraper)

Scrape Wattpad stories into several txt files and images files or fb2 for offline reading.

Please use this for personal use only.

## Usage

List one or more story or chapter URLs as command line arguments.

```
$ python3 scrape.py [fb2/txt] http://www.wattpad.com/story/9876543-example-story http://www.wattpad.com/story/9999999-example-story-2 https://my.w.tt/ShortLinkExample
```

If you need to download all the books from the reading list

```
$ python3 getall.py list https://www.wattpad.com/list/882495357-list-link https://my.w.tt/ShortLinkExample
```

[Not stable] To save all lists from a profile

```
$ python3 getall.py profile Nickname
```

## Details

This uses documented and undocumented portions of the Wattpad API. The undocumented portions of the API allow downloading story text, which conceivably could break in the future.

The story details API call is also undocumented and is from the internal v3 API used by the Android app. This would be a very useful API call to make public.

## Dependencies

Install them with `pip`:

```
$ pip install requests python-dateutil smartypants bs4 cfscrape colorama
```

## TODO

*   Verify the user input to actually be a valid story URL (regex).
*   Slow down downloads to comply with the requirement that "any automated system [...] that accesses the Website in a manner that sends more request messages to the Wattpad.com servers in a given period of time than a human can reasonably produce in the same period by using a conventional on-line web browser" from the [terms of service](http://www.wattpad.com/terms).
    -   That said, this probably violates the rest of the ToS everywhere else, but may as well be nice and not thrash sites with fast downloads.
*   Actually do error checking on API responses
