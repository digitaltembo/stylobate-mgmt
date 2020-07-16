from setuptools import setup

setup(
    name='stylobate-mgmt',
    version='0.0.1',
    description='Manage instances of Stylobate starter projects',
    url='http://github.com/digitaltembo/stylobate-mgmt',
    author='Nolan Hawkins',
    author_email='nolanhhawkins@gmail.com',
    license='MIT',
    packages=['stylobate_mgmt'],
    zip_safe=False,
    entry_points = {
        'console_scripts': 'stylo=stylobate_mgmt.stylo:main'
    }
)