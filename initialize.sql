-- Drop the "trax" database if it exists
DROP DATABASE IF EXISTS trax;

-- Create it afresh
CREATE DATABASE trax;

-- Connect to the new database
\c trax

-- Execute the schema creation script
\i create.SQL

<<<<<<< HEAD
-- load the data
\copy "User"(UserID,Username,email) FROM './User.csv' csv header;
\copy Channel(ChannelID, Channelname, Permission, Rank) FROM './Channel.csv' csv header;
\copy Channel_Message(Message,Time,UserID,ChannelID,ServerID) FROM './Channel_Message.csv' csv header;
\copy Message(MessageID,Sent_From,Sent_To,message) FROM './Message.csv' csv header;
\copy Common_User(UserID,"Role") FROM './Common_User.csv' csv header;
\copy Event(EventID,Event_Time) FROM './Event.csv' csv header;
\copy Event_Participation(Time_Duration,Time_participated,UserID,EventID) FROM './Event_Participation.csv' csv header;
\copy Server_Owner(UserID,Date_Owned) FROM './Server_Owner.csv' csv header;
\copy User_Server(UserID,ServerID) FROM './User_Server.csv' csv header;
\copy Admin(UserID,Responsibility) FROM './Admin.csv' csv header;
\copy Server(ServerID,ServerName,DateCreated,OwnerID) FROM './Server.csv' csv header;
\copy Channel_server()
=======
-- Load data into tables
\copy "User"(UserID, Username, email) FROM 'User.csv' CSV HEADER;
\copy Common_User(UserID, Role) FROM 'Common_User.csv' CSV HEADER;
\copy Server_Owner(UserID) FROM 'Server_Owner.csv' CSV HEADER;
\copy Server(ServerID, ServerName, DateCreated, OwnerID) FROM 'Server.csv' CSV HEADER;
\copy User_Server(UserID, ServerID, Role) FROM 'User_Server.csv' CSV HEADER;
\copy Channel(ChannelID, Channelname, Permission, Rank, ServerID) FROM 'Channel.csv' CSV HEADER;
\copy Channel_Message(Message,Time,UserID,ChannelID) FROM 'Channel_Message.csv' CSV HEADER;
\copy Event(EventID, Event_time) FROM 'Event.csv' CSV HEADER;
\copy Event_Participation(UserID, EventId, Time_Duration, Time_participated) FROM 'Event_Participation.csv' CSV HEADER;
\copy Message(MessageID, Sent_From, Sent_To, message) FROM 'Message.csv' CSV HEADER;
>>>>>>> 34aa304 (lots of us)
