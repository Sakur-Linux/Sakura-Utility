from setuptools import setup


setup(
        name='SakuraCMD-Core',
        version='1.0.0',
        install_requires=['speedtest_cli','hardware'],
        entry_points={
            "console_scripts": ['hw_info = hardware:main', 'speedtest = speedtest:speed','help_sk = help_sk:help']
        }
)