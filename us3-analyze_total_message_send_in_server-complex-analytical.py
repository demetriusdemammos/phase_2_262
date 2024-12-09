from common import conn, cur, print_cmd, show_table


MESSAGE_THRESHOLD = 2 

us = '''
* User Story

   As a:  Server owner
 I want:  Analyze total amount of messages sent by users in the server
So That:  Identify active and inactive users and reward and punish correspondingly
'''

print(us)


def trigger_update_user_role(user_id):
    """
    Simulates a SQL trigger function: Updates the user's role in the Common_User table
    after a new message is inserted into the Channel_Message table.
    """
    try:

        tmpl_count = '''
        SELECT cm.UserID, COUNT(cm.Message) AS MessageCount
          FROM Channel_Message AS cm
         WHERE cm.UserID = %s
         GROUP BY cm.UserID;
        '''
        cmd_count = cur.mogrify(tmpl_count, (user_id,))
        print_cmd(cmd_count)


        cur.execute(cmd_count)
        rows = cur.fetchall()


        message_count = rows[0][1] if rows else 0

        if message_count > MESSAGE_THRESHOLD:
            new_role = 'moderator'
        elif message_count == MESSAGE_THRESHOLD:
            new_role = 'regular'
        else:
            new_role = 'inactive'

        tmpl_update = '''
        UPDATE Common_User
           SET Role = %s
         WHERE UserID = %s;
        '''
        cmd_update = cur.mogrify(tmpl_update, (new_role, user_id))
        print_cmd(cmd_update)

        cur.execute(cmd_update)

        conn.commit()

        print(f"User role updated for UserID {user_id} to {new_role}")

    except Exception as e:
        conn.rollback()
        print(f"Error in trigger simulation: {e}")


def insert_message_with_trigger(message, time, user_id, channel_id):
    """
    Inserts a message into the Channel_Message table and invokes the simulated trigger
    to update user roles.
    """
    try:
        tmpl_insert = '''
        INSERT INTO Channel_Message (Message, Time, UserID, ChannelID)
        VALUES (%s, %s, %s, %s);
        '''
        cmd_insert = cur.mogrify(tmpl_insert, (message, time, user_id, channel_id))
        print_cmd(cmd_insert)
        cur.execute(cmd_insert)
        conn.commit()

        print(f"Message inserted successfully for UserID {user_id}")

        trigger_update_user_role(user_id)

    except Exception as e:
        conn.rollback()
        print(f"Error inserting message with trigger: {e}")


if __name__ == "__main__":
    try:
        message = input("Enter the Message: ").strip()
        time = input("Enter the Time (YYYY-MM-DD HH:MM:SS): ").strip()
        channel_id = int(input("Enter the Channel ID: ").strip())
        user_id = int(input("Enter the User ID: ").strip())

        insert_message_with_trigger(message, time, user_id, channel_id)

    except ValueError as e:
        print(f"Invalid input: {e}. Please enter the correct data types.")
