from common import conn, cur, print_cmd, show_table

us = '''
* User Story

   As a:  User
 I want:  To see the number of users who have posted in a channel since a specific date
So That:  I can understand channel activity and engagement
'''

print(us)

def show_unique_users_since_date(channel_id, since_date):
    try:
        # Define the columns for the output
        cols = 'ChannelID ChannelName UniqueUserCount'

        # SQL template
        tmpl = f'''
        SELECT c.ChannelID, c.Channelname, COUNT(DISTINCT cm.UserID) AS UniqueUserCount
          FROM Channel AS c
               LEFT JOIN Channel_Message AS cm ON c.ChannelID = cm.ChannelID
         WHERE c.ChannelID = %s AND cm.Time >= %s
         GROUP BY c.ChannelID, c.Channelname
         ORDER BY c.ChannelID;
        '''

        # Format the query with the user inputs
        cmd = cur.mogrify(tmpl, (channel_id, since_date))
        print_cmd(cmd)

        # Execute the query
        cur.execute(cmd)

        # Fetch results
        rows = cur.fetchall()

        # Display the results
        show_table(rows, cols)
    except Exception as e:
        print(f"Error retrieving user count: {e}")

# Test the function
if __name__ == "__main__":
    try:
        channel_id = int(input("Enter the channel ID to view unique users: "))
        since_date = input("Enter the date (YYYY-MM-DD) to filter messages since: ")
        show_unique_users_since_date(channel_id, since_date)
    except ValueError:
        print("Invalid input. Please enter the correct values for channel ID and date.")
