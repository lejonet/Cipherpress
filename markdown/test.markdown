Markdown: Basics
================

Getting the Gist of Markdown's Formatting Syntax
------------------------------------------------

This page offers a brief overview of what it's like to use Markdown.
The [syntax page] [s] provides complete, detailed documentation for
every feature, but Markdown should be very easy to pick up simply by
looking at a few examples of it in action. The examples on this page
are written in a before/after style, showing example syntax and the
HTML output produced by Markdown.

It's also helpful to simply try Markdown out; the [Dingus] [d] is a
web application that allows you type your own Markdown-formatted text
and translate it to XHTML.

**Note:** This document is itself written using Markdown; you
can [see the source for it by adding '.text' to the URL] [src].

  [s]: /projects/markdown/syntax  "Markdown Syntax"
  [d]: /projects/markdown/dingus  "Markdown Dingus"
  [src]: /projects/markdown/basics.text


## Paragraphs, Headers, Blockquotes ##

A paragraph is simply one or more consecutive lines of text, separated
by one or more blank lines. (A blank line is any line that looks like
a blank line -- a line containing nothing but spaces or tabs is
considered blank.) Normal paragraphs should not be indented with
spaces or tabs.

Markdown offers two styles of headers: *Setext* and *atx*.
Setext-style headers for `<h1>` and `<h2>` are created by
"underlining" with equal signs (`=`) and hyphens (`-`), respectively.
To create an atx-style header, you put 1-6 hash marks (`#`) at the
beginning of the line -- the number of hashes equals the resulting
HTML header level.

Blockquotes are indicated using email-style '`>`' angle brackets.

Markdown:

    A First Level Header
    ====================
    
    A Second Level Header
    ---------------------

    Now is the time for all good men to come to
    the aid of their country. This is just a
    regular paragraph.

    The quick brown fox jumped over the lazy
    dog's back.
    
    ### Header 3

    > This is a blockquote.
    > 
    > This is the second paragraph in the blockquote.
    >
    > ## This is an H2 in a blockquote

### Phrase Emphasis ###

Markdown uses asterisks and underscores to indicate spans of emphasis.

Markdown:

    Some of these words *are emphasized*.
    Some of these words _are emphasized also_.
    
    Use two asterisks for **strong emphasis**.
    Or, if you prefer, __use two underscores instead__.

