from flask import Flask

pagehtml = """
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The Schooner</title>
  <meta name="description" content="The Schooner">
  <meta name="author" content="Kristofer">

<style>
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  line-height: 1.6;
  color: #303030;
  max-width: 40rem;
  padding: 2rem;
  margin: auto;
  background: #FEF4FF;
}
img {
  max-width: 100%;
}
a {
  color: #2ECC40;
}
h1, h2, strong {
  color: #303030;
}
</style>
</head>

<body>
  <h1>Python</h1>
  <p><img src="https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F0%2F0a%2FPython.svg%2F1200px-Python.svg.png&imgrefurl=https%3A%2F%2Fen.wikiversity.org%2Fwiki%2FPython&tbnid=XmmuGvoln--UuM&vet=12ahUKEwjM6YDWkNjtAhUQON8KHW5FBlMQMygDegUIARDRAQ..i&docid=k36Oe0TGOvdiNM&w=1200&h=1200&q=python%20image&ved=2ahUKEwjM6YDWkNjtAhUQON8KHW5FBlMQMygDegUIARDRAQ"</p>
<p>What is Python? Executive Summary</p>

<p>
Python is an interpreted, object-oriented, high-level programming language 
with dynamic semantics. Its high-level built in data structures, 
combined with dynamic typing and dynamic binding, 
make it very attractive for Rapid Application Development, 
as well as for use as a scripting or glue language to connect existing components together. 
Python's simple, easy to learn syntax emphasizes readability and 
therefore reduces the cost of program maintenance. 
Python supports modules and packages, which encourages program modularity and code reuse. 
The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, 
and can be freely distributed.
</p>
<h2></h2>
<p>
Often, programmers fall in love with Python because of the increased productivity 
it provides. Since there is no compilation step, 
the edit-test-debug cycle is incredibly fast. 
Debugging Python programs is easy: a bug or bad input will never 
cause a segmentation fault. Instead, when the interpreter discovers an error, 
it raises an exception. When the program doesn't catch the exception, 
the interpreter prints a stack trace. 
A source level debugger allows inspection of local and global variables, 
evaluation of arbitrary expressions, setting breakpoints, 
stepping through the code a line at a time, and so on.
The debugger is written in Python itself, 
testifying to Python's introspective power. 
On the other hand, often the quickest way to debug a program is to add a few print statements to the source: 
the fast edit-test-debug cycle makes this simple approach very effective.
</p>
</body>
</html>
"""
app = Flask(__name__)

@app.route("/")
def hello():
    return pagehtml
