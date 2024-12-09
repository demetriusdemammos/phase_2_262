from common import conn, cur, print_cmd

us = '''
* User Story

   As a: Server Owner
 I want: To establish a server
So That: I can share interests with more people
'''

print(us)

def establish_server(server_name, owner_id):
    from datetime import datetime

    try:
        tmpl_check_user = '''
        SELECT COUNT(*) FROM "User"
         WHERE UserID = %s;
        '''
        cur.execute(tmpl_check_user, (owner_id,))
        user_exists = cur.fetchone()[0]

        if not user_exists:
            print(f"Error: UserID {owner_id} does not exist in the system. Cannot create server.")
            return

        tmpl_insert_owner = '''
        INSERT INTO Server_Owner (UserID)
        SELECT %s
        WHERE NOT EXISTS (SELECT 1 FROM Server_Owner WHERE UserID = %s);
        '''
        cmd_insert_owner = cur.mogrify(tmpl_insert_owner, (owner_id, owner_id))
        print_cmd(cmd_insert_owner)
        cur.execute(cmd_insert_owner)

        tmpl_get_max_id = '''
        SELECT COALESCE(MAX(ServerID), 0) + 1 FROM Server;
        '''
        cur.execute(tmpl_get_max_id)
        server_id = cur.fetchone()[0]

        current_date = datetime.now().strftime('%Y-%m-%d')
        tmpl_insert_server = '''
        INSERT INTO Server (ServerID, ServerName, DateCreated, OwnerID)
        VALUES (%s, %s, %s, %s);
        '''
        cmd_insert_server = cur.mogrify(tmpl_insert_server, (server_id, server_name, current_date, owner_id))
        print_cmd(cmd_insert_server)
        cur.execute(cmd_insert_server)

        conn.commit()
        print(f"Server '{server_name}' successfully created with ID {server_id}, owned by User {owner_id}.")


        tmpl_show_servers = '''
        SELECT * FROM Server;
        '''
        cur.execute(tmpl_show_servers)
        rows = cur.fetchall()

        print("\nCurrent Server Table:")
        print("ServerID | ServerName | DateCreated | OwnerID")
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

    except Exception as e:
        conn.rollback()
        print(f"Error creating server: {e}")

if __name__ == "__main__":
    try:
        server_name = input("Enter the Server Name: ")
        owner_id = int(input("Enter the Owner ID: "))
        establish_server(server_name, owner_id)
    except ValueError:
        print("Invalid input. Please enter a valid numerical value for Owner ID.")
