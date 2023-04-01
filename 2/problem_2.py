import os

def find_files(suffix, path):
    result = []
    get_file_match_suffix(result, path, suffix)
    return result

def get_file_match_suffix(result, path, suffix):
    if os.path.exists(path):
        root_dir = get_list_dir(path)
        for item in root_dir:
            new_child_path = join_path(path, item)

            if is_dir(new_child_path):
                get_file_match_suffix(result, new_child_path, suffix)

            elif is_file(new_child_path):
                if is_match_suffix(new_child_path, suffix):
                    result.append(new_child_path)
                    return

def is_dir(path):
    return os.path.isdir(path)

def is_file(path):
    return os.path.isfile(path)

def is_match_suffix(path, suffix):
    return path.endswith(suffix)

def get_list_dir(path):
    return os.listdir(path)

def join_path(path, after_path):
    return os.path.join(path, after_path)

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
# Test Case 1

print(find_files(".c", "./testdir/subdir1"))
'''
['./testdir/subdir1\\a.c']
'''

# Test Case 2

print(find_files(".c", ""))
'''
[]
'''

# Test Case 3

print(find_files(".c", "./not_exist_folder"))
'''
[]
'''
