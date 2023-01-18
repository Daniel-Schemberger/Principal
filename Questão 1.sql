/* QUESTÃO 1 */

/* Raciocínio por trás da solução*/

/*
	Para responder a questão 1 foram utilizadas as tabelas
Rental, Inventory & Film. 
	Inicialmente foi utilizado a tabela 'Rental' que contém 
informação dos filmes alugados, uma destas informações é 
uma "id" do produto no Inventário.
	Com a tabela 'Inventory' associamos a "id" do inventário, 
na tabela 'Rental', a uma "id" de Filme. 
	Em seguida foi associado as "id's" dos filmes aos seus
respectivos títulos com a tabela 'Film'.
	A contagem de alugueis de cada filme foi feita através
da contagem de "id's" de filmes na tabela 'Inventory'
*/

/* Código */

SELECT Film.title, COUNT(Inventory.film_id) AS aluguéis
FROM Rental
	INNER JOIN Inventory
	ON Rental.inventory_id = Inventory.inventory_id
	INNER JOIN Film
	ON Inventory.film_id = Film.film_id
GROUP BY Inventory.film_id, Film.title
ORDER BY COUNT(Inventory.film_id) DESC
LIMIT 2;
