# Model requirements

**Model tested**
1) grc_odycy_joint_sm
2) grc_odycy_joint_trf

**Version**
grc_odycy_joint_sm       0.7.0
grc_odycy_joint_trf      0.7.0

`pip list` to show version of models 

In order to work, models of spacy needs python 3.10 (or, better, with python 3.10 they work, so...)


_**Installattion issues**_ 
Some of them models fais at installing because of OSError Space not enough. Install them  with: `pip install --no-cache-dir grc <name_model.whl>`

**problem 1**: _model rtf not found_, even if pip list shows it installed. Launch the script from terminal, not using the button on top-right