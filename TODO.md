TODO
====

* Get rid of `Formatter.add_item()`.
  - In particular, we should be formatting the string as we go along
    (now that we are computing the max length in advance).
* Think about a process where I can generically iterate through the tree.
  In the first pass I may calculate the max length.  In the second
  I may build the actual formatted string.

* Rework the `Formatter.add_*()` methods to build a tree.
  Then formatting can be a matter of iterating through the tree.