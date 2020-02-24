import setuptools

setuptools.setup(
    name='haggadah',
    version='0.0.1',
    packages=['haggadah'],
    install_requires=[
        'python-bidi>=0.4.2',
        'reportlab>=3.5.34',
    ],
    package_data={'haggadah': ['*.ttf']},
)
