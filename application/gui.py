import dearpygui.dearpygui as dpg

from db_sql import DbManager

W = 1600 # WITDH OF THE WINDOW
H = 900 # HEIGHT OF THE WINDOW

dpg.create_context()

dpg.create_viewport(title='Product Information Manager Process ', width=W, height=H)



def print_me(sender):
    print(f"Menu Item: {sender}")

# add a font registry
with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("fonts\\HelveticaNeueMediumExtended.otf", 16)
    second_font = dpg.add_font("fonts\\HelveticaNeueLTW0697BlkCnObl.otf", 16)

with dpg.window(width=W-15, height=H-200, no_collapse=True, no_title_bar=True, no_move=True) as main_window:
    with dpg.menu_bar():
        with dpg.menu(label="Filer"):
            dpg.add_menu_item(label="Tilslut Database", callback=print_me)
            dpg.add_menu_item(label="Gem Database", callback=print_me)

        with dpg.menu(label="Vis"):
            dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
            dpg.add_menu_item(label="Setting 2", callback=print_me)


        with dpg.menu(label="Plugins"):
            dpg.add_checkbox(label="Pick Me", callback=print_me)
            dpg.add_button(label="Press Me", callback=print_me)


        dpg.add_menu_item(label="Hjælp", callback=print_me)
    dpg.add_spacer(height=10)

    with dpg.table(header_row=True, row_background=True,
                   borders_innerH=True, borders_outerH=True, borders_innerV=True,
                   borders_outerV=True, height=H//2, sort_multi=True) as table_window:
        # use add_table_column to add columns to the table,
        # table columns use slot 0
        dpg.add_table_column(label="Projekt ID", default_sort=True)
        dpg.add_table_column(label="Navn", default_sort=True)
        dpg.add_table_column(label="Leder", default_sort=True)
        dpg.add_table_column(label="Status%", default_sort=True)
        dpg.add_table_column(label="Startet", default_sort=True)
        dpg.add_table_column(label="Est. Slut", default_sort=True)
        dpg.add_table_column(label="Udviklingsfase", default_sort=True)
        dpg.add_table_column(label="Dage i fasen", default_sort=True)
        dpg.add_table_column(label="Ansvarlig", default_sort=True)
        dpg.add_table_column(label="Næste Ansvarlig", default_sort=True)

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        db = DbManager()
        for _ in range(len(db.return_list())):
            with dpg.table_row(height=30):
                for row in db.return_list()[_]:
                    dpg.add_text(row)




    with dpg.window(label="Buttons", pos=(0, H-150), no_collapse=True, no_title_bar=True, no_background=True) as button_options:
        with dpg.group(horizontal=True):
            dpg.add_button(label="Tilføj Projekt", width=100, height=50)
            dpg.add_button(label="Slet Projekt", width=100, height=50)

dpg.bind_font(default_font)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()