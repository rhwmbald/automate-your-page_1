#HTML generator python - w.h.bald 6/8/15
#This program will generate html code 
#using two string inputs (title and description)
#that are picked out of one large input text (test_text)
#until are selected and written to html

TEST_TEXT = """TITLE: Why Computers are Stupid
DESCRIPTION: The phrase "computers are stupid" refers 
to how they interpret instructions literally. This 
means that small typos can cause big problems.
TITLE: Python
DESCRIPTION: Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly executes the body of
the loop until the "test condition" is no longer true."""


tTile='TITLE:'
tDescription = 'DESCRIPTION:'

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find(tTile)
    end_location = concept.find(tDescription)
    title = concept[start_location+len(tTile) +1 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find(tDescription)
    description = concept[start_location+len(tDescription) +1:]
    return description

def get_concept_by_number(text, concept_number):
    countr=0
    start_location=0
    end_location=0
    while countr < concept_number:
        start_location = text.find(tTile,end_location)
#        print start_location
        end_location = text.find(tTile,start_location+1)
        if end_location == -1:
            end_location=len(text)
#        print end_location
        reqText = text[start_location:end_location]
        countr += 1
    return reqText

def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(TEST_TEXT)