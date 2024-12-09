from common import conn, cur, print_cmd, show_table

us = '''
* User Story

   As a: Common User
 I want: To create a new username
So That: I can customize my online persona
'''

print(us)

def change_username(user_id, new_username):
    """
    Changes the username for a given user and displays the updated user details.
    """
    try:
        # Check if the user exists
        tmpl_check_user = '''
        SELECT COUNT(*) FROM "User"
         WHERE UserID = %s;
        '''
        cur.execute(tmpl_check_user, (user_id,))
        user_exists = cur.fetchone()[0]

        if not user_exists:
            print(f"Error: UserID {user_id} does not exist.")
            return

        # Update the username
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

        # Display the updated user details
        display_updated_user(user_id)

    except Exception as e:
        conn.rollback()
        print(f"Error updating username: {e}")


def display_updated_user(user_id):
    """
    Displays the updated user details from the 'User' table.
    """
    try:
        cols = 'UserID, Username, Email'

        tmpl = '''
        SELECT UserID, Username, email
          FROM "User"
         WHERE UserID = %s;
        '''
        cmd = cur.mogrify(tmpl, (user_id,))
        print_cmd(cmd)

        cur.execute(cmd)
        rows = cur.fetchall()

        if rows:
            print("\nUpdated User Details:")
            show_table(rows, cols)
        else:
            print(f"No details found for UserID {user_id}.")

    except Exception as e:
        print(f"Error displaying updated user details: {e}")


if __name__ == "__main__":
    try:
        user_id = int(input("Enter your User ID: "))
        new_username = input("Enter your new Username: ")
        change_username(user_id, new_username)
    except ValueError:
        print("Invalid input. Please enter a valid User ID.")
