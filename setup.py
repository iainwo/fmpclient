import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the files
README = (HERE / "README.md").read_text()
LICENSE = (HERE / "LICENSE.txt").read_text()

setup(
  name = 'fmpclient',
  packages = ['fmpclient'],
  include_package_data=True,
  version = '0.1.1',
  license='MIT License',
  description = 'A FinancialModellingPrep API wrapper.',
  long_description_content_type="text/markdown",
  long_description=README,
  author = 'Iain Wong',
  author_email = 'iainwong@outlook.com',
  url = 'https://github.com/iainwo/fmpclient',
  download_url = 'https://github.com/iainwo/fmpclient/archive/v0.1.1.tar.gz',
  keywords = ['investing', 'finance', 'api', 'valuation', 'wrapper', 'client'],
  install_requires=[            
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)