"""
App entry point, will capture all unhandled errors and report to user in a messagebox.
"""
try:
    import ctypes, os, sys

    PLATFORM_IS_WINDOWS = sys.platform.startswith("win")

    if not PLATFORM_IS_WINDOWS:
        raise Exception("non-windows platform not supported")

    def message_box(msg, title=f"Python Exception"):
        if PLATFORM_IS_WINDOWS:
            # MB_OK | MB_ICONEXCLAMATION | MB_SYSTEMMODAL
            flags = 0x00000000 | 0x00000030 | 0x00001000
            ctypes.windll.user32.MessageBoxW(None, msg, title, flags)
        else:
            raise Exception("non-windows platform not supported")

    ######################################################################
    ##                        PUT USER CODE HERE                        ##
    ######################################################################

    from app import App

    app = App()
    app.MainLoop()

# Unhandled exceptions get displayed as a message box to the user
except Exception as ex:
    import sys, traceback

    module_path = os.path.realpath(__file__)
    trace = "".join(traceback.format_exception(ex))
    message_box(
        trace
        + "-" * 60
        + f"\nScript Path: {module_path}\n\nPython Version: {sys.version}",
        title="Python Exception Traceback",
    )
