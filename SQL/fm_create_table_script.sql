ALTER SCHEMA players RENAME TO fm;




CREATE TABLE fm.nations (
    nation_id INTEGER PRIMARY KEY,
    nation_short VARCHAR(5),
    nation_full VARCHAR(100),
    nation_continent VARCHAR(20)
);



CREATE TABLE fm.leagues (
    league_id SERIAL PRIMARY KEY,
    league_name VARCHAR(100),
    nation_id INTEGER REFERENCES fm.nations (nation_id),
    team_count INTEGER
);


CREATE TABLE fm.clubs (
    club_id INTEGER PRIMARY KEY,
    club_name VARCHAR(100),
    nation_id INTEGER REFERENCES fm.nations (nation_id),
    league_id INTEGER REFERENCES fm.leagues (league_id),
    club_id_fm INTEGER 
);

   

CREATE TABLE fm.players (
    player_id BIGINT PRIMARY KEY,
    player_name VARCHAR(100),
    birthdate DATE,
    nation_id INTEGER REFERENCES fm.nations (nation_id),
    club_id INTEGER REFERENCES fm.clubs (club_id),
    preferred_foot VARCHAR(20),
    right_foot VARCHAR(20),
    left_foot VARCHAR(20),
    height SMALLINT,
    weight SMALLINT
);
   


CREATE TABLE fm.player_features (
    features_id SERIAL PRIMARY KEY,
    player_id BIGINT REFERENCES fm.players (player_id),
    Aggression SMALLINT CHECK (Aggression >= 0 AND Aggression <= 20),
    Jumping_Reach SMALLINT CHECK (Jumping_Reach >= 0 AND Jumping_Reach <= 20),
    Punching SMALLINT CHECK (Punching >= 0 AND Punching <= 20),
    Natural_Fitness SMALLINT CHECK (Natural_Fitness >= 0 AND Natural_Fitness <= 20),
    Vision SMALLINT CHECK (Vision >= 0 AND Vision <= 20),
    Long_Throws SMALLINT CHECK (Long_Throws >= 0 AND Long_Throws <= 20),
    Long_Shots SMALLINT CHECK (Long_Shots >= 0 AND Long_Shots <= 20),
    Off_The_Ball SMALLINT CHECK (Off_The_Ball >= 0 AND Off_The_Ball <= 20),
    Tackling SMALLINT CHECK (Tackling >= 0 AND Tackling <= 20),
    Technique SMALLINT CHECK (Technique >= 0 AND Technique <= 20),
    Teamwork SMALLINT CHECK (Teamwork >= 0 AND Teamwork <= 20),
    Composure SMALLINT CHECK (Composure >= 0 AND Composure <= 20),
    Free_Kick_Taking SMALLINT CHECK (Free_Kick_Taking >= 0 AND Free_Kick_Taking <= 20),
    Reflexes SMALLINT CHECK (Reflexes >= 0 AND Reflexes <= 20),
    "Position" SMALLINT CHECK ("Position" >= 0 AND "Position" <= 20),
    Penalty_Taking SMALLINT CHECK (Penalty_Taking >= 0 AND Penalty_Taking <= 20),
    "Passing" SMALLINT CHECK ("Passing" >= 0 AND "Passing" <= 20),
    Flair SMALLINT CHECK (Flair >= 0 AND Flair <= 20),
    Anticipation SMALLINT CHECK (Anticipation >= 0 AND Anticipation <= 20),
    Crossing SMALLINT CHECK (Crossing >= 0 AND Crossing <= 20),
    Marking SMALLINT CHECK (Marking >= 0 AND Marking <= 20),
    Leadership SMALLINT CHECK (Leadership >= 0 AND Leadership <= 20),
    Corners SMALLINT CHECK (Corners >= 0 AND Corners <= 20),
    Concentration SMALLINT CHECK (Concentration >= 0 AND Concentration <= 20),
    Determination SMALLINT CHECK (Determination >= 0 AND Determination <= 20),
    Decision SMALLINT CHECK (Decision >= 0 AND Decision <= 20),
    Heading SMALLINT CHECK (Heading >= 0 AND Heading <= 20),
    First_Touch SMALLINT CHECK (First_Touch >= 0 AND First_Touch <= 20),
    Communication SMALLINT CHECK (Communication >= 0 AND Communication <= 20),
    Acceleration SMALLINT CHECK (Acceleration >= 0 AND Acceleration <= 20),
    Pace SMALLINT CHECK (Pace >= 0 AND Pace <= 20),
    Aerial_Reach SMALLINT CHECK (Aerial_Reach >= 0 AND Aerial_Reach <= 20),
    Strength SMALLINT CHECK (Strength >= 0 AND Strength <= 20),
    Throwing SMALLINT CHECK (Throwing >= 0 AND Throwing <= 20),
    Handling SMALLINT CHECK (Handling >= 0 AND Handling <= 20),
    Eccentricity SMALLINT CHECK (Eccentricity >= 0 AND Eccentricity <= 20),
    Dribbling SMALLINT CHECK (Dribbling >= 0 AND Dribbling <= 20),
    Balance SMALLINT CHECK (Balance >= 0 AND Balance <= 20),
    Kicking SMALLINT CHECK (Kicking >= 0 AND Kicking <= 20),
    Stamina SMALLINT CHECK (Stamina >= 0 AND Stamina <= 20),
    Agility SMALLINT CHECK (Agility >= 0 AND Agility <= 20),
    Work_Rate SMALLINT CHECK (Work_Rate >= 0 AND Work_Rate <= 20),
    Bravery SMALLINT CHECK (Bravery >= 0 AND Bravery <= 20),
    Command_Of_Area SMALLINT CHECK (Command_Of_Area >= 0 AND Command_Of_Area <= 20),
    Finishing SMALLINT CHECK (Finishing >= 0 AND Finishing <= 20),
    One_vs_One SMALLINT CHECK (One_vs_One >= 0 AND One_vs_One <= 20),
    TRO SMALLINT CHECK (TRO >= 0 AND TRO <= 20)
);



CREATE TABLE fm.positions (
    position_id SERIAL PRIMARY KEY,
    player_id BIGINT REFERENCES fm.players (player_id),
    position_short VARCHAR(5),
    position_fullname VARCHAR(50)
);




