import tkinter as tk
import random

# Konfigurace hry
WIDTH = 600
HEIGHT = 400
GRID_SIZE = 20
DELAY = 100  # Rychlost hry v ms

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hra Had - Zmenšování")
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # Had začíná s 10 články
        self.snake = [(100 + i * GRID_SIZE, 100) for i in range(10)][::-1]
        self.direction = "Right"
        self.food = None
        
        self.info_label = self.canvas.create_text(
            80, 15, text=f"Článků k odstranění: {len(self.snake) - 1}", fill="white", font=("Arial", 12)
        )

        self.root.bind("<KeyPress>", self.change_direction)
        
        self.spawn_food()
        self.play()

    def spawn_food(self):
        while True:
            x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            self.food = (x, y)
            if self.food not in self.snake:
                break
        
        self.canvas.delete("food")
        self.canvas.create_rectangle(
            x, y, x + GRID_SIZE, y + GRID_SIZE, fill="red", tags="food"
        )

    def change_direction(self, event):
        new_dir = event.keysym
        all_dirs = {"Up", "Down", "Left", "Right"}
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        
        if new_dir in all_dirs and new_dir != opposites.get(self.direction):
            self.direction = new_dir

    def move_snake(self):
        head_x, head_y = self.snake[0]
        
        if self.direction == "Up":
            head_y -= GRID_SIZE
        elif self.direction == "Down":
            head_y += GRID_SIZE
        elif self.direction == "Left":
            head_x -= GRID_SIZE
        elif self.direction == "Right":
            head_x += GRID_SIZE
            
        new_head = (head_x, head_y)
        
        # Kontrola kolize se stěnami nebo tělem (kromě ocasu, který se posouvá)
        if (head_x < 0 or head_x >= WIDTH or 
            head_y < 0 or head_y >= HEIGHT or 
            new_head in self.snake[:-1]):
            self.end_game("PROHRA!", "red")
            return False

        self.snake.insert(0, new_head)
        
        # Kontrola kolize s jídlem
        if new_head == self.food:
            # Snědení jídla -> celkové zkrácení o 1 článek.
            # Musíme odebrat 2 články, protože jeden (hlava) byl přidán.
            for _ in range(2):
                if len(self.snake) > 1:
                    self.snake.pop()
            
            self.canvas.itemconfig(self.info_label, text=f"Článků k odstranění: {len(self.snake) - 1}")
            
            if len(self.snake) <= 1:
                self.draw_snake()
                self.end_game("VÍTĚZSTVÍ!", "gold")
                return False
                
            self.spawn_food()
        else:
            # Klasický pohyb (délka se nemění)
            self.snake.pop()
            
        return True

    def draw_snake(self):
        self.canvas.delete("snake")
        for i, (x, y) in enumerate(self.snake):
            color = "green" if i > 0 else "darkgreen"
            self.canvas.create_rectangle(
                x, y, x + GRID_SIZE, y + GRID_SIZE, fill=color, tags="snake"
            )

    def end_game(self, message, color):
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2, 
            text=message, fill=color, font=("Arial", 35, "bold")
        )

    def play(self):
        if self.move_snake():
            self.draw_snake()
            self.root.after(DELAY, self.play)

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
