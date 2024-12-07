from common import conn, cur, print_cmd, show_table

us = '''
* User Story

   As a:  Sevver owner
 I want:  Analyze total amount of messages sent by users in the server
So That:  Identify active and inactive users and reward and punish correspondingly

'''

print(us)

def send_channel_message():
    heading("send_message")
    Message = input('Message is: ')
    Time = input('Time is: ')
    UserID = input("User ID is: ")
    ChannelID = input('Channel ID is: ')
    send_message(Message=Message, Time=Time, UserID=UserID, ChannelID=ChannelID)

def send_channel_message(Message,Time,UserID,ChannelID):
    tmpl = '''
        INSERT INTO Messages (Message,Time,UserID,ChannelID)
        VALUES (%s,%s,%s,%s);
    '''
    cmd = cur.mogrify(tmpl, (Message,Time,UserID,ChannelID))
    print_cmd(cmd)
    cur.execute(cmd)
    print()

# Test the function
if __name__ == "__main__":
    try:
        user_id = int(input("Enter the user ID to view the channel with most message: "))
        show_user_most_message_count_channel(user_id)
    except ValueError:
        print("Invalid input. Please enter a numerical user ID.")#US4-Rank_most_frequent_Channels-complex-analytical
