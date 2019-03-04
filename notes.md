## 02/27/19

**properties of priority queue**
* smallest element at root
* parents are smaller than or equal to children
* things are left-justified

## 02/25/19

* there is a class of problems that machines cannot solve

## 02/14/19

* python can ask OS for memory, and when the program terminates, python's garbage collector will remove it

## 02/13/19

* priority queue
* `nice fred` where fred is a large computational program and fred will use less memory since itll use a lot of CPU
* with administrative priviledges, you can raise priority of a program. normal uses can only lower priority
* unix was developed for small machines(multix was for the big computer) 

**properties of priority queue tree**
* parent has 0, 1, or 2 children
* priority of parent is equal or greater than of children
* all the levels are filled except for the last one, and the last one is filled left to right
* root is always highest priority

**process of rebalancing tree**
* remove root(highest priority)
* put last item in tree into root
* look at the larger child of the new root, and swap it(this is called bubbling down)

**process of adding to tree**
* put the new element in its position node
* bubble it up

**array version of priority queue**
* make array of n + 1 elements size
* dont use the 0th element
* 1st element is root, read left to right and fill in the new positions
* subtracting:
    * set smallest(last element) to position 1(root)
    * find the children(2n and 2n + 1, swap with biggest)
* adding:
    * divide by 2 to bubble up

## 02/12/19
```python
a = Node(5)
fred = a

def fred(q):

```

## 02/11/19

* C was created to be almost as efficient but much easier to program in than assembly language

```python
import sys
temp = sys.argv # ["harry.py", "fred.csv", "george.csv"]
try:
    # the U fills in the line endings with \n since different OS have different line endings
    f = open(temp[1], "rU") 
    lines = f.read().split("\n")
    f.close()
except:
    print("error!")
    return

words = lines[0].split(",")

ints = [int(x) for x in words]
answers = [7, -5, 12]

f = open(sys.argv[2], "w")
toWrite = [str(x) for x in answers]
f.write(",".join(toWrite) + "\n")
f.close()

```

## 02/06/19

**Aim**: Hashing

* log base 2 compression is extremely powerful(1,000,000 elements only require 20 searches)
* mapping works by turning each character of a word into a corresponding number 1-26. Then, to convert it to one number, you multiple the first number by 26, the second by 26^2... etc. This **gaurantees** an unique number, but the number will be huge
* this would assume you have an insane amount of memory, and then you would map each value of each word into the cooresponding place in the memory block. This is **O(1) operation**
* you can just modulo a huge number with another number to shrink it. This small number is found by moduloing by the number of values you actually need. This is **hashing**
* **collision** occurs on rare occasion when two modulos give the same location, and you just have to relocate it.
* the point of a good hash function is to randomize the data(brooks and pprooks should be very different locations). You can use hashes to identify/tag a paper since each paper will produce different hash numbers.(serves as a signature)
* sets can immediately tell you by telling you if it contains an element or not(*O(1)*)
```python
# $ python3 fred.py 45 brooks
import sys
sys.argv # ["fred.py", "45", "brooks"]
```

## 02/04/19

* you can custom set parameters(python doesn't have to be parameter-place restricted)
* c is convenient for the machine, python is convenient for the programmer
* python is about 100 times slower than java/c. this doesn't usually matter because we have so much computing power
*

```python
def fred(a, b = 4):
	return a / b
print(fred(1, 2)) # 0.5
print(fred(b = 3, a = 2)) # 0.6666666
print(fred(3)) # a = 3, b is by default = 4

a [1, 4, 2, 4, 6, 7, 2] # there are duplication
b = set(a)
print(b) # {1, 2, 4, 6, 7, 45.099, 45.098}
c = list(b)
print(c) # prints the list in a
```

* set properties:
	* no duplicates
	* to look up a value in a set is an O(1) process **this is the most valuable aspect of sets**
* you can't depend on the ordering of sets

## 02/01/19

* tuples are special in Python and will allow you to understand how python does things
* list are mutable
* tuples are **immutable**
* strings are immutable, in order to change characters you must make a new string, change the letter, and then return the new string

```python
A = [1, 5, "HI"]
A[1] = 18
# A = [1, 18, "HI"]

Q = (1, 5)
R, S = Q
# R = 1, S = 5
u, v = R, S
# u = 1, v = 5
R, S = S, R
# easiest way to swap two variables

# ----------------------------------
DEF F(A, B):
	return A / B;
# but if B = 0, program will blow
# you want this program to pass out 2 results; a quotient and a pass/fail result

DEF F(A, B):
	if b == 0:
		return False, 0
	return True, A / B
success, Q = F(u ,v)

```

* you can't allow anythnig to happy, you must have an impposible action in order to know that something went wrong

-----

## 01/31/19

* in AI you need to understand some linear alg, calculus, statistics, etc, in order to truly understand what's going on beneath the hood
* commenatorial explosion:
	* the primary problem in AI because you have to be smarter than trying to brute force your way through all combinations
* jupyter notebook is perfect IDE for python(and other notebooks)
	* Google Colab is the easiest way to do Jupyter Notebook
	* right now we write program in text-editor, then use interpreter to run it
	* the other approach with jupyter is using the browser to write code. The web server will give the code to python interpreter then sends back the result. In jupyter it's cool because the front-end notebook can be separate from the back-end server. The interpreter can be in Atlanta but your code will still be run.
	* look into Colab by Google. They give you a jupyter platform and stores code onto ur google drive. Integrates well with GitHub.
	* Anaconda distribution to setup jupyter and a whole series of other tools for data science and machine learning

-----

## 01/30/19

**Aim**

* speech recoginition is difficult since there are ambiguities
* how to differentiate:
	* context of conversation
	* invading a nice beach in normandy xd
	* likeliness of phrases
* in ai there's constant probability of phrases and **never** certainties
* jeopardy is a hard game to play for AI since there are incorrect spelling, cultural references, jokes, etc.
* years for special taxis to even be avialable: 1, 2, 5, 7, 10, 15
* taxi regular: 10, 30
* buy a driverless hybrid car: 10, 30
* there are a lot of implications for driverless cars:
	* jobs will be lost
	* new method of driving since AI dont need street lights etc
	* car insurance changes
	* people waiting for transplants will be lost since there are less accidents
	* many interesting/unintended effects

-----

## 01/29/19

**Aim**: What is AI?

* machine learning
* google's deep dreams
* games
* turing test
* self-driving cars
* facial recognition
* recommendation engines
* netflix(it costs them money for them to send you bandwidth. why?)
	* using YOU as a recommendation engine
	* so you dont cancel subscription
* behind **all** AI products(behind the scenes) is *money*. This drives AI behind the scenes
* in games big news:
	* **2016**: alphago, deep mind
		* trained over vast quantities of games, find patterns that lead to winning
	* **2017**: alphagoZero
		* completely different(no human games)
		* given the rules for Go, and was told to play itself
		* within 4 days, it beat alphago
		* we're talking about billions of games
	* **2017**: alphaZero
		* a question: can AI learn multiple games and master them?
		* alphaZero beat alphagoZero within 10 hours, and mastered not only Go but chess as well
	* woke up China to the capabilities on AI when AI beat a Go player
* machines
	* high number of calculations
	* Chinese can start doing pattern recognition soon b/c they're doing their social credit score(like credit score)
	* vast amounts of info has been collected by Chinese gov and corporations to model consumption behavior(also **Amazon**)
* humans
	* high level pattern recognition(though recently machines can start doing this)
* Amazon will be collecting the most data from users
* facial recognition is important since it can be used as surveillance(this is why money is going into this)
