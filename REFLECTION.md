# Reflection ## Successful Request

In `cli.py` typing `adjust 3 offset=2 scale=4` grabs the command, value and options. the terminal command `Operations.adjust` moves the inputs to numbers and creates a `Calculation`. This performs the calculation (3 + 2) * 4 = 20. It is shown to me, and saved to history after it succeeds.

## Failed Request The span operation needs at least two values. If there is only one value it raises a `ValueError`. Session does the calculation before saving, so failed calculations are not added to history. The last result is the last successful result.

## Design The static methods `adjust` and `span` depend only on their arguments. Commands like `LastCommand` need a session object because they use saved history. `*values` allows operations to take a variable number of inputs. `**options` accepts named options such as `offset`, `scale`, `exponent`, `ddof` and so on.

The factory selects the right operation and does the calculation. Commands control actions such as calculate, display history or display last result. `LastCommand` uses stored result instead of calculating it again.

## Error Handling The factory uses `try/except` when it looks up an operation. If the operation does not exist, it catches the `KeyError` and raises a more informative `ValueError`.



## Student Tests

My tests verify that:- `adjust` applies offset prior to scale
- the default adjust values feature
- `span` is the difference between max and min`span` returns less than 2 values
- the factory makes a proper adjustment calculation
`last` shows the last successful result- failed calculations are not added to history


## Attribution

Since I copied the repo, I just added code to CLI, factory, commands, history, validation, and existing operations. I added `adjust`, `span`, factory support, `last`, CSV span support, fixed the session history bug, and added my own tests.