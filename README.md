# Responsible research practices could be more strongly endorsed by Australian university codes of research conduct

Yi Kai Ong,<sup>1</sup> 
Kay L Double,<sup>2,3</sup>
Lisa Bero,<sup>4</sup>
Joanna Diong<sup>2,5</sup>

1. School of Health Sciences, Faculty of Medicine and Health, The University of Sydney, New South Wales, Australia
2. School of Medical Sciences, Faculty of Medicine and Health, The University of Sydney, New South Wales, Australia
3. Brain and Mind Centre, The University of Sydney, New South Wales, Australia
4. Center for Bioethics and Humanities, University of Colorado, Colorado, USA
5. Charles Perkins Centre, The University of Sydney, New South Wales, Australia

## Suggested citation

Ong YK, Double KL, Bero L, Diong J (2023) Responsible research practices could be more strongly endorsed by Australian university codes of research conduct. Research Integrity and Peer Review (in press).

## Protocol registration

University codes of research conduct and all related documents assessed
are available in the project folder of the Open Science Framework (OSF): [https://osf.io/yfz8k/][project_folder]

The protocol for this study is stored in the OSF project folder, and registered: [https://osf.io/kd8xm][rego]

## Data

Raw data are stored in **data/raw/**.

* Codesofconductreview_DATA_2021-08-26_0940.csv
* Codesofconductreview_DATA_LABELS_2021-03-08_1401.csv

## Code

Python code files (Python v3.9) were written by Joanna Diong.

### Python files

`script`: Main script to run analysis.

`proc`: Module containing functions used to clean data and plot figures.

### Running Python code

A reliable way to reproduce the analysis would be to run the code in an integrated development environment for Python (e.g. [PyCharm][pycharm]). 

Create a virtual environment and install dependencies. Using the Terminal (Mac or Linux, or PyCharm Terminal), 

```bash 
python -m venv env
```
Next, activate the virtual environment. 

For Mac or Linux, 

```bash
source env/bin/activate
```

For Windows, 

```bash
.\env\Scripts\activate
```

Then, install dependencies,

```bash
pip install -r requirements.txt
```

Download all files into a single folder and run `script.py`.

## Output

Output are generated and stored in **data/proc/**:

* Figures of Non-Group of Eight results:
  * definitions.svg
  * ethics.svg
  * misbehaviours.svg
  * outcomes.svg
* Figures of Group of Eight results are stored in **data/proc/go8/**:
  * definitions_.svg
  * ethics_.svg
  * misbehaviours_.svg
  * outcomes_.svg
* results.txt
* fig1.svg


[project_folder]: https://osf.io/yfz8k/
[rego]: https://osf.io/kd8xm
[pycharm]: https://www.jetbrains.com/pycharm/promo/?gclid=Cj0KCQiAtqL-BRC0ARIsAF4K3WFahh-pzcvf6kmWnmuONEZxi544-Ty-UUqKa4EelnOxa5pAC9C4_d4aAisxEALw_wcB 
