from common import conn, cur, print_cmd, show_table

us = '''
* User Story

   As a: Server Owner
 I want: To update the name of a server
So That: I can have a more fitting server name for my interest group
'''

print(us)

def change_server_name(server_id, new_server_name):
    try:
        # Check if the ServerID exists
        tmpl_check_server = '''
        SELECT COUNT(*) FROM Server
         WHERE ServerID = %s;
        '''
        cur.execute(tmpl_check_server, (server_id,))
        server_exists = cur.fetchone()[0]

        if not server_exists:
            print(f"Error: ServerID {server_id} does not exist.")
            return

        # Update the ServerName
        tmpl_update_server_name = '''
        UPDATE Server
           SET ServerName = %s
         WHERE ServerID = %s;
        '''
        cmd_update_server_name = cur.mogrify(tmpl_update_server_name, (new_server_name, server_id))
        print_cmd(cmd_update_server_name)
        cur.execute(cmd_update_server_name)

        conn.commit()
        print(f"Server name for ServerID {server_id} successfully updated to '{new_server_name}'.")

        # Display the updated server details
        display_updated_server(server_id)

    except Exception as e:
        conn.rollback()
        print(f"Error updating server name: {e}")

def display_updated_server(server_id):
    try:
        cols = 'ServerID, ServerName, DateCreated, OwnerID'

        tmpl = '''
        SELECT ServerID, ServerName, DateCreated, OwnerID
          FROM Server
         WHERE ServerID = %s;
        '''
        cmd = cur.mogrify(tmpl, (server_id,))
        print_cmd(cmd)
        cur.execute(cmd)
        rows = cur.fetchall()

        # Show the updated server details
        show_table(rows, cols)
    except Exception as e:
        print(f"Error displaying updated server: {e}")

if __name__ == "__main__":
    try:
        server_id = int(input("Enter the Server ID: "))
        new_server_name = input("Enter the new Server Name: ")
        change_server_name(server_id, new_server_name)
    except ValueError:
        print("Invalid input. Please enter a valid Server ID.")
