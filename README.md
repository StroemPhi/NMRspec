# A data model and code prototype for the semantification of NMR spectroscopy research data.
The present use case of this repository is the conversion of JCAMP-DX files, which contain research data of pulsed NMR assays, into RDF knowledge graphs. It is part of my work within the [NFDI4Chem](https://www.nfdi4chem.de/) project.

The backbone is the LinkML based [data model](model/schema/), which is used for the automatic generation of its JSON-LD, JSON schema and Python data class representations (see [NMRspec](NMRspec/), as well as for the [**Documentation**](https://StroemPhi.github.io/NMRspec/) of the NMRspec model itself.

## Alignment with IUPAC-FAIRspec & ISA-Tools
The work done here is intended to help with the standardization of spectroscopic data, currently driven by the [IUPAC-FAIRspec](https://github.com/IUPAC/IUPAC-FAIRSpec) and the [ISA-Tools](https://isa-tools.org/) project. Wheras the need to align with the more general IUPAC-FAIRspec data model is obvious, it still needs to be discussed wether this repository will serve only as a demonstrating prototype for the ongoing development of ISA-tools, or if it will be further developed into an independend python module. If the latter, it will be moved to https://github.com/NFDI4Chem.
