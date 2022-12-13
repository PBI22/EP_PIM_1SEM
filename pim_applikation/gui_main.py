import dearpygui.dearpygui as dpg
from pim import PimManager
from datetime import datetime, date

"""
db.py -> Database klient m. class DbManager
pim.py -> PIM Class der håndteres og bearbejder data´en til visning i GUI
gui_main.py -> GUI til App´en, som også håndterer lidt af datatransformeringen ligeledes.

______
Der mangler oprydning, kommentarer og generel struktur. Koden er rodet, da det har været meget trial and error.
Forslag til forbedringer vil være:
Lav GUI som en class og funktionernes som methods og renskrive koden, samt bygge methods der hvor store dele af koden går igen. 
Lægge alt databehandling/transformaton der stadig er i gui(main) over i pim
Antallet af globals vil/skal ligeledes reduceres
og der skal bruges en reel gui_main.py med korrekt opsætning.


custom_sql bør ligge i en database eller andet sted.

db_login og table_route skal ikke ligge i filen. Login dog lokal sandbox login, så ikke farligt at have med i dette tilfælde. 

"""

# Vi forsøger at holde det i 16:9format
W = 1600 # WITDH OF THE WINDOW
H = 900 # HEIGHT OF THE WINDOW


table_route = ["portfolio", "project", "product", "design", "construction", "prototype","employee"]

db_login = ["DIN_BRUGER", "DIT_PASSWORD", "localhost", "PIM_DATABASE"] # bør placeres andre steder eller laves som en "sikker" løsning.
dpg.create_context()
pimp = PimManager(db_login, table_route=table_route) # Iniatiere PimManager Class
custom_result = []
custom_col_names = []
search_result = []
search_col_id = []
table_colums = []
table_rows = []
table_cell_rows = []

custom_sql = {"Q1": """
SELECT d.name, d.specifications, d.beskrivelse, d.start_date, d.end_date, IFNULL(end_date-start_date,CURRENT_DATE()-start_date) as 'Antal dage i fase',CONCAT(employee.name," (",employee.role,") ") AS 'Manager' FROM design as d
JOIN employee ON employee.id = d.manager_id
WHERE d.start_date IS NOT NULL AND d.end_date IS NULL
ORDER BY 6 DESC;""",
              "Q2": """SELECT project.name AS 'Projekt', 
product.id AS 'Produkt ID',
product.name AS 'Produktnavn', 
product.description AS 'beskrivelse',
employee.name AS 'PManager', 
design.start_date AS 'Start dato', 
CASE 
	WHEN prototype.end_date IS NOT NULL THEN DATEDIFF(prototype.end_date,design.start_date)
    ELSE DATEDIFF(CURRENT_DATE(),design.start_date)
    END AS 'Ialt Dage',
CASE
	WHEN prototype.end_date IS NOT NULL THEN 'Afsluttet'
    WHEN prototype.start_date IS NOT NULL THEN 'Prototype'
    WHEN construction.start_date IS NOT NULL THEN 'Konstruktion'
    ELSE 'Design'
END AS 'Fase',
IFNULL(mng.name,'Afsluttet') AS 'Ansvarlig',
IFNULL(nmng.name,'Afsluttet') AS 'Næste Ansvarlig'

FROM product
JOIN project on product.project_id = project.id
JOIN design on design.product_id = product.id
JOIN construction on construction.product_id = product.id
JOIN prototype on prototype.product_id = product.id
JOIN employee on product.manager_id = employee.id
-- Join to get the employee name for the current manager
LEFT JOIN employee mng ON
    (CASE
        WHEN prototype.end_date IS NOT NULL THEN NULL
        WHEN prototype.start_date IS NOT NULL THEN prototype.manager_id
        WHEN construction.start_date IS NOT NULL THEN construction.manager_id
        ELSE design.manager_id
    END) = mng.id
LEFT JOIN employee nmng ON
    (CASE
        WHEN prototype.end_date IS NOT NULL THEN NULL
        WHEN prototype.start_date IS NOT NULL THEN NULL
        WHEN construction.start_date IS NOT NULL THEN prototype.manager_id
        ELSE construction.manager_id
    END) = nmng.id;"""}

#theme hentet inde fra dearpygui-ext fra github.
def light_theme():
    with dpg.theme() as theme_id:
        with dpg.theme_component(0):
            dpg.add_theme_color(dpg.mvThemeCol_Text                   , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TextDisabled           , (0.60 * 255, 0.60 * 255, 0.60 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg               , (0.94 * 255, 0.94 * 255, 0.94 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg                , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_PopupBg                , (1.00 * 255, 1.00 * 255, 1.00 * 255, 0.98 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_Border                 , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.30 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_BorderShadow           , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg                , (1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered         , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.40 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive          , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.67 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TitleBg                , (0.96 * 255, 0.96 * 255, 0.96 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive          , (0.82 * 255, 0.82 * 255, 0.82 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed       , (1.00 * 255, 1.00 * 255, 1.00 * 255, 0.51 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg              , (0.86 * 255, 0.86 * 255, 0.86 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg            , (0.98 * 255, 0.98 * 255, 0.98 * 255, 0.53 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab          , (0.69 * 255, 0.69 * 255, 0.69 * 255, 0.80 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered   , (0.49 * 255, 0.49 * 255, 0.49 * 255, 0.80 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive    , (0.49 * 255, 0.49 * 255, 0.49 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_CheckMark              , (0.26 * 255, 0.59 * 255, 0.98 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrab             , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.78 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive       , (0.46 * 255, 0.54 * 255, 0.80 * 255, 0.60 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_Button                 , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.40 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered          , (0.26 * 255, 0.59 * 255, 0.98 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive           , (0.06 * 255, 0.53 * 255, 0.98 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_Header                 , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.31 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered          , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.80 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_HeaderActive           , (0.26 * 255, 0.59 * 255, 0.98 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_Separator              , (0.39 * 255, 0.39 * 255, 0.39 * 255, 0.62 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_SeparatorHovered       , (0.14 * 255, 0.44 * 255, 0.80 * 255, 0.78 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_SeparatorActive        , (0.14 * 255, 0.44 * 255, 0.80 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip             , (0.35 * 255, 0.35 * 255, 0.35 * 255, 0.17 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered      , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.67 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive       , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.95 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_Tab                    , (0.76 * 255, 0.80 * 255, 0.84 * 255, 0.93 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TabHovered             , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.80 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TabActive              , (0.60 * 255, 0.73 * 255, 0.88 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused           , (0.92 * 255, 0.93 * 255, 0.94 * 255, 0.99 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive     , (0.74 * 255, 0.82 * 255, 0.91 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_DockingPreview         , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.22 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_DockingEmptyBg         , (0.20 * 255, 0.20 * 255, 0.20 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_PlotLines              , (0.39 * 255, 0.39 * 255, 0.39 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_PlotLinesHovered       , (1.00 * 255, 0.43 * 255, 0.35 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_PlotHistogram          , (0.90 * 255, 0.70 * 255, 0.00 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_PlotHistogramHovered   , (1.00 * 255, 0.45 * 255, 0.00 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg          , (0.78 * 255, 0.87 * 255, 0.98 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TableBorderStrong      , (0.57 * 255, 0.57 * 255, 0.64 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TableBorderLight       , (0.68 * 255, 0.68 * 255, 0.74 * 255, 1.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBg             , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.00 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBgAlt          , (0.30 * 255, 0.30 * 255, 0.30 * 255, 0.09 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg         , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.35 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_DragDropTarget         , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.95 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_NavHighlight           , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.80 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_NavWindowingHighlight  , (0.70 * 255, 0.70 * 255, 0.70 * 255, 0.70 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_NavWindowingDimBg      , (0.20 * 255, 0.20 * 255, 0.20 * 255, 0.20 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_ModalWindowDimBg       , (0.20 * 255, 0.20 * 255, 0.20 * 255, 0.35 * 255))
            dpg.add_theme_color(dpg.mvPlotCol_FrameBg       , (1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_PlotBg        , (0.42 * 255, 0.57 * 255, 1.00 * 255, 0.13 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_PlotBorder    , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.00 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendBg      , (1.00 * 255, 1.00 * 255, 1.00 * 255, 0.98 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendBorder  , (0.82 * 255, 0.82 * 255, 0.82 * 255, 0.80 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendText    , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_TitleText     , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_InlayText     , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_XAxis         , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_XAxisGrid     , (1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxis         , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid     , (1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxis2        , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid2    , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.50 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxis3        , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid3    , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.50 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_Selection     , (0.82 * 255, 0.64 * 255, 0.03 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_Query         , (0.00 * 255, 0.84 * 255, 0.37 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_Crosshairs    , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.50 * 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (240, 240, 240, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundHovered, (240, 240, 240, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundSelected, (240, 240, 240, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeOutline, (100, 100, 100, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (248, 248, 248, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, (209, 209, 209, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, (209, 209, 209, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_Link, (66, 150, 250, 100), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, (66, 150, 250, 242), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, (66, 150, 250, 242), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_Pin, (66, 150, 250, 160), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_PinHovered, (66, 150, 250, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_BoxSelector, (90, 170, 250, 30), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_BoxSelectorOutline, (90, 170, 250, 150), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_GridBackground, (225, 225, 225, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_GridLine, (180, 180, 180, 100), category=dpg.mvThemeCat_Nodes)
            # dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 140, 23), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_CellPadding, 8, 2, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 6, 8, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 12, 0, category=dpg.mvThemeCat_Core)
            #dpg.add_theme_color(dpg.mvThemeCol_TableBorderLight, (255, 255, 255, 150), category=dpg.mvThemeCat_Core)
            #dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (5, 54, 116), category=dpg.mvThemeCat_Core)
            dpg.bind_theme(theme_id)

def custom_q(sender, app_data, user_data):
    global custom_result
    global custom_col_names
    print(f"custom_q: {sender}, {app_data}, {user_data}")
    custom_result, custom_col_names = pimp.db_client.run_custom_query(custom_sql[f"{user_data}"])
    dpg.set_value("current_table", f'Custom Dataudtræk: {user_data}')
    hent_tabel()

def search_func(sender, app_data, user_data):
    global search_result
    global search_col_id
    search_result, search_col_id = [], []
    search_value = dpg.get_value("search")
    dpg.set_value("current_table",  f'{pimp.active_table.upper()} - Søgning på : {search_value}')
    if search_value == "":
        return hent_tabel()
    at = pimp.get_active(pimp.active_table)
    for row in at:
        for col in row:
            if search_value in str(col):
                print(row)
                if row not in search_result:
                    search_result.append(row)
                    search_col_id.append(row[0])
    if search_result == []:
        dpg.set_value("current_table",  f'{pimp.active_table.upper()} - Søgning på : {search_value} - Ingen resultater')
    hent_tabel()




def back_button(push=None, push_id=None):
    if pimp.active_table == "portfolio":
        print("Cant go more back")
    elif not push:
        pimp.active_table = pimp.table_route[pimp.table_route.index(pimp.active_table) - 1]
        dpg.set_value("current_table",f"{pimp.active_table.upper()} with ID: {push_id}")

    else:
        pimp.active_table = pimp.table_route[pimp.table_route.index(pimp.active_table) - 1]
        dpg.set_value("current_table", pimp.active_table.upper())
        hent_tabel()

def next_button(push=None, push_id=None):

    if pimp.active_table == "prototype":
        print("Cant go more forward")
    elif not push:
        pimp.active_table = pimp.table_route[pimp.table_route.index(pimp.active_table) + 1]
        dpg.set_value("current_table",f"{pimp.active_table.upper()} with ID: {push_id}")

    else:
        pimp.active_table = pimp.table_route[pimp.table_route.index(pimp.active_table) + 1]
        dpg.set_value("current_table",pimp.active_table.upper())
        hent_tabel()

def print_x(sender, app_data, user_data):
    print(f"print_x: {sender}, {app_data}, {user_data}")
    print("CALL:", dpg.get_item_children("edit_table_row",1))
    for child in dpg.get_item_children("edit_table_row",1):
        for child2 in dpg.get_item_children(child,1):
            print("CHILD:", child2)
            print("VALUE:", dpg.get_value(child2))
        print(dpg.get_value(child))



def print_info(sender, app_data, user_data):
    print(f"Sender: {sender} \napp_data: {app_data}, \nuser_data{user_data}")

def table_id_go(sender, app_data, user_data):
    global table_colums, table_rows, search_result, search_col_id

    id_pressed = table_rows.index(int(sender)-2) + 1 + user_data
    print(f"ID pressed: {id_pressed-user_data}")
    print(search_col_id)
    if search_col_id:
        id_pressed = search_col_id[id_pressed-user_data-1]
    print(f"ID pressed: {id_pressed}")
    print(f"Sender: {sender} \napp_data: {app_data}, \nuser_data{user_data}")

    custom_table= pimp.table_route[pimp.table_route.index(pimp.active_table) + 1]
    next_button(push=False, push_id=id_pressed)
    #print(pimp.active_table)
    hent_tabel(custom_table=custom_table, custom_id=id_pressed)



def table_info_callback(sender, app_data, user_data):
    global table_colums
    global table_rows
    global table_cell_rows
    table_colums = dpg.get_item_children(sender,0)
    table_rows = dpg.get_item_children(sender,1)
    table_cell_rows = [dpg.get_item_children(x,1) for x in table_rows]


    #for row in table_rows:
        #print(dpg.get_item_children(row,1))
    #for col in table_colums:
        #print(col)


def hent_tabel(custom_table = None, custom_id = None):
    global custom_result
    global custom_col_names
    global search_result
    global search_col_id
    #print(custom_table, custom_id)
    dpg.delete_item("maintabel")

    with dpg.table(header_row=True, row_background=True,
                   borders_innerH=True, borders_outerH=True, borders_innerV=True,
                   borders_outerV=True, height=H//2-100, sortable=True, tag="maintabel", parent=main_window, resizable=True, callback=table_info_callback) as table_window:
        # use add_table_column to add columns to the table,
        # table columns use slot 0
        if custom_table and custom_id:
            if custom_table in ["design", "construction", "prototype"]:
                linked_id = "id"
            else:
                linked_id = f"{pimp.table_route[pimp.table_route.index(pimp.active_table) - 1]}_id"
            active_table = pimp.db_client.get_columns(custom_table)
            pimp.active_table = custom_table
            col_id = active_table.index(linked_id)

        elif custom_result:
            active_table = custom_col_names
            linked_id = None
        else:
            active_table = pimp.db_client.get_columns(pimp.active_table)
            linked_id = None
        small_col = ["id", "portfolio_id", "project_id", "product_id", "manager_id", "Produkt ID", "PManager"]
        date_col = ["start_date","est_end_date","end_date","ended_date"]



        for col in active_table:

            if col in small_col:
                dpg.add_table_column(label=col, width_fixed=True, width=30)

            elif col in date_col:
                dpg.add_table_column(label=col, width_fixed=True, width=70)

            elif col == "name":
                dpg.add_table_column(label=col, width_fixed=True, width=100)
            else:
                dpg.add_table_column(label=col)


        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        if custom_result:
            data_rows = custom_result
            diff = 0
        elif search_result:
            data_rows = search_result
            data_full = pimp.get_active(pimp.active_table)
            diff = len(data_full) - len(data_rows)
        else:
            data_full = pimp.get_active(pimp.active_table)
            data_rows =  pimp.get_active(pimp.active_table, lookup_table=linked_id, lookup_id=custom_id)
            diff = len(data_full) - len(data_rows)
        for row in data_rows:
                with dpg.table_row(height=30):
                        for i, row in enumerate(row):
                            if active_table[i] == 'id':
                                with dpg.group(horizontal=True):
                                    dpg.add_image_button(texture_tag="enter_icon", callback=table_id_go, user_data=diff,
                                                         height=20, width=20)
                                    dpg.add_text(row)
                            elif active_table[i] in date_col:
                                if active_table[i] == "ended_date" or active_table[i] == "end_date":
                                    if row != None:
                                        with dpg.group(horizontal=True):
                                            dpg.add_text(row.strftime("%d/%m/%Y"))
                                            dpg.add_image("done_icon", width=20, height=20)
                                    else:

                                        dpg.add_text("")
                                else:
                                    dpg.add_text(row.strftime("%d/%m/%Y"))
                            else:

                                dpg.add_text(row)
    print("GLOBALS")
    custom_result,custom_col_names,search_result = [], [], []

def dialog_popup():
    with dpg.window(label="Advarsel", modal=True, show=True, tag="modal_id", no_title_bar=True, pos=(500, 300)):
        dpg.add_text(
            "Du har ikke indtastet et ID\nMed mindre det er nødvendigt, anbefales det at du redigerer et enkelt felt ad gangen\nBrug * for at redigere alle")
        dpg.add_separator()
        with dpg.group(horizontal=True):
            dpg.add_button(label="OK", width=75, callback=lambda: dpg.delete_item("modal_id"),
                           indent=350)
def get_edit_fields(sender, app_data, user_data):
    print(f"print_x: {sender}, {app_data}, {user_data}")
    print(f"current table: {pimp.active_table}")
    columns = pimp.db_client.get_columns(pimp.active_table)
    print(f"colums: {columns}")
    try:
        for x in range(len(pimp.active_table)):
            update_row = []
            for i, child in enumerate(dpg.get_item_children(f"edit_table_row{x}",1)):
                update_row.append(dpg.get_value(child))
                print(dpg.get_value(child))
                pimp.update_database(pimp.active_table, columns[i], update_row[i], update_row[0])
    except SystemError: # No more rows , find another fix
        pass
    dpg.delete_item("edit_save_button")
    pimp.refresh_db()
    hent_tabel()


def edit_product_test(table = None):
    input_id = dpg.get_value("edit_product_input")
    active_table = pimp.db_client.get_columns(pimp.active_table)
    current_product = pimp.get_active(pimp.active_table) if input_id == "*" else pimp.get_active(pimp.active_table,input_id)
    if not current_product:
        dpg.set_value("current_table", f"{input_id} er ikke et valid {pimp.active_table} id")
        return None
    elif input_id== "":
        dialog_popup()
        return None
    print(current_product)
    dpg.set_value("current_table", f"Edit af {pimp.active_table} med ID: {input_id}")
    dpg.delete_item("maintabel")
    with dpg.group(parent=main_window):
        dpg.add_button(label="Gem Ændringer", callback=get_edit_fields, tag="edit_save_button", height=30, width=300, parent=main_window)
    with dpg.table(header_row=True, row_background=True,
                   borders_innerH=True, borders_outerH=True, borders_innerV=True,
                   borders_outerV=True, height=H//2-100, sortable=True, tag="maintabel", parent=main_window, resizable=True, callback=table_info_callback) as table_window:
        # use add_table_column to add columns to the table,
        # table columns use slot 0

        small_col = ["id", "portfolio_id", "project_id", "product_id", "manager_id", "Produkt ID", "PManager"]
        date_col = ["start_date","est_end_date","end_date","ended_date"]

        for col in active_table:
            if col in small_col:

                dpg.add_table_column(label=col, width_fixed=True, width=30)
            elif col in date_col:
                dpg.add_table_column(label=col, width_fixed=True, width=70)

            elif col == "name":
                dpg.add_table_column(label=col, width_fixed=True, width=100)
            else:
                dpg.add_table_column(label=col)


        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        for idx,row in enumerate(current_product):
                with dpg.table_row(height=30, tag=f"edit_table_row{idx}"):
                        for i, row in enumerate(row):
                            if active_table[i] == 'id':
                                    dpg.add_text(row)
                            elif active_table[i] == 'name':
                                dpg.add_input_text(default_value=row, width=200)
                            elif active_table[i] in ['specifications', 'beskrivelse']:
                                dpg.add_input_text(default_value=row, width=500)
                            elif active_table[i] in date_col:
                                if active_table[i] == "ended_date" or active_table[i] == "end_date":
                                    if row != None:
                                        dpg.add_input_text(default_value=row.strftime("%d/%m/%Y"), decimal=True)

                                    else:
                                        dpg.add_input_text(default_value="")
                                else:
                                    dpg.add_input_text(default_value=row.strftime("%d/%m/%Y"), decimal=True)
                            else:

                                dpg.add_input_text(default_value=row)


dpg.create_viewport(title='Product Information Manager Process ', width=W, height=H)


# add a font registry
with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("fonts\\HelveticaNeueMediumExtended.otf", 16)
    second_font = dpg.add_font("fonts\\HelveticaNeueLTW0697BlkCnObl.otf", 60)
    col_heading = dpg.add_font("fonts\\HelveticaNeueMediumExtended.otf", 22)

#iw, ih, ic, idata = dpg.load_image("icons/icons8-back-arrow-48.png")
#iw2, ih2, ic2, idata2 = dpg.load_image("icons/icons8-forward-button-48.png")
with dpg.texture_registry(show=True):
    iw, ih, ic, idata = dpg.load_image("icons/icons8-back-arrow-48.png")
    dpg.add_static_texture(width=iw, height=ih, default_value=idata, tag="back_icon")
    iw, ih, ic, idata = dpg.load_image("icons/icons8-forward-button-48.png")
    dpg.add_static_texture(width=iw, height=ih, default_value=idata, tag="next_icon")
    iw, ih, ic, idata = dpg.load_image("icons/icons8-done-48.png")
    dpg.add_static_texture(width=iw, height=ih, default_value=idata, tag="done_icon")
    iw, ih, ic, idata = dpg.load_image("icons/icons8-enter-48.png")
    dpg.add_static_texture(width=iw, height=ih, default_value=idata, tag="enter_icon")
    iw, ih, ic, idata = dpg.load_image("icons/icons8-edit-48.png")
    dpg.add_static_texture(width=iw, height=ih, default_value=idata, tag="edit_icon")

with dpg.window(width=W-15, height=H-220, no_collapse=True, no_title_bar=True, no_move=True) as main_window:

    with dpg.menu_bar():
        with dpg.menu(label="Filer"):
            dpg.add_menu_item(label="Tilslut Database", callback=print_info)
            dpg.add_menu_item(label="Luk Database", callback=print_info)

        with dpg.menu(label="Vis"):
            dpg.add_menu_item(label="Show Data Magic", callback=lambda: dpg.configure_item(data_magic, show=True))
            dpg.add_menu_item(label="Hide Data Magic", callback=print_info)


        with dpg.menu(label="Moduler"):
            dpg.add_checkbox(label="Fashion Modul", callback=print_info, default_value=True)
            dpg.add_checkbox(label="Emballage Modul", callback=print_info, default_value=False)
            dpg.add_checkbox(label="Møbel Modul", callback=print_info,  default_value=False)
        dpg.add_text(f"Logget på som @Kim d. {datetime.now().strftime('%d/%m/%Y - %H:%M:%S')}", color=[0, 0, 255, 255], parent=main_window, tag="user")

    dpg.add_spacer(height=10)

    with dpg.group(horizontal=True, width=200):

        dpg.add_text("Fra dato")
        dpg.add_input_text(decimal=True, callback=print_info)
        dpg.add_text("Til dato")
        dpg.add_input_text(decimal=True, callback=print_info)
        dpg.add_button(label="Filtrer", callback=print_info)
        dpg.add_combo(label="Produktstadie", items=["Alle", "Igangværende", "Afsluttede"], callback=print_info)
        dpg.add_input_text(indent=1150, tag="search", callback=search_func)
        dpg.add_button(label="Søg", callback=search_func)
    dpg.add_spacer(height=20)
    with dpg.group(horizontal=True):
        dpg.add_image_button(texture_tag="back_icon", callback=back_button)
        dpg.add_image_button(texture_tag="next_icon", callback=next_button)
    dpg.add_text(pimp.active_table.upper(), tag="current_table")
    with dpg.group(horizontal=True):
        dpg.add_text(f"Redigere ID: ")
        dpg.add_input_text(tag="edit_product_input", width=100)
        dpg.add_image_button(texture_tag="edit_icon", callback=edit_product_test, height=16, width=16, user_data=dpg.get_value("edit_product_input"))
    with dpg.window(label="Data Magic",width=600, height=300, pos=(800,150), show=False) as data_magic:
            with dpg.group(horizontal=True):
                #TODO Færdiggør Custom Queries og Visualisering
                dpg.add_button(label=f"Overview 1", callback=custom_q, user_data="Q1")
                dpg.add_button(label=f"Overview 2", callback=custom_q, user_data="Q2")




    dpg.add_spacer(height=40)


with dpg.window(label="PIM STATS",width=800, height=220, pos=(0,680), no_title_bar=True, no_collapse=True, no_move=True, no_resize=True):
    with dpg.group(horizontal=True):
        dpg.add_simple_plot(label="", default_value=(0.3, 0.9, 2.5, 8.9, 3.6,4.2,7.1,6.5,2.9), overlay="VISUALISERING PLACEHOLDER", height=180, width=800, histogram=True)
        dpg.add_spacer(width=50)
with dpg.window(label="Ændringslog",width=780, height=220, pos=(W//2,680), no_title_bar=True, no_collapse=True, no_move=True, no_resize=True):
    #change_log = pimp.db_client.run_custom_query('SHOW BINARY LOGS') # TODO: Change to show changes in the database via. cloud access
    change_user = [x for x in pimp.get_employees()]
    change_info = ["ID: 1 - updated project progress to 50%","ID: 2 - added new product to project","ID: 3 - updated design specifications",
                   "ID: 4 - started construction phase","ID: 5 - completed prototype testing", "ID: 6 - revised project timeline",
                   "ID: 7 - added new team member to project","ID: 8 - updated project budget","ID: 9 - resolved issue with product design",
                   "ID: 10 - completed project milestone"]

    dpg.add_text(default_value="Seneste Ændringer:", tag="change_log_title")
    for i,change in enumerate(change_user[:10]):

        dpg.add_text(f"User: {change[1]} Role: {change[2]} Change: {change_info[i]}")

# with dpg.window(label="Buttons", pos=(0, H-150), no_collapse=False, no_title_bar=True, no_background=True) as button_options:
#
#     with dpg.group(horizontal=True, width=200):
#         dpg.add_button(label="<-", callback=back_button)
#         dpg.add_button(label="->", callback=next_button)
#         dpg.add_button(label="Commit Data Ændringer", callback=get_edit_fields)
#         dpg.add_button(label="Hent Data", callback=hent_tabel)


light_theme()



#dpg.bind_theme(global_theme)


hent_tabel()
dpg.bind_font(default_font)
dpg.bind_item_font("current_table", second_font)
dpg.bind_item_font("change_log_title", col_heading)


#dpg.bind_item_font("maintabel", col_heading)
#dpg.bind_theme(global_theme)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
