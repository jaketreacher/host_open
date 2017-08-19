from setuptools import setup, Command
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='hostopen',
    version='0.1.1',

    description='Open files/directories in a vagrant synced folder on the host',
    long_description=long_description,

    url='https://github.com/jaketreacher/hostopen',

    author='Jake Treacher',
    author_email='git@jaketreacher.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities'
    ],

    python_requires='>=3',
    packages=['hostopen', ],
    entry_points={
        'console_scripts': [
            'hostopen = hostopen.client:main',
            'hostopen-server = hostopen.server:main'
        ],
    },
)
