# Linked lists & Arrays

## Questions:

### Compare advantages and disadvantages of arrays vs linked list (complexity of task completion)

A large advantage of linked lists is resizability. In many languages, the sizes of arrays cannot change;
however, this is not true in python. Arrays in python are dynamic, but are inefficient when memory relocation
is necessary to increase the size. Linked lists do not hold this burden; consequently, they are optimal when
the desired size of an array is unknown. 
Arrays are advantageous when

### For arrays, we are interested in implementing a replace function that acts as a deletion
### followed by insertion. How can this function be implemented to minimize the impact of
### each of the standalone tasks

The replace function (assuming a value to find and replace, and the value to replace with) could do both the deletion and the insertion in the same line of code. This is done by looping through each element of the array until we find the desired value. Once the value is found we can use the iterator variable to hold our index, then in one line of code we can set the value of the index at the array equal to the value to replace with. Since python has a garbage collector, the value that we replaced with will get deleted.

###Assuming you are tasked to implement a Singly Linked List with a sort function, given
the list of sort functions below, state the feasibility of using each one of them and
elaborate why is it possible or not to use them. Also show the expected complexity for
each and how it differs from applying it to a regular array



