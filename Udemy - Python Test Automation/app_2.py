blogs = dict() #blog_name : Blog object
POST_TEMPLATE = '''
    --- {} ---
    
    '''


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def ask_create_blog():
    title = input('Enter your blog title: ')
    author = input('Enter your name: ')

    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input('Enter the blog title you want to read: ')
    print_post(blogs[title])

def print_post(post):
    print(POST_TEMPLATE)

def print_blogs():
    for key, blog in blogs.items():
        # print the available blogs
        print(f'-{blog}!')