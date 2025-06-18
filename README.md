# GoCard System

This repository contains a small Python program that models a GoCard
account for public transport.  Users can top up, take rides and print
statements.  Two specialised card types are provided:

* **RegularGoCard** – After every ten full‑price rides, the next five rides
  receive a 5% discount.
* **PensionerGoCard** – Every ride receives a 5% discount.

Transactions can be entered interactively or loaded from a file.  Lines in
the file follow the same syntax as the interactive commands.

## Running

Interactively:

```bash
python3 main.py
```

From a file of commands:

```bash
python3 main.py transactions.txt
```

The file may contain multiple customers.  Use a line starting with
`person` to start a new account.  For example:

```
person Alice regular 20
r 3.5
t 10
q
person Bob pensioner 15
r 4.0
q
```
