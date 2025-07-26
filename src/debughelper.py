def debug_pretty_print_list(liste, name = None):
    if type(liste) is not list:
        #print(f"DEBUG_pretty_print called not on a list, Input is type:", type(liste))
        return
    if name == None:
        print("\nDEBUG start print list")
    else: 
        print(f"\nDEBUG start print list |{name}|")
    i = 0
    for entry in liste:
        i = i + 1
        print(f"-{i} ", entry)
    print("DEBUG end print list\n")