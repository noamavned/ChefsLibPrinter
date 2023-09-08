INDENTATION = "    "

def __printFunc__(method_obj, method_name, printDocs, printReturns) -> None:
    return_type = method_obj.__annotations__.get("return", "Any")
    docstring = method_obj.__doc__ if method_obj.__doc__ else "No documentation"

    if not printReturns and not printDocs:
        print(f"{INDENTATION}{method_name}()")
    else:
        doc_lines = docstring.split('\n')
        indented_doc = '\n'.join([f" {line}" for line in doc_lines])

        longest_line_length = max(len(line) for line in doc_lines)
        box_width = longest_line_length + 6
        box_line = INDENTATION*2 + "+" + "-" * (box_width - 2) + "+"

        print(f"{INDENTATION}{method_name}():")
        print(f"{INDENTATION*2}Returns: {return_type}")
        if printDocs:
            print(f"{INDENTATION*2}Documentation:")
            print(box_line)
            for line in indented_doc.split('\n'):
                print(f"{INDENTATION*2}| {line.ljust(box_width - 4)} |")
            print(box_line)

def print_obj(class_obj, showBoundMethods=True, printDocs=True, printReturns=True) -> None:
    """Prints the arguments of the object given for a better debugging experience

    Args:
        class_obj (any): Class object.
        showBoundMethods (bool, optional): Whether or not to show bound Methods. Defaults to True.
        printDocs (bool, optional): Whether or not to print documentations. Defaults to True.
        printReturns (bool, optional): Whether or not to print what type the function is returning. Defaults to True.
    """ 
    class_name = class_obj.__class__.__name__
    print(f"Class Name: {class_name}")
    
    print("Values:")
    for attr_name, attr_value in vars(class_obj).items():
        if not callable(attr_value):
            print(f"{INDENTATION}{attr_name}: {attr_value}")
    
    print("Functions:")
    for method_name, method_obj in vars(class_obj.__class__).items():
        if callable(method_obj):
            if showBoundMethods:
                __printFunc__(method_obj, method_name, printDocs, printReturns)
            else:
                if not method_name.startswith("__"):
                    __printFunc__(method_obj, method_name, printDocs, printReturns)
