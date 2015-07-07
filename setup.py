from setuptools import setup, Extension

__auhtor__ = 'Takayuki Suzuki'
__version__ = '0.1'

requires = [
]

module = Extension('daikei_test',
                   sources=['devide-rule-learn.c',
                            'src/main.c',
                            'src/func_test.c',
                            'src/minimum.c'],
                   include_dirs=['src'])

setup(name='devide-rule-learn',
      version='0.1',
      description='c ext sample daikei_test',
      author=__auhtor__,
      author_email='sample@mail.com',
      url='http://sample/url.html',
      long_description='''
devide rule learn alg.
''',
      ext_modules=[module])

