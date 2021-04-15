#Парсинг названий всех животных в Википедии

from bs4 import BeautifulSoup
import requests

url_list = [
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pageuntil=%D0%90%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F+%D0%BF%D1%83%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F+%D0%BF%D1%83%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D1%87%D1%91%D1%80%D0%BD%D0%B0%D1%8F+%D0%BA%D1%80%D1%8F%D0%BA%D0%B2%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D0%BD%D0%BE%D0%BB%D0%B8%D1%81-%D1%80%D1%8B%D1%86%D0%B0%D1%80%D1%8C#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D1%80%D0%BC%D0%B8%D0%BB%D0%BB%D0%B8%D1%84%D0%B5%D1%80%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B5+%D0%B7%D0%B5%D0%BB%D1%91%D0%BD%D1%8B%D0%B5+%D1%83%D0%B6%D0%B8#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%B0%D1%80%D1%85%D0%B0%D1%82%D0%BD%D0%B8%D1%86%D0%B0+%D0%B0%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D1%8F#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%B5%D0%BB%D0%BE%D0%B1%D1%80%D1%8E%D1%85%D0%B8%D0%B9+%D1%80%D1%8F%D0%B1%D0%BE%D0%BA#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%B5%D0%BB%D0%BE%D1%85%D0%B2%D0%BE%D1%81%D1%82%D1%8B%D0%B9+%D0%BE%D0%BB%D0%B5%D0%BD%D1%8C#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%B8%D1%80%D1%8E%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F+%D1%82%D0%B0%D0%BD%D0%B0%D0%B3%D1%80%D0%B0-%D0%BC%D0%B5%D0%B4%D0%BE%D1%81%D0%BE%D1%81#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%B5%D0%B3%D0%BB%D0%B0%D0%B7%D0%B0%D1%8F+%D1%81%D0%B5%D0%BB%D1%8C%D0%B4%D1%8C#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%BE%D1%80%D0%BE%D0%B4%D0%B0%D1%82%D1%8B%D0%B5+%D0%BA%D0%BE%D0%BB%D0%B8%D0%B1%D1%80%D0%B8#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D1%83%D0%BB%D0%B0%D0%B2%D0%BE%D0%B1%D1%80%D1%8E%D1%85+%D0%92%D0%B0%D0%BD%D0%B1%D1%80%D0%B8%D0%BD%D0%BA%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%92%D0%B0%D0%BB%D0%BB%D0%B0%D0%B1%D0%B8+%D0%9F%D0%B0%D1%80%D1%80%D0%B8#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%92%D0%B8%D1%88%D0%BD%D1%91%D0%B2%D1%8B%D0%B9+%D1%81%D0%BB%D0%BE%D0%BD%D0%B8%D0%BA#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B9+%D0%B2%D0%BE%D0%BB%D0%BA#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%93%D0%B0%D0%BF%D0%BB%D0%BE%D0%BA%D0%B0%D0%BD%D1%82%D0%BE%D0%B7%D0%B0%D0%B2%D1%80#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%93%D0%B8%D0%BC%D0%B0%D0%BB%D0%B0%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D0%BA%D0%B0%D0%B1%D0%B0%D1%80%D0%B3%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%93%D0%BE%D0%BB%D0%BE%D1%88%D0%B5%D0%B9%D0%BD%D1%8B%D0%B9+%D0%BF%D0%BB%D0%BE%D0%B4%D0%BE%D0%B5%D0%B4#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%93%D0%BE%D1%80%D0%BD%D0%B0%D1%8F+%D0%BA%D0%B0%D0%BF%D1%81%D0%BA%D0%B0%D1%8F+%D0%B7%D0%B5%D0%B1%D1%80%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%93%D1%83%D0%B9%D1%87%D0%B6%D0%BE%D1%83%D1%81%D0%BA%D0%B0%D1%8F+%D0%BB%D1%8F%D0%B3%D1%83%D1%88%D0%BA%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pageuntil=%D0%94%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D1%80%D1%8B%D0%BB%D0%B0%D1%8F+%D1%80%D1%8B%D0%B1%D0%B0-%D0%B1%D0%B0%D0%B1%D0%BE%D1%87%D0%BA%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%94%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D1%80%D1%8B%D0%BB%D0%B0%D1%8F+%D1%80%D1%8B%D0%B1%D0%B0-%D0%B1%D0%B0%D0%B1%D0%BE%D1%87%D0%BA%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%94%D1%80%D0%B5%D0%B2%D0%B5%D1%81%D0%BD%D0%B8%D1%86%D0%B5%D0%B2%D1%8B%D0%B5#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%95%D0%B3%D0%B8%D0%BF%D1%82%D0%BE%D0%BF%D0%B8%D1%82%D0%B5%D0%BA#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%96%D0%B5%D0%BB%D1%82%D0%BE%D0%BF%D0%BE%D1%8F%D1%81%D0%BD%D0%B8%D1%87%D0%BD%D0%B0%D1%8F+%D1%81%D0%BB%D0%B0%D0%B2%D0%BA%D0%BE%D0%B2%D0%B0%D1%8F+%D1%82%D0%B0%D0%BD%D0%B0%D0%B3%D1%80%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%96%D1%83%D1%80%D1%87%D0%B0%D0%BB%D0%BA%D0%B0+%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%BE%D0%B2%D0%B8%D0%B4%D0%BD%D0%B0%D1%8F#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%97%D0%B5%D0%BB%D1%91%D0%BD%D0%B0%D1%8F+%D0%BF%D1%80%D0%B8%D0%BD%D0%B8%D1%8F#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%97%D0%BB%D0%B0%D1%82%D0%BE%D0%B3%D0%BB%D0%B0%D0%B7%D0%B8%D0%BA%D0%B8#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%98%D0%B1%D0%B5%D1%80%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9+%D0%B7%D0%B0%D1%8F%D1%86#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%98%D0%BD%D0%B4%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9+%D0%BC%D0%B5%D0%B4%D0%BE%D1%83%D0%BA%D0%B0%D0%B7%D1%87%D0%B8%D0%BA#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9A%D0%B0%D0%BB%D0%B0%D0%BE-%D1%82%D1%80%D1%83%D0%B1%D0%B0%D1%87#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9A%D0%B0%D0%BF%D1%81%D0%BA%D0%B8%D0%B9+%D0%B4%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D0%BA%D1%80%D1%8B%D0%BB%D1%8B%D0%B9+%D0%BF%D0%BE%D0%BF%D1%83%D0%B3%D0%B0%D0%B9#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9A%D0%B0%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BA%D0%B0%D1%83%D0%B4%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9A%D0%B8%D1%82%D0%B0%D0%B9%D1%81%D0%BA%D0%B8%D0%B9+%D1%85%D0%BE%D0%BC%D1%8F%D1%87%D0%BE%D0%BA#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9A%D0%BE%D0%BB%D1%83%D0%BC%D0%B1%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D0%BB%D0%B0%D1%81%D0%BA%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9A%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D0%B9+%D1%82%D0%B8%D1%80%D0%B0%D0%BD%D0%BD#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9A%D0%BE%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D0%B7%D1%8B%D0%B5+%D0%B7%D0%BC%D0%B5%D0%B8#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B3%D1%80%D1%83%D0%B4%D1%8B%D0%B9+%D0%B4%D1%83%D1%82%D1%8B%D0%B9+%D1%83%D1%81%D0%B0%D1%87#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D1%8B%D0%B9+%D0%B8%D0%B1%D0%B8%D1%81#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9A%D1%80%D1%8B%D0%BB%D0%B0%D0%BD%D0%BE%D0%B2%D1%8B%D0%B5#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9A%D1%8E%D0%B2%D1%8C%D0%B5%D1%80%D0%BE%D0%B2+%D0%BF%D0%B0%D1%81%D1%82%D1%83%D1%88%D0%BE%D0%BA#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9B%D0%B5%D0%BF%D1%82%D0%BE%D1%80%D0%BE%D1%84%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9B%D0%B8%D1%81%D1%82%D0%BE%D0%B5%D0%B4+%D0%BC%D0%B5%D0%B4%D0%BD%D1%8B%D0%B9#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9B%D1%83%D1%86%D0%B8%D0%B0%D0%BD%D0%BE%D0%B2%D1%8B%D0%B5#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9C%D0%B0%D0%BB%D0%B0%D0%B1%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9+%D1%82%D0%BE%D0%BA#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9C%D0%B0%D0%BB%D1%8B%D0%B9+%D0%BE%D0%BB%D0%B8%D0%B2%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9+%D0%B8%D0%B1%D0%B8%D1%81#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9C%D0%B5%D0%B3%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%B8#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9C%D0%B8%D0%B4%D0%B8%D1%8F+%D0%93%D1%80%D0%B5%D1%8F#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9C%D0%BE%D1%80%D0%B6#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9C%D1%83%D1%85%D0%B0+%D1%81%D0%B8%D0%BD%D1%8F%D1%8F+%D0%BC%D1%8F%D1%81%D0%BD%D0%B0%D1%8F#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9D%D0%B0%D1%82%D0%B8%D0%BA%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9D%D0%BE%D0%B2%D0%BE%D0%BA%D0%B0%D0%BB%D0%B5%D0%B4%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9+%D0%BF%D1%91%D1%81%D1%82%D1%80%D1%8B%D0%B9+%D0%B3%D0%BE%D0%BB%D1%83%D0%B1%D1%8C#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9E%D0%B1%D1%8B%D0%BA%D0%BD%D0%BE%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F+%D1%86%D0%B8%D1%82%D0%B0%D1%80%D0%B8%D0%BD%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9E%D0%B3%D0%BD%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9+%D0%B1%D0%B0%D1%80%D1%85%D0%B0%D1%82%D0%BD%D1%8B%D0%B9+%D1%82%D0%BA%D0%B0%D1%87#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9E%D1%80%D0%B8%D0%BD%D0%BE%D0%BA%D1%81%D0%BA%D0%B8%D0%B9+%D0%B3%D1%83%D1%81%D1%8C#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9E%D1%88%D0%B5%D0%B9%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9+%D0%B2%D0%BE%D1%80%D0%BE%D0%B1%D1%8C%D0%B8%D0%BD%D1%8B%D0%B9+%D1%81%D1%8B%D1%87#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9F%D0%B0%D1%80%D0%B5%D0%B9%D0%B0%D0%B7%D0%B0%D0%B2%D1%80%D1%8B#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9F%D0%B5%D0%BD%D0%BE%D1%87%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9F%D0%B5%D1%81%D1%82%D1%80%D1%83%D1%88%D0%BA%D0%B0+%D0%A0%D0%B0%D0%B4%D0%B4%D0%B5#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9F%D0%BB%D0%B0%D0%B2%D1%82%D1%8B#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9F%D0%BE%D0%BB%D0%B8%D1%80%D0%B0%D1%85%D0%B8%D1%81#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9F%D1%80%D0%B0%D0%B7%D0%B4%D0%BD%D0%B8%D1%87%D0%BD%D1%8B%D0%B9+%D0%B0%D0%BC%D0%B0%D0%B7%D0%BE%D0%BD#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9F%D1%82%D0%B5%D1%80%D0%BE%D0%B8%D0%B4%D0%B8%D1%85%D1%82%D1%8B#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%9F%D1%8F%D1%82%D0%BD%D0%B8%D1%81%D1%82%D0%BE%D0%B1%D1%80%D1%8E%D1%85%D0%B0%D1%8F+%D1%84%D0%B8%D0%B4%D0%B6%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D0%B8%D0%B3%D1%83%D0%B0%D0%BD%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A0%D0%B5%D0%BB%D0%B8%D0%BA%D1%82%D0%BE%D0%B2%D0%B0%D1%8F+%D0%B3%D0%B0%D0%B4%D1%8E%D0%BA%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A0%D0%BE%D0%BA%D1%81%D0%B5%D0%BB%D0%BB%D0%B0%D0%BD%D0%BE%D0%B2+%D1%80%D0%B8%D0%BD%D0%BE%D0%BF%D0%B8%D1%82%D0%B5%D0%BA#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A1%D0%B0%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5+%D0%B4%D1%8F%D1%82%D0%BB%D1%8B#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A1%D0%B2%D1%8F%D1%89%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F+%D0%B0%D0%BB%D1%8C%D1%86%D0%B8%D0%BE%D0%BD%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A1%D0%B5%D1%80%D0%B0%D1%8F+%D1%82%D0%B8%D1%80%D0%BA%D1%83%D1%88%D0%BA%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A1%D0%B6%D0%B0%D1%82%D0%BE%D0%B1%D1%80%D1%8E%D1%85+%D0%A4%D0%BE%D0%BD%D0%BA%D0%BE%D0%BB%D0%BE%D0%BC%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A1%D0%B8%D0%BD%D0%BE%D1%84%D0%BE%D0%BD%D0%B5%D1%83%D1%81#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A1%D0%BA%D1%80%D1%8B%D1%82%D0%BE%D1%83%D1%85%D0%B8%D0%B5+%D0%B0%D0%B3%D0%B0%D0%BC%D1%8B#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A1%D0%BE%D0%BC%D0%B8%D0%BA-%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D1%91%D1%80%D1%82%D1%8B%D1%88#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A1%D1%82%D0%B5%D0%BF%D0%BD%D0%B0%D1%8F+%D0%BF%D1%83%D1%81%D1%82%D0%B5%D0%BB%D1%8C%D0%B3%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A1%D1%83%D1%80%D0%BE%D0%BA+%D0%9C%D0%B5%D0%BD%D0%B7%D0%B1%D0%B8%D1%80%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A2%D0%B5%D0%BB%D0%B5%D0%BD%D0%BE%D0%BC%D1%83%D1%81%D1%8B#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A2%D0%B8%D1%80%D0%B8%D0%BA%D0%B0#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A2%D0%BE%D0%BD%D0%BA%D0%BE%D0%BF%D0%BE%D0%B7%D0%B2%D0%BE%D0%BD%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A2%D1%80%D0%BE%D0%B3%D0%BE%D0%BD%D1%82%D0%B5%D1%80%D0%B8%D0%B9#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A3%D0%B4%D0%BE%D0%B4%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BD%D1%8B%D0%B5#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A4%D0%B0%D0%B7%D0%B0%D0%BD%D0%BE%D0%B2%D1%8B%D0%B5+%28%D0%BF%D0%BE%D0%B4%D1%81%D0%B5%D0%BC%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%BE%29#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A5%D0%B0%D0%BF%D1%82%D0%BE%D0%B4%D1%83%D1%81%D1%8B#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A5%D1%80%D1%83%D1%81%D1%82%D0%B0%D0%BD#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A6%D0%B8%D0%BD%D0%BE%D0%B3%D0%BD%D0%B0%D1%82#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A7%D0%B5%D1%80%D0%BD%D0%BE%D0%B1%D1%80%D1%8E%D1%88%D0%BA%D0%B8#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A7%D0%B5%D1%80%D0%BD%D0%BE%D1%88%D0%B0%D0%BF%D0%BE%D1%87%D0%BD%D1%8B%D0%B9+%D1%85%D0%B5%D0%BC%D0%B8%D1%81%D0%BF%D0%B8%D0%BD%D0%B3%D1%83%D1%81#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A7%D0%B5%D1%88%D1%83%D0%B9%D1%87%D0%B0%D1%82%D0%BE%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D1%8B%D0%B9+%D0%BE%D1%88%D0%B5%D0%B9%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9+%D0%BF%D0%BE%D0%BF%D1%83%D0%B3%D0%B0%D0%B9#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A8%D0%B8%D1%80%D0%BE%D0%BA%D0%BE%D0%BA%D0%BB%D1%8E%D0%B2%D1%8B%D0%B9+%D1%82%D0%BE%D0%B4%D0%B8#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%A9%D0%B8%D1%82%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5+%D1%81%D1%86%D0%B8%D0%BD%D0%BA%D0%B8#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%AD%D1%81%D1%82%D0%B5%D0%BC%D0%BC%D0%B5%D0%BD%D0%BE%D0%B7%D1%83%D1%85%D0%B8#mw-pages',
    'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%AF%D0%B2%D0%B0%D0%BD%D1%82%D1%80%D0%BE%D0%BF#mw-pages',

    ]
animals = []
a = []
b = []
v = []
g = []
d = []
e = []
yo = []
zh = []
z = []
ii = []
ikrat = []
k = []
l = []
m = []
nn = []
o = []
pp = []
rr = []
s = []
t = []
u = []
f = []
h = []
c = []
ch = []
sh = []
sha = []
eh = []
yu = []
ya = []



def pars():
    p = 0
    while p < len(url_list):
        r = requests.get(url_list[p])
        soup = BeautifulSoup(r.text, 'html.parser')
        div = soup.find('div', {'class': 'mw-category-group'})
        n = 0
        for an in div.find_all('a'):
            animals.append(an.get_text())
            n += 1
        p += 1
        for i in animals:
            if i[0] == 'А':
                a.append(i)
            elif i[0] == 'Б':
                b.append(i)
            elif i[0] == 'В':
                v.append(i)
            elif i[0] == 'Г':
                g.append(i)
            elif i[0] == 'Д':
                d.append(i)
            elif i[0] == 'Е':
                e.append(i)
            elif i[0] == 'Ё':
                yo.append(i)
            elif i[0] == 'Ж':
                zh.append(i)
            elif i[0] == 'З':
                z.append(i)
            elif i[0] == 'И':
                ii.append(i)
            elif i[0] == 'Й':
                ikrat.append(i)
            elif i[0] == 'К':
                k.append(i)
            elif i[0] == 'Л':
                l.append(i)
            elif i[0] == 'М':
                m.append(i)
            elif i[0] == 'Н':
                nn.append(i)
            elif i[0] == 'О':
                o.append(i)
            elif i[0] == 'П':
                pp.append(i)
            elif i[0] == 'Р':
                rr.append(i)
            elif i[0] == 'С':
                s.append(i)
            elif i[0] == 'Т':
                t.append(i)
            elif i[0] == 'У':
                u.append(i)
            elif i[0] == 'Ф':
                f.append(i)
            elif i[0] == 'Х':
                h.append(i)
            elif i[0] == 'Ц':
                c.append(i)
            elif i[0] == 'Ч':
                ch.append(i)
            elif i[0] == 'Ш':
                sh.append(i)
            elif i[0] == 'Щ':
                sha.append(i)
            elif i[0] == 'Э':
                eh.append(i)
            elif i[0] == 'Ю':
                yu.append(i)
            elif i[0] == 'Я':
                ya.append(i)
    print('А:', len(a))
    print('Б:', len(b))
    print('В:', len(v))
    print('Г:', len(g))
    print('Д:', len(d))
    print('Е:', len(e))
    print('Ё:', len(yo))
    print('Ж:', len(zh))
    print('З:', len(z))
    print('И:', len(ii))
    print('Й:', len(ikrat))
    print('К:', len(k))
    print('Л:', len(l))
    print('М:', len(m))
    print('Н:', len(nn))
    print('О:', len(o))
    print('П:', len(pp))
    print('Р:', len(rr))
    print('С:', len(s))
    print('Т:', len(t))
    print('У:', len(u))
    print('Ф:', len(f))
    print('Х:', len(h))
    print('Ц:', len(c))
    print('Ч:', len(ch))
    print('Ш:', len(sh))
    print('Щ:', len(sha))
    print('Э:', len(eh))
    print('Ю:', len(yu))
    print('Я:', len(ya))

pars()
