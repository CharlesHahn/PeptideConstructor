from setuptools import setup


INSTALL_REQUIRES = ["Biopython"]

TEST_REQUIRES = [
    # testing and coverage
    "pytest",
    "coverage",
    "pytest-cov",
    # to be able to run `python setup.py checkdocs`
    "collective.checkdocs",
    "pygments",
]


with open("README.md", "r") as f:
    long_description = f.read()

with open("PeptideBuilder/__init__.py", "r") as f:
    init = f.readlines()

for line in init:
    if "__version__" in line:
        __version__ = line.split('"')[-2]

setup(
    name="PeptideBuilder",
    version=__version__,
    author="DuIvy, Charles Hahn",
    author_email="",
    description="Create (DL-)peptide PDB files with specified geometry",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CharlesHahn/DL-PeptideBuilder",
    download_url="https://github.com/CharlesHahn/DL-PeptideBuilder/releases",
    platforms="Tested on Windows 10 but not fully tested",
    packages=["PeptideBuilder"],
    install_requires=INSTALL_REQUIRES,
    extras_require={"test": TEST_REQUIRES + INSTALL_REQUIRES,},
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Intended Audience :: Science/Research",
    ],
)
