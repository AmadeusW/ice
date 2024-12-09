from setuptools import setup, Extension

module = Extension('callback_module', 
                   sources=['callback_module.cpp'],
                   extra_compile_args=['-std=c++11'])

setup(name='CallbackModule',
      version='1.0',
      description='Python-C Callback Module',
      ext_modules=[module])
      