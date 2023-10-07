def dictionary_assign_in_list(file_name):
    keyword = []

    try:
        with open(file_name, 'r') as file:
            keyword = [k.strip() for k in file]
    except FileNotFoundError:
        print('Error : Your dictionary not found!!!')
        
    
    print(keyword)
    return keyword