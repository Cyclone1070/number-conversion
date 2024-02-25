from num_con import intToRom
import pytest

@pytest.mark.parametrize("int, rom", [
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
])
def test_int_to_rom(int, rom):
    assert intToRom(int) == rom, 'Should be ' + rom