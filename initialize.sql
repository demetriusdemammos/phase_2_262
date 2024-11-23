-- drop the trax database if it exists
DROP database if EXISTS trax;

-- create it afresh
CREATE database trax;
\c trax
\i create.SQL

-- load the data
\copy Message(MessageID, message) FROM data/Messages.csv csv header;
\copy Contact(UserID1, UserID2, Sent_From, Sent_To) FROM data/Contact.csv csv header;
\copy Message_Details(UserID1, UserID2, MessageID) FROM data/Message_Details.csv csv header;
\copy Channel(ChannelID Channel name, Permission, Rank) FROM data/Channel.csv csv header;
\copy Userinfo(ChannelID, UserID) FROM data/Userinfo.csv csv header;
