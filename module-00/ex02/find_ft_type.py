def all_thing_is_obj(object: any) -> int:
    type_of_obj = str(type(object)).split("'")[1]
    if (type_of_obj == "str"):
        print(f"Brian is in the kitchen : {type(object)}")
    elif (type_of_obj == "int"):
        print("Type not found")
    else:
        print(f"{type_of_obj.capitalize()} : {type(object)}")
    return 42
