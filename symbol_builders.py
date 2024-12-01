from typing import Callable


class NoLettersBuilderError(Exception):
    pass


BuilderType = Callable[[], list[str]]
registered_symbol_builders = { }


def register_symbol_builder(letter: str, print_character: str = '@') -> Callable[[BuilderType], BuilderType]:
    def register(original_symbol_builder: BuilderType) -> BuilderType:
        def decorated_symbol_builder() -> list[str]:
            original_rows = original_symbol_builder()
            letter_rows = []
            for row in original_rows:
                letter_rows.append(
                    row.replace('*', print_character)
                )
            return letter_rows
        registered_symbol_builders[letter] = decorated_symbol_builder
        return decorated_symbol_builder
    return register


def get_symbol_builder(letter: str) -> Callable[[], list[str]]:
    try:
        return registered_symbol_builders[letter.lower()]
    except KeyError:
        raise NoLettersBuilderError(f"There is no builder for '{letter}' letter.")


@register_symbol_builder('a', '#')
def build_a_letter() -> list[str]:
    return [
        '    *    ',
        '   * *   ',
        '  *   *  ',
        ' * * * * ',
        '*       *',
        '         ',
    ]
# build_a_letter = register_symbol_builder('a')(build_a_letter)

@register_symbol_builder('b', '!')
def build_b_letter() -> list[str]:
    return [
        '******** ',
        '*       *',
        '******** ',
        '*       *',
        '******** ',
        '         ',
    ]

@register_symbol_builder('c')
def build_c_letter() -> list[str]:
    return [
        ' ******* ',
        '*        ',
        '*        ',
        '*        ',
        ' ******* ',
        '         ',
    ]

@register_symbol_builder('d')
def build_d_letter() -> list[str]:
    return [
        '******** ',
        '*       *',
        '*       *',
        '*       *',
        '******** ',
        '         ',
    ]

@register_symbol_builder('e')
def build_e_letter() -> list[str]:
    return [
        '*********',
        '*        ',
        '*********',
        '*        ',
        '*********',
        '         ',
    ]
@register_symbol_builder('f')
def build_f_letter() -> list[str]:
    return [
        '*********',
        '*        ',
        '*********',
        '*        ',
        '*        ',
        '         ',
    ]

@register_symbol_builder('g')
def build_g_letter() -> list[str]:
    return [
        ' ********',
        '*        ',
        '*     ***',
        '*       *',
        '  *******',
        '         ',
    ]

@register_symbol_builder('h')
def build_h_letter() -> list[str]:
    return [
        '*       *',
        '*       *',
        '*********',
        '*       *',
        '*       *',
        '         ',
    ]

@register_symbol_builder('i')
def build_i_letter() -> list[str]:
    return [
        '    *    ',
        '    *    ',
        '    *    ',
        '    *    ',
        '    *    ',
        '         ',
    ]

@register_symbol_builder('j')
def build_j_letter() -> list[str]:
    return [
        '    *    ',
        '    *    ',
        '    *    ',
        ' *  *    ',
        '  **     ',
        '         ',
    ]

@register_symbol_builder('k')
def build_k_letter() -> list[str]:
    return [
        '*       *',
        '*     *  ',
        '*****    ',
        '*    *   ',
        '*       *',
        '         ',
    ]

@register_symbol_builder('l')
def build_l_letter() -> list[str]:
    return [
        '*        ',
        '*        ',
        '*        ',
        '*        ',
        '*********',
        '         ',
    ]

@register_symbol_builder('m')
def build_m_letter() -> list[str]:
    return [
        '*       *',
        '**     **',
        '*  * *  *',
        '*       *',
        '*       *',
        '         ',
    ]

@register_symbol_builder('n')
def build_n_letter() -> list[str]:
    return [
        '*       *',
        '**      *',
        '*  *    *',
        '*    *  *',
        '*      **',
        '         ',
    ]
@register_symbol_builder('o')
def build_o_letter() -> list[str]:
    return [
        ' ******* ',
        '*       *',
        '*       *',
        '*       *',
        ' ******* ',
        '         ',
    ]

@register_symbol_builder('f')
def build_p_letter() -> list[str]:
    return [
        '******** ',
        '*       *',
        '******** ',
        '*        ',
        '*        ',
        '         ',
    ]

@register_symbol_builder('q')
def build_q_letter() -> list[str]:
    return [
        ' ******* ',
        '*       *',
        '*       *',
        ' ******* ',
        '        *',
        '         ',
    ]

@register_symbol_builder('r')
def build_r_letter() -> list[str]:
    return [
        ' *****   ',
        '*     *  ',
        '******   ',
        '*     *  ',
        '*       *',
        '         ',
    ]

@register_symbol_builder('s')
def build_s_letter() -> list[str]:
    return [
        '  *****  ',
        ' *       ',
        '  *****  ',
        '       * ',
        '  *****  ',
        '         ',
    ]
@register_symbol_builder('t')
def build_t_letter() -> list[str]:
    return [
        '*******',
        '   *   ',
        '   *   ',
        '   *   ',
        '   *   ',
        '       ',
    ]
@register_symbol_builder('u')
def build_u_letter() -> list[str]:
    return [
        '*     *',
        '*     *',
        '*     *',
        '*     *',
        ' ***** ',
        '       ',
    ]
@register_symbol_builder('v')
def build_v_letter() -> list[str]:
    return [
        '*     *',
        '*     *',
        '*     *',
        ' *   * ',
        '  ***  ',
        '       ',
    ]
@register_symbol_builder('w')
def build_w_letter() -> list[str]:
    return [
        '*     *     *',
        '*     *     *',
        '*     *     *',
        ' *   * *   * ',
        '  * *   * *  ',
        '             ',
    ]
@register_symbol_builder('x')
def build_x_letter() -> list[str]:
    return [
        '*     *',
        ' *   * ',
        '  * *  ',
        ' *   * ',
        '*     *',
        '       ',
    ]

@register_symbol_builder('y')
def build_y_letter() -> list[str]:
    return [
        '*     *',
        ' *   * ',
        '  * *  ',
        '   *   ',
        '   *   ',
        '       ',
    ]
@register_symbol_builder('z')
def build_z_letter() -> list[str]:
    return [
        '*******',
        '     * ',
        '   *   ',
        ' *     ',
        '*******',
        '       ',
    ]
@register_symbol_builder(' ')
def build_space_letter() -> list[str]:
    return [
        '       ',
        '       ',
        '       ',
        '       ',
        '       ',
        '       ',
    ]
@register_symbol_builder(',')
def build_comma_letter() -> list[str]:
    return [
        '       ',
        '       ',
        '       ',
        '       ',
        '  *    ',
        '  *    ',
    ]
@register_symbol_builder('.')
def build_dot_letter() -> list[str]:
    return [
        '       ',
        '       ',
        '       ',
        '       ',
        '   *   ',
        '       ',
    ]

@register_symbol_builder('!')
def build_exclamation_letter() -> list[str]:
    return [
        '   *   ',
        '   *   ',
        '   *   ',
        '       ',
        '   *   ',
        '       ',
    ]

@register_symbol_builder('?')
def build_question_mark_letter() -> list[str]:
    return [
        '   **  ',
        ' *    *',
        '    *  ',
        '   *   ',
        '   *   ',
        '       ',
    ]

@register_symbol_builder('-')
def build_dash_letter() -> list[str]:
    return [
        '       ',
        '       ',
        '*******',
        '       ',
        '       ',
        '       ',
    ]

@register_symbol_builder('+')
def build_plus_letter() -> list[str]:
    return [
        "   *   ",
        "   *   ",
        "*******",
        "   *   ",
        "   *   ",
        "       ",
    ]

@register_symbol_builder('=')
def build_equal_sign_letter() -> list[str]:
    return [
        "       ",
        "*******",
        "       ",
        "*******",
        "       ",
        "       ",
    ]

@register_symbol_builder('/')
def build_slash_letter() -> list[str]:
    return [
        "     * ",
        "    *  ",
        "   *   ",
        "  *    ",
        " *     ",
        "       ",
    ]

@register_symbol_builder('0')
def build_0_letter() -> list[str]:
    return [
        ' ***** ',
        '*     *',
        '*     *',
        '*     *',
        ' ***** ',
        '       ',
    ]

@register_symbol_builder('1')
def build_1_letter() -> list[str]:
    return [
        '   *   ',
        '  **   ',
        '   *   ',
        '   *   ',
        '  ***  ',
        '       ',
    ]

@register_symbol_builder('2')
def build_2_letter() -> list[str]:
    return [
        ' ***** ',
        '*     *',
        '    ** ',
        '  **   ',
        '*******',
        '       ',
    ]

@register_symbol_builder('3')
def build_3_letter() -> list[str]:
    return [
        ' ***** ',
        '     **',
        '   *** ',
        '     **',
        ' ***** ',
        '       ',
    ]

@register_symbol_builder('4')
def build_4_letter() -> list[str]:
    return [
        '    ** ',
        '   * * ',
        '  *  * ',
        '*******',
        '     * ',
        '       ',
    ]

@register_symbol_builder('5')
def build_5_letter() -> list[str]:
    return [
        '*******',
        '*      ',
        '****** ',
        '      *',
        '****** ',
        '       ',
    ]

@register_symbol_builder('6')
def build_6_letter() -> list[str]:
    return [
        ' ***** ',
        '*      ',
        '****** ',
        '*     *',
        ' ***** '
        '       ',
    ]

@register_symbol_builder('7')
def build_7_letter() -> list[str]:
    return [
        '*******',
        '     * ',
        '    *  ',
        '   *   ',
        '  *    ',
        '       ',
    ]

@register_symbol_builder('8')
def build_8_letter() -> list[str]:
    return [
        ' ***** ',
        '*     *',
        ' ***** ',
        '*     *',
        ' ***** ',
        '       ',
    ]

@register_symbol_builder('9')
def build_9_letter() -> list[str]:
    return [
        ' ***** ',
        '*     *',
        ' ******',
        '      *',
        ' ***** ',
        '       ',
    ]
