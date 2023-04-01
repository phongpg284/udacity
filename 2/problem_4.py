class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_users_list(user, users_list):
    for user_name in users_list:
        if user == user_name:
            return True
    return False 

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if is_user_in_users_list(user, group.get_users()) is True:
        return True
    else:
        for child_group in group.get_groups():
            if is_user_in_group(user, child_group) == True:
                return True
    return None

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print (is_user_in_group(sub_child_user, parent))
'''
True
'''

# Test Case 2
not_in_group_user = "not_in_group_user"
print (is_user_in_group(not_in_group_user, parent))
'''
None
'''

# Test Case 3

print (is_user_in_group("", parent))
'''
None
'''
