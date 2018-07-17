# DUNE Technical Proposal (TP)
Info and links on this page:

* Guidelines
* Quick Start
* Best Practices for interacting with github
* Find auto-build PDF files of each Volume
* Management
* Major news (regarding any changes to this repository)

## Guidelines and information

Please follow the editing guidelines in [Document Guidance](https://github.com/DUNE/document-guidance). You will find information on:
* how to use git
* how to get the files and build the document
* DUNE standards for editing (images, tables, labels, citations, numbers/units, upper/lower case, grammar, punctuation, inserting "fixmes", etc.)

Do you want to reference content from previous design reports? Go to: 

* [CDR](https://github.com/DUNE/cdr)
* [ProtoDUNE-SP TDR](https://github.com/DUNE/protodune-tdr)
* (We can add others, or you can go to [the DUNE area in github](https://github.com/DUNE) and search for the one you want.)

## Quick start
This shows how to clone the repository and build a TP volume. Bare bones. See more detailed and non-TP-specific information in the "Best practices" section below and at [Document Guidance](https://github.com/DUNE/document-guidance).

-  [Get a github account](https://help.github.com/articles/signing-up-for-a-new-github-account) and send your username to Brett (bv@bnl.gov).
-  [Install Git on Mac](https://github.com/DUNE/document-guidance/blob/master/install-git-on-mac.org), requires Mac OS X, [Apple ID](https://appleid.apple.com), [XCode](https://developer.apple.com/xcode/downloads), and [Command Line Tools](https://developer.apple.com/download/more/).
-  [Github Desktop](https://desktop.github.com/) Manage your [GitHub flow](https://guides.github.com/introduction/flow/) using this dandy interface. 

If you need a reliable LaTeX installation, Tom Junk has installed texlive 2017 in his area on the dunegpvm's at Fermilab. Feel free to use it! Just login and run his setup file:

```
  $ ssh dunesl7gpvm01.fnal.gov  
  for bash and sh:  $ source /grid/fermiapp/products/dune/texlive2017/setup.sh
  for tcsh and csh: $ source /grid/fermiapp/products/dune/texlive2017/setup.csh
  $ mkdir /my/work/area
```


 
- Type this sequence to clone the repository:
```
  $ cd /my/work/area
  $ git clone https://github.com/DUNE/Technical-Proposal.git
```
 
- Do a test edit and test build, e.g., the software-computing volume (yes, run pdflatex twice)
```
  $ cd DUNE-TDR
  $ pdflatex software-computing
  $ pdflatex software-computing
```

There is also a script to run with the above as well as build bibliography and indices.

```
   $ ./compilit software-computing
   $ ./compilit software-computing print
   $ ./compilit software-computing clean
```

The first will build with line numbers, fixme's and other things useful for editing, the second will build with "print quality".  The third deletes intermediate files except the final PDF.
 
- Type this sequence to commit (after it builds successfully):
```
  $ git commit -a -m "Brief explanation of what you updated"
  $ git push
```

- One must add new files just once and then commit as above.
```
  $ git add path/to/the/file.ext
```


## Best practices for interacting with GitHub
Please follow these four important guidelines that will help avoid headaches:

1. Always do a pull immediately before you begin working on a file just in case someone else modified it recently.
2. We recommend that you compile frequently as you compose and edit; it will be easier to resolve any compilation problems.
3. Make sure the document compiles before you commit it and push it to the repository. Ask Anne (aheavey@fnal.gov) if you need help.
4. Commit and push immediately after you finish your edits so that others have the best chance of picking up your changes before they edit.  (Yes, git can resolve conflicts, but it's better to avoid them.)

## Autobuilt PDFs from the repository

Shortly after successful commits are pushed, these links should point to updated files:  

* [Executive Summary Volume](https://dune.bnl.gov/docs/technical-proposal/executive-summary.pdf)
* [FD Single-Phase Volume](https://dune.bnl.gov/docs/technical-proposal/far-detector-single-phase.pdf)
* [FD Dual-Phase Volume](https://dune.bnl.gov/docs/technical-proposal/far-detector-dual-phase.pdf)
* [Software and Computing Volume](https://dune.bnl.gov/docs/technical-proposal/software-computing.pdf)

If a build fails an error message will be sent to the committer if they have registered an email with GitHub.

The documents in this repository can of course be built by you with your favorite LaTeX tools.  This repository provides some support for a few popular tools as described in [tools.org](tools.org).


## Management

* The management area in the DUNE wiki for development of this volume is at [Technical Proposal](https://wiki.dunescience.org/wiki/Technical_Proposal).
* We may also maintain assignments and status info at [Technical Proposal Tracking](https://wiki.dunescience.org/wiki/Technical_Proposal_Tracking).

For general DUNE information: Go to [DUNE at Work](https://web.fnal.gov/collaboration/DUNE/SitePages/home.aspx)


## Major News
Repository created 19 December 2017!

-- Anne Heavey




