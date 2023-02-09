# Question 5

Exercise 5
Stacks and Queues are a special form of linked lists with some modifications that makes
operation better. For parts 1 and 2 assume we are using a singly linked list
1. In stacks, insertion (push) adds the newly inserted data at head
a. why? (0.5 pts)
b. Can we insert data at the end of the linked list? (0.5 pts)
c. If yes, then what is the difference in operation time (if any) for pushing and
popping data from the stack? (1 pt)
2. In Queues, we added a new pointer that points to the tail of the linked list
a. why? (0.5 pts)
b. Can we implement the Queue without the tail? (0.5 pts)
c. If yes, then what is the difference in operation time (if any) for enqueuing and
dequeuing data from the stack? (1 pt)
d. Can we change the behavior of the enqueue and dequeue where we enqueue at
head and dequeue at tai? Do you think it is a good idea? (1 pt)
3. Revisit your answers for part 1 and 2 but now with the assumption that we are using
circular doubly linked list (5 pts)

### 1.
a) To save time and code. Since the 'head' node is already accessibly it is much easier to insert data at the head rather than traverse through the whole list to insert data at the end.
b) Yes, to insert data at the end of a (singly) linked list we would need to traverse to the final node in the list and then link the new data.
c) It would be longer to push and pop data from the end of a stack, since traversing the list is needed O(n). The pointer to the start of the list already exists and makes it much quicker to push and pop data from the list O(1), whereas the end of the list requires a traversal.
### 2.
a) A pointer to the end of the linked list exists so that the end of the linked list can easily be found, not requiring a traversal of the list. It is not needed, but without it the list would have to be iterated through till the end was found everytime a new item was added to the queue.
b) Yes, but the queue will take longer to enqueue data, as a full iteration of the queue is needed to get to where new data is to be enqueued.
c) Since operation with the tail pointer is one operation to find the end of the queue, the complexity is O(1). We would go from O(1) to traversing the queue until we find the tail item, which means n amount of iterations resulting in O(n) complexity.
d) Yes, it is possible to do so. But since this would result in having a "last-in first-out" we would basically have a stack. I do not think it would be a good idea since some applications of queues are used due to the "first-in first-out" nature of them - removing this from them would not make them ideal for these applications anymore.

### 3.




