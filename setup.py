from setuptools import setup, find_packages

setup(
    name='fnkutils',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # Choose an appropriate license
    description='FNK Utils is a Django app that provides a set of utilities for Django projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/fakanakavera/fnkutils',  # Update with your GitHub URL
    author='FakaNaKavera',
    author_email='fakanakavera666@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)