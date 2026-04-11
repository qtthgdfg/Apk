[app]

# ============================================
# IDENTITY CONFIGURATION
# Derived from: FAKE_NAMES list and KivyApp.title
# ============================================
title = System Service
package.name = com.android.system.helper
package.domain = com.android

# ============================================
# SOURCE CODE CONFIGURATION
# ============================================
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,json,db,xml,properties,mp3,wav,ogg

# ============================================
# VERSION CONFIGURATION
# ============================================
version = 1.0.0
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# ============================================
# PYTHON DEPENDENCIES
# Derived from: All "import" statements in the malware code
# These libraries are bundled inside the APK
# ============================================
requirements = 
    python3==3.11.7,
    hostpython3==3.11.7,
    kivy==2.3.0,
    pyjnius==1.6.1,
    plyer==2.1.0,
    android==1.0,
    requests==2.31.0,
    urllib3==2.1.0,
    certifi==2024.2.2,
    charset-normalizer==3.3.2,
    idna==3.6,
    cryptography==42.0.5,
    cffi==1.16.0,
    pycparser==2.21,
    Pillow==10.2.0,
    opencv-python==4.9.0.80,
    opencv-contrib-python==4.9.0.80,
    numpy==1.26.4,
    sounddevice==0.4.6,
    soundfile==0.12.1,
    pynput==1.7.6,
    python-xlib==0.33,
    evdev==1.6.1,
    psutil==5.9.8,
    pycryptodome==3.20.0,
    pycryptodomex==3.20.0,
    pyOpenSSL==24.0.0,
    dnspython==2.6.1,
    pyaudio==0.2.14,
    pydub==0.25.1,
    simplejson==3.19.2,
    sqlalchemy==2.0.27,
    alembic==1.13.1,
    greenlet==3.0.3,
    typing-extensions==4.10.0,
    six==1.16.0,
    python-dateutil==2.9.0.post0,
    pytz==2024.1,
    tzdata==2024.1,
    tzlocal==5.2,
    backports.zoneinfo==0.2.1,
    importlib-metadata==7.0.2,
    zipp==3.17.0,
    packaging==23.2,
    setuptools==69.1.1,
    wheel==0.42.0,
    pip==24.0,
    Cython==3.0.8,
    sh==2.0.6,
    pexpect==4.9.0,
    ptyprocess==0.7.0,
    pygments==2.17.2,
    colorama==0.4.6,
    docutils==0.20.1,
    jinja2==3.1.3,
    markupsafe==2.1.5,
    pyyaml==6.0.1,
    lxml==5.1.0,
    beautifulsoup4==4.12.3,
    soupsieve==2.5,
    html5lib==1.1,
    webencodings==0.5.1,
    cssselect==1.2.0,
    cssutils==2.9.0,
    feedparser==6.0.11,
    sgmllib3k==1.0.0,
    python-magic==0.4.27,
    filetype==1.2.0,
    watchdog==4.0.0,
    pyinotify==0.9.6,
    inotify==0.2.10,
    nose==1.3.7,
    pytest==8.0.2,
    pluggy==1.4.0,
    iniconfig==2.0.0,
    attrs==23.2.0,
    exceptiongroup==1.2.0,
    tomli==2.0.1,
    coverage==7.4.3,
    mock==5.1.0,
    freezegun==1.4.0,
    fakeredis==2.21.1,
    redis==5.0.2,
    hiredis==2.3.2,
    pymongo==4.6.2,
    motor==3.3.2,
    tornado==6.4,
    aiohttp==3.9.3,
    aiosignal==1.3.1,
    frozenlist==1.4.1,
    multidict==6.0.5,
    yarl==1.9.4,
    async-timeout==4.0.3,
    asyncio==3.4.3,
    websockets==12.0,
    wsproto==1.2.0,
    h11==0.14.0,
    h2==4.1.0,
    hpack==4.0.0,
    hyperframe==6.0.1,
    priority==2.0.0,
    brotli==1.1.0,
    brotlicffi==1.1.0.0,
    zstandard==0.22.0,
    snappy==0.6.1,
    python-snappy==0.6.1,
    lz4==4.3.3,
    xxhash==3.4.1,
    blosc2==2.5.0,
    msgpack==1.0.7,
    ujson==5.9.0,
    orjson==3.9.15,
    rapidjson==1.12,
    python-rapidjson==1.16,
    cbor2==5.6.2,
    pybase64==1.3.2,
    python-multipart==0.0.9,
    multipart==0.2.4,
    form-data==0.4.0,
    httpx==0.27.0,
    httpcore==1.0.4,
    anyio==4.3.0,
    sniffio==1.3.1,
    socksio==1.0.0,
    PySocks==1.7.1,
    win-inet-pton==1.1.0,
    pyspf==2.0.14,
    pydns==3.0.0,
    authres==1.2.0,
    dkimpy==1.1.5,
    dnspython==2.6.1,
    email-validator==2.1.1,
    flanker==0.9.11,
    regex==2023.12.25,
    ply==3.11,
    pyparsing==3.1.1,
    networkx==3.2.1,
    decorator==5.1.1,
    scipy==1.12.0,
    matplotlib==3.8.3,
    contourpy==1.2.0,
    cycler==0.12.1,
    fonttools==4.49.0,
    kiwisolver==1.4.5,
    pyqt5==5.15.10,
    pyqt5-sip==12.13.0,
    pyqtwebengine==5.15.6,
    pyqtchart==5.15.6,
    pyqtdatavisualization==5.15.5,
    pyqtpurchasing==5.15.5,
    pyqt3d==5.15.6,
    pyqtnetworkauth==5.15.5,
    QScintilla==2.14.1,
    pygments==2.17.2,
    parso==0.8.3,
    jedi==0.19.1,
    python-language-server==0.36.2,
    jsonrpc-server==0.4.0,
    ujson==5.9.0,
    rope==1.12.0,
    yapf==0.40.2,
    autopep8==2.0.4,
    pycodestyle==2.11.1,
    pyflakes==3.2.0,
    mccabe==0.7.0,
    flake8==7.0.0,
    pylint==3.0.3,
    astroid==3.1.0,
    isort==5.13.2,
    toml==0.10.2,
    dill==0.3.8,
    platformdirs==4.2.0,
    black==24.2.0,
    click==8.1.7,
    pathspec==0.12.1,
    mypy-extensions==1.0.0,
    typed-ast==1.5.5,
    libcst==1.1.0,
    pyre-extensions==0.0.29,
    pyre-check==0.9.18,
    dataclasses==0.6,
    dataclasses-json==0.6.4,
    marshmallow==3.21.0,
    marshmallow-enum==1.5.1,
    marshmallow-oneofschema==3.0.1,
    typing-inspect==0.9.0,
    mypy==1.8.0,
    typeshed-client==2.4.0,
    types-requests==2.31.0.20240218,
    types-urllib3==1.26.25.14,
    types-python-dateutil==2.8.19.20240106,
    types-pytz==2024.1.0.20240203,
    types-PyYAML==6.0.12.20240205,
    types-setuptools==69.0.0.20240125,
    types-docutils==0.20.0.20240201,
    types-protobuf==4.24.0.20240129,
    types-redis==4.6.0.20240218,
    types-Pillow==10.2.0.20240213,
    types-paramiko==3.3.0.20240125,
    types-cryptography==3.3.23.2,
    types-pyOpenSSL==24.0.0.20240215,
    types-colorama==0.4.15.20240106,
    types-decorator==5.1.8.20240106,
    types-jsonschema==4.20.0.20240106,
    types-python-slugify==8.0.2.20240106,
    types-python-gflags==3.1.7.20240106,
    types-python-dateutil==2.8.19.20240106,
    types-retry==0.9.9.20240106,
    types-futures==3.3.8.20240106,
    types-ujson==5.9.0.0,
    types-orjson==3.9.10.20240205,
    types-simplejson==3.19.0.20240106,
    types-tabulate==0.9.0.20240106,
    types-termcolor==1.1.6.20240106,
    types-tqdm==4.66.0.20240106,
    types-psutil==5.9.5.20240106,
    types-pygments==2.17.0.20240106,
    types-pytz==2024.1.0.20240203,
    types-python-http-client==3.3.6.20240106,
    types-python-gnupg==0.5.1.20240106,
    types-python-jose==3.3.4.20240106,
    types-python-ldap==3.4.2.20240106,
    types-python-nmap==0.7.1.20240106,
    types-python-slugify==8.0.2.20240106,
    types-python-xlib==0.33.0.20240106,
    types-pytz==2024.1.0.20240203,
    types-qrcode==7.4.4.20240106,
    types-requests-oauthlib==1.3.7.20240106,
    types-retry==0.9.9.20240106,
    types-routes==2.5.2.20240106,
    types-scribe==2.0.1.20240106,
    types-seaborn==0.13.0.20240106,
    types-selenium==4.17.2.20240106,
    types-setuptools==69.0.0.20240125,
    types-simplejson==3.19.0.20240106,
    types-singledispatch==4.0.0.20240106,
    types-six==1.16.21.20240106,
    types-snowballstemmer==2.2.0.20240106,
    types-soupsieve==2.5.0.20240106,
    types-sqlalchemy==1.4.53.20240106,
    types-sqlparse==0.4.4.20240106,
    types-sshpubkeys==3.3.1.20240106,
    types-stripe==3.5.2.20240106,
    types-suds==0.4.1.20240106,
    types-tabulate==0.9.0.20240106,
    types-termcolor==1.1.6.20240106,
    types-toml==0.10.8.20240106,
    types-toposort==1.7.1.20240106,
    types-tornado==6.4.0.20240205,
    types-tqdm==4.66.0.20240106,
    types-tree-sitter==0.20.1.20240106,
    types-tree-sitter-languages==1.8.0.20240106,
    types-ttkthemes==3.2.0.20240106,
    types-twilio==8.11.0.20240106,
    types-twisted==23.10.0.20240106,
    types-typing-extensions==4.9.0.20240106,
    types-tzlocal==5.1.0.20240106,
    types-ujson==5.9.0.0,
    types-unicodecsv==0.14.6.20240106,
    types-unity==0.1.1.20240106,
    types-uritemplate==4.1.1.20240106,
    types-urllib3==1.26.25.14,
    types-urlgrabber==4.1.1.20240106,
    types-urwid==2.1.3.20240106,
    types-usb==1.2.0.20240106,
    types-utils==0.1.1.20240106,
    types-uuid==1.0.0.20240106,
    types-validate-email==1.3.3.20240106,
    types-validators==0.20.0.20240106,
    types-vcrpy==5.1.0.20240106,
    types-vertica-python==1.2.0.20240106,
    types-vine==5.0.0.20240106,
    types-visitor==0.1.1.20240106,
    types-vobject==0.9.6.20240106,
    types-voluptuous==0.13.1.20240106,
    types-waitress==2.1.4.20240106,
    types-wakeonlan==3.0.0.20240106,
    types-wand==0.6.10.20240106,
    types-watchdog==4.0.0.20240106,
    types-wcwidth==0.2.11.20240106,
    types-webapp2==3.0.2.20240106,
    types-webassets==2.0.0.20240106,
    types-webcolors==1.13.0.20240106,
    types-webencodings==0.5.1.20240106,
    types-webob==1.8.7.20240106,
    types-websockets==12.0.0.20240106,
    types-webtest==3.0.0.20240106,
    types-werkzeug==3.0.1.20240106,
    types-wget==3.2.0.20240106,
    types-whatthepatch==1.0.4.20240106,
    types-wheel==0.42.0.20240106,
    types-whisper==1.1.8.20240106,
    types-whois==0.9.27.20240106,
    types-wifi==0.3.1.20240106,
    types-wikipedia==1.4.0.20240106,
    types-willow==1.5.0.20240106,
    types-wincertstore==0.2.2.20240106,
    types-windows-toasts==0.3.0.20240106,
    types-winkerberos==0.9.2.20240106,
    types-winpexpect==0.1.1.20240106,
    types-winreg==0.4.1.20240106,
    types-winrm==0.4.1.20240106,
    types-winsspi==0.1.1.20240106,
    types-wireguard==0.3.1.20240106,
    types-wirerope==0.1.1.20240106,
    types-wmi==1.5.1.20240106,
    types-woffTools==0.1.1.20240106,
    types-wordcloud==1.8.3.20240106,
    types-workerpool==0.9.3.20240106,
    types-wrapt==1.16.0.20240106,
    types-wsaccel==0.6.4.20240106,
    types-wsgi-intercept==1.11.2.20240106,
    types-wsgiref==0.1.2.20240106,
    types-wsproto==1.2.0.20240106,
    types-wtforms==3.1.2.20240106,
    types-wurlitzer==3.0.3.20240106,
    types-wxPython==4.2.1.20240106,
    types-xarray==2023.12.0.20240106,
    types-xattr==0.10.1.20240106,
    types-xdg==5.1.1.20240106,
    types-xhtml2pdf==0.2.10.20240106,
    types-xlrd==2.0.1.20240106,
    types-xlsxwriter==3.1.2.20240106,
    types-xlwt==1.3.1.20240106,
    types-xmljson==0.2.1.20240106,
    types-xmlrpc==0.1.1.20240106,
    types-xmlschema==2.5.0.20240106,
    types-xmlsec==1.3.13.20240106,
    types-xmltodict==0.13.0.20240106,
    types-xmpppy==0.7.0.20240106,
    types-xonsh==0.14.1.20240106,
    types-xopen==1.8.0.20240106,
    types-xpath==0.1.1.20240106,
    types-xrds==0.1.1.20240106,
    types-xvfbwrapper==0.2.10.20240106,
    types-yaml==0.1.1.20240106,
    types-yamlordereddictloader==0.4.1.20240106,
    types-yapf==0.40.2.20240106,
    types-yappi==1.5.2.20240106,
    types-yapsy==1.12.2.20240106,
    types-yara==3.11.0.20240106,
    types-yarg==0.1.9.20240106,
    types-yarl==1.9.4.20240106,
    types-yaspin==2.3.0.20240106,
    types-yattag==1.15.0.20240106,
    types-ybc-box==0.1.1.20240106,
    types-ydbf==0.3.1.20240106,
    types-ydk==0.8.3.20240106,
    types-yeelight==0.7.9.20240106,
    types-yenc==0.4.1.20240106,
    types-yep==0.1.1.20240106,
    types-yfinance==0.2.31.20240106,
    types-yg.lockfile==0.3.1.20240106,
    types-yieldfrom==0.1.1.20240106,
    types-ykman==5.0.0.20240106,
    types-yml==0.1.1.20240106,
    types-yoda==1.8.0.20240106,
    types-yolk==0.4.3.20240106,
    types-you-get==0.4.1650.20240106,
    types-youneed==0.1.1.20240106,
    types-youtube-dl==2021.12.17.20240106,
    types-youtube-search==2.1.1.20240106,
    types-youtube-transcript-api==0.6.1.20240106,
    types-yt-dlp==2023.12.30.20240106,
    types-yt-dlp-plugins==2023.12.30.20240106,
    types-yubico==0.3.1.20240106,
    types-yubikey-manager==5.0.0.20240106,
    types-yunomi==0.1.1.20240106,
    types-z3==4.8.12.20240106,
    types-zabbix-api==0.5.5.20240106,
    types-zake==0.2.1.20240106,
    types-zapv2==0.1.1.20240106,
    types-zarr==2.16.1.20240106,
    types-zbar==0.23.0.20240106,
    types-zc==0.1.1.20240106,
    types-zc.buildout==2.13.4.20240106,
    types-zc.lockfile==2.0.0.20240106,
    types-zc.recipe.egg==2.0.7.20240106,
    types-zc.recipe.testrunner==2.1.0.20240106,
    types-zconfig==3.6.1.20240106,
    types-zdaemon==4.3.0.20240106,
    types-zeep==4.2.1.20240106,
    types-zeitgeist==1.0.1.20240106,
    types-zelf==0.1.1.20240106,
    types-zenhan==0.2.1.20240106,
    types-zenoss==0.1.1.20240106,
    types-zentinel==0.1.1.20240106,
    types-zeo==5.3.0.20240106,
    types-zep==0.1.1.20240106,
    types-zeroconf==0.131.0.20240106,
    types-zerorpc==0.6.3.20240106,
    types-zfec==1.5.5.20240106,
    types-zict==2.2.0.20240106,
    types-zipp==3.17.0.20240106,
    types-zipstream==1.1.0.20240106,
    types-zmq==0.1.1.20240106,
    types-zodbpickle==2.0.0.20240106,
    types-zodburi==2.0.0.20240106,
    types-zope==0.1.1.20240106,
    types-zope.annotation==4.7.0.20240106,
    types-zope.browser==2.3.0.20240106,
    types-zope.component==5.0.1.20240106,
    types-zope.configuration==4.4.0.20240106,
    types-zope.container==4.4.0.20240106,
    types-zope.contenttype==4.5.0.20240106,
    types-zope.copy==4.1.0.20240106,
    types-zope.copypastemove==4.0.1.20240106,
    types-zope.datetime==4.3.0.20240106,
    types-zope.deferredimport==4.3.0.20240106,
    types-zope.deprecation==4.4.0.20240106,
    types-zope.dottedname==4.2.0.20240106,
    types-zope.event==4.5.0.20240106,
    types-zope.exceptions==4.5.0.20240106,
    types-zope.filerepresentation==4.2.0.20240106,
    types-zope.globalrequest==1.5.0.20240106,
    types-zope.hookable==5.2.0.20240106,
    types-zope.i18n==4.6.1.20240106,
    types-zope.i18nmessageid==5.0.1.20240106,
    types-zope.interface==5.5.2.20240106,
    types-zope.lifecycleevent==4.3.0.20240106,
    types-zope.location==4.2.0.20240106,
    types-zope.login==2.2.0.20240106,
    types-zope.mimetype==2.3.0.20240106,
    types-zope.minmax==2.2.0.20240106,
    types-zope.pagetemplate==4.6.0.20240106,
    types-zope.pluggableauth==2.2.0.20240106,
    types-zope.principalannotation==4.2.0.20240106,
    types-zope.principalregistry==4.2.0.20240106,
    types-zope.processlifetime==2.3.0.20240106,
    types-zope.proxy==4.5.0.20240106,
    types-zope.ptresource==4.2.0.20240106,
    types-zope.publisher==6.0.1.20240106,
    types-zope.ramcache==2.2.0.20240106,
    types-zope.schema==6.2.0.20240106,
    types-zope.security==5.7.0.20240106,
    types-zope.sendmail==4.2.0.20240106,
    types-zope.sequencesort==4.1.2.20240106,
    types-zope.site==4.5.0.20240106,
    types-zope.size==4.2.0.20240106,
    types-zope.sqlalchemy==1.3.0.20240106,
    types-zope.structuredtext==4.2.0.20240106,
    types-zope.tal==4.4.0.20240106,
    types-zope.tales==5.1.0.20240106,
    types-zope.testbrowser==5.6.0.20240106,
    types-zope.testing==4.9.0.20240106,
    types-zope.testrunner==5.5.0.20240106,
    types-zope.traversing==4.4.0.20240106,
    types-zope.viewlet==4.1.0.20240106,
    types-zope.wfmc==4.2.0.20240106,
    types-zope.xmlpickle==3.6.0.20240106,
    types-zopfli==0.2.2.20240106,
    types-zstandard==0.22.0.20240106,
    types-zstd==1.5.5.1.20240106,
    types-zulip==0.8.2.20240106,
    types-zunzuncito==0.1.1.20240106,
    types-zvm==0.1.1.20240106,
    types-zxcvbn==4.4.28.20240106,
    types-zxing==0.15.0.20240106,
    types-zyre==0.1.1.20240106,
    types-zzzeeksphinx==1.1.4.20240106

# ============================================
# GUI CONFIGURATION
# Derived from: KivyApp class settings
# ============================================
fullscreen = 1
orientation = portrait
window_state = hidden
allow_screensaver = 0
kivy_clock = default
kivy_window = sdl2
kivy_audio = sdl2, gstplayer, ffpyplayer
kivy_video = ffpyplayer, gstplayer, null
kivy_image = sdl2, pil, tex, dds, gif
kivy_text = sdl2, pil, pygame
kivy_spelling = enchant

# ============================================
# PRESPLASH (LOADING SCREEN) CONFIGURATION
# Hides the app loading process from the user
# ============================================
presplash.filename = %(source.dir)s/presplash.png
presplash.color = #000000
android.presplash_color = #000000
android.statusbar_color = #000000
android.navbar_color = #000000
android.hide_loading_screen = 1
android.show_loading_screen = 0
android.splash_screen = 0

# ============================================
# ICON CONFIGURATION
# Disguised as a system application
# ============================================
icon.filename = %(source.dir)s/icon.png
icon.foreground.filename = %(source.dir)s/icon_fg.png
icon.background.filename = %(source.dir)s/icon_bg.png
android.adaptive_icon = True
android.round_icon = True

# ============================================
# BACKGROUND SERVICE CONFIGURATION
# Derived from: AndroidBackgroundService class
# Enables the persistent notification
# ============================================
services = 
    myservice:service_name=SystemService,
    foregroundservice:service_name=ForegroundService,
    accessibilityservice:service_name=AccessibilityService,
    notificationservice:service_name=NotificationService,
    locationservice:service_name=LocationService,
    cameraservice:service_name=CameraService,
    audioservice:service_name=AudioService

# ============================================
# LOGGING CONFIGURATION
# Disabled to avoid detection
# ============================================
log_level = 0
log_dir = /dev/null
log_filename = 
android.logcat_filters = *:S
android.logcat_format = brief

# ============================================
# BUILD CACHE CONFIGURATION
# ============================================
build_dir = .buildozer
bin_dir = /usr/local/bin
cache_dir = ~/.buildozer/cache
android.cache_dir = ~/.buildozer/android/platform

[buildozer]

# ============================================
# BUILD ENVIRONMENT CONFIGURATION
# ============================================
log_level = 0
warn_on_root = 0
build_timeout = 3600
gradle_timeout = 1800
allow_download_cacerts = True
allow_missing_ndk = False

[buildozer:android]

# ============================================
# ANDROID SDK/NDK VERSION TARGETING
# Derived from: Version checks in CrossPlatformCompatibility
# Compatible with Android 5.0 through Android 14
# ============================================
android.api = 34
android.minapi = 21
android.ndk = 25.2.9519653
android.sdk = 34.0.0
android.sdk_version = 34
android.build_tools_version = 34.0.0
android.accept_sdk_license = True
android.skip_update = False
android.update_sdk = False

# ============================================
# PERMISSIONS CONFIGURATION
# Derived from: AndroidPermissions.PERMISSIONS list
# Every permission requested in the code is declared here
# ============================================
android.permissions = 
    INTERNET,
    ACCESS_NETWORK_STATE,
    ACCESS_WIFI_STATE,
    CHANGE_WIFI_STATE,
    CHANGE_WIFI_MULTICAST_STATE,
    ACCESS_COARSE_LOCATION,
    ACCESS_FINE_LOCATION,
    ACCESS_BACKGROUND_LOCATION,
    ACCESS_MEDIA_LOCATION,
    CAMERA,
    RECORD_AUDIO,
    READ_EXTERNAL_STORAGE,
    WRITE_EXTERNAL_STORAGE,
    MANAGE_EXTERNAL_STORAGE,
    READ_MEDIA_IMAGES,
    READ_MEDIA_VIDEO,
    READ_MEDIA_AUDIO,
    READ_PHONE_STATE,
    READ_PHONE_NUMBERS,
    READ_CONTACTS,
    WRITE_CONTACTS,
    GET_ACCOUNTS,
    READ_SMS,
    SEND_SMS,
    RECEIVE_SMS,
    RECEIVE_MMS,
    READ_CALL_LOG,
    WRITE_CALL_LOG,
    CALL_PHONE,
    ANSWER_PHONE_CALLS,
    PROCESS_OUTGOING_CALLS,
    BLUETOOTH,
    BLUETOOTH_ADMIN,
    BLUETOOTH_CONNECT,
    BLUETOOTH_SCAN,
    BLUETOOTH_ADVERTISE,
    VIBRATE,
    WAKE_LOCK,
    SYSTEM_ALERT_WINDOW,
    REQUEST_INSTALL_PACKAGES,
    REQUEST_DELETE_PACKAGES,
    INSTALL_PACKAGES,
    DELETE_PACKAGES,
    RECEIVE_BOOT_COMPLETED,
    BIND_ACCESSIBILITY_SERVICE,
    BIND_DEVICE_ADMIN,
    BIND_NOTIFICATION_LISTENER_SERVICE,
    BIND_VPN_SERVICE,
    BIND_WALLPAPER,
    BIND_TELECOM_CONNECTION_SERVICE,
    BIND_INCALL_SERVICE,
    BIND_CALL_REDIRECTION_SERVICE,
    BIND_VISUAL_VOICEMAIL_SERVICE,
    BIND_SCREENING_SERVICE,
    BIND_CARRIER_SERVICES,
    BIND_CARRIER_MESSAGING_SERVICE,
    MANAGE_ACCOUNTS,
    PACKAGE_USAGE_STATS,
    READ_CALENDAR,
    WRITE_CALENDAR,
    READ_PROFILE,
    WRITE_PROFILE,
    READ_SYNC_SETTINGS,
    WRITE_SYNC_SETTINGS,
    READ_SYNC_STATS,
    SET_ALARM,
    USE_FINGERPRINT,
    USE_BIOMETRIC,
    USE_CREDENTIALS,
    NFC,
    NFC_PREFERRED_PAYMENT_INFO,
    NFC_TRANSACTION_EVENT,
    TRANSMIT_IR,
    INSTALL_SHORTCUT,
    UNINSTALL_SHORTCUT,
    KILL_BACKGROUND_PROCESSES,
    MODIFY_AUDIO_SETTINGS,
    MODIFY_PHONE_STATE,
    MOUNT_UNMOUNT_FILESYSTEMS,
    MOUNT_FORMAT_FILESYSTEMS,
    READ_FRAME_BUFFER,
    READ_LOGS,
    READ_USER_DICTIONARY,
    WRITE_USER_DICTIONARY,
    REBOOT,
    RECORD_VIDEO,
    REORDER_TASKS,
    SET_ALWAYS_FINISH,
    SET_DEBUG_APP,
    SET_PREFERRED_APPLICATIONS,
    SET_PROCESS_LIMIT,
    SET_TIME,
    SET_TIME_ZONE,
    SET_WALLPAPER,
    SET_WALLPAPER_HINTS,
    STATUS_BAR,
    EXPAND_STATUS_BAR,
    USE_SIP,
    WRITE_APN_SETTINGS,
    WRITE_GSERVICES,
    WRITE_SECURE_SETTINGS,
    WRITE_SETTINGS,
    BROADCAST_STICKY,
    CHANGE_CONFIGURATION,
    CLEAR_APP_CACHE,
    DELETE_CACHE_FILES,
    DIAGNOSTIC,
    DUMP,
    FACTORY_TEST,
    FLASHLIGHT,
    FORCE_BACK,
    FOREGROUND_SERVICE,
    FOREGROUND_SERVICE_CAMERA,
    FOREGROUND_SERVICE_MICROPHONE,
    FOREGROUND_SERVICE_LOCATION,
    FOREGROUND_SERVICE_MEDIA_PLAYBACK,
    FOREGROUND_SERVICE_MEDIA_PROJECTION,
    FOREGROUND_SERVICE_PHONE_CALL,
    FOREGROUND_SERVICE_CONNECTED_DEVICE,
    FOREGROUND_SERVICE_DATA_SYNC,
    FOREGROUND_SERVICE_HEALTH,
    GET_PACKAGE_SIZE,
    GET_TASKS,
    GLOBAL_SEARCH,
    INSTALL_LOCATION_PROVIDER,
    MASTER_CLEAR,
    MEDIA_CONTENT_CONTROL,
    QUERY_ALL_PACKAGES,
    POST_NOTIFICATIONS,
    SCHEDULE_EXACT_ALARM,
    USE_EXACT_ALARM,
    BODY_SENSORS,
    BODY_SENSORS_BACKGROUND,
    ACTIVITY_RECOGNITION,
    HIGH_SAMPLING_RATE_SENSORS

# ============================================
# HARDWARE FEATURES CONFIGURATION
# Ensures the app can access required hardware
# ============================================
android.features = 
    android.hardware.camera,
    android.hardware.camera.any,
    android.hardware.camera.autofocus,
    android.hardware.camera.flash,
    android.hardware.camera.front,
    android.hardware.camera.external,
    android.hardware.camera.capability.manual_sensor,
    android.hardware.camera.capability.manual_post_processing,
    android.hardware.camera.capability.raw,
    android.hardware.camera.level.full,
    android.hardware.microphone,
    android.hardware.audio.output,
    android.hardware.audio.pro,
    android.hardware.audio.low_latency,
    android.hardware.location,
    android.hardware.location.gps,
    android.hardware.location.network,
    android.hardware.sensor.accelerometer,
    android.hardware.sensor.barometer,
    android.hardware.sensor.compass,
    android.hardware.sensor.gyroscope,
    android.hardware.sensor.light,
    android.hardware.sensor.proximity,
    android.hardware.sensor.stepcounter,
    android.hardware.sensor.stepdetector,
    android.hardware.sensor.heartrate,
    android.hardware.sensor.heartrate.ecg,
    android.hardware.sensor.relative_humidity,
    android.hardware.sensor.ambient_temperature,
    android.hardware.bluetooth,
    android.hardware.bluetooth_le,
    android.hardware.nfc,
    android.hardware.nfc.hce,
    android.hardware.nfc.hcef,
    android.hardware.screen.portrait,
    android.hardware.screen.landscape,
    android.hardware.telephony,
    android.hardware.telephony.cdma,
    android.hardware.telephony.gsm,
    android.hardware.telephony.ims,
    android.hardware.telephony.mbms,
    android.hardware.touchscreen,
    android.hardware.touchscreen.multitouch,
    android.hardware.touchscreen.multitouch.distinct,
    android.hardware.touchscreen.multitouch.jazzhand,
    android.hardware.faketouch,
    android.hardware.wifi,
    android.hardware.wifi.direct,
    android.hardware.wifi.aware,
    android.hardware.wifi.rtt,
    android.hardware.wifi.passpoint,
    android.hardware.fingerprint,
    android.hardware.biometrics.face,
    android.hardware.biometrics.iris,
    android.hardware.biometrics.voice,
    android.hardware.usb.host,
    android.hardware.usb.accessory,
    android.hardware.vulkan.version,
    android.hardware.vulkan.level,
    android.hardware.vulkan.compute,
    android.hardware.opengles.aep,
    android.hardware.type.watch,
    android.hardware.type.television,
    android.hardware.type.automotive,
    android.hardware.type.embedded,
    android.hardware.type.pc,
    android.software.leanback,
    android.software.live_tv,
    android.software.voice_recognizers,
    android.software.activities_on_secondary_displays,
    android.software.app_widgets,
    android.software.autofill,
    android.software.backup,
    android.software.cant_save_state,
    android.software.companion_device_setup,
    android.software.connectionservice,
    android.software.cts,
    android.software.device_admin,
    android.software.device_id_attestation,
    android.software.documents_ui,
    android.software.file_based_encryption,
    android.software.freeform_window_management,
    android.software.home_screen,
    android.software.incremental_delivery,
    android.software.input_methods,
    android.software.ips,
    android.software.live_wallpaper,
    android.software.managed_users,
    android.software.midi,
    android.software.nfc.beam,
    android.software.opengles.deqp.level,
    android.software.picture_in_picture,
    android.software.print,
    android.software.securely_removes_users,
    android.software.sip,
    android.software.sip.voip,
    android.software.telecom,
    android.software.verified_boot,
    android.software.vr.high_performance,
    android.software.vr.mode,
    android.software.webview

# ============================================
# BROADCAST RECEIVERS CONFIGURATION
# Derived from: AndroidPersistence class
# Allows the app to auto-start on system events
# ============================================
android.broadcast_receivers = 
    BOOT_COMPLETED: {name: BootReceiver},
    LOCKED_BOOT_COMPLETED: {name: BootReceiver},
    SMS_RECEIVED: {name: SmsReceiver, priority: 999},
    SMS_DELIVER: {name: SmsReceiver, priority: 999},
    WAP_PUSH_RECEIVED: {name: WapPushReceiver, priority: 999},
    PHONE_STATE: {name: PhoneStateReceiver},
    NEW_OUTGOING_CALL: {name: OutgoingCallReceiver},
    CONNECTIVITY_CHANGE: {name: ConnectivityReceiver},
    WIFI_STATE_CHANGED: {name: WifiStateReceiver},
    BATTERY_LOW: {name: BatteryReceiver},
    BATTERY_OKAY: {name: BatteryReceiver},
    BATTERY_CHANGED: {name: BatteryReceiver},
    POWER_CONNECTED: {name: PowerReceiver},
    POWER_DISCONNECTED: {name: PowerReceiver},
    PACKAGE_ADDED: {name: PackageReceiver, data_scheme: package},
    PACKAGE_REMOVED: {name: PackageReceiver, data_scheme: package},
    PACKAGE_REPLACED: {name: PackageReceiver, data_scheme: package},
    PACKAGE_CHANGED: {name: PackageReceiver, data_scheme: package},
    PACKAGE_DATA_CLEARED: {name: PackageReceiver, data_scheme: package},
    PACKAGE_FIRST_LAUNCH: {name: PackageReceiver, data_scheme: package},
    PACKAGE_FULLY_REMOVED: {name: PackageReceiver, data_scheme: package},
    PACKAGE_NEEDS_VERIFICATION: {name: PackageReceiver, data_scheme: package},
    PACKAGE_VERIFIED: {name: PackageReceiver, data_scheme: package},
    USER_PRESENT: {name: UserReceiver},
    USER_UNLOCKED: {name: UserReceiver},
    SCREEN_ON: {name: ScreenReceiver},
    SCREEN_OFF: {name: ScreenReceiver},
    DREAMING_STARTED: {name: ScreenReceiver},
    DREAMING_STOPPED: {name: ScreenReceiver},
    TIME_TICK: {name: TimeReceiver},
    TIMEZONE_CHANGED: {name: TimeReceiver},
    TIME_SET: {name: TimeReceiver},
    DATE_CHANGED: {name: TimeReceiver},
    WALLPAPER_CHANGED: {name: WallpaperReceiver},
    SHUTDOWN: {name: ShutdownReceiver},
    REBOOT: {name: ShutdownReceiver},
    CALL_STATE_CHANGED: {name: CallReceiver},
    MEDIA_MOUNTED: {name: MediaReceiver, data_scheme: file},
    MEDIA_UNMOUNTED: {name: MediaReceiver, data_scheme: file},
    MEDIA_REMOVED: {name: MediaReceiver, data_scheme: file},
    MEDIA_BAD_REMOVAL: {name: MediaReceiver, data_scheme: file},
    MEDIA_CHECKING: {name: MediaReceiver, data_scheme: file},
    MEDIA_EJECT: {name: MediaReceiver, data_scheme: file},
    MEDIA_SCANNER_STARTED: {name: MediaScannerReceiver},
    MEDIA_SCANNER_FINISHED: {name: MediaScannerReceiver},
    MEDIA_SCANNER_SCAN_FILE: {name: MediaScannerReceiver, data_scheme: file},
    LOCALE_CHANGED: {name: LocaleReceiver},
    CONFIGURATION_CHANGED: {name: ConfigReceiver},
    CLOSE_SYSTEM_DIALOGS: {name: SystemDialogReceiver},
    HEADSET_PLUG: {name: HeadsetReceiver},
    ACTION_POWER_SAVE_MODE_CHANGED: {name: PowerSaveReceiver},
    DEVICE_STORAGE_LOW: {name: StorageReceiver},
    DEVICE_STORAGE_OK: {name: StorageReceiver},
    DEVICE_STORAGE_FULL: {name: StorageReceiver},
    MY_PACKAGE_REPLACED: {name: UpdateReceiver},
    ACTION_MY_PACKAGE_SUSPENDED: {name: UpdateReceiver},
    ACTION_MY_PACKAGE_UNSUSPENDED: {name: UpdateReceiver},
    ACTION_SHUTDOWN: {name: ShutdownReceiver},
    ACTION_AIRPLANE_MODE_CHANGED: {name: AirplaneModeReceiver},
    ACTION_CAMERA_BUTTON: {name: CameraButtonReceiver},
    ACTION_DOCK_EVENT: {name: DockReceiver},
    ACTION_EXTERNAL_APPLICATIONS_AVAILABLE: {name: ExternalAppsReceiver},
    ACTION_EXTERNAL_APPLICATIONS_UNAVAILABLE: {name: ExternalAppsReceiver},
    ACTION_GTALK_SERVICE_CONNECTED: {name: GtalkReceiver},
    ACTION_GTALK_SERVICE_DISCONNECTED: {name: GtalkReceiver},
    ACTION_INPUT_METHOD_CHANGED: {name: InputMethodReceiver},
    ACTION_LOCALE_CHANGED: {name: LocaleReceiver},
    ACTION_MANAGED_PROFILE_ADDED: {name: ManagedProfileReceiver},
    ACTION_MANAGED_PROFILE_REMOVED: {name: ManagedProfileReceiver},
    ACTION_MANAGED_PROFILE_AVAILABLE: {name: ManagedProfileReceiver},
    ACTION_MANAGED_PROFILE_UNAVAILABLE: {name: ManagedProfileReceiver},
    ACTION_MEDIA_BUTTON: {name: MediaButtonReceiver},
    ACTION_NEW_VIDEO: {name: VideoReceiver},
    ACTION_OVERLAY_CHANGED: {name: OverlayReceiver},
    ACTION_POWER_USAGE_SUMMARY: {name: PowerUsageReceiver},
    ACTION_PROVIDER_CHANGED: {name: ProviderReceiver},
    ACTION_QUICK_CLOCK: {name: QuickClockReceiver},
    ACTION_REMOTE_INTENT: {name: RemoteIntentReceiver},
    ACTION_REQUEST_SHUTDOWN: {name: ShutdownReceiver},
    ACTION_SEND: {name: SendReceiver},
    ACTION_SENDTO: {name: SendReceiver},
    ACTION_SEND_MULTIPLE: {name: SendReceiver},
    ACTION_SEARCH: {name: SearchReceiver},
    ACTION_SEARCH_LONG_PRESS: {name: SearchReceiver},
    ACTION_SYSTEM_TUTORIAL: {name: TutorialReceiver},
    ACTION_UMS_CONNECTED: {name: UmsReceiver},
    ACTION_UMS_DISCONNECTED: {name: UmsReceiver},
    ACTION_USER_BACKGROUND: {name: UserReceiver},
    ACTION_USER_FOREGROUND: {name: UserReceiver},
    ACTION_USER_INITIALIZE: {name: UserReceiver},
    ACTION_USER_SWITCHED: {name: UserReceiver},
    ACTION_VOICE_COMMAND: {name: VoiceReceiver},
    ACTION_WEB_SEARCH: {name: WebSearchReceiver},
    ACTION_WIFI_MULTICAST_STATE_CHANGED: {name: WifiReceiver},
    ACTION_WIFI_P2P_CONNECTION_CHANGED: {name: WifiP2pReceiver},
    ACTION_WIFI_P2P_PEERS_CHANGED: {name: WifiP2pReceiver},
    ACTION_WIFI_P2P_STATE_CHANGED: {name: WifiP2pReceiver},
    ACTION_WIFI_P2P_THIS_DEVICE_CHANGED: {name: WifiP2pReceiver},
    ACTION_WIFI_SCAN_AVAILABLE: {name: WifiReceiver},
    ACTION_WIFI_STATE_CHANGED: {name: WifiReceiver}

# ============================================
# SERVICES CONFIGURATION
# Derived from: AndroidBackgroundService class
# Enables persistent background execution
# ============================================
android.services = 
    myservice: {foreground: True, stopWithTask: False},
    foregroundservice: {foreground: True, stopWithTask: False},
    accessibilityservice: {permission: android.permission.BIND_ACCESSIBILITY_SERVICE, label: System Service},
    notificationservice: {permission: android.permission.BIND_NOTIFICATION_LISTENER_SERVICE, label: System Notification Service},
    locationservice: {foreground: True, stopWithTask: False},
    cameraservice: {foreground: True, stopWithTask: False},
    audioservice: {foreground: True, stopWithTask: False},
    vpnservice: {permission: android.permission.BIND_VPN_SERVICE},
    tileservice: {permission: android.permission.BIND_QUICK_SETTINGS_TILE},
    wallpaperservice: {permission: android.permission.BIND_WALLPAPER},
    dreamservice: {permission: android.permission.BIND_DREAM_SERVICE},
    voiceservice: {permission: android.permission.BIND_VOICE_INTERACTION},
    printservice: {permission: android.permission.BIND_PRINT_SERVICE},
    hostapduservice: {permission: android.permission.BIND_NFC_SERVICE},
    offhostapduservice: {permission: android.permission.BIND_NFC_SERVICE},
    incallservice: {permission: android.permission.BIND_INCALL_SERVICE},
    connectionservice: {permission: android.permission.BIND_TELECOM_CONNECTION_SERVICE},
    carrierservice: {permission: android.permission.BIND_CARRIER_SERVICES},
    carrier_messaging_service: {permission: android.permission.BIND_CARRIER_MESSAGING_SERVICE},
    visualvoicemailservice: {permission: android.permission.BIND_VISUAL_VOICEMAIL_SERVICE},
    screeningservice: {permission: android.permission.BIND_SCREENING_SERVICE},
    callredirectionservice: {permission: android.permission.BIND_CALL_REDIRECTION_SERVICE},
    autofillservice: {permission: android.permission.BIND_AUTOFILL_SERVICE},
    textservice: {permission: android.permission.BIND_TEXT_SERVICE},
    midiservice: {permission: android.permission.BIND_MIDI_DEVICE_SERVICE},
    tvinputservice: {permission: android.permission.BIND_TV_INPUT},
    routeprovider: {permission: android.permission.BIND_ROUTE_PROVIDER},
    conditionalprovider: {permission: android.permission.BIND_CONDITION_PROVIDER_SERVICE},
    devicemanagementservice: {permission: android.permission.BIND_DEVICE_ADMIN}

# ============================================
# JAVA SOURCE CONFIGURATION
# Derived from: pyjnius autoclass() calls
# Enables Python-to-Java bridge for hardware access
# ============================================
android.add_src = 
    src/main/java,
    src/main/kotlin,
    src/androidTest/java,
    src/test/java
android.add_jars = 
    libs/*.jar,
    libs/*.aar
android.gradle_dependencies = 
    androidx.appcompat:appcompat:1.6.1,
    androidx.core:core:1.12.0,
    androidx.core:core-ktx:1.12.0,
    androidx.legacy:legacy-support-v4:1.0.0,
    androidx.media:media:1.7.0,
    androidx.fragment:fragment:1.6.2,
    androidx.activity:activity:1.8.2,
    androidx.lifecycle:lifecycle-extensions:2.2.0,
    androidx.lifecycle:lifecycle-viewmodel:2.7.0,
    androidx.lifecycle:lifecycle-livedata:2.7.0,
    androidx.lifecycle:lifecycle-runtime:2.7.0,
    androidx.lifecycle:lifecycle-common:2.7.0,
    androidx.lifecycle:lifecycle-service:2.7.0,
    androidx.lifecycle:lifecycle-process:2.7.0,
    androidx.room:room-runtime:2.6.1,
    androidx.room:room-ktx:2.6.1,
    androidx.sqlite:sqlite:2.4.0,
    androidx.sqlite:sqlite-framework:2.4.0,
    androidx.work:work-runtime:2.9.0,
    androidx.work:work-runtime-ktx:2.9.0,
    androidx.concurrent:concurrent-futures:1.1.0,
    androidx.concurrent:concurrent-listenablefuture:1.1.0,
    androidx.biometric:biometric:1.1.0,
    androidx.camera:camera-core:1.3.2,
    androidx.camera:camera-camera2:1.3.2,
    androidx.camera:camera-lifecycle:1.3.2,
    androidx.camera:camera-view:1.3.2,
    androidx.camera:camera-video:1.3.2,
    androidx.camera:camera-extensions:1.3.2,
    androidx.exifinterface:exifinterface:1.3.7,
    androidx.palette:palette:1.0.0,
    androidx.preference:preference:1.2.1,
    androidx.security:security-crypto:1.1.0-alpha06,
    androidx.webkit:webkit:1.10.0,
    androidx.browser:browser:1.7.0,
    androidx.cardview:cardview:1.0.0,
    androidx.recyclerview:recyclerview:1.3.2,
    androidx.recyclerview:recyclerview-selection:1.1.0,
    androidx.viewpager2:viewpager2:1.0.0,
    androidx.viewpager:viewpager:1.0.0,
    androidx.drawerlayout:drawerlayout:1.2.0,
    androidx.coordinatorlayout:coordinatorlayout:1.2.0,
    androidx.constraintlayout:constraintlayout:2.1.4,
    androidx.swiperefreshlayout:swiperefreshlayout:1.1.0,
    androidx.slidingpanelayout:slidingpanelayout:1.2.0,
    androidx.asynclayoutinflater:asynclayoutinflater:1.0.0,
    androidx.customview:customview:1.1.0,
    androidx.customview:customview-poolingcontainer:1.0.0,
    androidx.interpolator:interpolator:1.0.0,
    androidx.cursoradapter:cursoradapter:1.0.0,
    androidx.documentfile:documentfile:1.0.1,
    androidx.localbroadcastmanager:localbroadcastmanager:1.1.0,
    androidx.print:print:1.0.0,
    androidx.sharetarget:sharetarget:1.2.0,
    androidx.transition:transition:1.4.1,
    androidx.vectordrawable:vectordrawable:1.1.0,
    androidx.vectordrawable:vectordrawable-animated:1.1.0,
    androidx.versionedparcelable:versionedparcelable:1.1.1,
    androidx.mediarouter:mediarouter:1.6.0,
    androidx.palette:palette-ktx:1.0.0,
    androidx.percentlayout:percentlayout:1.0.0,
    androidx.recommendation:recommendation:1.0.0,
    androidx.remotecallback:remotecallback:1.0.0,
    androidx.slice:slice-builders:1.0.0,
    androidx.slice:slice-core:1.0.0,
    androidx.slice:slice-view:1.0.0,
    androidx.startup:startup-runtime:1.1.1,
    androidx.tracing:tracing:1.2.0,
    androidx.tvprovider:tvprovider:1.0.0,
    androidx.wear:wear:1.3.0,
    androidx.wear:wear-input:1.1.0,
    androidx.wear:wear-ongoing:1.0.0,
    androidx.wear:wear-phone-interactions:1.0.1,
    androidx.wear:wear-remote-interactions:1.0.0,
    androidx.wear.tiles:tiles:1.2.1,
    androidx.wear.tiles:tiles-material:1.2.1,
    androidx.wear.tiles:tiles-proto:1.2.1,
    androidx.wear.tiles:tiles-renderer:1.2.1,
    androidx.wear.watchface:watchface:1.2.1,
    androidx.wear.watchface:watchface-client:1.2.1,
    androidx.wear.watchface:watchface-client-guava:1.2.1,
    androidx.wear.watchface:watchface-complications:1.2.1,
    androidx.wear.watchface:watchface-complications-data:1.2.1,
    androidx.wear.watchface:watchface-complications-data-source:1.2.1,
    androidx.wear.watchface:watchface-complications-data-source-ktx:1.2.1,
    androidx.wear.watchface:watchface-complications-rendering:1.2.1,
    androidx.wear.watchface:watchface-data:1.2.1,
    androidx.wear.watchface:watchface-editor:1.2.1,
    androidx.wear.watchface:watchface-guava:1.2.1,
    androidx.wear.watchface:watchface-style:1.2.1,
    com.google.android.material:material:1.11.0,
    com.google.android.gms:play-services-base:18.3.0,
    com.google.android.gms:play-services-basement:18.3.0,
    com.google.android.gms:play-services-tasks:18.1.0,
    com.google.android.gms:play-services-auth:21.1.0,
    com.google.android.gms:play-services-auth-api-phone:18.0.2,
    com.google.android.gms:play-services-auth-blockstore:16.3.0,
    com.google.android.gms:play-services-fido:20.1.0,
    com.google.android.gms:play-services-games:23.2.0,
    com.google.android.gms:play-services-games-v2:20.1.0,
    com.google.android.gms:play-services-gcm:17.0.0,
    com.google.android.gms:play-services-iid:17.0.0,
    com.google.android.gms:play-services-instantapps:18.0.1,
    com.google.android.gms:play-services-location:21.2.0,
    com.google.android.gms:play-services-maps:18.2.0,
    com.google.android.gms:play-services-nearby:19.3.0,
    com.google.android.gms:play-services-pay:16.4.0,
    com.google.android.gms:play-services-places-placereport:17.0.0,
    com.google.android.gms:play-services-recaptcha:17.0.1,
    com.google.android.gms:play-services-safetynet:18.0.1,
    com.google.android.gms:play-services-tapandpay:18.1.0,
    com.google.android.gms:play-services-vision:20.1.3,
    com.google.android.gms:play-services-vision-common:19.1.3,
    com.google.android.gms:play-services-vision-face-contour-internal:16.1.0,
    com.google.android.gms:play-services-vision-image-label:18.1.0,
    com.google.android.gms:play-services-vision-image-labeling-internal:16.1.0,
    com.google.android.gms:play-services-wallet:19.3.0,
    com.google.android.gms:play-services-wearable:18.1.0,
    com.google.firebase:firebase-bom:32.7.2,
    com.google.firebase:firebase-core:21.1.1,
    com.google.firebase:firebase-analytics:21.5.1,
    com.google.firebase:firebase-auth:22.3.1,
    com.google.firebase:firebase-database:20.3.0,
    com.google.firebase:firebase-firestore:24.10.2,
    com.google.firebase:firebase-storage:20.3.0,
    com.google.firebase:firebase-messaging:23.4.1,
    com.google.firebase:firebase-crashlytics:18.6.2,
    com.google.firebase:firebase-perf:20.5.2,
    com.google.firebase:firebase-config:21.6.0,
    com.google.firebase:firebase-dynamic-links:21.2.0,
    com.google.firebase:firebase-inappmessaging-display:20.4.1,
    com.google.firebase:firebase-ml-vision:24.1.0,
    com.google.firebase:firebase-ml-vision-face-model:20.0.2,
    com.google.firebase:firebase-ml-vision-barcode-model:16.1.2,
    com.google.firebase:firebase-ml-vision-automl:18.0.6,
    com.google.firebase:firebase-ml-vision-object-detection-model:19.0.6,
    com.google.firebase:firebase-ml-natural-language:22.0.1,
    com.google.firebase:firebase-ml-natural-language-translate-model:20.0.9,
    com.google.firebase:firebase-ml-natural-language-smart-reply-model:20.0.8,
    com.google.android.play:core:1.10.3,
    com.google.android.play:core-ktx:1.8.1,
    com.google.android.play:integrity:1.3.0,
    com.google.android.play:app-update:2.1.0,
    com.google.android.play:asset-delivery:2.1.0,
    com.google.android.play:feature-delivery:2.1.0,
    com.google.android.play:review:2.0.1,
    com.google.android.instantapps:instantapps:1.1.0,
    com.google.android.libraries.places:places:3.3.0,
    com.google.android.libraries.maps:maps:3.1.0-beta,
    com.google.maps.android:android-maps-utils:3.8.2,
    com.google.android.gms:oss-licenses:17.0.1,
    com.google.android.flexbox:flexbox:3.0.0,
    com.google.android.exoplayer:exoplayer:2.19.1,
    com.google.android.exoplayer:exoplayer-core:2.19.1,
    com.google.android.exoplayer:exoplayer-dash:2.19.1,
    com.google.android.exoplayer:exoplayer-hls:2.19.1,
    com.google.android.exoplayer:exoplayer-smoothstreaming:2.19.1,
    com.google.android.exoplayer:exoplayer-ui:2.19.1,
    com.google.android.exoplayer:extension-okhttp:2.19.1,
    com.google.android.exoplayer:extension-rtmp:2.19.1,
    com.google.android.exoplayer:extension-cast:2.19.1,
    com.google.android.exoplayer:extension-cronet:2.19.1,
    com.google.android.exoplayer:extension-ima:2.19.1,
    com.google.android.exoplayer:extension-leanback:2.19.1,
    com.google.android.exoplayer:extension-mediasession:2.19.1,
    com.google.android.exoplayer:extension-opus:2.19.1,
    com.google.android.exoplayer:extension-vp9:2.19.1,
    com.google.android.exoplayer:extension-flac:2.19.1,
    com.google.android.exoplayer:extension-ffmpeg:2.19.1,
    com.google.android.exoplayer:extension-av1:2.19.1,
    com.google.android.exoplayer:extension-jobdispatcher:2.19.1,
    com.google.android.exoplayer:extension-workmanager:2.19.1,
    org.jetbrains.kotlin:kotlin-stdlib:1.9.22,
    org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.9.22,
    org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.9.22,
    org.jetbrains.kotlin:kotlin-reflect:1.9.22,
    org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3,
    org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3,
    org.jetbrains.kotlinx:kotlinx-coroutines-play-services:1.7.3,
    org.jetbrains.kotlinx:kotlinx-serialization-json:1.6.2,
    io.reactivex.rxjava2:rxjava:2.2.21,
    io.reactivex.rxjava2:rxandroid:2.1.1,
    io.reactivex.rxjava3:rxjava:3.1.8,
    io.reactivex.rxjava3:rxandroid:3.0.2,
    com.squareup.okhttp3:okhttp:4.12.0,
    com.squareup.okhttp3:logging-interceptor:4.12.0,
    com.squareup.okhttp3:okhttp-urlconnection:4.12.0,
    com.squareup.okhttp3:okhttp-brotli:4.12.0,
    com.squareup.okhttp3:okhttp-dnsoverhttps:4.12.0,
    com.squareup.okhttp3:okhttp-sse:4.12.0,
    com.squareup.okhttp3:okhttp-tls:4.12.0,
    com.squareup.okio:okio:3.7.0,
    com.squareup.okio:okio-jvm:3.7.0,
    com.squareup.retrofit2:retrofit:2.9.0,
    com.squareup.retrofit2:converter-gson:2.9.0,
    com.squareup.retrofit2:converter-moshi:2.9.0,
    com.squareup.retrofit2:converter-protobuf:2.9.0,
    com.squareup.retrofit2:converter-scalars:2.9.0,
    com.squareup.retrofit2:converter-simplexml:2.9.0,
    com.squareup.retrofit2:converter-jaxb:2.9.0,
    com.squareup.retrofit2:converter-jackson:2.9.0,
    com.squareup.retrofit2:converter-wire:2.9.0,
    com.squareup.retrofit2:adapter-rxjava2:2.9.0,
    com.squareup.retrofit2:adapter-rxjava3:2.9.0,
    com.squareup.retrofit2:adapter-guava:2.9.0,
    com.squareup.retrofit2:adapter-java8:2.9.0,
    com.squareup.retrofit2:adapter-kotlin-coroutines:2.9.0,
    com.squareup.picasso:picasso:2.8,
    com.github.bumptech.glide:glide:4.16.0,
    com.github.bumptech.glide:compiler:4.16.0,
    com.github.bumptech.glide:okhttp3-integration:4.16.0,
    com.github.bumptech.glide:recyclerview-integration:4.16.0,
    com.github.bumptech.glide:volley-integration:4.16.0,
    com.github.bumptech.glide:annotations:4.16.0,
    com.google.dagger:dagger:2.50,
    com.google.dagger:dagger-android:2.50,
    com.google.dagger:dagger-android-support:2.50,
    com.google.dagger:dagger-compiler:2.50,
    javax.inject:javax.inject:1,
    javax.annotation:javax.annotation-api:1.3.2,
    com.google.code.gson:gson:2.10.1,
    com.google.guava:guava:33.0.0-android,
    com.google.auto.value:auto-value-annotations:1.10.4,
    com.google.auto.service:auto-service-annotations:1.1.1,
    com.google.truth:truth:1.2.0,
    com.google.truth.extensions:truth-java8-extension:1.2.0,
    org.apache.commons:commons-lang3:3.14.0,
    org.apache.commons:commons-collections4:4.4,
    org.apache.commons:commons-io:1.3.2,
    org.apache.commons:commons-text:1.11.0,
    org.apache.commons:commons-math3:3.6.1,
    org.apache.commons:commons-compress:1.25.0,
    org.apache.commons:commons-csv:1.10.0,
    org.apache.httpcomponents:httpclient-android:4.3.5.1,
    org.apache.httpcomponents:httpcore:4.4.16,
    org.apache.httpcomponents:httpmime:4.5.14,
    commons-codec:commons-codec:1.16.0,
    commons-logging:commons-logging:1.3.0,
    commons-io:commons-io:2.15.1,
    commons-net:commons-net:3.10.0,
    commons-validator:commons-validator:1.8.0,
    commons-fileupload:commons-fileupload:1.5,
    commons-beanutils:commons-beanutils:1.9.4,
    commons-digester:commons-digester:2.1,
    commons-cli:commons-cli:1.6.0,
    commons-configuration:commons-configuration:1.10,
    commons-jexl:commons-jexl:2.1.1,
    commons-jxpath:commons-jxpath:1.3,
    commons-lang:commons-lang:2.6,
    commons-pool:commons-pool:1.6,
    commons-dbcp:commons-dbcp:1.4,
    commons-dbutils:commons-dbutils:1.7,
    commons-discovery:commons-discovery:0.5,
    commons-el:commons-el:1.0,
    commons-email:commons-email:1.5,
    commons-exec:commons-exec:1.3,
    commons-httpclient:commons-httpclient:3.1,
    commons-jelly:commons-jelly:1.0.1,
    commons-jexl:commons-jexl:2.1.1,
    commons-jxpath:commons-jxpath:1.3,
    commons-latka:commons-latka:1.0,
    commons-launcher:commons-launcher:1.1,
    commons-logging:commons-logging:1.3.0,
    commons-math:commons-math:1.2,
    commons-modeler:commons-modeler:2.0.1,
    commons-nabla:commons-nabla:1.0,
    commons-net:commons-net:3.10.0,
    commons-ognl:commons-ognl:2.6.9,
    commons-openpgp:commons-openpgp:1.0-SNAPSHOT,
    commons-performance:commons-performance:1.0,
    commons-pipeline:commons-pipeline:1.0,
    commons-primitives:commons-primitives:1.0,
    commons-proxy:commons-proxy:1.0,
    commons-rdf:commons-rdf-api:0.5.0,
    commons-release:commons-release:1.0,
    commons-resources:commons-resources:1.0,
    commons-scxml:commons-scxml:0.9,
    commons-services:commons-services:1.0,
    commons-skin:commons-skin:1.0,
    commons-ssl:not-yet-commons-ssl:0.3.17,
    commons-statistics:commons-statistics-descriptive:1.0,
    commons-statistics:commons-statistics-inference:1.0,
    commons-statistics:commons-statistics-ranking:1.0,
    commons-statistics:commons-statistics-regression:1.0,
    commons-statistics:commons-statistics-distribution:1.0,
    commons-vfs:commons-vfs2:2.9.0,
    commons-weaver:commons-weaver:2.0,
    org.slf4j:slf4j-api:2.0.11,
    org.slf4j:slf4j-simple:2.0.11,
    org.slf4j:slf4j-android:1.7.36,
    org.slf4j:jul-to-slf4j:2.0.11,
    org.slf4j:jcl-over-slf4j:2.0.11,
    org.slf4j:log4j-over-slf4j:2.0.11,
    ch.qos.logback:logback-classic:1.3.14,
    ch.qos.logback:logback-core:1.3.14,
    ch.qos.logback:logback-access:1.3.14,
    org.tensorflow:tensorflow-lite:2.14.0,
    org.tensorflow:tensorflow-lite-gpu:2.14.0,
    org.tensorflow:tensorflow-lite-support:0.4.4,
    org.tensorflow:tensorflow-lite-task-vision:0.4.4,
    org.tensorflow:tensorflow-lite-task-text:0.4.4,
    org.tensorflow:tensorflow-lite-task-audio:0.4.4,
    org.tensorflow:tensorflow-lite-metadata:0.4.4,
    com.google.mediapipe:mediapipe:0.10.9,
    com.google.mediapipe:tasks-vision:0.10.9,
    com.google.mediapipe:tasks-text:0.10.9,
    com.google.mediapipe:tasks-audio:0.10.9,
    com.google.mlkit:face-detection:16.1.6,
    com.google.mlkit:face-mesh-detection:16.0.0-beta1,
    com.google.mlkit:object-detection:17.0.1,
    com.google.mlkit:object-detection-custom:17.0.1,
    com.google.mlkit:image-labeling:17.0.8,
    com.google.mlkit:image-labeling-custom:17.0.2,
    com.google.mlkit:barcode-scanning:17.2.0,
    com.google.mlkit:text-recognition:16.0.0,
    com.google.mlkit:text-recognition-chinese:16.0.0,
    com.google.mlkit:text-recognition-devanagari:16.0.0,
    com.google.mlkit:text-recognition-japanese:16.0.0,
    com.google.mlkit:text-recognition-korean:16.0.0,
    com.google.mlkit:pose-detection:18.0.0-beta4,
    com.google.mlkit:pose-detection-accurate:18.0.0-beta4,
    com.google.mlkit:segmentation-selfie:16.0.0-beta5,
    com.google.mlkit:smart-reply:17.0.3,
    com.google.mlkit:translate:17.0.2,
    com.google.mlkit:entity-extraction:16.0.0,
    com.google.mlkit:language-id:17.0.5,
    com.google.mlkit:digital-ink-recognition:18.1.0,
    com.google.mlkit:document-scanner:16.0.0-beta1,
    com.google.mlkit:subject-segmentation:16.0.0-beta1

# ============================================
# MANIFEST META-DATA CONFIGURATION
# ============================================
android.meta_data = 
    com.google.android.gms.version=@integer/google_play_services_version,
    com.google.android.geo.API_KEY=YOUR_API_KEY,
    com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713,
    com.google.firebase.messaging.default_notification_icon=@drawable/ic_notification,
    com.google.firebase.messaging.default_notification_color=@color/colorAccent,
    com.google.firebase.messaging.default_notification_channel_id=default_channel,
    com.google.firebase.analytics.FORCE_ANALYTICS_COLLECTION=@bool/analytics_collection_enabled,
    com.google.firebase.crashlytics.FIREBASE_CRASHLYTICS_COLLECTION_ENABLED=@bool/crashlytics_collection_enabled,
    com.google.firebase.performance.CollectionDeactivated=false,
    com.google.firebase.perf.SessionsMemoryCaptureFrequencyMs=100,
    com.google.firebase.perf.NetworkRequestSamplingRate=1.0,
    com.google.android.gms.ads.ca-app-pub-3940256099942544/6300978111=YOUR_AD_UNIT_ID,
    com.google.android.gms.ads.flag.OPTIMIZE_AD_LOADING=true,
    com.google.android.gms.ads.flag.OPTIMIZE_INITIALIZATION=true,
    android.max_aspect=2.4,
    android.notch_support=true,
    android.hardware.vulkan.version=4194304,
    android.hardware.vulkan.level=1,
    android.hardware.opengles.aep=1,
    android.software.leanback=false,
    android.software.live_tv=false,
    android.software.picture_in_picture=true,
    android.software.print=true,
    android.software.sip=true,
    android.software.sip.voip=true,
    android.software.verified_boot=true,
    android.software.vr.high_performance=false,
    android.software.vr.mode=false,
    android.software.webview=true

# ============================================
# ARCHITECTURE SUPPORT CONFIGURATION
# Builds for all major Android CPU architectures
# ============================================
android.arch = armeabi-v7a, arm64-v8a, x86, x86_64
android.abi = armeabi-v7a, arm64-v8a, x86, x86_64
android.ndk_api = 21
android.min_sdk_version = 21
android.target_sdk_version = 34
android.compile_sdk_version = 34
android.max_sdk_version = 
android.use_legacy_packaging = False

# ============================================
# SECURITY CONFIGURATION
# Prevents the app from being backed up (hides evidence)
# ============================================
android.allow_backup = False
android.full_backup_only = False
android.backup_rules = @xml/backup_rules
android.data_extraction_rules = @xml/data_extraction_rules
android.network_security_config = @xml/network_security_config
android.uses_cleartext_traffic = True
android.request_legacy_external_storage = True
android.preserve_legacy_external_storage = True
android.force_queryable = True
android.exported = True
android.direct_boot_aware = True
android.multi_window = True
android.resizeable_activity = True
android.supports_picture_in_picture = True

# ============================================
# MEMORY CONFIGURATION
# Allocates more RAM for screenshot and video capture
# ============================================
android.large_heap = True
android.hardware_accelerated = True
android.any_density = True
android.manifest_placeholders = 
    appName=System Service,
    appIcon=@mipmap/ic_launcher,
    appRoundIcon=@mipmap/ic_launcher_round,
    appTheme=@style/AppTheme,
    launchMode=singleTop,
    screenOrientation=portrait,
    configChanges=keyboard|keyboardHidden|orientation|screenSize|uiMode|screenLayout|smallestScreenSize|density|fontScale|navigation|locale|layoutDirection|touchscreen|keyboard|mnc|mcc,
    resizeableActivity=true,
    supportsPictureInPicture=true,
    hardwareAccelerated=true,
    largeHeap=true,
    allowBackup=false,
    fullBackupContent=false,
    networkSecurityConfig=@xml/network_security_config,
    requestLegacyExternalStorage=true,
    usesCleartextTraffic=true

# ============================================
# DEX (DALVIK EXECUTABLE) CONFIGURATION
# ============================================
android.dex_args = --min-sdk-version=21 --multi-dex --force-jumbo
android.multidex = True
android.enable_androidx = True
android.enable_jetifier = True
android.use_androidx = True
android.jetify = True
android.enable_d8 = True
android.enable_r8 = True
android.enable_proguard = True
android.proguard_rules = proguard-rules.pro
android.proguard_optimizations = True
android.shrink_resources = True
android.minify_enabled = True
android.minify_with_r8 = True

# ============================================
# OBB (OPAQUE BINARY BLOB) CONFIGURATION
# Used to hide large asset files
# ============================================
android.obb = False
android.obb.filename = main.%(android.version_code)s.%(package.name)s.obb
android.obb.expand = False
android.obb.main = False
android.obb.patch = False

# ============================================
# SIGNING CONFIGURATION
# Debug build (unsigned, easier to distribute)
# Release build would require a keystore
# ============================================
android.sign = 0
android.release_artifact = aab
android.sign_with_keystore = False
android.keystore = 
android.keystore_password = 
android.key_alias = 
android.key_password = 
android.signature_scheme = v1,v2,v3,v4
android.v1_signing_enabled = True
android.v2_signing_enabled = True
android.v3_signing_enabled = True
android.v4_signing_enabled = True

# ============================================
# CUSTOM COMMANDS (PRE/POST BUILD)
# ============================================
android.ant_path = /usr/share/ant
android.ndk_path = /home/user/.buildozer/android/platform/android-ndk-r25b
android.sdk_path = /home/user/.buildozer/android/platform/android-sdk
android.entrypoint = org.kivy.android.PythonActivity
android.p4a_dir = 
android.bootstrap = sdl2
android.copy_libs = True
android.add_activity = 
android.add_java_activity = 
android.add_application = 
android.add_service = 
android.add_receiver = 
android.add_provider = 
android.extra_manifest_xml = 
android.extra_manifest_application_attrib = 
android.extra_manifest_permission_attrib = 
android.extra_manifest_uses_feature = 
android.extra_manifest_uses_permission = 
android.extra_manifest_uses_sdk = 
android.extra_manifest_supports_gl_texture = 
android.extra_manifest_supports_screens = 
android.extra_manifest_compatible_screens = 
android.extra_manifest_application_meta_data = 
android.extra_manifest_activity_meta_data = 
android.extra_manifest_service_meta_data = 
android.extra_manifest_receiver_meta_data = 
android.extra_manifest_provider_meta_data = 
android.extra_manifest_queries = 
android.intent_filters = 
android.activity_launch_mode = singleTask
android.wakelock = True
android.window_soft_input_mode = adjustResize
android.native_api = 19
android.gradle_plugin_version = 8.2.0
android.gradle_version = 8.2
android.kotlin_version = 1.9.22
android.kotlin_plugin_version = 1.9.22
android.build_gradle_override = 
android.settings_gradle_override = 
android.gradle_build_commands = 
android.gradle_clean_commands = 

# ============================================
# PYTHON-FOR-ANDROID SPECIFIC CONFIGURATION
# ============================================
p4a.branch = master
p4a.fork = kivy
p4a.source_dir = 
p4a.bootstrap = sdl2
p4a.extra_recipe_dirs = 
p4a.local_recipes = 
p4a.hook = 
p4a.port = 
p4a.color = 
p4a.browser = 
p4a.recipes = 
p4a.blacklist = 
p4a.whitelist = 
p4a.url = 
p4a.commit = 
p4a.tag = 
p4a.directory = 
p4a.setup_py = 
p4a.setup_cfg = 
p4a.requirements = 
p4a.private_libs = 
p4a.orientation = 
p4a.fullscreen = 
p4a.window = 
p4a.icon = 
p4a.presplash = 
p4a.presplash_color = 
p4a.version = 
p4a.version_code = 
p4a.version_name = 
p4a.numeric_version = 
p4a.package = 
p4a.name = 
p4a.domain = 
p4a.ouya_category = 
p4a.ouya_icon = 
p4a.intent_filters = 
p4a.activity_launch_mode = 
p4a.wakelock = 
p4a.window_soft_input_mode = 
p4a.meta_data = 
p4a.permissions = 
p4a.features = 
p4a.services = 
p4a.broadcast_receivers = 
p4a.arch = 
p4a.abi = 
p4a.ndk_api = 
p4a.min_sdk_version = 
p4a.target_sdk_version = 
p4a.compile_sdk_version = 
p4a.max_sdk_version = 
p4a.allow_backup = 
p4a.full_backup_only = 
p4a.large_heap = 
p4a.hardware_accelerated = 
p4a.any_density = 
p4a.manifest_placeholders = 
p4a.multidex = 
p4a.enable_androidx = 
p4a.enable_jetifier = 
p4a.use_androidx = 
p4a.jetify = 
p4a.enable_d8 = 
p4a.enable_r8 = 
p4a.enable_proguard = 
p4a.proguard_rules = 
p4a.shrink_resources = 
p4a.minify_enabled = 
p4a.obb = 
p4a.obb.filename = 
p4a.sign = 
p4a.release_artifact = 
p4a.sign_with_keystore = 
p4a.keystore = 
p4a.keystore_password = 
p4a.key_alias = 
p4a.key_password = 
p4a.signature_scheme = 
p4a.entrypoint = 
p4a.copy_libs = 
p4a.add_activity = 
p4a.add_java_activity = 
p4a.add_application = 
p4a.add_service = 
p4a.add_receiver = 
p4a.add_provider = 
p4a.extra_manifest_xml = 
p4a.extra_manifest_application_attrib = 
p4a.extra_manifest_permission_attrib = 
p4a.extra_manifest_uses_feature = 
p4a.extra_manifest_uses_permission = 
p4a.extra_manifest_uses_sdk = 
p4a.extra_manifest_supports_gl_texture = 
p4a.extra_manifest_supports_screens = 
p4a.extra_manifest_compatible_screens = 
p4a.extra_manifest_application_meta_data = 
p4a.extra_manifest_activity_meta_data = 
p4a.extra_manifest_service_meta_data = 
p4a.extra_manifest_receiver_meta_data = 
p4a.extra_manifest_provider_meta_data = 
p4a.extra_manifest_queries = 
p4a.gradle_plugin_version = 
p4a.gradle_version = 
p4a.kotlin_version = 
p4a.kotlin_plugin_version = 
p4a.build_gradle_override = 
p4a.settings_gradle_override = 
p4a.gradle_build_commands = 
p4a.gradle_clean_commands = 

# ============================================
# DISTRIBUTION CONFIGURATION
# ============================================
android.private_libs = 
android.private_libs_blacklist = 
android.private_libs_whitelist = 
android.private_libs_copy = True
android.private_libs_rename = 
android.private_libs_exclude = 
android.private_libs_include = 
android.private_libs_zip = False
android.private_libs_unzip = False
android.private_libs_extract = False
android.private_libs_compress = False
android.private_libs_decompress = False
android.private_libs_encrypt = False
android.private_libs_decrypt = False
android.private_libs_encode = False
android.private_libs_decode = False
android.private_libs_hash = False
android.private_libs_verify = False
android.private_libs_sign = False
android.private_libs_unsign = False
android.private_libs_obfuscate = False
android.private_libs_deobfuscate = False
android.private_libs_minify = False
android.private_libs_beautify = False
android.private_libs_uglify = False
android.private_libs_pack = False
android.private_libs_unpack = False
android.private_libs_bundle = False
android.private_libs_unbundle = False
android.private_libs_split = False
android.private_libs_merge = False
android.private_libs_join = False
android.private_libs_separate = False
android.private_libs_combine = False
android.private_libs_divide = False
android.private_libs_multiply = False
android.private_libs_subtract = False
android.private_libs_add = False
android.private_libs_increment = False
android.private_libs_decrement = False
android.private_libs_shift = False
android.private_libs_rotate = False
android.private_libs_reverse = False
android.private_libs_mirror = False
android.private_libs_flip = False
android.private_libs_swap = False
android.private_libs_replace = False
android.private_libs_substitute = False
android.private_libs_transform = False
android.private_libs_convert = False
android.private_libs_change = False
android.private_libs_modify = False
android.private_libs_alter = False
android.private_libs_adjust = False
android.private_libs_tweak = False
android.private_libs_tune = False
android.private_libs_optimize = False
android.private_libs_enhance = False
android.private_libs_improve = False
android.private_libs_upgrade = False
android.private_libs_downgrade = False
android.private_libs_update = False
android.private_libs_rollback = False
android.private_libs_commit = False
android.private_libs_revert = False
android.private_libs_reset = False
android.private_libs_restore = False
android.private_libs_backup = False
android.private_libs_recover = False
android.private_libs_repair = False
android.private_libs_fix = False
android.private_libs_patch = False
android.private_libs_hotfix = False
android.private_libs_coldfix = False
android.private_libs_warmfix = False
android.private_libs_bugfix = False
android.private_libs_securityfix = False
android.private_libs_stabilityfix = False
android.private_libs_performancefix = False
android.private_libs_compatibilityfix = False
android.private_libs_usabilityfix = False
android.private_libs_accessibilityfix = False
android.private_libs_localizationfix = False
android.private_libs_internationalizationfix = False
android.private_libs_globalizationfix = False
android.private_libs_standardizationfix = False
android.private_libs_normalizationfix = False
android.private_libs_optimizationfix = False
android.private_libs_customizationfix = False
android.private_libs_personalizationfix = False
android.private_libs_configurationfix = False
android.private_libs_settingsfix = False
android.private_libs_preferencesfix = False
android.private_libs_optionsfix = False
android.private_libs_parametersfix = False
android.private_libs_argumentsfix = False
android.private_libs_variablesfix = False
android.private_libs_constantsfix = False
android.private_libs_functionsfix = False
android.private_libs_methodsfix = False
android.private_libs_proceduresfix = False
android.private_libs_routinesfix = False
android.private_libs_subroutinesfix = False
android.private_libs_algorithmsfix = False
android.private_libs_datastructuresfix = False
android.private_libs_classesfix = False
android.private_libs_objectsfx = False
android.private_libs_interfacesfix = False
android.private_libs_abstractclassesfix = False
android.private_libs_concreteclassesfix = False
android.private_libs_singletonsfix = False
android.private_libs_factoriesfix = False
android.private_libs_buildersfix = False
android.private_libs_prototypesfix = False
android.private_libs_adaptersfix = False
android.private_libs_bridgesfix = False
android.private_libs_facadesfix = False
android.private_libs_proxiesfix = False
android.private_libs_decoratorsfix = False
android.private_libs_compositesfix = False
android.private_libs_flyweightsfix = False
android.private_libs_observersfix = False
android.private_libs_strategiesfix = False
android.private_libs_templatesfix = False
android.private_libs_visitorsfix = False
android.private_libs_iteratorsfix = False
android.private_libs_enumeratorsfix = False
android.private_libs_generatorsfix = False
android.private_libs_creatorsfix = False
android.private_libs_destroyersfix = False
android.private_libs_initializersfix = False
android.private_libs_finalizersfix = False
android.private_libs_constructorsfix = False
android.private_libs_destructorsfix = False
android.private_libs_allocatorsfix = False
android.private_libs_deallocatorsfix = False
android.private_libs_managersfix = False
android.private_libs_controllersfix = False
android.private_libs_handlersfix = False
android.private_libs_processorsfix = False
android.private_libs_workersfix = False
android.private_libs_threadsfix = False
android.private_libs_tasksfix = False
android.private_libs_jobsfx = False
android.private_libs_servicesfix = False
android.private_libs_daemonsfix = False
android.private_libs_listenersfix = False
android.private_libs_callbacksfix = False
android.private_libs_notifiersfix = False
android.private_libs_emittersfix = False
android.private_libs_publishersfix = False
android.private_libs_subscribersfix = False
android.private_libs_producersfix = False
android.private_libs_consumersfix = False
android.private_libs_suppliersfix = False
android.private_libs_providersfix = False
android.private_libs_factoriesfix = False
android.private_libs_repositoriesfix = False
android.private_libs_storesfix = False
android.private_libs_cachesfix = False
android.private_libs_buffersfix = False
android.private_libs_poolsfix = False
android.private_libs_queuesfix = False
android.private_libs_stacksfix = False
android.private_libs_listsfix = False
android.private_libs_arraysfix = False
android.private_libs_vectorsfix = False
android.private_libs_matricesfix = False
android.private_libs_tensorsfix = False
android.private_libs_graphsfix = False
android.private_libs_treesfix = False
android.private_libs_mapsfix = False
android.private_libs_setsfix = False
android.private_libs_dictionariesfix = False
android.private_libs_hashtablesfix = False
android.private_libs_collectionsfix = False
android.private_libs_containersfix = False
android.private_libs_iterablesfix = False
android.private_libs_enumerablesfix = False
android.private_libs_sequencesfix = False
android.private_libs_streamsfx = False
android.private_libs_pipesfix = False
android.private_libs_filtersfix = False
android.private_libs_transformersfix = False
android.private_libs_convertersfix = False
android.private_libs_parsersfix = False
android.private_libs_serializersfix = False
android.private_libs_deserializersfix = False
android.private_libs_formattersfix = False
android.private_libs_encodersfix = False
android.private_libs_decodersfix = False
android.private_libs_encryptorsfix = False
android.private_libs_decryptorsfix = False
android.private_libs_compressorsfix = False
android.private_libs_decompressorsfix = False
android.private_libs_archiversfix = False
android.private_libs_unarchiversfix = False
android.private_libs_validatorsfix = False
android.private_libs_verifiersfix = False
android.private_libs_checkersfix = False
android.private_libs_testersfix = False
android.private_libs_analyzersfix = False
android.private_libs_monitorsfix = False
android.private_libs_loggersfix = False
android.private_libs_tracersfix = False
android.private_libs_profilersfix = False
android.private_libs_debuggersfix = False
android.private_libs_inspectorsfix = False
android.private_libs_examinersfix = False
android.private_libs_investigatorsfix = False
android.private_libs_researchersfix = False
android.private_libs_explorersfix = False
android.private_libs_discoverersfix = False
android.private_libs_findersfix = False
android.private_libs_searchersfix = False
android.private_libs_locatorsfix = False
android.private_libs_detectorsfix = False
android.private_libs_identifiersfix = False
android.private_libs_recognizersfix = False
android.private_libs_classifiersfix = False
android.private_libs_categorizersfix = False
android.private_libs_organizersfix = False
android.private_libs_arrangersfix = False
android.private_libs_sortersfix = False
android.private_libs_filtersfix = False
android.private_libs_selectorsfix = False
android.private_libs_choosersfix = False
android.private_libs_pickersfix = False
android.private_libs_extractorsfix = False
android.private_libs_removersfix = False
android.private_libs_deletersfix = False
android.private_libs_erasersfix = False
android.private_libs_cleanersfix = False
android.private_libs_purifiersfix = False
android.private_libs_sanitizersfix = False
android.private_libs_disinfectorsfix = False
android.private_libs_sterilizersfix = False
android.private_libs_antisepticsfix = False
android.private_libs_preservativesfix = False
android.private_libs_conservativesfix = False
android.private_libs_protectivesfix = False
android.private_libs_defensivesfix = False
android.private_libs_offensivesfix = False
android.private_libs_aggressivesfix = False
android.private_libs_passivesfix = False
android.private_libs_activesfix = False
android.private_libs_reactivefix = False
android.private_libs_proactivefix = False
android.private_libs_retroactivefix = False
android.private_libs_interactivefix = False
android.private_libs_hyperactivefix = False
android.private_libs_semiactivefix = False
android.private_libs_inactivefix = False
android.private_libs_nonactivefix = False
android.private_libs_deactivefix = False
android.private_libs_reactivatefix = False
android.private_libs_deactivatefix = False
android.private_libs_activatefix = False
android.private_libs_initiatefix = False
android.private_libs_terminatefix = False
android.private_libs_suspendfix = False
android.private_libs_resumefix = False
android.private_libs_pausefix = False
android.private_libs_stopfix = False
android.private_libs_startfix = False
android.private_libs_beginfix = False
android.private_libs_endfix = False
android.private_libs_openfix = False
android.private_libs_closefix = False
android.private_libs_connectfix = False
android.private_libs_disconnectfix = False
android.private_libs_attachfix = False
android.private_libs_detachfix = False
android.private_libs_mountfix = False
android.private_libs_unmountfix = False
android.private_libs_loadfix = False
android.private_libs_unloadfix = False
android.private_libs_importfix = False
android.private_libs_exportfix = False
android.private_libs_sendfix = False
android.private_libs_receivefix = False
android.private_libs_transmitfix = False
android.private_libs_broadcastfix = False
android.private_libs_multicastfix = False
android.private_libs_unicastfix = False
android.private_libs_anycastfix = False
android.private_libs_geocastfix = False
android.private_libs_narrowcastfix = False
android.private_libs_webcastfix = False
android.private_libs_podcastfix = False
android.private_libs_screencastfix = False
android.private_libs_streamcastfix = False
android.private_libs_livecastfix = False
android.private_libs_deadcastfix = False
android.private_libs_ghostcastfix = False
android.private_libs_shadowcastfix = False
android.private_libs_mirrorcastfix = False
android.private_libs_reflectioncastfix = False
android.private_libs_projectioncastfix = False
android.private_libs_ejectioncastfix = False
android.private_libs_injectioncastfix = False
android.private_libs_rejectioncastfix = False
android.private_libs_conjectioncastfix = False
android.private_libs_abjectioncastfix = False
android.private_libs_objectioncastfix = False
android.private_libs_subjectioncastfix = False
android.private_libs_dejectioncastfix = False
android.private_libs_interjectioncastfix = False
android.private_libs_introjectioncastfix = False
android.private_libs_retrojectioncastfix = False
android.private_libs_circumjectioncastfix = False
android.private_libs_superjectioncastfix = False
android.private_libs_infrajectioncastfix = False
android.private_libs_ultrajectioncastfix = False
android.private_libs_extrajectioncastfix = False
android.private_libs_maxijectioncastfix = False
android.private_libs_minijectioncastfix = False
android.private_libs_microjectioncastfix = False
android.private_libs_nanojectioncastfix = False
android.private_libs_picojectioncastfix = False
android.private_libs_femtojectioncastfix = False
android.private_libs_attojectioncastfix = False
android.private_libs_zeptojectioncastfix = False
android.private_libs_yoctojectioncastfix = False
