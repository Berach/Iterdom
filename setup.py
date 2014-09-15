from setuptools import setup

setup(
    name="Iterdom",
    version="0.0.1",

    packages=["iterdom"],
    install_requires=["itertools",
                      "random"],

    author="Joseph Mulligan",
    author_email="joseph@jmulligan.me",
    description="A random library for generators",
    long_description="",
    license="MIT",
    keywords="random generators generator iterator itertools",
    url="https://github.com/Berach/Iterdom",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "license :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7"
    ]
)
