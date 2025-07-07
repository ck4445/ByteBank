import scratchattach as sa


import my_secrets  # This imports USERNAME and PASSWORD

session = sa.login(my_secrets.USERNAME, my_secrets.PASSWORD)





project = session.connect_project("1188783204")

def get_comment_id(user, message):
    comments = project.comments(limit=40)
    
    class CommentInfo:
        def __init__(self):
            self.content = "n/a"
            self.id = "n/a"

    info = CommentInfo()

    for comment in comments:
        # If comment.author is callable, call it to get the user object
        author = comment.author
        if callable(author):
            author = author()

        if author.username == user and comment.content.strip() == message.strip():
            info.content = comment.content
            info.id = comment.id
            break  # stop once found

    return info



def get_content(id):
    
    if not id == "n/a":
        try:
            return(project.comment_by_id(id).content) #Finds the comment and returns it as as sa.Comment object
        except:
            return "Taken Down"
    else:
        return("n/a")
    
    
comment_info = get_comment_id("wvzack", "hi")
print(comment_info.id)
print(get_content(comment_info.id))