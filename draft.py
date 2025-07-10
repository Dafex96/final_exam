
quantity = 0
name = ""
year = ""

def save(movie):
    quantity = int(input("Insert how many movies do you want to add: "))
    for i in range(1,quantity+1):
        print(f"-----------Save {i} Movie--------------")
        name = input("Insert the movie name: ").lower()
        year = int(input("Insert the year of release: "))
        
        movie.append({
            "name": name,
            "year": year
        })
