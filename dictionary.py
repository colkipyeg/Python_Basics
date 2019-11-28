from typing import Dict

my_dict={
    1:'Orange',
    2:'Bananas',
    3:'apples'
}

vr=my_dict[2]
print(vr)

details={
    "name":"Collins",
    "age" : "25",
    "married":"True",

}
a=[details]
print("age")

details3={
"name":"Collins",
    "dislikes":["lazy","broke"],
    "parents":{
        "mother":"alice",
        "father":"dad",
    }
}
h=details3["dislikes"]
print(h)



taskList = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]
print(type(taskList))
print(taskList[2][2]["currency"])
print(taskList[2][1])
print(len(taskList))

