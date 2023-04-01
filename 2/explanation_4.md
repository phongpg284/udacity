We create some function to check if user is showing in user list of a group.
After that we create one recursion loop through all sub groups with any level beneath input group to find user.
Time complexity for worst case is O(n) where we need to loop through all exist groups and users.

----------------------------------------------------------------------

Space complexity will be O(n) given n is number of both users and groups. Cause no other data need to be stored.
