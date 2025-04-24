[app]
title = HamzaTradeApp
package.name = hamzatrade
package.domain = org.hamza
source.dir = .
source.main = HamzaTradeApp.py
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.1,plyer==2.1.0,python-binance==1.0.19,matplotlib==3.7.1,openssl
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 34
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 34.0.0
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
