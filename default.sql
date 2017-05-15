Truncate table applicants;

INSERT INTO applicants VALUES (1, 'Dominique', 'Williams', '003630/734-4926', 'dolor@laoreet.co.uk', 61823);
INSERT INTO applicants VALUES (2, 'Jemima', 'Foreman', '003620/834-6898', 'magna@etultrices.net', 58324);
INSERT INTO applicants VALUES (3, 'Zeph', 'Massey', '003630/216-5351', 'a.feugiat.tellus@montesnasceturridiculus.co.uk', 61349);
INSERT INTO applicants VALUES (4, 'Joseph', 'Crawford', '003670/923-2669', 'lacinia.mattis@arcu.co.uk', 12916);
INSERT INTO applicants VALUES (5, 'Ifeoma', 'Bird', '003630/465-8994', 'diam.duis.mi@orcitinciduntadipiscing.com', 65603);
INSERT INTO applicants VALUES (6, 'Arsenio', 'Matthews', '003620/804-1652', 'semper.pretium.neque@mauriseu.net', 39220);
INSERT INTO applicants VALUES (7, 'Jemima', 'Cantu', '003620/423-4261', 'et.risus.quisque@mollis.co.uk', 10384);
INSERT INTO applicants VALUES (8, 'Carol', 'Arnold', '003630/179-1827', 'dapibus.rutrum@litoratorquent.com', 70730);
INSERT INTO applicants VALUES (9, 'Jane', 'Forbes', '003670/653-5392', 'janiebaby@adipiscingenimmi.edu', 56882);
INSERT INTO applicants VALUES (10, 'Ursa', 'William', '003620/496-7064', 'malesuada@mauriseu.net', 91220);

SELECT pg_catalog.setval('applicants_id_seq', 10, true);

