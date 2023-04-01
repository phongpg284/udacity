In this problem we just need one recursion function take `path`, `suffix` and `result` list: 
- check if current path is directoris or files
- if files, check if matching suffix 
- if directories, recursion to check all its child path

Time complexity is O(n) for n is files and folders input since we iterate through all file and folders for worst case.

----------------------------------------------------------------

Space complexity will be O(n) given n is number of directories and files
