### Put all the output to a sub directory
$out_dir = "latexmk-out";

### Use "pdflatex"
$pdf_mode = 1;

### This is needed to build indicies for glossaries and accronyms
add_cus_dep( 'glo', 'gls', 0, 'makeglo2gls' );
sub makeglo2gls {
    system("makeindex -s \"$_[0].ist\" -t \"$_[0].glg\" -o \"$_[0].gls\" \"$_[0].glo\"" );
}
add_cus_dep( 'acn', 'acr', 0, 'makeacr2acn' );
sub makeacr2acn {
    system( "makeindex -s \"$_[0].ist\" -t \"$_[0].alg\" -o \"$_[0].acr\" \"$_[0].acn\"" );
}




####################################################################
### Some addtional suggestions.  Do NOT uncomment them in this file
### but rather copy what you want to your own personal ~/.latexmkrc.
####################################################################

### If you use "mupdf" or another PDF viewer that requires a key
### stroke to refresh its view of the PDF you can tell latexmk to type
### that keystroke with the help of the "xdotool":
# $pdf_previewer = "start mupdf %S";
# $pdf_update_method = 4;
# $pdf_update_command = "xdotool search --class mupdf key --window %@ r";

### Or, simply tell latexmk to use start some different PDF viewer
### than default.  It probably defaults to xpdf which isn't so user
### friendly by today's standards.
### 
### MATE (will auto refresh by default)
# $pdf_previewer = "start atril %S";
### Gnome/Unity (will auto refresh by default)
# $pdf_previewer = "start evince %S";

