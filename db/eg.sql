use pim;
drop table if exists design;
drop table if exists sampling;
drop table if exists konstruktion;
drop table if exists portfolio;


/*Brug design tabellen som vores primær tabel
THOUGHT: get rid of the associative entity and build the table on top of the DESIGN table. I don't see any m2m relation between design, sampling and konstruktion. 
####ADD A PORTFOLIO TABLE AND TO CATCH ALL DESIGNS IN A SPECIFIC PRODUCT LINE.
#####CALL IT PORTFOLIO. */

create table portfolio(
Project_ID int not null, 
Started date, 
Forventet_End date, 
Fase varchar(10), 
Værdi float, 
Kommenter varchar(25),
Project_navn varchar(10),
primary key (Project_ID)
)
;

CREATE TABLE  design(
Design_ID int not null, 
Mål float, 
Farve int, 
Skitse longblob, 
Material varchar(25), 
Kommentar varchar(25), 
Modeboard varchar(25), 
Holdninger varchar(25),
Project int,
primary key(Design_ID),
foreign key (Project) references portfolio(Project_ID)
)
;


create table konstruktion(
Konstruktion_Id int not null,
Estimate float,
Kommentar varchar(25),
Tid date,
Leverandør varchar(25),
Design int,
primary key (Konstruktion_Id),
foreign key (Design) references design (Design_ID)
)
;

create table sampling(
Model_Id int not null,
Test_Result varchar(5),
Feedback varchar (25),
Design int,
Konstruktion int,
primary key (Model_Id),
foreign key (Konstruktion) references konstruktion(Konstruktion_Id)
)
;



/*måske gøre status tabellen til en select statement der kør efter behov
create table snap(
select * from tbs
)
;*/