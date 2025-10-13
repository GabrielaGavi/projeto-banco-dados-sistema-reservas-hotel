INSERT INTO hospede VALUES ('123.456.789-00', 'Maria Silva', '27999999999', SYSDATE);
INSERT INTO hospede VALUES ('987.654.321-00', 'João Santos', '27988888888', SYSDATE);

INSERT INTO quarto VALUES (101, 'Casal', 300.00, 'Disponível');
INSERT INTO quarto VALUES (102, 'Solteiro', 180.00, 'Disponível');

INSERT INTO reserva VALUES (
    1, '123.456.789-00', 101,
    TO_DATE('2025-10-20', 'YYYY-MM-DD'),
    TO_DATE('2025-10-25', 'YYYY-MM-DD'),
    2, 1500.00, 'Ativa', SYSTIMESTAMP
);

COMMIT;