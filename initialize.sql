-- drop the trax database if it exists
DROP database if EXISTS trax;

-- create it afresh
CREATE database trax;
\c trax
\i create.SQL

-- load the data
\copy User(UserID,Username,email) FROM data/User.csv header;
\copy Channel(ChannelID, Channel name, Permission, Rank) FROM data/Channel.csv csv header;
\copy Channel_Message(ChannelID, UserID,Message) FROM data/Channel_Message.csv csv header;
