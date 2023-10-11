
from prettytable import PrettyTable
from turtle import Turtle, Screen


# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)

# my_screen = Screen()
# my_screen.canvheight
# print(my_screen.canvheight)
# my_screen.exitonclick()


table = PrettyTable()

# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Eletric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])

table.align = "l"

print(table)
