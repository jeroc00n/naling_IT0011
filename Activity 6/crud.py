class Game:
    def __init__(self, game_id, name, description, price):
        self.id = game_id
        self.name = name
        self.description = description
        self.price = price
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: Php {self.price:.2f}"

class GameManager:
    def __init__(self):
        self.games = []
        
    def create_game(self, game_id, name, description, price):
        if not isinstance(game_id, int) or game_id <= 0:
            raise ValueError("ID must be a positive integer.")
        if not name or not isinstance(name, str):
            raise ValueError("Name must a string that is not empty.")
        if not description or not isinstance(description, str):
            raise ValueError("Description must be a string that is not empty.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        
        if any(game.id == game_id for game in self.games):
            raise ValueError("A game with this ID already exists.")
        
        new_game = Game(game_id, name, description, price)
        self.games.append(new_game)
        print("Game created successfully!")
    
    def read_games(self):
        if not self.games:
            print("No games found.")
        else:
            for game in self.games:
                print(game)
    
    def update_game(self, game_id, name=None, description=None, price=None):
        game = next((game for game in self.games if game.id == game_id), None)
        if not game:
            raise ValueError("Game not found.")
        
        if name is not None:
            if not name or not isinstance(name, str):
                raise ValueError("Name must not be an empty string.")
            game.name = name
        if description is not None:
            if not description or not isinstance(description, str):
                raise ValueError("Description must not be an empty string.")
            game.description = description
        if price is not None:
            if not isinstance(price, (int, float)) or price <= 0:
                raise ValueError("Price must be a positive number.")
            game.price = price
        
        print("Game updated successfully.")
        
    def delete_game(self, game_id):
        game = next((game for game in self.games if game.id == game_id), None)
        if not game:
            raise ValueError("Game not found.")
        self.games.remove(game)
        print("Game deleted successfully.")
        
def menu():
        print("\n---Game Management System ---")
        print("[C] - Create Item")
        print("[R] - Read Items")
        print("[U] - Update Item")
        print("[D] - Delete Item")
        print("[Q] - Quit")

def main():
    manager = GameManager()
    
    while True:
        menu()
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'Q':
            print("Exiting... Thank you for using the program!")
            break
        
        try:
            if choice == 'C':
                game_id = int(input("Enter game ID: "))
                name = input("Enter game name: ")
                description = input("Enter game description: ")
                price = float(input("Enter game price: "))
                if price <= 0:
                    print("Error: Price must be a positive number.")
                    continue
                manager.create_game(game_id, name, description, price)
            
            elif choice == 'R':
                manager.read_games()
            
            elif choice == 'U':
                game_id = int(input("Enter game ID to update: "))
                name = input("Enter new name (leave blank to skip): ") or None
                description = input("Enter new description (leave blank to skip): ") or None
                price = None
                price_input = input("Enter new price (leave blank to skip): ")
                if price_input:
                    price = float(price_input)
                    if price <= 0:
                        print("Error: Price must be a positive number.")
                        continue
                manager.update_game(game_id, name, description, price)
                
            elif choice == 'D':
                game_id = int(input("Enter game ID to delete: "))
                manager.delete_game(game_id)
            
            else:
                print("Invalid choice. Please only choose between: C, R, U, D, or Q.")
        
        except ValueError as e:
            print("Error: ", e)
        except Exception as e:
            print("An unexpected error occurred: ", e)

main()

    
    