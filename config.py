# Configuration

# config_local is out of git repo
try:
    from config_local import wifi_pswd as local_wifi_pswd, wifi_ssid as local_wifi_ssid
except ImportError:
    local_wifi_pswd = ""
    local_wifi_ssid = ""

# Wifi connection configuration
wifi_ssid = local_wifi_ssid
wifi_pswd = local_wifi_pswd
wifi_hostname = "w1070"

# Web server port
web_port = 80

# Pins config for RS
rs_tx_pin = 0
rs_rx_pin = 1

# Logging
verbose = True

# Watchdog enabled/disabled
wdt_enabled = False

# Host to ping for checking the connection is alive (eg router), if not watchdog will restart the app
wdt_url = "11.1.1.1"

# enabling/disabling live reload
live_reload = False