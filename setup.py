import cliff

from setuptools import setup, find_packages


setup(
    name='bolster-cliff',
    version=cliff.__version__,
    description='A database-based email templating system.',
    author='Bolster Labs, Inc',
    author_email='opensource@bolsterlabs.com',
    license='BSD',
    url='https://github.com/bolster/cliff',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics',
        'Framework :: Django',
    ],
    install_requires=[
        'Django',
        'djang-ace',
    ]
)
