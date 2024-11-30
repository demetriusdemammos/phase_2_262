-- drop the trax database if it exists
DROP database if EXISTS trax;

-- create it afresh
CREATE database trax;
\c trax
\i create.SQL

-- load the data
\copy "User"(UserID,Username,email) FROM './User.csv' csv header;
\copy Channel(ChannelID, Channelname, Permission, Rank) FROM './Channel.csv' csv header;
\copy Channel_Message(Message,Time,UserID,ChannelID) FROM './Channel_Message.csv' csv header;
\copy Message(MessageID,Sent_From,Sent_To,message) FROM './Message.csv' csv header;
