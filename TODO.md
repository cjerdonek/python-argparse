TODO
====

* Make a function to calculate the max action length in a first pass.
* The Formatter should not have `_current_indent` as an attribute (to
  remove state).
* Get rid of `Formatter.add_item()`.
* Think about a process where I can generically iterate through the tree.
  In the first pass I may calculate the max length.  In the second
  I may build the actual formatted string.

* Rework the `Formatter.add_*()` methods to build a tree.
  Then formatting can be a matter of iterating through the tree.