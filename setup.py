from setuptools import setup, find_packages 

setup(
    name='file_monitoring',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'watchdog',
    ],
    entry_points={
        'console_scripts': [
            'file_monitoring = file_monitoring.monitor:run_monitor',
        ],
    },
    author='Brett EMory',
    author_email='Brettemory2@gmail.com',
    description='A Python package for monitoring file changes and writing contents to a .txt file',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/file_monitoring',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
