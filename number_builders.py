from typing import Callable
class NoLettersBuilderError(Exception):
    pass
def get_number_builder(letter: str) -> Callable[..., list[str]]:
    letter_builders = {
        '0': build_0_letter,
        '1': build_1_letter,
        '2': build_2_letter,
        '3': build_3_letter,
        '4': build_4_letter,
        '5': build_5_letter,
        '6': build_6_letter,
        '7': build_7_letter,
        '8': build_8_letter,
        '9': build_9_letter,
    }
    try:
        return letter_builders[letter.lower()]
    except KeyError:
        raise NoLettersBuilderError(f"There is no builder for '{letter}' letter.")

def build_0_letter() -> list[str]:
    return [
        ' ***** ',
        '*     *',
        '*     *',
        '*     *',
        ' ***** ',
        '       ',
    ]

def build_1_letter() -> list[str]:
    return [
        '   *   ',
        '  **   ',
        '   *   ',
        '   *   ',
        '  ***  ',
        '       ',
    ]

def build_2_letter() -> list[str]:
    return [
        ' ***** ',
        '*     *',
        '    ** ',
        '  **   ',
        '*******',
        '       ',
    ]

def build_3_letter() -> list[str]:
    return [
        ' ***** ',
        '     **',
        '   *** ',
        '     **',
        ' ***** ',
        '       ',
    ]

def build_4_letter() -> list[str]:
    return [
        '    ** ',
        '   * * ',
        '  *  * ',
        '*******',
        '     * ',
        '       ',
    ]

def build_5_letter() -> list[str]:
    return [
        '*******',
        '*      ',
        '****** ',
        '      *',
        '****** ',
        '       ',
    ]

def build_6_letter() -> list[str]:
    return [
        ' ***** ',
        '*      ',
        '****** ',
        '*     *',
        ' ***** '
        '       ',
    ]

def build_7_letter() -> list[str]:
    return [
        '*******',
        '     * ',
        '    *  ',
        '   *   ',
        '  *    ',
        '       ',
    ]

def build_8_letter() -> list[str]:
    return [
        ' ***** ',
        '*     *',
        ' ***** ',
        '*     *',
        ' ***** ',
        '       ',
    ]

def build_9_letter() -> list[str]:
    return [
        ' ***** ',
        '*     *',
        ' ******',
        '      *',
        ' ***** ',
        '       ',
    ]


