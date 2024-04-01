from setuptools import find_packages, setup

setup(
    name = 'Generative AI Project',
    version= '0.0.0',
    author= 'Varun',
    author_email= 'varun1924@gmail.com',
    packages= find_packages(), # It will lokk for the constructer (__init__.py) file, src foder is consider as my local package 
    install_requires = []

)