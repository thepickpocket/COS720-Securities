from setuptools import setup

setup(
    name='COS 720 - Securities Assignment',
    version='0.0.1',
    packages=['Securites_Main'],
    entry_points={
        'console_scripts': [
            'Securities_Main = Securities_Main.Main:Main.main'
        ]
    }
)