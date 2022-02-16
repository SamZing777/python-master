fixed_items = ('electricity', 'tapes', 'polyethylyn', 'flash', 'battery')
print(fixed_items)

print(fixed_items[0])
print(fixed_items[1])

"""
    lists are immutable
    fixed_items[0] = "crayon"
    will result into an error

    Error:
        TypeError:
            'tuple' object does not support item assignment
"""

for items in fixed_items:
    print(items)
    
