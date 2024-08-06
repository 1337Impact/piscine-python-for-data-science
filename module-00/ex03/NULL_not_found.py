def NULL_not_found(object: any) -> int:
    if object and object == object:
        print("Type not Found")
        return 1
    type_of_obj = str(type(object)).split("'")[1]
    title = ""
    if type_of_obj == "NoneType":
        title = "Nothing"
    elif type_of_obj == "float":
        title = "Cheese"
    elif type_of_obj == "int":
        title = "Zero"
    elif type_of_obj == "str":
        title = "Empty"
    elif type_of_obj == "bool":
        title = "Fake"
    print(f"{title}: {object} {type(object)}")
    return 0
