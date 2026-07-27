# hero.py 

class Hero:

    def __init__(self, name, starting_health=100):
        '''Instance properties:
        name: String 
        starting_health: Integer

        current_health: Integer
        '''

        self.name = name

        self.starting_health = starting_health

        self.current_health = starting_health

# Call the class to create an instance 
hero = Hero("Starfire", 100)

if __name__ == "__main__":

    my_hero = Hero("Starfire", 100)
    print(my_hero.name)  # Output: Starfire
    print(my_hero.current_health)  # Output: 100

    def battle(self, opponent):
        ''' Current hero will take turns fighting the opponent hero passed in.
        '''
        # fight each hero until there is a winner
        # phases to implement:
        #1 ) randomly choose a winner, print the name of the winner
        #hint: look into random library, more specifically the choice method

    class Hero:
        def __init__(self, name, health, attack_power, defense_power):
            self.name = name
            self.health = health
            self.max_damage = attack_power
            self.max_block = defense_power
            self.armor = []
            self.abilities = []

            def add_ability(self, ability):
                ''' Add ability to abilities list '''
                self.abilities.append(ability)
                print(f"{self.name} has gained the ability: {ability.name}")

                # lightning = Ability("Lightning Strike", 50)
                # starfire.add_ability(lightning)