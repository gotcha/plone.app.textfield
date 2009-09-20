from setuptools import setup, find_packages
import os

version = '1.0b1'

setup(name='plone.app.textfield',
      version=version,
      description="Text field with MIME type support",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone schema field',
      author='Martin Aspeli',
      author_email='optilude@gmail.com',
      url='http://pypi.python.org/pypi/plone.app.textfield',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.schema',
          'zope.interface',
          'zope.component',
          'ZODB3 >= 3.8.1',
          'rwproperty',
      ],
      tests_require=['collective.testcaselayer'],
      extras_require={
        'portraltransforms': ['Products.PortalTransforms'],
        'supermodel': ['plone.supermodel'],
        'widget': ['z3c.form'],
        'tests': ['collective.testcaselayer'],
      },
      entry_points="""
      """,
      )
