from setuptools import setup, find_packages

from chatwatch import __version__

setup(
    name="chatwatch",
    version=__version__,
    packages=find_packages(),
    url="https://github.com/TAG-Epic/chatwatch.py",
    license="GNU GPLv3",
    author="Epic",
    author_email="admin@itzepic.net",
    description="ChatWatch library",
)
