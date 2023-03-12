## Binary Search Implementation vs Sequential Search
Observing from the given code the difference in time complexity between the two searching algorithms.

## Theoritical Implementation

The binary seach algorthim that is implemented in the code "run.py" uses the recursion to implement the algorithm, this is considered to run in time complexity:
O(log(n))
But first of all, the data should be sorted, so this binary sort can benefit from the merge sort which has the time complexity:
O(nLogn)
so from the two time complexities:
logn + nLogn ≈ O(nLogn)
which is faster than the sequential search O(n)


## Results

| Algorithm | Running Time(s) |
| ------------- | ------------- |
| Sequential  | 0.03999 |
| Binary  | 0.00099 |

## Running the code

You can Run the code using the following command.
Make sure python is installed.
```bash
python run.py
```


## Authors

- [@Basheer](https://www.github.com/basheerrjoub)



## Appendix

Data Structures and Algorithms in Python (Michael T. Goodrich, Roberto Tamassia etc.)


## License

[MIT](https://choosealicense.com/licenses/mit/)

