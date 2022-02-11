
try:
    file= open("a_file.txt")
    a_dict={"key":"value"}
    print(a_dict["key"])
except FileNotFoundError:
    file=open("a_file.txt","w")
except KeyError as error_message:
    print(f"The key {error_message} does not exists")
else:
    content=file.read()
    print(content)

finally:
    file.close()
    print("File was closed.")
    raise TypeError("This is an error I made up")
