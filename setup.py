from setuptools import setup


INSTALL_REQUIRES = ["Biopython", "numpy"]

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

with open("PeptideConstructor/__init__.py", "r") as f:
    init = f.readlines()

for line in init:
    if "__version__" in line:
        __version__ = line.split('"')[-2]

setup(
    name="PeptideConstructor",
    version=__version__,
    author="CharlesHahn",
    author_email="",
    description="Create (DL-) peptide PDB files with specified secondary structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CharlesHahn/PeptideConstructor",
    download_url="https://github.com/CharlesHahn/PeptideConstructor/releases",
    platforms="cross-platform",
    packages=["PeptideConstructor"],
    install_requires=INSTALL_REQUIRES,
    extras_require={
        "test": TEST_REQUIRES + INSTALL_REQUIRES,
    },
    entry_points={"console_scripts": ["PCcli = PeptideConstructor.PCcli:main"]},
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Intended Audience :: Science/Research",
    ],
)
