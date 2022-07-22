import requests

from bs4 import BeautifulSoup as bs


wiki_root_url = "https://ru.wikipedia.org"
page_url = "/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pageuntil=%D0%90%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B9+%D0%BC%D1%83%D1%80%D0%B0%D0%B2%D0%B5%D0%B9-%D0%BF%D0%BE%D1%80%D1%82%D0%BD%D0%BE%D0%B9#mw-pages"

animals_abc_dict = {}
all_animals = []

# Этот счётчик нужен для определения первой и последней страницы
# я заметил что на первой и последней только по одной кнопке (на самом деле они дублируются сверху и снизу)
counter = 0
while counter < 2:
    url = wiki_root_url + page_url
    response = requests.get(url)
    # мало ли)
    assert response.status_code == 200, "Something got wrong"

    soup = bs(response.content, "html.parser")

    mw_pages = soup.find("div", {"id": "mw-pages"})
    
    # заметил что у кнопок у кнопок навигации есть атрибут title
    nav_buttons = mw_pages.find_all("a", {"title": "Категория:Животные по алфавиту"})
    # из-за дублирования на последней и первой странице 2 идентичные кнопки
    # на остальных по 2 кнопки (они также продублированны, т.е. на всех страницах кроме первой и последней по 4 кнопки)
    if len(nav_buttons) == 2:
        counter += 1

    # достаем из кнопки навигации ссылку на следующую страницу
    page_url = nav_buttons[1].attrs["href"]
    
    print(page_url)

    mw_category_group = mw_pages.find("div", {"class": "mw-category-group"})
    animal_links = mw_category_group.find_all("a")
    
    for link in animal_links:
        animal_name = link.text
        all_animals.append(animal_name)
        try:
            animals_abc_dict[animal_name[0].upper()] += 1
        except KeyError:
            animals_abc_dict[animal_name[0].upper()] = 1


print(all_animals)
print(animals_abc_dict)
