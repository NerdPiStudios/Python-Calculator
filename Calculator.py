print("Welcome to NPS calculator.")
print("Type quit at any time to exit the program.")
print("Please enter a problem.")

def check_to_quit(info):
    try:
        info.lower()
    except AttributeError:
        return
    if info.lower() == "quit":
        print('Now exiting...')
        sys.exit()
    else:
        return
