from setuptools import setup

from m10s import __version__ as version

setup(
    name='m10s',
    version=version,
    description='Easily convert values of different units of measurement.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ihavenonickname/m10s',
    author='Gabriel Blank Stift Mousquer',
    author_email='gabrielblanksm@gmail.com',
    license='MIT',
    packages=['m10s'],
    include_package_data=True,
)
