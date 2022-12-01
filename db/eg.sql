drop table if exists sampling;
drop table if exists konstruktion;
CREATE TABLE  design(
Design_ID int not null, 
Mål float, 
Farve int, 
Skitse longblob, 
Material varchar(25), 
Kommentar varchar(25), 
Modeboard varchar(25), 
Holdninger varchar(25),
primary key(Design_ID)
)
;
create table sampling(
Model_Id int not null,
Test_Result varchar(5),
Feedback varchar (25),
primary key (Model_Id))

;

create table konstruktion(
Konstruktion_Id int not null,
Estimate float,
Kommentar varchar(25),
Tid date,
Leverandør varchar(25),
primary key (Konstruktion_Id))
sampling
;