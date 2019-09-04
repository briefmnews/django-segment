from setuptools import setup

import segment

setup(
    name='django-segment',
    version=segment.__version__,
    description='Segment integration in Django',
    long_description='Small app to easily integrate the Segment analytics library into Django.',
    keywords='django, analytics, segment, segmentio',
    author='Michael Pedersen <michael.pedersen@steelseries.com>',
    author_email='michael.pedersen@steelseries.com',
    url='https://github.com/briefmnews/django-segment',
    license='MIT',
    packages=['segment'],
    install_requires=[
        'analytics-python>=1.2.4',
    ],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Django :: 2.2'
    ],
)
