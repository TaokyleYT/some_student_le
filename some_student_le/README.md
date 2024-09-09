# **some student le**
<h2>really not good</h2>
<p>-by Dr Lo (my math teacher)</p>

This is a library containing 1 single line
the line rewrites some module (mostly built-in functions) into some impractical fancy function designed to replace the original

To use it, simply do `from some_student_le import *`  and watch the magic happen

(its buggy I know, but only when you use it with random advance thingy like the original)

<br><br>

*KNOWN ISSUE:*
- input doesn't allow the prompt to include ANSI code
- non-tty terminal cannot enjoy the effect (errors)
- print to file results in a raw binary crap
- editing/moving/changing size of the terminal (I dont actually know how it happen or when, but it just do) mid-print/mid-input results in ANSI code leaking (somehow)

source code: <a href="https://github.com/TaokyleYT/some_student_le">github</a> <a href="https://pypi.org/project/really-not-good/">PyPI</a>

*Roadmap:*
| version |    info    |
|---------|------------|
|0.0.0    | test version to see if the test platform works under 2 different versions of the project<br>also see if anything is wrong on PyPI|  
|1.0.0    | first release, featuring typewrite-like animated effect for `print` and `input`|