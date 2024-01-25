def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Manjot Singh",
        "student_id": 10311115,
        "pizza_toppings": ["ONIONS", "PEPPERONI", "PEPPERS"],
        "movies": [
        {"title": "anchorman"}
        ],
    }
    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {"title": "anchorman", "genre": "comedy"}
    about_me =["movies"].append(new_movie)

    print_student_name_and_id(about_me)

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = (about_me["full_name"])
    first_name = full_name.split()[0]
    student_id = (about_me["student_id"])
    print(
        f"My name is {full_name}, but you can call me {first_name}./nMy student id is {student_id}."
    )
    return
   
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    add_pizza_toppings(about_me, ('ONION', 'PEPPERONI'))
    about_me['pizza_toppings'].extend(toppings)
    about_me['pizza_toppings'] = sorted(about_me['pizza_toppings'])
    about_me['pizza_toppings'] = [topping.lower() for topping in about_me['pizza_toppings']]
    return
      
# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print_pizza_toppings(about_me)
    print("My favourite pizza toppings are:")
    for topping in about_me['pizza_toppings']:
        print(f"- {topping.capitalize()}")
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie['genre'] for movie in about_me['movies']]
    print(f"I like to watch {', '.join(genres)} movies.")
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()