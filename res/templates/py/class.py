class {{ Name }}:
    def __init__(self):
	    print('init')


{% include "py/main.py" %}
    c = {{ Name }}()
