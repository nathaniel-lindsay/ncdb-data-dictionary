# :book: ncdb-data-dictionary :book:
A data dictionary is a compilation of information pertaining to and describing the contents, format, and structure of a database and the relationship between its elements. A data dictionary may be used to control access to and manipulation of the database.

Unfortunately, when presented in `HTML` format, a data dictionary is essentially useless to researchers. On the other hand, when converted to a JSON object that is malleable and easily trasportable, the data dictionary becomes a powerful tool for researchers 

*In this project, the Python module BeautifulSoup4 is used to parse raw html from the [NCDB's public use file](http://ncdbpuf.facs.org/node/259?q=print-pdf-all) into a dictionary, which is then converted into a JSON object.* 

# Documentation:

### Installation
I recommend using [pip](https://pip.pypa.io/en/stable/installing/) to install BeautifulSoup4 from the terminal

`pip install --user Beautifulsoup4`

or:

`sudo pip install BeautifulSoup4`

### Setup

* From the terminal, `mkdir ncdb_data_dictionary` (this will be your directory for the cloned repository)
* `cd` to `ncdb_data_dictionary`
* run `git init`
* run `git clone https://github.com/nathaniel-lindsay/ncdb-data-dictionary.git`

A cloned repository will be added to `ncdb_data_dictionary` containing `parse.py`

**In order to effectively run `parse.py`, one must download the raw `HTML` from the [NCDB's public use file](http://ncdbpuf.facs.org/node/259?q=print-pdf-all)...**

**To do this,**
* Navigate to `View` :arrow_right: `Developer` :arrow_right: `View Source` on the webpage of the link above
* Once viewing the source code, `File` :arrow_right: `Save Page As`
* Name the file `ncdb.html` and under `'Format'`, select `'Webpage, HTML Only'`, save the file to `ncdb_data_dictionary`

### Instructions

* From the terminal, `cd` to `ncdb_data_dictionary`
* `ls` and ensure both `parse.py` and `ncdb.html` are in `ncdb_data_dictionary`
* Run `python parse.py` and wait for the process to return (*should take around 3 seconds*)
* A new file, `ncdb_data_dictionary.json` has now been created, open this file in your favorite text editor 

Enjoy! :smiley:
