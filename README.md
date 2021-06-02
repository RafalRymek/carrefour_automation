# Carrefour online shopping script

## Automation test script in python which help book delivery date and add products to basket

## Following tech stack is using:  
python  
unittest

## Before your first run a test you should:

1. Create account on https://zakupycodzienne.carrefour.pl/
2. Create settings.py file where you need to put:

`USER_LOGIN = "your login"`  
`USER_PASSWORD = "your password"`    
`ZAKUPYCODZIENNE_URL = "https://zakupycodzienne.carrefour.pl/"`

You need to choose your products:  
`milk = "Mlekovita Mleko Polskie spożywcze 3,2% 1 l"`  
`yogurt = "Bakoma Jogurt Bio naturalny 140 g"`  
`cheese = "Sierpc Ser królewski 135 g"`

And create your shopping list:  
`shopping_list = [milk, yogurt, cheese, cottage_cheese]`

And choose your shop from list of shops on carrefour page and add it:
to `delivery_date_page.py` e.g. "Kraków, Pokoju 44 - Carrefour Kraków Plaza"

## Setup

1. open terminal
2. run `git clone https://github.com/RafalRymek/bootcamp_selenium_bdd_framework` to clone repository
3. run `cd bootcamp_selenium_bdd_framework` to move to local repository folder
4. run `pipenv install` to set up all necessary dependencies from Pipfile.lock
5. run `pipenv shell` to be able to use all pipenv dependencies from terminal

## Test execution
1. run `export PYTHONPATH=`pwd`` 
2. run `python3 tests/test_purchase.py`
