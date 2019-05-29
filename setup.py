from setuptools import setup

setup(
    name='quackmyip',
    version='0.2.2',
    description='Updates your IP address for your Duck DNS domain',
    url='https://github.com/tuxedoar/quackmyip',
    author='tuxedoar',
    author_email='tuxedoar@gmail.com',
    packages=['quackmyip'],
    install_requires=[
    'urllib3',
    'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        ],
)
