from setuptools import setup


setup(
    name='monitoring_report',
    version='0.1',
    py_moduels=['cli'],
    install_requires=[
        "icmplib==3.0.3"
    ],
    entry_points={
        'console_scripts': [
            'monitoring_report = cli:main',
        ],
    },
    url='https://github.com/Yourun-proger/sites-monitoring/',
    license='MIT',
    author='Yourun-Proger',
    platform='any',
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

