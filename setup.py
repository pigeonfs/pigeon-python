from setuptools import find_packages, setup

setup(
    name="pigeon",
    version="0.1.0",
    description="Python SDK for the Pigeon email API",
    url="https://github.com/pigeonfs/pigeon-python",
    license="MIT",
    packages=find_packages(exclude=["tests", "examples"]),
    python_requires=">=3.9",
)
