import callback_module

def my_callback(value):
    print(f"Python callback received: {value}")
    # Do some processing and return a result
    return value * 2

# Call the C function with our Python callback
result = callback_module.process_with_callback(my_callback)
print(f"Final result: {result}")
