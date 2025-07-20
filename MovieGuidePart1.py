# Jeffrey Brandt
# CIS261
# Movie Guide Part 1

def display_menu():
    print("Movie Guide")
    print("-----------")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()

def initialize_movies():
    return["The Matrix", "Inception", "Interstellar"]

def list_movies(movie_list):
    for i, title in enumerate(movie_list, start = 1):
        print(f"{i}. {title}")
    print()

def add_movie(movie_list):
    title = input("Enter movie title: ").strip()
    if title == "":
        print("Movie title cannot be empty.\n")
        return
    if title in movie_list:
        print(f'"{title}" is already in the list.\n')
        return
    movie_list.append(title)
    print(f'"{title}" was added.\n')
    list_movies(movie_list)

def delete_movie(movie_list):
    try:
        index = int(input("Enter movie number to delete: "))
        if 1 <= index <= len(movie_list):
            removed = movie_list.pop(index - 1)
            print(f'"{removed}" was deleted.\n')
        else:
            print("Invalid movie number.\n")
    except ValueError:
        print("Please enter a valid number.\n")
    list_movies(movie_list)

def main():
    movies = initialize_movies()
    display_menu()
   
    while True:
        command = input("Command: ").strip().lower()
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.\n")

if __name__ == "__main__":
    main()