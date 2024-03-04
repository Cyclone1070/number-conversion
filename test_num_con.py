from num_con import numberToRoman, romanToNumber
import pytest


@pytest.mark.parametrize(
    "int, rom",
    [
        (1, "I"),
        (4, "IV"),
        (5, "V"),
        (9, "IX"),
        (10, "X"),
        (40, "XL"),
        (50, "L"),
        (90, "XC"),
        (100, "C"),
        (400, "CD"),
        (500, "D"),
        (900, "CM"),
        (1000, "M"),
        (3998, "MMMCMXCVIII"),
        (3999, "MMMCMXCIX"),
        (123, "CXXIII"),
        (678, "DCLXXVIII"),
        (1987, "MCMLXXXVII"),
        (399, "CCCXCIX"),
        (777, "DCCLXXVII"),
        (2000, "MM"),
        (0, "invalid number, please enter a number from 1 to 3999"),
        (4000, "invalid number, please enter a number from 1 to 3999"),
        (-198, "invalid number, please enter a number from 1 to 3999"),
    ],
)
def testNumberToRoman(int, rom):
    assert numberToRoman(int) == rom, "Got " + numberToRoman(int) + ", expected " + rom


@pytest.mark.parametrize(
    "rom, int",
    [
        ("I", 1),
        ("IV", 4),
        ("V", 5),
        ("IX", 9),
        ("X", 10),
        ("XL", 40),
        ("L", 50),
        ("XC", 90),
        ("C", 100),
        ("CD", 400),
        ("D", 500),
        ("CM", 900),
        ("M", 1000),
        ("MMMCMXCVIII", 3998),
        ("MMMCMXCIX", 3999),
        ("CXXIII", 123),
        ("DCLXXVIII", 678),
        ("MCMLXXXVII", 1987),
        ("CCCXCIX", 399),
        ("DCCLXXVII", 777),
        ("MM", 2000),
        ("ABC", "invalid Roman numeral"),
        ("IIIIX", "invalid Roman numeral"),
        ("imna", "invalid Roman numeral"),
        ("LIXli", "invalid Roman numeral"),
        ("MMMCCCIXVVVV", "invalid Roman numeral"),
        ("IIV", "invalid Roman numeral"),
        ("DLC", "invalid Roman numeral"),
        ("MCDIL", "invalid Roman numeral"),
    ],
)
def testRomanToNumber(rom, int):
    assert romanToNumber(rom) == int, (
        "Got " + str(romanToNumber(rom)) + ", expected " + str(int)
    )
