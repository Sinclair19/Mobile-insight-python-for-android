
from jnius import autoclass


def hide_loading_screen():
    mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
    mActivity.removeLoadingScreen()
