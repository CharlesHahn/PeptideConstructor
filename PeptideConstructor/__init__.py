"""``PeptideConstructor`` package for creating (DL-)peptide models in PDB format based on geometrical parameters.
Written by Charles Hahn. This package is based on Lun4m/PeptideBuilder.git and clauswilke/PeptideBuilder.git. 
Python modules
----------------
The package consists of the following Python modules:
* PeptideBuilder
* Geometry
* PCcli
"""

__version__ = "0.2.1"
from .PeptideBuilder import *
from .Geometry import *
