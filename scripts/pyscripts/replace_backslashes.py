############################
# Brian Hooper             #
# 11/26/2019               #
#                          #
# Replace any backslashes  #
# with forward slashes     #
# in the current item      #
# you have copied          #
############################

try:
    import win32clipboard
except ImportError:
    print("Error: You must install the \"pywin32\" module to use this script")
    exit(1)

def get_cb():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

def fix_data(data):
    return data.replace("\\", "/")

def set_cb(data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(data)
    win32clipboard.CloseClipboard()

if __name__ == "__main__":
    data = get_cb()
    data = fix_data(data)
    set_cb(data)