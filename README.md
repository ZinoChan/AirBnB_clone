# The AirBnB Clone Console :house_with_garden: :star2:

Welcome to our exciting Python project! This project is all about creating a custom console or a command line interpreter for managing a system of data. It's part of a larger system where we deal with instances of different classes representing various types of data and manipulate their persistence.

## The Command Interpreter :computer:
The command interpreter we're creating is designed to manage objects of various types, providing commands to create new objects, manage existing ones, retrieve information about them, and more. It's designed in a user-friendly manner, following a simple syntax and providing informative feedback.

## How to start :rocket:
To start the console, navigate to the project directory in your terminal and run the console file (let's call it console.py). Like this:
```
$ ./console.py
```
## How to use :bulb:
When you're inside our custom console, you can start executing commands. The syntax is straightforward, making it easy to interact with the system:

1. `create <class name>` - Creates a new instance of <class name>, saves it to a JSON file, and prints its id.
2. `show <class name> <id>` - Prints the string representation of an instance based on the class name and id.
3. `destroy <class name> <id>` - Deletes an instance based on the class name and id.
4. `all <class name>` or just all - Prints all instances of a class, or if no class is specified, all instances of all classes.
5. `update <class name> <id> <attribute name> "<attribute value>"` - Updates an instance based on the class name and id by adding or updating an attribute.

## Examples :eyes:
Here are some examples of how you can use the commands:

```
(hbnb) create User
246c227a-d5c1-403d-9bc7-6a47bb9f0f68
(hbnb) show User 246c227a-d5c1-403d-9bc7-6a47bb9f0f68
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'created_at': '2023-07-14T22:31:03.879122', 'updated_at': '2023-07-14T22:31:03.879153'}
(hbnb) update User 246c227a-d5c1-403d-9bc7-6a47bb9f0f68 first_name "Alex"
(hbnb) all User
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'created_at': '2023-07-14T22:31:03.879122', 'updated_at': '2023-07-14T22:31:03.879153', 'first_name': 'Alex'}
```
## Contributors :sparkles:
The list of contributors can be found in the [`AUTHORS`](./AUTHORS) file.
