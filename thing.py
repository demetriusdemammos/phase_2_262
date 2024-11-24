from common import conn, cur, print_cmd, show_table

us = '''
* User Story

   As a:  User
 I want:  To view the number of messages I’ve sent in each channel
So That:  I can understand my activity across channels
'''

print(us)

def show_user_message_count_per_channel(user_id):
    try:
        cols = 'c.ChannelID c.ChannelName MessageCount'

        tmpl = f'''
        SELECT c.ChannelID, c.Channelname, COUNT(cm.Message) AS MessageCount
          FROM Channel AS c
               LEFT JOIN Channel_Message AS cm ON c.ChannelID = cm.ChannelID
         WHERE cm.UserID = %s
         GROUP BY c.ChannelID, c.Channelname
         ORDER BY c.ChannelID;
        '''

        # Format the query with the user_id
        cmd = cur.mogrify(tmpl, (user_id,))
        print_cmd(cmd)

        # Execute the query
        cur.execute(cmd)

        # Fetch results
        rows = cur.fetchall()

        # Display the results
        show_table(rows, cols)
    except Exception as e:
        print(f"Error retrieving message count: {e}")

# Test the function
if __name__ == "__main__":
    try:
        user_id = int(input("Enter the user ID to view their message count per channel: "))
        show_user_message_count_per_channel(user_id)
    except ValueError:
        print("Invalid input. Please enter a numerical user ID.")
