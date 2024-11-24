from typing import Callable
class NoLettersBuilderError(Exception):
    pass

def get_letter_builder(letter: str) -> Callable[..., list[str]]:
    letter_builders = {
        'a': build_a_letter,
        'b': build_b_letter,
        'c': build_c_letter,
        'd': build_d_letter,
        'e': build_e_letter,
        'f': build_f_letter,
        'g': build_g_letter,
        'h': build_h_letter,
        'i': build_i_letter,
        'j': build_j_letter,
        'k': build_k_letter,
        'l': build_l_letter,
        'm': build_m_letter,
        'n': build_n_letter,
        'o': build_o_letter,
        'p': build_p_letter,
        'q': build_q_letter,
        'r': build_r_letter,
        's': build_s_letter,
        't': build_t_letter,
        'u': build_u_letter,
        'v': build_v_letter,
        'w': build_w_letter,
        'x': build_x_letter,
        'y': build_y_letter,
        'z': build_z_letter,
        ' ': build_space_letter,
        ',': build_comma_letter,
        '.': build_dot_letter,
        '!': build_exclamation_letter,
        '?': build_question_mark_letter,
        '-': build_dash_letter,
        '+': build_plus_letter,
        '=': build_equal_sign_letter,
        '/': build_slash_letter,
    }
    try:
        return letter_builders[letter.lower()]
    except KeyError:
        raise NoLettersBuilderError(f"There is no builder for '{letter}' letter.")

def build_a_letter() -> list[str]:
    return [
        '    *    ',
        '   * *   ',
        '  *   *  ',
        ' * * * * ',
        '*       *',
        '         ',
    ]
def build_b_letter() -> list[str]:
    return [
        '******** ',
        '*       *',
        '******** ',
        '*       *',
        '******** ',
        '         ',
    ]


def build_c_letter() -> list[str]:
    return [
        ' ******* ',
        '*        ',
        '*        ',
        '*        ',
        ' ******* ',
        '         ',
    ]

def build_d_letter() -> list[str]:
    return [
        '******** ',
        '*       *',
        '*       *',
        '*       *',
        '******** ',
        '         ',
    ]

def build_e_letter() -> list[str]:
    return [
        '*********',
        '*        ',
        '*********',
        '*        ',
        '*********',
        '         ',
    ]

def build_f_letter() -> list[str]:
    return [
        '*********',
        '*        ',
        '*********',
        '*        ',
        '*        ',
        '         ',
    ]


def build_g_letter() -> list[str]:
    return [
        ' ********',
        '*        ',
        '*     ***',
        '*       *',
        '  *******',
        '         ',
    ]


def build_h_letter() -> list[str]:
    return [
        '*       *',
        '*       *',
        '*********',
        '*       *',
        '*       *',
        '         ',
    ]


def build_i_letter() -> list[str]:
    return [
        '    *    ',
        '    *    ',
        '    *    ',
        '    *    ',
        '    *    ',
        '         ',
    ]


def build_j_letter() -> list[str]:
    return [
        '    *    ',
        '    *    ',
        '    *    ',
        ' *  *    ',
        '  **     ',
        '         ',
    ]


def build_k_letter() -> list[str]:
    return [
        '*       *',
        '*     *  ',
        '*****    ',
        '*    *   ',
        '*       *',
        '         ',
    ]


def build_l_letter() -> list[str]:
    return [
        '*        ',
        '*        ',
        '*        ',
        '*        ',
        '*********',
        '         ',
    ]


def build_m_letter() -> list[str]:
    return [
        '*       *',
        '**     **',
        '*  * *  *',
        '*       *',
        '*       *',
        '         ',
    ]


def build_n_letter() -> list[str]:
    return [
        '*       *',
        '**      *',
        '*  *    *',
        '*    *  *',
        '*      **',
        '         ',
    ]

def build_o_letter() -> list[str]:
    return [
        ' ******* ',
        '*       *',
        '*       *',
        '*       *',
        ' ******* ',
        '         ',
    ]


def build_p_letter() -> list[str]:
    return [
        '******** ',
        '*       *',
        '******** ',
        '*        ',
        '*        ',
        '         ',
    ]


def build_q_letter() -> list[str]:
    return [
        ' ******* ',
        '*       *',
        '*       *',
        ' ******* ',
        '        *',
        '         ',
    ]


def build_r_letter() -> list[str]:
    return [
        ' *****   ',
        '*     *  ',
        '******   ',
        '*     *  ',
        '*       *',
        '         ',
    ]


def build_s_letter() -> list[str]:
    return [
        '  *****  ',
        ' *       ',
        '  *****  ',
        '       * ',
        '  *****  ',
        '         ',
    ]

def build_t_letter() -> list[str]:
    return [
        '*******',
        '   *   ',
        '   *   ',
        '   *   ',
        '   *   ',
        '       ',
    ]

def build_u_letter() -> list[str]:
    return [
        '*     *',
        '*     *',
        '*     *',
        '*     *',
        ' ***** ',
        '       ',
    ]

def build_v_letter() -> list[str]:
    return [
        '*     *',
        '*     *',
        '*     *',
        ' *   * ',
        '  ***  ',
        '       ',
    ]

def build_w_letter() -> list[str]:
    return [
        '*     *     *',
        '*     *     *',
        '*     *     *',
        ' *   * *   * ',
        '  * *   * *  ',
        '             ',
    ]

def build_x_letter() -> list[str]:
    return [
        '*     *',
        ' *   * ',
        '  * *  ',
        ' *   * ',
        '*     *',
        '       ',
    ]

def build_y_letter() -> list[str]:
    return [
        '*     *',
        ' *   * ',
        '  * *  ',
        '   *   ',
        '   *   ',
        '       ',
    ]

def build_z_letter() -> list[str]:
    return [
        '*******',
        '     * ',
        '   *   ',
        ' *     ',
        '*******',
        '       ',
    ]

def build_space_letter() -> list[str]:
    return [
        '       ',
        '       ',
        '       ',
        '       ',
        '       ',
        '       ',
    ]

def build_comma_letter() -> list[str]:
    return [
        '       ',
        '       ',
        '       ',
        '       ',
        '  *    ',
        '  *    ',
    ]

def build_dot_letter() -> list[str]:
    return [
        '       ',
        '       ',
        '       ',
        '       ',
        '   *   ',
        '       ',
    ]

def build_exclamation_letter() -> list[str]:
    return [
        '   *   ',
        '   *   ',
        '   *   ',
        '       ',
        '   *   ',
        '       ',
    ]

def build_question_mark_letter() -> list[str]:
    return [
        '   **  ',
        ' *    *',
        '    *  ',
        '   *   ',
        '   *   ',
        '       ',
    ]

def build_dash_letter() -> list[str]:
    return [
        '       ',
        '       ',
        '*******',
        '       ',
        '       ',
        '       ',
    ]

def build_plus_letter() -> list[str]:
    return [
        "   *   ",
        "   *   ",
        "*******",
        "   *   ",
        "   *   ",
        "       ",
    ]

def build_equal_sign_letter() -> list[str]:
    return [
        "       ",
        "*******",
        "       ",
        "*******",
        "       ",
        "       ",
    ]

def build_slash_letter() -> list[str]:
    return [
        "     * ",
        "    *  ",
        "   *   ",
        "  *    ",
        " *     ",
        "       ",
    ]
