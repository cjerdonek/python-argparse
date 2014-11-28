TODO
====

* The Formatter should not have the section as an attribute.
  The "root section" should be passed in to format().
* Get rid of `Formatter.add_item()`.
* Think about a process where I can generically iterate through the tree.
  In the first pass I may calculate the max length.  In the second
  I may build the actual formatted string.

* Rework the `Formatter.add_*()` methods to build a tree.
  Then formatting can be a matter of iterating through the tree.