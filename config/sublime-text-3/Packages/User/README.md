# competelib
Competitive programming library (subl3 snippets)

A little collection of useful algorithms and templates for comptetitive programming in the form of [Sublime Text 3](https://www.sublimetext.com/) C++ code snippets.

To use tham simply put the files in your Sublime Text 3 configuration folder under _.../Packages/User_ and once in a C++ file type then name of the snippet which you want to use (naems of the sinppets are that of which files they are located in) and press enter or tab to expand the snippet.

Most of the algorithms are highly optimized but that doesn't imply that they are the optimal solution for the given problem.

The list of algorithms:

* [The Templator 9000](https://github.com/klzxs/competelib/blob/master/bmain.sublime-snippet "bmain.sublime-snippet"): An unhealthy amount of templates, defines and typedefs packed in with a gcd<sup>[wikipedia](https://en.wikipedia.org/wiki/Greatest_common_divisor)</sup> implementation cause I can.
* [The Standard](https://github.com/klzxs/competelib/blob/master/imain.sublime-snippet "imain.sublime-snippet"): A standard, very much not exciting main function with some handy headers pre-included.
* [The Sieve of Eratosthenese](https://github.com/klzxs/competelib/blob/master/sito.sublime-snippet "sito.sublime-snippet")<sup>[wikipedia](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)</sup>: A famous algorithm to find prime numbers<sup>[wikipedia](https://en.wikipedia.org/wiki/Prime_number)</sup> up to __*N*__. Comes with two factoring functions: factor_small() for numbers up to __*SITO_MAX*__ and factor() which can be used up to _10<sup>12</sup>_.
* [DFS](https://github.com/klzxs/competelib/blob/master/dfs.sublime-snippet "dfs.sublime-snippet")<sup>[wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)</sup>: The base I use for my DFS algorithms
* [BFS](https://github.com/klzxs/competelib/blob/master/bfs.sublime-snippet "bfs.sublime-snippet")<sup>[wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)</sup>: The base I use for my BFS algorithms
* [Modint](https://github.com/klzxs/competelib/blob/master/modint.sublime-snippet "modint.sublime-snippet"): A struct that helps with calculations that use modulo<sup>[wikipedia](https://en.wikipedia.org/wiki/Modulo_operation)</sup>.
