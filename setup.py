try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
  name = 'fmpclient',
  packages = ['fmpclient'],
  version = '0.1',
  license='MIT',
  description = 'A FinancialModellingPrep API wrapper.',
  author = 'Iain Wong',
  author_email = 'iainwong@outlook.com',
  url = 'https://github.com/iainwo/fmpclient',
  download_url = 'https://github.com/iainwo/fmpclient/archive/v0.1.tar.gz',
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