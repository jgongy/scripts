# Description
A Python script that takes an Excel spreadsheet with a single sheet of course
information and returns all rows containing keywords specified in the
"keywords.txt" file.

# "keywords.txt" Requirements
Please put each keyword on a new line and surround by quotation marks. The
quotation marks allow you to add leading spaces for a keyword.

Example "keywords.txt":  
"apple"  
"banana "  
" coconut"  
" durian "  

As you can see, surrounding quotes allow you to distinct word fragments
or smaller words from whole or larger words. For example, distinguishing
" sea " from "reSEArch" can be done by using spaces within the quotes. Note,
however, that you will not find phrases like "sea." or "sea," as a result.

Keywords are case sensitive. There is no support for wildcard characters.
