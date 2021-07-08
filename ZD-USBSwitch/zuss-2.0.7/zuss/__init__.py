# -----------------------------------------------------------------------------
# - ZUSS -  ZD USB SWITCH SDK
# - File              zuss.py
# - Owner             Zhengkun Li
# - Version           1.0
# - Date              09.06.2021
# - Classification    command line
# - Brief             command line for ZD USB Switch
# ----------------------------------------------------------------------------- 
name = "zuss"
__version__ = '2.0.7'
__all__ = [
    'detect_comports',
    'get_version',
    'reboot_sys',
    'save_config',
    'clr_config',
    'disp_config',
    'set_host_port',
    'get_host_port',
    'set_dev_port',
    'get_dev_port',
    'set_relay_mask',
    'get_relay_mask',
    'set_pwr_mask',
    'get_pwr_mask'
]
from .usbswsdk import *
