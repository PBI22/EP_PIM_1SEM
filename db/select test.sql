use pim;
#Der er tre queries her. Det er den sidste der er vigtigst. Den giver adgang til alle tabellerne. 

#design to portfolio 
#select d.Material
#from portfolio as p
#left join design as d
#on p.Project_ID = d.Project
#;

#konstruktion to portfolio
#select *
#from portfolio as p 
#left join design as d on p.Project_ID = d.Project
#join konstruktion as k on d.Design_ID = k.Design
#;
#sampling to portfolio

select *
from portfolio as p 
join design as d on p.Project_ID = d.Project
join konstruktion as k on d.Design_ID = k.Design
join sampling as s on k.Konstruktion_Id = s.Konstruktion
;

