# Baking Challenge
# You are having a bake sale and are going to sell sugar cookies
# You look up the recipe and the prices from your local grocery store
# and decide to write a Python script that calculates how many batches
# of cookies you must sell in order to make your desired profit.

# Below are two dictionaries:
# The recipe dictionary is expressed in cups and single eggs.
# It is the recipe for just one batch of sugar cookies.
recipe = {'butter': 1, 'sugar': 2, 'flour': 3, 'eggs': 1}
# The prices dictionary is expressed in dollars per pound and dollars
# per dozen of eggs
prices = {'butter': 3.60, 'sugar': 1.60, 'flour': 1.00, 'eggs': 3.00}

# There are 4 cups in a pound
# You will sell your cookies for $5 per batch
# You invest $100 for a table

# Write a function, profit_calculator, that returns the number of batches
# of cookies that you must sell in order to get the desired profit


def batch_recur(
        i,
        number_of_batches,
        desired_profit,
        batch_profit,
        investment):

    if i < desired_profit + investment:
        return batch_recur(
            i=i + batch_profit,
            number_of_batches=number_of_batches + 1,
            desired_profit=desired_profit,
            batch_profit=batch_profit,
            investment=investment)
    else:
        return number_of_batches


def number_of_batches(
        desired_profit,
        batch_profit):

    return batch_recur(
        i=0,
        number_of_batches=0,
        desired_profit=desired_profit,
        batch_profit=batch_profit,
        investment=100)


def batch_calculator(
        batch_sale_price,
        cost_of_booth,
        desired_profit):

    cost_per_batch = \
        ((prices['butter'] / 4) * recipe['butter']) + \
        ((prices['sugar'] / 4) * recipe['sugar']) + \
        ((prices['flour'] / 4) * recipe['flour']) + \
        ((prices['eggs'] / 12) * recipe['eggs'])

    profit_per_batch = batch_sale_price - cost_per_batch

    return number_of_batches(
        desired_profit=desired_profit,
        batch_profit=profit_per_batch)


def profit_calculator(desired_profit):
    return batch_calculator(
        batch_sale_price=5,
        cost_of_booth=100,
        desired_profit=desired_profit)


# Example:
print(profit_calculator(desired_profit=250))
# >>> 153
