from common import conn, cur, print_cmd

us = '''
* User Story

   As an: Admin
 I want: To remove participants from a server
So That: I can manage users who no longer belong to the server
'''

print(us)

def remove_user_from_server(user_id, server_id):
    try:

        tmpl1 = '''
        DELETE FROM Channel_Message
         WHERE UserID = %s
           AND ChannelID IN (
               SELECT ChannelID
                 FROM Channel
                WHERE ServerID = %s
           );
        '''
        cmd1 = cur.mogrify(tmpl1, (user_id, server_id))
        print_cmd(cmd1)
        cur.execute(cmd1)


        tmpl2 = '''
        DELETE FROM User_Server
         WHERE UserID = %s
           AND ServerID = %s;
        '''
        cmd2 = cur.mogrify(tmpl2, (user_id, server_id))
        print_cmd(cmd2)
        cur.execute(cmd2)


        conn.commit()
        print(f"User {user_id} successfully removed from server {server_id}, and their messages deleted.")
    except Exception as e:
     
        conn.rollback()
        print(f"Error removing user: {e}")

if __name__ == "__main__":
    try:
        user_id = int(input("Enter the user ID to remove: "))
        server_id = int(input("Enter the server ID from which to remove the user: "))
        remove_user_from_server(user_id, server_id)
    except ValueError:
        print("Invalid input. Please enter numerical values for UserID and ServerID.")
