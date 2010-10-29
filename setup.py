from setuptools import setup, find_packages
import os

version = '0.1'

install_requires = [
    'setuptools',
    'zope.annotation',
    'zope.security',
    'zope.securitypolicy',
    'grokcore.component',
    ]

tests_require = [
    'zope.interface',
    'zope.app.testing',
    'zope.principalregistry',
    'zope.testing',
    ]

setup(name='dolmen.security.policies',
      version=version,
      description="A collection of security maps baseclasses",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license = 'GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages = ['dolmen', 'dolmen.security'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      tests_require = tests_require,
      install_requires = install_requires,
      extras_require = {'test': tests_require},
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
