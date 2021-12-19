"""``PeptideConstructor`` package for creating (DL-)peptide models in PDB format based on geometrical parameters.
Written by Charles Hahn. This package is based on Lun4m/PeptideBuilder.git and clauswilke/PeptideBuilder.git. 
Python modules
----------------
The package consists of the following Python modules:
* PeptideBuilder
* Geometry
"""
__version__ = "0.1.0"
from .PeptideBuilder import *
from .Geometry import *
