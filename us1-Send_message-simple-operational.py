from common import conn, cur, print_cmd, show_table

us = '''
* User Story

   As a:  User
 I want:  Send a message
So That:  Communicate with my friend
'''

print(us)
def 
def show_user_message(MessageID):
    try:
        cols = 'm.MessageID m.Sent_From m.Sent_To m.message'

        tmpl = f'''
        SELECT m.MessageID, m.Sent_From, m.Sent_To, m.message
          FROM Channel AS c
         WHERE m.MessageID = %s
         ORDER BY m.MessageID;
        '''

        # Format the query with the MessageID
        cmd = cur.mogrify(tmpl, (MessageID,))
        print_cmd(cmd)

        # Execute the query
        cur.execute(cmd)

        # Fetch results
        rows = cur.fetchall()

        # Display the results
        show_table(rows, cols)
    except Exception as e:
        print(f"Error retrieving message: {e}")

# Test the function
if __name__ == "__main__":
    try:
        MessageID = int(input("Enter the Message ID to view the message: "))
        show_user_message_count_per_channel(user_id)
    except ValueError:
        print("Invalid input. Please enter a numerical user ID.")
