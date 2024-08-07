def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
    return

#inner_function() NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
test_function()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
