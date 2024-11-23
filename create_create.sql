-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2024-11-23 00:05:55.569

-- tables
-- Table: Channel
CREATE TABLE Channel (
    ChannelID int  NOT NULL,
    Channel_name text  NOT NULL,
    Permission text  NOT NULL,
    Rank int  NOT NULL,
    CONSTRAINT Channel_pk PRIMARY KEY (ChannelID)
);

-- Table: Contact
CREATE TABLE Contact (
    UserID1 int  NOT NULL,
    UserID2 int  NOT NULL,
    Sent_From text  NOT NULL,
    Sent_To text  NOT NULL,
    CONSTRAINT Contact_pk PRIMARY KEY (UserID1,UserID2)
);

-- Table: Message
CREATE TABLE Message (
    MessageID int  NOT NULL,
    message text  NOT NULL,
    CONSTRAINT Message_pk PRIMARY KEY (MessageID)
);

-- Table: Message_Details
CREATE TABLE Message_Details (
    MessageID int  NOT NULL,
    UserID1 int  NOT NULL,
    R3_UserID2 int  NOT NULL,
    CONSTRAINT Message_Details_pk PRIMARY KEY (MessageID,UserID1,R3_UserID2)
);

-- Table: Userinfo
CREATE TABLE Userinfo (
    UserID int  NOT NULL,
    R5_ChannelID int  NOT NULL,
    CONSTRAINT Userinfo_pk PRIMARY KEY (UserID,R5_ChannelID)
);

-- foreign keys
-- Reference: R4_R1 (table: Message_Details)
ALTER TABLE Message_Details ADD CONSTRAINT R4_R1
    FOREIGN KEY (MessageID)
    REFERENCES Message (MessageID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: R4_R3 (table: Message_Details)
ALTER TABLE Message_Details ADD CONSTRAINT R4_R3
    FOREIGN KEY (UserID1, R3_UserID2)
    REFERENCES Contact (UserID1, UserID2)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: R6_R5 (table: Userinfo)
ALTER TABLE Userinfo ADD CONSTRAINT R6_R5
    FOREIGN KEY (R5_ChannelID)
    REFERENCES Channel (ChannelID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

