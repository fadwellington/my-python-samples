#pickling in python

import pickle


class pickleexample_class:
    a_number = 40
    a_string = "Hello"
    a_list = {1,2,3}
    a_dict = {"first":"a", "second":"2", "third": {1,2,3,}}
    a_tuple = (25,29)

my_object = pickleexample_class()
my_pickled_object = pickle.dumps(my_object)
print(f"This is my first pickled object:\n{my_pickled_object}\n")

my_object.a_dict=None
my_unpickled_object = pickle.loads(my_pickled_object)
print(
    f"a_dict -f unpickled object:\n{my_unpickled_object.a_dict}\n"
)
