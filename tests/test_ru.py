# -*- encoding: utf-8 -*-
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA
from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


class Num2WordsRUTest(TestCase):

    def test_cardinal(self):
        self.assertEqual(num2words(100, lang='ru'), "сто")
        self.assertEqual(num2words(101, lang='ru'), "сто один")
        self.assertEqual(num2words(110, lang='ru'), "сто десять")
        self.assertEqual(num2words(115, lang='ru'), "сто пятнадцать")
        self.assertEqual(num2words(123, lang='ru'), "сто двадцать три")
        self.assertEqual(num2words(1000, lang='ru'), "одна тысяча")
        self.assertEqual(num2words(1001, lang='ru'), "одна тысяча один")
        self.assertEqual(num2words(2012, lang='ru'), "две тысячи двенадцать")
        self.assertEqual(
            num2words(12519.85, lang='ru'),
            "двенадцать тысяч пятьсот девятнадцать запятая восемьдесят пять")
        self.assertEqual(
            num2words(1234567890, lang='ru'),
            "один миллиард двести тридцать четыре миллиона пятьсот "
            "шестьдесят семь тысяч восемьсот девяносто")
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='ru'),
            "двести пятнадцать нониллионов четыреста шестьдесят один "
            "октиллион четыреста семь септиллионов восемьсот девяносто "
            "два секстиллиона тридцать девять квинтиллионов два квадриллиона "
            "сто пятьдесят семь триллионов сто восемьдесят девять миллиардов "
            "восемьсот восемьдесят три миллиона девятьсот одна тысяча "
            "шестьсот семьдесят шесть")
        self.assertEqual(
            num2words(719094234693663034822824384220291, lang='ru'),
            "семьсот девятнадцать нониллионов девяносто четыре октиллиона "
            "двести тридцать четыре септиллиона шестьсот девяносто три "
            "секстиллиона шестьсот шестьдесят три квинтиллиона тридцать "
            "четыре квадриллиона восемьсот двадцать два триллиона восемьсот "
            "двадцать четыре миллиарда триста восемьдесят четыре миллиона "
            "двести двадцать тысяч двести девяносто один")
        self.assertEqual(num2words(5, lang='ru'), "пять")
        self.assertEqual(num2words(15, lang='ru'), "пятнадцать")
        self.assertEqual(num2words(154, lang='ru'), "сто пятьдесят четыре")
        self.assertEqual(
            num2words(1135, lang='ru'), "одна тысяча сто тридцать пять"
        )
        self.assertEqual(
            num2words(418531, lang='ru'),
            "четыреста восемнадцать тысяч пятьсот тридцать один"
        )
        self.assertEqual(
            num2words(1000139, lang='ru'), "один миллион сто тридцать девять"
        )

    def test_floating_point(self):
        self.assertEqual(num2words(5.2, lang='ru'), "пять запятая два")
        self.assertEqual(
            num2words(561.42, lang='ru'),
            "пятьсот шестьдесят один запятая сорок два"
        )

    def test_to_ordinal(self):
        self.assertEqual(num2words(0, lang='ru', to='ordinal'), "нулевой")
        self.assertEqual(num2words(1, lang='ru', to='ordinal'), "первый")
        self.assertEqual(num2words(3, lang='ru', to='ordinal'), "третий")
        self.assertEqual(num2words(14, lang='ru', to='ordinal'), "четырнадцатый")
        self.assertEqual(num2words(62, lang='ru', to='ordinal'), "шестьдесят второй")
        self.assertEqual(num2words(100, lang='ru', to='ordinal'), "сотый")
        self.assertEqual(num2words(101, lang='ru', to='ordinal'), "сто первый")
        self.assertEqual(num2words(600, lang='ru', to='ordinal'), "шестисотый")
        self.assertEqual(num2words(555, lang='ru', to='ordinal'), "пятьсот пятьдесят пятый")
        self.assertEqual(num2words(999, lang='ru', to='ordinal'), "девятьсот девяносто девятый")
        self.assertEqual(num2words(1000, lang='ru', to='ordinal'), "тысячный")
        self.assertEqual(num2words(1001, lang='ru', to='ordinal'), "одна тысяча первый")
        self.assertEqual(num2words(2002, lang='ru', to='ordinal'), "две тысячи второй")
        self.assertEqual(num2words(2012, lang='ru', to='ordinal'), "две тысячи двенадцатый")
        self.assertEqual(num2words(1110, lang='ru', to='ordinal'), "одна тысяча сто десятый")
        self.assertEqual(num2words(14999, lang='ru', to='ordinal'), "четырнадцать тысяч девятьсот девяносто девятый")
        self.assertEqual(num2words(15000, lang='ru', to='ordinal'), "пятнадцатитысячный")
        self.assertEqual(num2words(15200, lang='ru', to='ordinal'), "пятнадцать тысяч двухсотый")
        self.assertEqual(num2words(110000, lang='ru', to='ordinal'), "стадесятитысячный")
        self.assertEqual(num2words(500000, lang='ru', to='ordinal'), "пятисоттысячный")
        self.assertEqual(num2words(550000, lang='ru', to='ordinal'), "пятисотпятидесятитысячный")
        self.assertEqual(num2words(3000000, lang='ru', to='ordinal'), "трёхмиллионный")
        self.assertEqual(num2words(95000000, lang='ru', to='ordinal'), "девяностапятимиллионный")
        self.assertEqual(num2words(122000000, lang='ru', to='ordinal'), "стадвадцатидвухмиллионный")
        self.assertEqual(num2words(5156168518000, lang='ru', to='ordinal'), "пять триллионов сто пятьдесят шесть миллиардов "
            "сто шестьдесят восемь миллионов пятисотвосемнадцатитысячный")
        self.assertEqual(num2words(40000000000000000000, lang='ru', to='ordinal'), "сорокаквинтиллионный") #10**18 

    def test_to_currency(self):
        self.assertEqual(
            num2words(1.0, lang='ru', to='currency', currency='EUR'),
            'один евро, ноль центов'
        )
        self.assertEqual(
            num2words(1.0, lang='ru', to='currency', currency='RUB'),
            'один рубль, ноль копеек'
        )
        self.assertEqual(
            num2words(1234.56, lang='ru', to='currency', currency='EUR'),
            'одна тысяча двести тридцать четыре евро, пятьдесят шесть центов'
        )
        self.assertEqual(
            num2words(1234.56, lang='ru', to='currency', currency='RUB'),
            'одна тысяча двести тридцать четыре рубля, пятьдесят шесть копеек'
        )
        self.assertEqual(
            num2words(10111, lang='ru', to='currency', currency='EUR',
                      seperator=' и'),
            'сто один евро и одиннадцать центов'
        )
        self.assertEqual(
            num2words(10121, lang='ru', to='currency', currency='RUB',
                      seperator=' и'),
            'сто один рубль и двадцать одна копейка'
        )
        self.assertEqual(
            num2words(10122, lang='ru', to='currency', currency='RUB',
                      seperator=' и'),
            'сто один рубль и двадцать две копейки'
        )
        self.assertEqual(
            num2words(10121, lang='ru', to='currency', currency='EUR',
                      seperator=' и'),
            'сто один евро и двадцать один цент'
        )
        self.assertEqual(
            num2words(-1251985, lang='ru', to='currency', currency='EUR',
                      cents=False),
            'минус двенадцать тысяч пятьсот девятнадцать евро, 85 центов'
        )
        self.assertEqual(
            num2words('38.4', lang='ru', to='currency', seperator=' и',
                      cents=False, currency='EUR'),
            "тридцать восемь евро и 40 центов"
        )
