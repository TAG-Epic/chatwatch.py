from setuptools import setup, find_packages
from setuptools.command import install

from chatwatch import __version__
from chatwatch import Statistics


class InstallWithStats(install):
    def run(self):
        print("We store statistics about our library, by installing this library you agree.")
        stats = Statistics()
        stats.register_install()
        super().run()


setup(
    name="chatwatch",
    version=__version__,
    packages=find_packages(),
    url="https://github.com/TAG-Epic/chatwatch.py",
    license="GNU GPLv3",
    author="Epic",
    author_email="admin@itzepic.net",
    description="chatwatch library",
    cmdclass={
        "install": InstallWithStats
    }
)
