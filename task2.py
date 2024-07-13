import turtle

def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
        return
    length /= 3.0
    koch_snowflake(t, length, level-1)
    t.left(60)
    koch_snowflake(t, length, level-1)
    t.right(120)
    koch_snowflake(t, length, level-1)
    t.left(60)
    koch_snowflake(t, length, level-1)

def draw_snowflake(t, length, level):
    for _ in range(3):
        koch_snowflake(t, length, level)
        t.right(120)

def main():
    t = turtle.Turtle()
    t.speed(5)
    t.hideturtle()
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    level = int(input("Ввведіть рівень рекурсії: "))

    draw_snowflake(t, 400, level)

    turtle.done()

if __name__ == "__main__":
    main()