--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: handphone; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.handphone (
    brand character varying NOT NULL,
    ram character varying,
    prosesor character varying,
    storage character varying,
    baterai character varying,
    harga character varying,
    os character varying
);


ALTER TABLE public.handphone OWNER TO postgres;

--
-- Data for Name: handphone; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.handphone (brand, ram, prosesor, storage, baterai, harga, os) FROM stdin;
OPPO A18	4 GB	Helio G85 (12nm)	128 GB	5000 mAh	1799000	Android 13
OPPO A78 5G	8 GB	MT6833 Dimensity 700 (7 nm)	128 GB	5000 mAh	3535000	Android 12
OPPO A77s	8 GB	SM6225 Snapdragon 680 4G (6 nm)	128 GB	5000 mAh	2650000	Android 12
OPPO A78 4G	8 GB	Snapdragon 680 4G (6 nm)	256 GB	5000 mAh	3075000	Android 13
OPPO A57	4 GB	MT6765G Helio G35 (12 nm)	64 GB	5000 mAh	1730000	Android 12
OPPO A96	8 GB	SM6225 Snapdragon 680 4G (6 nm)	256 GB	5000 mAh	3750000	Android 11
OPPO A55	4 GB	MT6765G Helio G35 (12 nm)	64 GB	5000 mAh	1800000	Android 11
OPPO A76	6 GB	SM6225 Snapdragon 680 4G (6 nm)	256 GB	4500 mAh	2580000	Android 11
OPPO A17	4 GB	MT6765 Helio G35 (12 nm)	64 GB	5000 mAh	1575000	Android 12
OPPO Reno8 T 5G	8 GB	Snapdragon 695 (SDM 695)	128 GB	4800 mAh	4700000	Android 13
\.


--
-- Name: handphone handphone_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.handphone
    ADD CONSTRAINT handphone_pk PRIMARY KEY (brand);


--
-- PostgreSQL database dump complete
--

