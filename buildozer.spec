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
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
log_level = 2
warn_on_root = 1
