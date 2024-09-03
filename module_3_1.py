calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string: str):
    count_calls()
    a = (len(string), string.upper(), string.lower())
    return a

def is_contains(string: str, list_to_search: list):
    count_calls()
    if string.lower() in map(str.lower, list_to_search):
        return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



