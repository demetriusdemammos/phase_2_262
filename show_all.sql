SELECT u.UserID,u.Username,u.email,c1.Message,c1.Time,c2.ChannelID,c2.Channelname,c2.Permission,c2.Rank
  FROM User AS u
  JOIN Channel_Message AS c1 ON u.UserID=c1.UserID
  JOIN Channel AS c2 ON c1.ChannelID=c2.ChannelID;
