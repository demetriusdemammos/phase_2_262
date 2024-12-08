from common import conn, cur, print_cmd, show_table

us = '''
* User Story

   As a:  Sevver owner
 I want:  Analyze total amount of messages sent by users in the server
So That:  Identify active and inactive users and reward and punish correspondingly

'''

print(us)


def trigger_update_user_role(UserID):
    """
    Simulates a SQL trigger function: Updates the user's role in the Common_User table
    after a new message is inserted into the Channel_Message table.
    """
    try:
        cols = 'cm.UserID, COUNT(cm.Message) AS MessageCount'

        # SQL query to count messages for the user
        tmpl_count = '''
        SELECT cm.UserID, COUNT(cm.Message) AS MessageCount
          FROM Channel_Message AS cm
         WHERE cm.UserID = %s
         GROUP BY cm.UserID;
        '''

        cmd_count = cur.mogrify(tmpl_count, (UserID,))
        print_cmd(cmd_count)

        # Execute the count query
        cur.execute(cmd_count)
        rows = cur.fetchall()

        # Determine message count
        message_count = rows[0][1] if rows else 0

        # Decide the role based on message count
        if message_count > 5:
            new_role = 'moderator'
        elif message_count < 2:
            new_role = 'regular'
        else:
            new_role = 'regular'

        # SQL query to update the role
        tmpl_update = '''
        UPDATE Common_User
           SET Role = %s
         WHERE UserID = %s;
        '''

        cmd_update = cur.mogrify(tmpl_update, (new_role, UserID))
        print_cmd(cmd_update)

        # Execute the update role query
        cur.execute(cmd_update)

        # Commit the changes
        conn.commit()

        print(f"User role updated for UserID {UserID} to {new_role}")

    except Exception as e:
        # Roll back the transaction in case of error
        conn.rollback()
        print(f"Error in trigger simulation: {e}")
def insert_message_with_trigger(Message, Time, UserID, ChannelID):
    """
    Inserts a message into the Channel_Message table and invokes the simulated trigger
    to update user roles.
    """
    try:
        cols = 'cm.Message, cm.Time, cm.UserID, cm.ChannelID'

        # SQL query to insert the message
        tmpl_insert = '''
        INSERT INTO Channel_Message (Message, Time, UserID, ChannelID)
        VALUES (%s, %s, %s, %s);
        '''

        cmd_insert = cur.mogrify(tmpl_insert, (Message, Time, UserID, ChannelID))
        print_cmd(cmd_insert)

        # Execute the insertion
        cur.execute(cmd_insert)

        # Commit the insertion
        conn.commit()

        print(f"Message inserted successfully for UserID {UserID}")

        # Call the simulated trigger function
        trigger_update_user_role(UserID)

    except Exception as e:
        # Roll back in case of an error
        conn.rollback()
        print(f"Error inserting message with trigger: {e}")
# Test the function
if __name__ == "__main__":
    try:
        Message = int(input("Enter the Message: "))
        Time=timestamp(input("Enter the Time:"))
        ChannelID= int(input("Enter the Channel ID: "))
        UserID= int(input("Enter the User ID"))
    except ValueError:
        print("Invalid input. Please enter a numerical user ID.")#US4-Rank_most_frequent_Channels-complex-analytical
