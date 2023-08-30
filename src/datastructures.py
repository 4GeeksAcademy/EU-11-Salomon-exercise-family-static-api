class Family:
    def __init__(self):
        self.family = []

    def initialize_with_initial_members(self):
        self.family = [
            {"first_name": "John", "id": 1, "age": 35, "lucky_numbers": [7, 13, 22]},
            {"first_name": "Jane", "id": 2, "age": 32, "lucky_numbers": [3, 9, 17]},
            {"first_name": "Tom", "id": 3, "age": 5, "lucky_numbers": [1]}
        ]

    def get_all_members(self):
        return self.family

    def add_member(self, member):
        self.family.append(member)

    def get_member_by_id(self, id):
        for member in self.family:
            if member["id"] == id:
                return member
        return None

    def delete_member(self, id):
        initial_length = len(self.family)
        self.family = [member for member in self.family if member["id"] != id]
        return len(self.family) < initial_length