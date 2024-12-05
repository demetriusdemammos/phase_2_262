from common import conn, cur, print_cmd, show_table

us = '''
* User Story

   As a:  User
 I want:  To view the channels with most messages sent
So That:  I can identify my messaging pattern and get easier access to the familiar channels

'''

print(us)

def show_user_most_message_count_channel(user_id):
    try:
        cols = 'c.ChannelID c.ChannelName MessageCount'

        tmpl = f'''
        SELECT c.ChannelID, c.Channelname, COUNT(cm.Message) AS MessageCount
          FROM Channel AS c
               LEFT JOIN Channel_Message AS cm ON c.ChannelID = cm.ChannelID
         WHERE cm.UserID = %s
         GROUP BY c.ChannelID, c.Channelname
         HAVING MessageCount=(SELECT COUNT(cm2.Message)
                                FROM Channel_Message AS cm2
                               WHERE cm2.UserID=cm.UserID
                               ORDER BY COUNT(cm2.Message)
                               LIMIT 1
                               )
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
        user_id = int(input("Enter the user ID to view the channel with most message: "))
        show_user_most_message_count_channel(user_id)
    except ValueError:
        print("Invalid input. Please enter a numerical user ID.")#US4-Rank_most_frequent_Channels-complex-analytical
