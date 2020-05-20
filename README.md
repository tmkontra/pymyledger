# PyMyLedger

Keep track of monthly income and expenses.

PyMyLedger is a minimal desktop application that aims to make it easy to quickly track month-over-month spending habits.

1. I wanted easier data-entry for expenses.
2. I wanted to try making a python desktop app.

![Application Screenshot](/docs/screen-shot-1.png)

## Overview

PyMyLedger is developed using python3.7 and requires a python3.5+ runtime (for dataclasses).

PyMyLedger is a PyQt5 application. PyQt5 is the only dependency. 

Serialization (save/load) is implemented via naive pickle.

## Installation

At present, there is no graphical installer or package distribution of PyMyLedger.

To install PyMyLedger:

1. Clone/download this repo
2. Run `pipenv install` in the repo root.

To run PyMyLedger:

> `pipenv run python app/main.py`

## Roadmap

- Finish save/load functionality
- Create distribution executable (cross-platform)
- Add import/export format (yaml? xlsx?)
- Add confirmation dialogs
- Implement visualizations

## Background

I've tried Mint, Personal Capital, etc. They do a good job of importing all my transactions, but a poor job of helping me understanding them. 

It's tedious to deduplicate credit card transactions and the latent credit card payments. Transfers from checkings to savings are misclassified. There's too much noise.

I started with a spreadsheet. I had "static" monthly items (paycheck, rent, etc.) and high-level "variable" expenses (i.e. each credit card). As I make credit card payments each month, I will enter the "new charges this statement period" to the "variable" expenses.

I realized how useful this would be when viewed over time. If I keep my data entry high-level, I am more likely to actually _do it_. If I see trends in spending (i.e. a growing amount on a single card), then I can log in to my credit card portal and dig deeper.

**I wanted a better way to do the data entry, and I also happened to be interesting in building a desktop application**.

Thus, I started PyMyLedger.