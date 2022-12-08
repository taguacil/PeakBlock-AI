"""
=============================================================================
Title    : Setup script
Project  : PeakBlock
File     : setup.py
-----------------------------------------------------------------------------

    Description:

    This file contains the setup


-----------------------------------------------------------------------------
Major Revisions:
    Date            Version     Name        Description
    28-Mar-2020     1.0         Taimir        First iteration of the script
"""

from package_settings import NAME, VERSION, PACKAGES, DESCRIPTION
from setuptools import setup
from pathlib import Path
import json
import urllib.request
from functools import lru_cache


@lru_cache(maxsize=50)
def _get_github_sha(github_install_url: str):
    """From the github_install_url get the hash of the latest commit"""
    repository = Path(github_install_url).stem.split('#egg', 1)[0]
    organisation = Path(github_install_url).parent.stem
    with urllib.request.urlopen(f'https://api.github.com/repos/{organisation}/{repository}/commits/master') as response:
        return json.loads(response.read())['sha']


setup(
    name=NAME,
    version=VERSION,
    long_description=DESCRIPTION,
    author='PeakBlock',
    author_email='taguacil@iis.ee.ethz.ch',
    packages=PACKAGES,
    include_package_data=True,
    install_requires=[
        'aiofiles ==  0.4.0',
        'certifi == 2022.12.7',
        'chardet == 3.0.4',
        'click == 7.1.1',
        'contextvars == 2.4',
        'h11 == 0.8.1',
        'h2 == 3.2.0',
        'hpack == 3.0.0',
        'hstspreload == 2020.3.25',
        'httptools == 0.1.1',
        'httpx == 0.9.3',
        'hyperframe == 5.2.0',
        'idna == 2.9',
        'immutables == 0.11',
        'itsdangerous == 1.1.0',
        'Jinja2 == 2.11.1',
        'joblib == 0.14.1',
        'MarkupSafe == 1.1.1',
        'multidict == 4.7.5',
        'numpy == 1.18.2',
        'pandas == 1.0.3',
        'python-dateutil == 2.8.1',
        'pytz == 2019.3',
        'rfc3986 == 1.3.2',
        'sanic == 19.12.2',
        'scikit-learn == 0.22.2.post1',
        'scipy == 1.4.1',
        'six == 1.14.0',
        'sklearn == 0.0',
        'sniffio == 1.1.0',
        'websockets == 8.1',
        'Werkzeug == 1.0.0',
    ],
    package_data={
        '': ['*.*'],
    },
)
