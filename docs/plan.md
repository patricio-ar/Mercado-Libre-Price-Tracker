# Price Tracker - Development Plan

Each step ends with the same routine: run the program, try the new feature (including invalid
input) and commit.

## Stage 1: manual prices

| Step | Goal | Concepts |
|---|---|---|
| 1 | Project setup: Git repository, `.gitignore`, first commit and GitHub remote | Git, GitHub |
| 2 | Menu that repeats until the user exits | `print`, `input`, `if`/`elif`/`else`, `while`, `break` |
| 3 | Add products and show them | lists, dictionaries, functions, `import`, `datetime`, `for` |
| 4 | Save and load the products | files, `with open`, `json`, `os.path.exists` |
| 5 | Update a price and compare it with the previous one | return values, `enumerate`, `abs`, nested loops |
| 6 | Handle invalid input without crashing | `try`/`except`, `continue`, `strip`, input validation |
| 7 | README and final push of Stage 1 | Markdown |

## Stage 2: Mercado Libre API

| Step | Goal | Concepts |
|---|---|---|
| 8 | Practice HTTP requests with a public API | `pip`, `requests`, status codes, JSON responses |
| 9 | Create the Mercado Libre application and get tokens | OAuth 2.0, client id and secret, authorization code |
| 10 | Get the list of the account's listings | headers, `Authorization: Bearer`, pagination |
| 11 | Get the title and price of a listing | returning `None` on failure |
| 12 | Sync the listings with `products.json` | `item_id`, `dict.get`, reusing existing functions |
| 13 | Refresh the access token automatically | refresh token, retrying a request |

## Checks for every step

- The normal case works.
- Edge cases work: empty list, first and last product, zero, empty input.
- Invalid input does not crash the program.
- `git status` does not show `products.json`, `credentials.json` or `tokens.json`.
