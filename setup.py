from setuptools import setup

from sv_converter import __version__ as version

setup(
    name='sv-converter',
    version=version,
    description='Easily convert values of different units of measurement.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ihavenonickname/sv-converter',
    author='Gabriel Blank Stift Mousquer',
    author_email='gabrielblanksm@gmail.com',
    license='MIT',
    packages=['sv_converter'],
    include_package_data=True,
)
