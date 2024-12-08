from common import conn, cur, print_cmd

us = '''
* User Story

   As a: Common User
 I want: To create a new username
So That: I can customize my online persona
'''

print(us)

def change_username(user_id, new_username):
    try:
        # Check if the UserID exists
        tmpl_check_user = '''
        SELECT COUNT(*) FROM "User"
         WHERE UserID = %s;
        '''
        cur.execute(tmpl_check_user, (user_id,))
        user_exists = cur.fetchone()[0]

        if not user_exists:
            print(f"Error: UserID {user_id} does not exist.")
            return

        # Update the Username
        tmpl_update_username = '''
        UPDATE "User"
           SET Username = %s
         WHERE UserID = %s;
        '''
        cmd_update_username = cur.mogrify(tmpl_update_username, (new_username, user_id))
        print_cmd(cmd_update_username)
        cur.execute(cmd_update_username)

        conn.commit()
        print(f"Username for UserID {user_id} successfully updated to '{new_username}'.")
    except Exception as e:
        conn.rollback()
        print(f"Error updating username: {e}")

if __name__ == "__main__":
    try:
        user_id = int(input("Enter your User ID: "))
        new_username = input("Enter your new Username: ")
        change_username(user_id, new_username)
    except ValueError:
        print("Invalid input. Please enter a valid User ID.")
