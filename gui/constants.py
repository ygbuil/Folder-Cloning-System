APP_NAME = "Easy Backup"
LABEL_CACHE = "label_cache.json"

X_ORIGIN_SELECTOR = 200
Y_ORIGIN_SELECTOR = 35

X_ARROW = 380
Y_ARROW = Y_ORIGIN_SELECTOR + 26
ARROW_PATH = "gui/arrow.png"
ARROW_SIZE = (38, 38)

X_DESTINATION_SELECTOR = X_ORIGIN_SELECTOR
Y_DESTINATION_SELECTOR = Y_ARROW + 35

X_TRIGGER_BUTTON = X_ORIGIN_SELECTOR
Y_TRIGGER_BUTTON = Y_DESTINATION_SELECTOR + 50

PROGRESSBAR_WIDTH = 150

ROOT_WINDOW_WIDTH = 800
ROOT_WINDOW_HEIGHT = 600

TITLE_FONT = ("Helvetica", 20, "bold")

WARNING_WINDOW_WIDTH = 400
WARNING_WINDOW_HEIGHT = 210

DIRECTORY_SELECTOR_BUTTON_COLOR = "#000000"
DIRECTORY_SELECTOR_BUTTON_HOVER_COLOR = "#505050"
CANCEL_BUTTON_COLOR = "#B23030"
CANCEL_BUTTON_HOVER_COLOR = "#FF0000"
CONTINUE_BUTTON_COLOR = TRIGGER_BUTTON_COLOR = "#238635"
CONTINUE_BUTTON_HOVER_COLOR = TRIGGER_BUTTON_HOVER_COLOR = "#2EA043"
