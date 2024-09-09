# **some student le**
<h2>really not good</h2>
<p>-by Dr Lo (my math teacher)</p>

This is a library containing 1 single line
the line rewrites some module (mostly built-in functions) into some impractical fancy function designed to replace the original

To use it, simply do `from really_not_good import *`  and watch the magic happen

(its buggy I know, but only when you use it with random advance thingy like the original)

<br><br>

*KNOWN ISSUE:*
- input doesn't allow the prompt to include ANSI code
- non-tty terminal cannot enjoy the effect (errors)
- print to file results in a raw binary crap
- editing/moving/changing size of the terminal (I dont actually know how it happen or when, but it just do, I cant even recreate it on purpose it just happens randomly) mid-print/mid-input results in ANSI code leaking (somehow)

source code: <a href="https://github.com/TaokyleYT/some_student_le">github</a> <a href="https://pypi.org/project/some-student-le/">PyPI 1</a> <a href="https://pypi.org/project/really-not-good/">PyPI 2</a> 

***Development log:***<br>
*(every version not shown here is either not exist or deleted for various reasons)*
| version |    info    |   yanked    |
|---------|------------|-------------|
|0.0.0    | test version to see if the test platform works under 2 different versions of the project<br>also see if anything is wrong on PyPI|**YES**|
|0.0.1    | more testing on top of 0.0.0, some bug fixed|**YES**|
|1.0.1    | first release, featuring typewrite-like animated effect for `print` and `input` (cause I accidentally deleted 1.0.0 so its now 1.0.1)|**YES**|
|1.0.3    | fixed a typo on readme where it's telling you to import the wrong thing to use it|**YES**|
|1.0.4    | fixed a bug where PyPI 1 version cannot be used (since the 2 versions are released together, one went wrong and the other need to be updated too so...)<br>Also added the link to 2 versions to README.md|**NO**|