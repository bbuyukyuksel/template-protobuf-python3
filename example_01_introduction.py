'''
[Tags]
The " = 1", " = 2" markers on each element identify the unique "tag" that field uses in the binary encoding. 
Tag numbers 1-15 require one less byte to encode than higher numbers, 
so as an optimization you can decide to use those tags for the commonly used or repeated elements, 
leaving tags 16 and higher for less-commonly used optional elements. 

Each element in a repeated field requires re-encoding the tag number, 
so repeated fields are particularly good candidates for this optimization.

[Modifiers]
Each field must be annotated with one of the following modifiers:

optional: the field may or may not be set. If an optional field value isn't set, a default value is used. For simple types, you can specify your own default value, as we've done for the phone number type in the example. Otherwise, a system default is used: zero for numeric types, the empty string for strings, false for bools. For embedded messages, the default value is always the "default instance" or "prototype" of the message, which has none of its fields set. Calling the accessor to get the value of an optional (or required) field which has not been explicitly set always returns that field's default value.
repeated: the field may be repeated any number of times (including zero). The order of the repeated values will be preserved in the protocol buffer. Think of repeated fields as dynamically sized arrays.
required: a value for the field must be provided, otherwise the message will be considered "uninitialized". Serializing an uninitialized message will raise an exception. Parsing an uninitialized message will fail. Other than this, a required field behaves exactly like an optional field.


[TYPES]
bool, int32, float, double, and string
'''

import sys
sys.path.append("build")

import addressbook_pb2

person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"

phone = person.phones.add()

phone.number = "555-4321"
phone.type = addressbook_pb2.Person.PhoneType.HOME

print(addressbook_pb2.Person.PhoneType.WORK) #has the value 2.

phone = person.phones.add()
phone.number = "555-4322"
phone.type = addressbook_pb2.Person.HOME

# Clear Fields
person.phones[-1].Clear()
# Delete
del person.phones[-1]


'''
person.no_such_field = 1  # raises AttributeError
person.id = "1234"        # raises TypeError
'''

print(person)
print(person.IsInitialized())
print(person.HasField("name"))

## Serialize
serialized = person.SerializeToString()

## De-Serialize
myperson = addressbook_pb2.Person()
myperson.ParseFromString(serialized)


