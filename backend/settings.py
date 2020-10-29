"""
Django settings for backend_ch1_sec1 project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USE_PROXY = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u_knrmvv2e+tdm2=^k4@a#qs2h=ss-9ivmdwh0&wi4)qk)qzl@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 新应用
    'apis.apps.ApisConfig',
    'authorization.apps.AuthorizationConfig'

    # 第三方应用
    'django_crontab'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'backend',
        'USER': 'root',
        'PASSWORD': 'bc0ecc96a6d8f7e4',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')
IMAGES_DIR = os.path.join(RESOURCES_DIR, 'images')

# app secret 由开发者在微信官网开发者页面生成的
WX_APP_SECRET = 'c1d5c56f6c9443a6c7b4e5e759d04276'

# session超时时间
SESSION_COOKIE_AGE = 60 * 60 * 24 * 1

# logging日志配置
LOG_DIR = os.path.join(BASE_DIR, 'log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {  # 日志格式
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] '
                      '[%(pathname)s:%(funcName)s:%(lineno)d] [%(levelname)s]- %(message)s'}
    },
    'filters': {  # 过滤器
        'test': {
            '()': 'ops.TestFilter'
        }
    },
    'handlers': {  # 处理器
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'error_handler': {  # error内容输出到另外的文件
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'error.log'),  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'formatter': 'standard',  # 使用哪种formatters日志格式
            'encoding': 'utf8',
        },
        'file_handler': {  # 记录到日志文件(需要创建对应的目录，否则会出错)
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'service.log'),  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'formatter': 'standard',  # 使用哪种formatters日志格式
            'encoding': 'utf8',
        },
        'console_handler': {  # 输出到控制台
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {  # logging管理器
        'django': {
            # 'handlers': ['console_handler', 'file_handler', 'error_handler'],
            'handlers': ['console_handler', 'file_handler'],
            'filters': ['test'],
            'level': 'INFO'
        }
    }
}

CACHES = {
    'default': {
        # 1. MemCache
        # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        # 'LOCATION': '127.0.0.1:11211',

        # 2. DB Cache
        # 'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        # 'LOCATION': 'my_cache_table',

        # 3. Filesystem Cache
        # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'LOCATION': '/var/tmp/django_cache',

        # 4. Local Mem Cache
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'backend-cache'
    }
}

CRONJOBS = [
    ('*/1 * * * *', 'cron.jobs.demo')
]
