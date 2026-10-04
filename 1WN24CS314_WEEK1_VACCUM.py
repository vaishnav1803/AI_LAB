import time

class VacuumAgent:
    def __init__(self):
        self.goal = {"Room A": "Clean", "Room B": "Clean"}

    def perceive_and_act(self, current_room, current_status, other_room, other_status):
        world_state = {current_room: current_status, other_room: other_status}
        if world_state == self.goal:
            return "STOP"

        if current_status == "Dirty":
            return "SUCK DIRT"
        else:
            return "MOVE"

class Environment:
    def __init__(self):
        self.rooms = {"Room A": "Dirty", "Room B": "Dirty"}
        self.agent_location = "Room A"

    def get_other_room(self):
        return "Room B" if self.agent_location == "Room A" else "Room A"

    def run_simulation(self):
        agent = VacuumAgent()
        steps = 0
        active = True

        print(f"Initial State: Room A = {self.rooms['Room A']}, Room B = {self.rooms['Room B']}")
        print(f"Target Goal State: Room A = Clean, Room B = Clean\n")

        while active:
            other_room = self.get_other_room()
            current_status = self.rooms[self.agent_location]
            other_status = self.rooms[other_room]

            steps += 1
            print(f"Step {steps} | Location: {self.agent_location} | Status: A={self.rooms['Room A']}, B={self.rooms['Room B']}")

            action = agent.perceive_and_act(self.agent_location, current_status, other_room, other_status)
            print(f"   Action Chosen: {action}")

            if action == "SUCK DIRT":
                self.rooms[self.agent_location] = "Clean"
            elif action == "MOVE":
                self.agent_location = other_room
            elif action == "STOP":
                print("\nGoal Reached! ")
                active = False

            time.sleep(0.4)

if __name__ == "__main__":
    env = Environment()
    env.run_simulation()
