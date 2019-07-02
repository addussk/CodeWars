#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

LICZBA_PROB = 5
liczba = random.randint(1, 10)



for proba in range(0, LICZBA_PROB):
    
    answer = input("Jaką liczbę od 1 do 10 mam na myśli? ")

    if liczba == int(answer):
        print("Zgadłeś! Dostajesz dlugopis!")
        break
    else : print(f'Niestety wylosowana liczba to: {liczba}')