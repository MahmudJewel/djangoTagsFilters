# Built-in template tags and filters
In templates, values are passed  {{value}} and Tags are passed {% tags %}
## filter==>Method or Function
Filters the contents of the block through one or more filters. Multiple filters can be specified with pipes and filters can have arguments, just as in variable syntax.
## Structure:
Note that the block includes all the text between the filter and endfilter tags.
```
{% filter force_escape|lower %}
	This text will be HTML-escaped, and will appear in all lowercase.	
{% endfilter %}
```
