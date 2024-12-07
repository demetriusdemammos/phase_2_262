-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2024-12-07 20:46:03.827

-- tables
-- Table: Channel
CREATE TABLE Channel (
    ChannelID int  NOT NULL,
    Channelname text  NOT NULL,
    Permission text  NOT NULL,
    Rank int  NOT NULL,
    ServerID int  NOT NULL,
    CONSTRAINT Channel_pk PRIMARY KEY (ChannelID)
);

-- Table: Channel_Message
CREATE TABLE Channel_Message (
    Message text  NOT NULL,
    Time timestamp  NOT NULL,
    UserID int  NOT NULL,
    ChannelID int  NOT NULL,
    CONSTRAINT Channel_Message_pk PRIMARY KEY (UserID,ChannelID,Time)
);

-- Table: Common_User
CREATE TABLE Common_User (
    UserID int  NOT NULL,
    Role text  NOT NULL,
    CONSTRAINT Common_User_pk PRIMARY KEY (UserID)
);

-- Table: Event
CREATE TABLE Event (
    EventID int  NOT NULL,
    Event_time timestamp  NOT NULL,
    CONSTRAINT Event_pk PRIMARY KEY (EventID)
);

-- Table: Event_Participation
CREATE TABLE Event_Participation (
    Time_Duration int  NOT NULL,
    Time_participated int  NOT NULL,
    UserID int  NOT NULL,
    EventId int  NOT NULL,
    CONSTRAINT Event_Participation_pk PRIMARY KEY (UserID,EventId)
);

-- Table: Message
CREATE TABLE Message (
    MessageID int  NOT NULL,
    Sent_From int  NOT NULL,
    Sent_To int  NOT NULL,
    message text  NOT NULL,
    CONSTRAINT Message_pk PRIMARY KEY (MessageID)
);

-- Table: Server
CREATE TABLE Server (
    ServerID int  NOT NULL,
    ServerName text  NOT NULL,
    DateCreated date  NOT NULL,
    CONSTRAINT Server_pk PRIMARY KEY (ServerID)
);

-- Table: User
CREATE TABLE "User" (
    UserID int  NOT NULL,
    Username text  NOT NULL,
    email varchar(255)  NOT NULL,
    CONSTRAINT User_pk PRIMARY KEY (UserID)
);

-- Table: User_Server
CREATE TABLE User_Server (
    Role text  NOT NULL,
    ServerID int  NOT NULL,
    UserID int  NOT NULL,
    CONSTRAINT User_Server_pk PRIMARY KEY (UserID,ServerID)
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

-- Reference: Channel_Server (table: Channel)
ALTER TABLE Channel ADD CONSTRAINT Channel_Server
    FOREIGN KEY (ServerID)
    REFERENCES Server (ServerID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Event_Participation_Common_User (table: Event_Participation)
ALTER TABLE Event_Participation ADD CONSTRAINT Event_Participation_Common_User
    FOREIGN KEY (UserID)
    REFERENCES Common_User (UserID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Event_Participation_Event (table: Event_Participation)
ALTER TABLE Event_Participation ADD CONSTRAINT Event_Participation_Event
    FOREIGN KEY (EventId)
    REFERENCES Event (EventID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Message_User (table: Message)
ALTER TABLE Message ADD CONSTRAINT Message_User
    FOREIGN KEY (Sent_From)
    REFERENCES "User" (UserID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: User_Common_User (table: Common_User)
ALTER TABLE Common_User ADD CONSTRAINT User_Common_User
    FOREIGN KEY (UserID)
    REFERENCES "User" (UserID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: User_Message (table: Message)
ALTER TABLE Message ADD CONSTRAINT User_Message
    FOREIGN KEY (Sent_To)
    REFERENCES "User" (UserID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: User_Server_Server (table: User_Server)
ALTER TABLE User_Server ADD CONSTRAINT User_Server_Server
    FOREIGN KEY (ServerID)
    REFERENCES Server (ServerID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: User_Server_User (table: User_Server)
ALTER TABLE User_Server ADD CONSTRAINT User_Server_User
    FOREIGN KEY (UserID)
    REFERENCES "User" (UserID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

