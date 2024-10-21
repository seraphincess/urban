calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    info = (len(string), string.upper(), string.lower())
    return info

def is_contains (string, list_to_search):
    count_calls()

    word = string.lower()
    list_research = []
    for i in list_to_search:
        list_research.append(i.lower())

    if list_research.count(word) > 0:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)