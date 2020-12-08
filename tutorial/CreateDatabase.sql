-- Create database
DROP DATABASE IF EXISTS Basketball;
CREATE DATABASE Basketball;
USE Basketball;

-- Create Team
CREATE TABLE Team
(
	team_ID VARCHAR(10) NOT NULL,
	name VARCHAR(20) NOT NULL,
	color VARCHAR(10) NOT NULL,
	CONSTRAINT Team_PK PRIMARY KEY (team_ID)
);

-- Create Coach
CREATE TABLE Coach
(
	coach_ID VARCHAR(10) NOT NULL,
	name VARCHAR(20) NOT NULL,
	cert VARCHAR(20) NOT NULL,
	salary DOUBLE NOT NULL,
	phone CHAR(10) NOT NULL,
	team_ID_FK VARCHAR(10) NOT NULL,
	CONSTRAINT Coach_PK PRIMARY KEY (coach_ID)
);

-- Create Player
CREATE TABLE Player
(
	player_ID VARCHAR(10) NOT NULL,
	first VARCHAR(20) NOT NULL,
	last VARCHAR(20) not NULL,
	percentage DOUBLE NOT NULL,
	age INTEGER NOT NULL,
	team_ID_FK VARCHAR(10) NOT NULL,
	CONSTRAINT Player_PK PRIMARY KEY (player_ID)
);

-- Create Parent
CREATE TABLE Parent
(
	parent_ID VARCHAR(10) NOT NULL,
	first VARCHAR(20) NOT NULL,
	last VARCHAR(20) NOT NULL,
	email VARCHAR(30) NOT NULL,
	phone CHAR(10) NOT NULL,
	address VARCHAR(30) NOT NULL,
	CONSTRAINT Parent_PK PRIMARY KEY (parent_ID)
);

-- Create RelatedTo
CREATE TABLE RelatedTo
(
	player_ID_FK VARCHAR(10) NOT NULL,
	parent_ID_FK VARCHAR(10) NOT NULL,
	CONSTRAINT RelatedTo_PK PRIMARY KEY (player_ID_FK, parent_ID_FK)
);


-- Create Inventory
CREATE TABLE Inventory
(
	itemNum INTEGER NOT NULL AUTO_INCREMENT,
	name VARCHAR(20) NOT NULL,
	decription VARCHAR(40) NOT NULL,
	price DOUBLE NOT NULL,
	quantity INTEGER NOT NULL,
	player_ID_FK VARCHAR(10),
	CONSTRAINT Inventory_PK PRIMARY KEY (itemNum)
);

-- Create CoachCheckOut
CREATE TABLE CoachCheckOut
(
	coach_ID_FK VARCHAR(10) NOT NULL,
	itemNum_FK INTEGER NOT NULL,
	checkNum INTEGER NOT NULL AUTO_INCREMENT,
	CONSTRAINT CoachCheckOut_PK PRIMARY KEY (checkNum)
);

-- Create relationship for tables
-- Add foreign key for Coach
ALTER TABLE Coach ADD CONSTRAINT Coach_FK1 FOREIGN KEY (team_ID_FK) REFERENCES Team(team_ID);

-- Add foreign key for Player
ALTER TABLE Player ADD CONSTRAINT Player_FK1 FOREIGN KEY (team_ID_FK) REFERENCES Team(team_ID);

-- Add foreign key for Inventory
ALTER TABLE Inventory ADD CONSTRAINT Inventory_FK1 FOREIGN KEY (player_ID_FK) REFERENCES Player(player_ID);

-- Add foreign key for CoachCheckOut
ALTER TABLE CoachCheckOut ADD CONSTRAINT CoachCheckOut_FK1 FOREIGN KEY (coach_ID_FK) REFERENCES Coach(coach_ID);
ALTER TABLE CoachCheckOut ADD CONSTRAINT CoachCheckOut_FK2 FOREIGN KEY (itemNum_FK) REFERENCES Inventory(itemNum);

-- Add foreign key for RelatedTo
ALTER TABLE RelatedTo ADD CONSTRAINT RelatedTo_FK1 FOREIGN KEY (parent_ID_FK) REFERENCES Parent(parent_ID);
ALTER TABLE RelatedTo ADD CONSTRAINT RelatedTot_FK2 FOREIGN KEY (player_ID_FK) REFERENCES Player(player_ID);



-- Insert data

-- Insert data to team
INSERT INTO Team(team_ID, name, color) VALUES
('T001', 'Team A', 'RED'),
('T002', 'Team B', 'GREEN'),
('T003', 'Team C', 'BLUE'),
('T004', 'Team D', 'YELLOW'),
('T005', 'Team E', 'WHITE');

-- Insert data to Coach
INSERT INTO Coach(coach_ID, name, cert, salary, phone, team_ID_FK) VALUES
('C001', 'Davis', 'Cert 1', 2000, '2672065338', 'T001'),
('C002', 'Peter', 'Cert 1', 3000, '2678798019', 'T002'),
('C003', 'Jame', 'Cert 1', 4000, '2159003265', 'T003'),
('C004', 'Joe', 'Cert 1', 5000, '2157240787', 'T004'),
('C005', 'Barry', 'Cert 1', 6000, '5128565334', 'T005');


-- Insert data to Player
INSERT INTO Player(player_ID, first, last, percentage, age, team_ID_FK) VALUES
('P001', 'JOE', 'BERRY', 90, 16, 'T001'),
('P002', 'SAM', 'GOODMAN', 91, 15, 'T001'),
('P003', 'CHERRY', 'WILLIAM', 93, 14, 'T001'),
('P004', 'NANI', 'WHITEMAN', 89, 15, 'T001'),
('P005', 'SAM', 'LEE', 70, 13, 'T001');

-- Insert data to Parent
INSERT INTO Parent(parent_ID, first, last, email, phone, address) VALUES
('PR001', 'JOE', 'BACON', 'joe@gmail.com', '2672065338', '4523 Baltimore AVE'),
('PR002', 'NINA', 'CHEESMAN', 'nina@gmail.com', '2678798019', '112 Buist AVE'),
('PR003', 'TASA', 'GOODWIN', 'tasa@gmail.com', '2159003265', '45 15 ST'),
('PR004', 'WINDRE', 'LEE', 'windr@gmail.com', '2157240787', '12 Green AVE'),
('PR005', 'KEYA', 'HEYNEE', 'key@gmail.com', '5128565334', '4 Snyder ST');

-- Insert data to Related to
INSERT INTO RelatedTo(player_ID_FK, parent_ID_FK) VALUES
('P001', 'PR001'),
('P002', 'PR002'),
('P003', 'PR003'),
('P004', 'PR004'),
('P005', 'PR005');

-- Insert data to Inventory
INSERT INTO Inventory(name, decription, price, quantity, player_ID_FK) VALUES
('Shoes', 'Shoe', 500, 1, 'P001'),
('Shirt', 'Shirt', 100, 1, 'P002'),
('Gloves', 'Gloves', 200, 1, 'P003'),
('Shocks', 'Shocks', 20, 1, 'P004'),
('Ball', 'Ball', 100, 1, 'P005');

-- Insert data to CoachCheckOut
INSERT INTO CoachCheckOut(coach_ID_FK, itemNum_FK) VALUES
('C001', 1),
('C002', 2),
('C003', 3),
('C004', 4),
('C005', 5);


-- Create view for player that have team information
CREATE OR REPLACE VIEW playerTeam
AS
SELECT p.player_ID, p.first, p.last, p.percentage, p.age, t.name as teamName, t.color
FROM Player p
INNER JOIN Team t
ON p.team_ID_FK = t.team_ID;


-- Create view that show only players that have percentage >= 90
CREATE OR REPLACE VIEW goodPlayer
AS
SELECT *
FROM Player p
WHERE p.percentage >= 90;