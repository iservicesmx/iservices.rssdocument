from setuptools import setup, find_packages
import os

version = '0.5.0'

setup(name='iservices.rssdocument',
      version=version,
      description="A dynamic RSS content-type for plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Topic :: Text Processing :: Markup :: HTML",
        "Development Status :: 4 - Beta",
        "Framework :: Plone",
        ],
      keywords='Plone, RSS, jQuery',
      author='Noe Nieto',
      author_email='desarrollo@iservices.com.mx',
      url='http://svn.plone.org/svn/collective/iservices.rssdocument',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['iservices'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
