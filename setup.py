from setuptools import setup, find_packages

setup(
    name='dental_clinic',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dental_clinic = dental_clinic.main:main'
        ]
    },
    install_requires=[
        'datetime'
        'requests',
        'numpy'
    ],
)
