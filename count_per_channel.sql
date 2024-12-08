CREATE OR REPLACE FUNCTION GetUserMessageCountPerChannel(UserIDInput INT)
RETURNS TABLE(ChannelID INT, ChannelName TEXT, MessageCount INT) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.ChannelID,
        c.Channelname,
        COUNT(cm.Message) AS MessageCount
    FROM
        Channel c
    LEFT JOIN
        Channel_Message cm ON c.ChannelID = cm.ChannelID
    WHERE
        cm.UserID = UserIDInput
    GROUP BY
        c.ChannelID, c.Channelname
    ORDER BY
        c.ChannelID;
END;
$$ LANGUAGE plpgsql;
