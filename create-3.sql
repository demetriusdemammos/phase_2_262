-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2024-11-23 03:20:09.304

-- tables
-- Table: Channel
CREATE TABLE Channel (
    ChannelID int  NOT NULL,
    Channelname int  NOT NULL,
    Permission int  NOT NULL,
    Rank int  NOT NULL,
    CONSTRAINT Channel_pk PRIMARY KEY (ChannelID)
);

-- Table: Channel_Message
CREATE TABLE Channel_Message (
    Message int  NOT NULL,
    Time int  NOT NULL,
    UserID int  NOT NULL,
    ChannelID int  NOT NULL,
    CONSTRAINT Channel_Message_pk PRIMARY KEY (UserID,ChannelID)
);

-- Table: User
CREATE TABLE "User" (
    UserID int  NOT NULL,
    Username text  NOT NULL,
    email varchar(255)  NOT NULL,
    CONSTRAINT User_pk PRIMARY KEY (UserID)
);

-- foreign keys
-- Reference: Channel_Message_Channel (table: Channel_Message)
ALTER TABLE Channel_Message ADD CONSTRAINT Channel_Message_Channel
    FOREIGN KEY (ChannelID)
    REFERENCES Channel (ChannelID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Channel_Message_User (table: Channel_Message)
ALTER TABLE Channel_Message ADD CONSTRAINT Channel_Message_User
    FOREIGN KEY (UserID)
    REFERENCES "User" (UserID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

