Inputs:
Beautified javascript file path
List of hex codes from the file
Output file path

Design:
The script takes a beautified javascript file. The javscript file must have a list of variables encoded into hex codes, whose elements are referenced throughout the javascript file. The script converts the hex codes into their alphanumeric equivalents and then replaces every reference of every element in the list with the actual element.
