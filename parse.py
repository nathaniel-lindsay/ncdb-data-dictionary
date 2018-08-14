# Get html from target                                                                 
import json

# Import BeautifulSoup
from bs4 import BeautifulSoup

# Load html file from disk
with open("ncdb.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# Get html for div#contentwrapper (all the articles)
all_articles = soup.find_all("article")

# Data Dictionary
data_dictionary = []  

def check_matches(matches):
    """Check length of matches"""
    if len(matches) > 1:
        return matches[0]
    elif len(matches) == 0:
        return None
    else:
        return matches[0]

def get_title(article):
    """Extract title from article."""
    return article.h2.text.strip('\n')

def get_field_name(content):
    """Extract field name from content div of article."""
    matches = article.find_all(
        "div",
        class_="field field-name-field-puf-date-item-name field-type-text field-label-hidden",
    )
    match = check_matches(matches)
    try:
        return match.div.div.text
    except TypeError:
        return None

def get_category(content):
    """Extract category of case field from content div of article."""
    matches = article.find_all(
        "div",
        class_="field field-name-taxonomy-vocabulary-7 field-type-taxonomy-term-reference field-label-hidden",
    )
    match = check_matches(matches)
    try:
        return match.div.div.text
    except TypeError:
        return None

def get_length(content):
    """Extract length value and assign to length key."""
    matches = article.find_all(
        "div",
        class_="field field-name-field-length field-type-text field-label-inline clearfix",
    )
    match = check_matches(matches)
    try:
        return match.div.next_sibling.text
    except TypeError:
        return None

def get_description(content):
    """Extract description of category"""
    matches = article.find_all(
        "div",
        class_="field field-name-field-description field-type-text-long field-label-above"
    )
    match = check_matches(matches)
    try:
        return match.div.next_sibling.text.replace(u'\n',' ')                      
    except AttributeError:
        return None

def get_registry_coding_instructions(content):
    """Extract unique coding instructions specialized for certain fields"""
    matches = article.find_all(
        "div",
        class_="field field-name-field-reg-coding field-type-text-long field-label-above"
    )
    match = check_matches(matches)
    try:
        return match.div.next_sibling.text.strip('\n\n ').replace(u'\u2013',u'-').replace(u'\u2019',u"'").replace(u'\u2014',u'--').replace(u'\u201c','"').replace(u'\u201d',u'"').replace(u'\n','      ')
    except AttributeError:
            return None

def get_allowable_values(content):
    """Extract allowable values within key-value relationship"""
    matches = article.find_all(
        "div",
        class_="field field-name-field-allow-value field-type-text field-label-inline clearfix"
    )
    match = check_matches(matches)
    try:
        return match.div.next_sibling.text.replace(u'\u2013',u'-')
    except AttributeError:
        return None

def get_ncdb_system_code_assignments(content):
    """Extract NCDB code assingment details and specifications per article"""
    matches = article.find_all(
        "div",
        class_="field field-name-field-code-assign field-type-text-long field-label-above"
    )
    match = check_matches(matches)
    try:
        return match.text.replace(u'\n','      ').replace(u'\u00a0',u' ')
    except AttributeError:
        return None

def get_analytical_note(content):
    """Extract Analytical note pertaining to data use"""
    matches = article.find_all(
        "div",
        class_="field field-name-field-analytic-note field-type-text-long field-label-above"
    )
    match = check_matches(matches)
    try:
        return match.div.next_sibling.text.strip('\n').replace(u'\u2013',u'-').replace(u'\u2019',u"'").replace(u'\u201c','"').replace(u'\u201d',u'"').replace(u'\n','      ')
    except AttributeError:
        return None

def get_naaccr_item_number(content):
    """extract NAACCR Item #"""
    matches = article.find_all(
        "div",
        class_="field field-name-field-item-num field-type-text field-label-inline clearfix"
    )
    match = check_matches(matches)
    try:
        return match.div.next_sibling.text
    except AttributeError:
        return None

def get_format(content):
    """extract format"""
    matches = article.find_all(
        "div",
        class_="field field-name-field-format field-type-text field-label-inline clearfix"
    )
    match = check_matches(matches)
    try:
        return match.div.next_sibling.text
    except AttributeError:
        return None

# Dictionary to store table values
def get_table(content):
    """extract table keys and values"""
    dictionary = {}
    
    matches = article.find_all(
        'tr'
        )
    for row in matches:
        if len(row.find_all('td')) < 4 and len(row.find_all('td')) > 1:
            label = row.find_all('td')[1:3]
            labelClean = [item.text.replace(u'\u2013',u'-').replace(u'\u2019',u"'").replace(u'\u201c','"').replace(u'\u201d',u'"').replace(u'\n',' ').replace(u'\t','     ')   for item in label]
            code = row.find_all('td')
            codeClean = [item.text.replace(u'\u2013',u'-') for item in code]
            dictionary.update(dict(zip(codeClean, [labelClean])))
        elif len(row.find_all('td')) == 4:
            label = row.find_all('td')[1:2]
            labelClean = [item.text.replace(u'\u2013',u'-').replace(u'\u2019',u"'").replace(u'\n',' ')   for item in label]
            code = row.find_all('td')
            codeClean = [item.text.replace(u'\u2013',u'-') for item in code]
            dictionary.update(dict(zip(codeClean, labelClean)))
    
    matches = article.find_all(
        'tr'
        )
    for row in matches:
        label = row.find_all('td')[3:]
        labelClean = [item.text.replace(u'\n',' ')   for item in label]
        code = row.find_all('td')[2:3]
        codeClean = [item.text for item in code]
        dictionary.update(dict(zip(codeClean, labelClean)))
    
    try:
        return dictionary
    except TypeError:
        return None


for article in all_articles:
    # Dictionary to hold values
    d = {}

    #  Get title of article
    d['title'] = get_title(article)

    #  Get content
    content = article.div

    #  Get the field name
    d['field_name'] = get_field_name(content)

    # Get the category of the field
    d['category'] = get_category(content)

    # Get length
    d['length'] = get_length(content)

    # Get description
    d['description'] = get_description(content)

    # Get registry coding instructions
    d['registry_coding_instructions'] = get_registry_coding_instructions(content)   

    # Get allowable values
    d['allowable_values'] = get_allowable_values(content)
   
    # Get NCDB system code assignments
    d['ncdb_system_code_assignments'] = get_ncdb_system_code_assignments(content)

    # Get analytical note
    d['analytical note'] = get_analytical_note(content) 

    # NAACCR item #
    d['NAACCR Item #'] = get_naaccr_item_number(content)
    
    # format
    d['format'] = get_format(content)

    # tables
    d['table'] = get_table(content)

    # Append field dictionary to list
    data_dictionary.append(d)


# for d in data_dictionary:
#     print(d)


# save file to disk
    with open('ncdb_data_dictionary.json', 'w') as f:
        json.dump(data_dictionary,f)







