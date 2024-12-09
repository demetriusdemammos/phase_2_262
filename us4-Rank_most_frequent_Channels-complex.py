from common import conn, cur, print_cmd, show_table

us = '''
* User Story

   As a:  User
 I want:  To view the channels with most messages sent
So That:  I can identify my messaging pattern and get easier access to the familiar channels
'''

print(us)


def show_user_most_message_count_channel(user_id):
    """
    Displays the channels where the user has sent the most messages.
    """
    try:

        cols = 'ChannelID, ChannelName, MessageCount'


        tmpl = '''
        WITH MessageCounts AS (
            SELECT c.ChannelID, c.Channelname, COUNT(cm.Message) AS MessageCount
              FROM Channel AS c
                   LEFT JOIN Channel_Message AS cm ON c.ChannelID = cm.ChannelID
             WHERE cm.UserID = %s
             GROUP BY c.ChannelID, c.Channelname
        )
        SELECT ChannelID, Channelname, MessageCount
          FROM MessageCounts
         WHERE MessageCount = (SELECT MAX(MessageCount) FROM MessageCounts)
         ORDER BY ChannelID;
        '''


        cmd = cur.mogrify(tmpl, (user_id,))
        print_cmd(cmd)

        
        cur.execute(cmd)


        rows = cur.fetchall()

        if rows:
 
            show_table(rows, cols)
        else:
            print(f"No messages found for UserID {user_id}.")
    except Exception as e:
        print(f"Error retrieving message count: {e}")

if __name__ == "__main__":
    try:
        user_id = int(input("Enter the User ID to view the channels with the most messages sent: "))
        show_user_most_message_count_channel(user_id)
    except ValueError:
        print("Invalid input. Please enter a numerical User ID.")
