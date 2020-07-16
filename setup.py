from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='stylobate-mgmt',
    version='0.0.1',
    description='Manage instances of Stylobate-based projects',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/digitaltembo/stylobate-mgmt',
    author='Nolan Hawkins',
    author_email='nolanhhawkins@gmail.com',
    license='MIT',
    packages=['stylobate_mgmt'],
    zip_safe=False,
    entry_points = {
        'console_scripts': 'stylo=stylobate_mgmt.stylo:main'
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.1',
)