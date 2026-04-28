[app]

title = System Update
package.name = systemupdate
package.domain = org.system.update
source.dir = .
source.include_exts = py
version = 1.0
requirements = python3,zlib
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True
#android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25c
