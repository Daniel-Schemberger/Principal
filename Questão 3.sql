/* QUESTÃO 3 */

/* Raciocínio por trás da solução */

/* Criando uma cópia da tabela 'Rental' */

SELECT * INTO Rental2 FROM Rental

/* Deletando as linhas onde a "id" do
cliente é igual para maiores "id's" de
aluguel (Mantendo assim apenas as linhas com
o primeiro pedido de cada cliente) na tabela
copiada */

DELETE FROM Rental2 USING Rental
WHERE Rental2.rental_id > Rental.rental_id
AND Rental2.costumer_id = Rental.costumer_id;

/* Com uma tabela com apenas os primeiros registros
de cada cliente (através das suas "id's"), podemos
ordenar por data de aluguel e fazer a contagem de
quantas "id's" existem agrupadaspor mês */

SELECT
TO_CHAR(rental_date, 'MM') AS mes,
COUNT(costumer_id) AS novos_clientes 
FROM Rental2
GROUP BY TO_CHAR(rental_date, 'MM')
ORDER BY mes;