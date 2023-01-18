/* QUESTÃO 2 */

/* Raciocínio por trás da solução*/

/* Utilizando a resposta da questão anterior foi possível
criar uma nova tabela com as "id's" dos 16 filmes mais
assistidos*/

/* ID dos 16 filmes mais assistidos */

CREATE TABLE top16_ids AS SELECT Inventory.film_id
FROM Rental
	INNER JOIN Inventory
	ON Rental.inventory_id = Inventory.inventory_id
	INNER JOIN Film
	ON Inventory.film_id = Film.film_id
GROUP BY Inventory.film_id, Film.title
ORDER BY COUNT(Inventory.film_id) DESC
LIMIT 16;

/* Com isso, foi utilizado um Join para associar as "id's" da 
tabela anterior com as "id's" dos filmes na tabela 'Film_Actor',
nesta tabela temos armazenado as "id's" dos atores.
	foi então utilizado um segundo Join para associar as 
"id's" dos atores na tabela inicial com as "id's" dos atores
ta tabela 'Actor', que armazena também o nome dos atores.
	Foi realizado uma contagem de repetições das "id's"
e selecionado a mais recorrente, selecionando apenas o nome
completo (através de concatenação das colunas "firts_name"
e "last_name" da tabela 'Actor')*/

/* Código */

SELECT Actor.first_name||' '||Actor.last_name AS Nome 
FROM top16_ids
	LEFT JOIN Film_Actor
	ON top16_ids.film_id = Film_Actor.film_id
	LEFT JOIN Actor
	ON Film_Actor.actor_id = Actor.actor_id
GROUP BY Actor.actor_id, Actor.first_name, Actor.last_name
ORDER BY COUNT (Actor.actor_id) DESC
LIMIT 1;

	
	