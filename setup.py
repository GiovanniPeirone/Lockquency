from setuptools import setup, find_packages

setup(
    name="Lockquency",
    version="0.0.1",
    author="Giovanni Peirone",
    description="Computer Listening Library",
    packages=find_packages(),
    install_requires=[
        "librosa>=0.10.1",
        "mutagen>=1.47.0",
        "sounddevice>=0.4.7"
    ],
)




