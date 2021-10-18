# Built-in template tags and filters
In templates, values are passed  {{value}} and Tags are passed {% tags %}
## filter==>Method or Function
Filters the contents of the block through one or more filters. Multiple filters can be specified with pipes and filters can have arguments, just as in variable syntax.

Structure:
Note that the block includes all the text between the filter and endfilter tags.
```
{% filter force_escape|lower %}
	This text will be HTML-escaped, and will appear in all lowercase.	
{% endfilter %}
```
Or
```
{{ value|add:"2" }}
```
If value is 4, then the output will be 6.
Here add is a filter (function), 2 is the argument


# Some Built-in tag reference
In the above example, filter is also a Built-in tags.
## comment
Ignores everything between {% comment %} and {% endcomment %}

Example:

``` {% comment "Optional note" %}
	<p>Commented out text with {{ create_date|date:"c" }}</p> 
{% endcomment %} ```



## extends
Signals that this template extends a parent template.
Example:
``` {% extends "base.html" %} ```


## include
Loads a template and renders it with the current context. This is a way of “including” other templates within a template.
Example:
``` {% include "foo/bar.html" %} ```


## load
Loads a custom template tag set
example:
{% load somelibrary package.otherlibrary %}

## lorem
Displays random “lorem ipsum” Latin text. This is useful for providing sample data in templates.
Example:
{% lorem %}
or

{% lorem count method random %}


Argument
Description
count
A number (or variable) containing the number of paragraphs or words to generate (default is 1).
method
Either w for words, p for HTML paragraphs or b for plain-text paragraph blocks (default is b).
random
The word random, which if given, does not use the common paragraph (“Lorem ipsum dolor sit amet…”) when generating text.

## url
Returns an absolute path reference (a URL without the domain name) matching a given view and optional parameters. Any special characters in the resulting path will be encoded using iri_to_uri().
Example:
{% url 'app-views-client' client.id %}
where
path('client/<int:id>/', app_views.client, name='app-views-client')

***
***
***




# Built-in filter reference
## add
Adds the argument to the value.
Syntax:
{{ first|add:second }}
Example:
{{ value|add:"2" }}
If value is 4, then the output will be 6.

## capfirst
Capitalizes the first character of the value
Example:
{{ value|capfirst }}
If value is "django", the output will be "Django".

## cut
Removes all values of arg from the given string.
Example:
{{ value|cut:" " }}
If value is "String with spaces", the output will be "Stringwithspaces".

## date
Formats a date according to the given format.
Example:
{{ value|date:"D d M Y" }}
If value is a datetime object (e.g., the result of datetime.datetime.now()), the output will be the string 'Wed 09 Jan 2008'

***
***
***

# Reference:
https://docs.djangoproject.com/en/3.2/ref/templates/builtins/



