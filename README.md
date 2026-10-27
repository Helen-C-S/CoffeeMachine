# Coffee Machine

A small command-line coffee ordering program written in Python as an object-oriented programming exercise. The program takes coffee orders through a text menu, keeps them in memory while it runs, and saves them to a timestamped text file on exit.

## Files

| File | Purpose |
|------|---------|
| `main.py` | Entry point. Shows the menu and calls the matching `CoffeeMachine` method. |
| `coffee_machine.py` | The `CoffeeMachine` class. Owns the list of orders and all order handling. |
| `coffee.py` | The `Coffee` class (one order) and the `Enum` lists for coffee type, cup size and cream. |

## How to run

```
python main.py
```

Requires Python 3.10 or later (the menu uses `match`/`case`).

## Menu

```
1. Order New Coffee
2. See list of previous coffee orders
3. Change the last coffee order
4. Delete the last coffee order
0. Exit
```

- **1** asks for a name, then presents numbered menus for coffee type, cup size and cream, and confirms the order.
- **2** lists all orders taken in this session.
- **3** re-runs the coffee menus for the last order, keeping the original name.
- **4** removes the last order.
- **0** saves all orders to a file named `orders_YYYYMMDD_HHMMSS.txt` (one order per line, fields separated by `;`) and exits.

## Design

- `Coffee` holds one order: name, time, coffee type, size and cream. Name and time are private attributes with getters.
- `CoffeeMachine` holds a private list of `Coffee` objects. Public methods: `take_order`, `list_orders`, `update_order`, `delete_order`, `print_last_order`, `save_orders`. Two private helpers avoid repeated code: `__choose_from` builds a numbered menu from any `Enum` and validates the input, and `__build_order` runs the questions and returns a `Coffee`.
- `main.py` only drives the menu; it never touches the order list directly.

## Error handling

- Menu input is validated in a loop: non-numeric input raises `ValueError`, out-of-range numbers raise `IndexError`, and the user is prompted again.
- Updating or deleting with no orders is caught with `IndexError` and reported instead of crashing.
- The order file is written with `with open(...)`, so it is closed correctly even if a write fails.

## Order file format

```
Helen;22-10-2026 13:40;Cafe Latte;Large;With Cream
```

The `;`-separated layout can be read into a pandas DataFrame with `pd.read_csv(filename, sep=";", header=None)`.
