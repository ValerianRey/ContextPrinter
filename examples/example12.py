from context_printer import ContextPrinter as Ctp
from context_printer import Color

Ctp.set_automatic_skip(True)
# Ctp.set_default_header('✘ ')
Ctp.set_max_depth(3)
Ctp.enter_section()
Ctp.enter_section('Main section', Color.BLUE)
Ctp.print('Text in main section')
for i in range(3):
    Ctp.enter_section(color="red")
    # Ctp.enter_section('Subsection {}'.format(i + 1), "red")
    Ctp.print('Text in subsection')
    Ctp.print('Text in subsection')
    Ctp.exit_section()
Ctp.exit_section()

Ctp.set_default_header('✘✘ ')
Ctp.set_coloring(False)
Ctp.enter_section('Main section', color='blue')
Ctp.print('Text in main section')
for i in range(3):
    Ctp.enter_section('Subsection {}'.format(i + 1), Color.BOLD)
    Ctp.print('Text in subsection')
    Ctp.print('Text in subsection')
    Ctp.exit_section()
Ctp.exit_section()

Ctp.set_default_header('✘✘✘ ')
Ctp.set_coloring(True)
Ctp.enter_section('Main section', color='blue')
Ctp.print('Text in main section')
for i in range(3):
    Ctp.enter_section('Subsection {}'.format(i + 1), Color.BOLD)
    Ctp.print('Text in subsection')
    Ctp.print('Text in subsection')
    Ctp.exit_section()
Ctp.exit_section()
Ctp.exit_section()
