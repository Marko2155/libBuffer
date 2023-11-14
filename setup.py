from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='libBuffer',
    long_description_content_type='text/markdown',
    long_description=long_description,
    keywords="buffer",
    version='1.0.3',
    packages=['tbgdl'],
    install_requires=[],
    url='https://github.com/Marko2155/libBuffer',
    license='MIT',
    author='Marko Camandioti',
    author_email='camandiotimarko@gmail.com',
    description="Library for Python to help with storing shit in memory (will reset after user has closed program)",
    project_urls={
        'Documentation': 'https://github.com/Marko2155/libBuffer#readme',
        'Source': 'https://github.com/Marko2155/libBuffer',
        'Tracker': 'https://github.com/Marko2155/libBuffer/issues',
    }
)
