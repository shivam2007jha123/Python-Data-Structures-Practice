student_info={
    "name":"sohan",
    "age":20,
    "course":"Computer Science",
    "city":"New York"
}
print(student_info)
student_info["birth place"]="pune"   #explain : this create a new key-value pair in the dictionary with the key "birth place" and the value "pune". If the key already exists, it will update the value associated with that key. In this case, since "birth place" is a new key, it adds it to the dictionary.
print(student_info)
#explain it update the value of the key "age" to 19 in the student_info dictionary. The update() method is used to modify existing key-value pairs or add new ones. In this case, it changes the age from 20 to 19.
student_info.update({"age":19})
print(student_info) 
del student_info["city"]  #explain : this line removes the key-value pair with the key "city" from the student_info dictionary. The del statement is used to delete items from a dictionary. After this operation, the "city" key and its associated value will no longer be present in the dictionary.
print(student_info)
print(student_info.items())


