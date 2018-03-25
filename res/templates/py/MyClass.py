class {% block Name %}MyClass{% endblock %}:
    def __init__(self):
	    print('init')


{% include "py/main.py" %}
    c = {{ self.Name() }}()
