from common import conn, cur, print_cmd, show_table

us = '''
* User Story

   As a:  User
 I want:  Send a message
So That:  Communicate with my friend
'''

print(us)


def send_message():
    """
    Collects user input to send a message, assigns the first available MessageID,
    inserts it into the database, and then displays the message details.
    """
    try:

        message_id = get_next_message_id()


        sent_from = int(input('Enter Sender User ID: ').strip())
        sent_to = int(input('Enter Recipient User ID: ').strip())
        message = input('Enter Message: ').strip()


        insert_message(message_id, sent_from, sent_to, message)


        show_user_message(message_id)

    except ValueError as e:
        print(f"Invalid input: {e}. Please provide valid numerical IDs and message text.")
    except Exception as e:
        print(f"Error sending message: {e}")


def get_next_message_id():
    """
    Retrieves the first available MessageID by finding the max MessageID in the database
    and returning the next number.
    """
    try:
        tmpl = '''
        SELECT COALESCE(MAX(MessageID), 0) + 1 AS NextID
          FROM Message;
        '''
        cur.execute(tmpl)
        next_id = cur.fetchone()[0]
        return next_id
    except Exception as e:
        print(f"Error determining next MessageID: {e}")
        raise


def insert_message(message_id, sent_from, sent_to, message):
    """
    Inserts a message into the Messages table.
    """
    try:
        tmpl = '''
            INSERT INTO Message (MessageID, Sent_From, Sent_To, message)
            VALUES (%s, %s, %s, %s);
        '''
        cmd = cur.mogrify(tmpl, (message_id, sent_from, sent_to, message))
        print_cmd(cmd)
        cur.execute(cmd)
        conn.commit()
        print(f"Message successfully sent from User {sent_from} to User {sent_to} with MessageID {message_id}.")
    except Exception as e:
        conn.rollback()
        print(f"Error inserting message: {e}")


def show_user_message(message_id):
    """
    Retrieves and displays a message from the Messages table based on MessageID.
    """
    try:
        cols = 'MessageID, Sent_From, Sent_To, message'

        tmpl = '''
        SELECT m.MessageID, m.Sent_From, m.Sent_To, m.message
          FROM Message AS m
         WHERE m.MessageID = %s;
        '''


        cmd = cur.mogrify(tmpl, (message_id,))
        print_cmd(cmd)


        cur.execute(cmd)


        rows = cur.fetchall()

        if rows:
            print("Message Details:")
            show_table(rows, cols)
        else:
            print(f"No message found with MessageID {message_id}.")

    except Exception as e:
        print(f"Error retrieving message: {e}")


if __name__ == "__main__":
    send_message()
