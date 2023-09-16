
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
    
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    
    def get_member(self, id):
        # fill this method and update the return
        # need a for loop to retreive a specific family member id to display
        for member in self._members:
            if member['id'] == int(id):
                return member
            return None

    def add_member(self, member):
        # fill this method and update the return
        id = self._generateId()
        member['id'] = id
        self._members.append(member)
        return None

    def delete_member(self, id): # have a tutor walk through how to check this and make sure it works alright
        # fill this method and update the return
        #for loop to find specific family member id to remove
        for member in self._members:
            if member['id'] == id:
                self._members.remove(member)
                return True
            return False

    