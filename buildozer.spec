[app]
title = HamzaTradeApp
package.name = hamzatrade
package.domain = org.hamza
source.dir = .
source.main = Hama2TradeApp.py
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 1.0
requirements = python3,kivy,plyer,python-binance,matplotlib,numpy,openssl,certifi,requests,pandas
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE, FOREGROUND_SERVICE, WAKE_LOCK
android.api = 34
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 34.0.0
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
java.heap_size = 4G
android.arch = arm64-v8a
