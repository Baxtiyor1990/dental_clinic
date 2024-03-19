from setuptools import setup, find_packages

setup(
    name='dental_clinic',
    version='1.0.0',
    packages={'': 'dental_clinic'},
    entry_points={
        'console_scripts': [
            'dental_clinic = dental_clinic.main:main'
        ]
    },
    install_requires=[
        'datetime'
        'requests',
        'numpy'
        'Flask>=2.1.0'
    ],
)
