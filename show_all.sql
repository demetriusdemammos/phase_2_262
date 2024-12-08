<<<<<<< HEAD
\c trax
\echo "display the User table"
SELECT * FROM "User";
\echo "display the Channel table"
SELECT * FROM Channel;
\echo "display Channel_Message table"
SELECT * FROM Channel_Message;
\echo "display Message table"
SELECT * FROM Message;
\echo "display Event table"
SELECT * FROM Event;
\echo "display Event_Participation table"
SELECT * FROM Event_Participation
\echo "deplay Common_User table"
SELECT * FROM Common_User
=======
SELECT 
    u.UserID,
    u.Username,
    u.email,
    c1.Message,
    c1.Time,
    c2.ChannelID,
    c2.Channelname,
    c2.Permission,
    c2.Rank,
    s.ServerID,
    s.ServerName,
    s.DateCreated
FROM 
    "User" AS u
    JOIN Channel_Message AS c1 ON u.UserID = c1.UserID
    JOIN Channel AS c2 ON c1.ChannelID = c2.ChannelID
    JOIN Server AS s ON c2.ServerID = s.ServerID;
>>>>>>> 34aa304 (lots of us)
