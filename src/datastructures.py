
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if member.id:
            id_to_use = member.id
        else:
            id_to_use = self._generateId()
        new_member = {
            "id": id_to_use,
            "first_name": member.first_name,
            "last_name": self.last_name,
            "age": member.age,
            "lucky_numbers": member.lucky_numbers
        }
        self._members.append(new_member)


    def delete_member(self, id):
        found_item = list(filter(lambda x: x["id"] == id, self._members))
        self._members = list(filter(lambda x: x["id"] != id, self._members))
        print(found_item)
        return found_item


    def get_member(self, id):
        found_item = list(filter(lambda x: x["id"] == id, self._members))
        return found_item


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

