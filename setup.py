from setuptools import setup
import os
import glob

setup(name='sharkpy',
      version='0.1',
      description='Left shark app',
      url='',
      author='Cody VanDeMark',
      author_email='cavigm@rit.edu',
      license='GPLv3',
      packages=['sharkpy'],
      scripts=['bin/sharkpy'],
      data_files=[('sharkpy/assets', ['sharkpy/assets/leftshark.png'])],
      zip_safe=False)
