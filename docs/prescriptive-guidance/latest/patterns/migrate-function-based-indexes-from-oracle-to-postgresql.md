---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-function-based-indexes-from-oracle-to-postgresql.html
---

# Migrate function-based indexes from Oracle to PostgreSQL
<a name="migrate-function-based-indexes-from-oracle-to-postgresql"></a>

*Veeranjaneyulu Grandhi and Navakanth Talluri, Amazon Web Services*

## Summary
<a name="migrate-function-based-indexes-from-oracle-to-postgresql-summary"></a>

Indexes are a common way to enhance database performance. An index allows the database server to find and retrieve specific rows much faster than it could without an index. But indexes also add overhead to the database system as a whole, so they should be used sensibly. Function-based indexes, which are based on a function or expression, can involve multiple columns and mathematical expressions. A function-based index improves the performance of queries that use the index expression.

Natively, PostgreSQL doesn't support creating function-based indexes using functions that have volatility defined as stable. However, you can create similar functions with volatility as `IMMUTABLE` and use them in index creation.

An `IMMUTABLE` function cannot modify the database, and it’s guaranteed to return the same results given the same arguments forever. This category allows the optimizer to pre-evaluate the function when a query calls it with constant arguments.

This pattern helps in migrating the Oracle function-based indexes when used with functions such as `to_char`, `to_date`, and `to_number` to the PostgreSQL equivalent.

## Prerequisites and limitations
<a name="migrate-function-based-indexes-from-oracle-to-postgresql-prereqs"></a>

**Prerequisites **
+ An active Amazon Web Services (AWS) account
+ A source Oracle database instance with the listener service set up and running
+ Familiarity with PostgreSQL databases

**Limitations**
+ Database size limit is 64 TB.
+ Functions used in index creation must be IMMUTABLE.

**Product versions**
+ All Oracle database editions for versions 11g (versions 11.2.0.3.v1 and later) and up to 12.2, and 18c
+ PostgreSQL versions 9.6 and later

## Architecture
<a name="migrate-function-based-indexes-from-oracle-to-postgresql-architecture"></a>

**Source technology stack**
+ An Oracle database on premises or on an Amazon Elastic Compute Cloud (Amazon EC2) instance, or an Amazon RDS for Oracle DB instance

**Target technology stack**
+ Any PostgreSQL engine

## Tools
<a name="migrate-function-based-indexes-from-oracle-to-postgresql-tools"></a>
+ **pgAdmin 4** is an open source management tool for Postgres. The pgAdmin 4 tool provides a graphical interface for creating, maintaining, and using database objects.
+ **Oracle SQL Developer** is an integrated development environment (IDE) for developing and managing Oracle Database in both traditional and cloud deployments.

## Epics
<a name="migrate-function-based-indexes-from-oracle-to-postgresql-epics"></a>

### Create a function-based index using a default function
<a name="create-a-function-based-index-using-a-default-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a function-based index on a column using the to\_char function. | Use the following code to create the function-based index.<pre>postgres=# create table funcindex( col1 timestamp without time zone);<br />CREATE TABLE<br />postgres=# insert into funcindex values (now());<br />INSERT 0 1<br />postgres=# select * from funcindex;<br />            col1<br />----------------------------<br /> 2022-08-09 16:00:57.77414<br />(1 rows)<br /> <br />postgres=# create index funcindex_idx on funcindex(to_char(col1,'DD-MM-YYYY HH24:MI:SS'));<br />ERROR:  functions in index expression must be marked IMMUTABLE</pre><br /> PostgreSQL doesn’t allow creating a function-based index without the `IMMUTABLE` clause. | DBA, App developer |
| Check the volatility of the function. | To check the function volatility, use the code in the *Additional information* section.   | DBA |

### Create function-based indexes using a wrapper function
<a name="create-function-based-indexes-using-a-wrapper-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a wrapper function. | To create a wrapper function, use the code in the *Additional information section*. | PostgreSQL developer |
| Create an index by using the wrapper function. | Use the code in the *Additional information* section to create a user-defined function with the keyword `IMMUTABLE` in the same schema as the application, and refer to it in the index-creation script.<br />If a user-defined function is created in a common schema (from the previous example), update the `search_path` as shown.<pre>ALTER ROLE <ROLENAME> set search_path=$user, COMMON;</pre> | DBA, PostgreSQL developer |

### Validate index creation
<a name="validate-index-creation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate index creation. | Validate that the index needs to be created, based on query access patterns. | DBA |
| Validate that the index can be used. | To check whether the function-based index is picked up by the PostgreSQL Optimizer, run an SQL statement using explain or explain analyze. Use the code in the *Additional information* section. If possible, gather the table statistics as well.If you notice the explain plan, PostgreSQL optimizer has chosen a function-based index because of the predicate condition. | DBA |

## Related resources
<a name="migrate-function-based-indexes-from-oracle-to-postgresql-resources"></a>
+ [Function-based indexes](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_indexes.htm#ADFNS00505) (Oracle documentation)
+ [Indexes on Expressions](https://www.postgresql.org/docs/9.4/indexes-expressional.html) (PostgreSQL documentation)
+ [PostgreSQL volatility](https://www.postgresql.org/docs/current/xfunc-volatility.html) (PostgreSQL documentation)
+ [PostgreSQL search\_path](https://www.postgresql.org/docs/current/ddl-schemas.html#DDL-SCHEMAS-PATH) (PostgreSQL documentation)
+ [Oracle Database 19c to Amazon Aurora PostgreSQL Migration Playbook](https://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/chap-oracle-aurora-pg.html)

## Additional information
<a name="migrate-function-based-indexes-from-oracle-to-postgresql-additional"></a>

**Create a wrapper function**

```
CREATE OR REPLACE FUNCTION myschema.to_char(var1 timestamp without time zone, var2 varchar) RETURNS varchar AS $BODY$ select to_char(var1, 'YYYYMMDD'); $BODY$ LANGUAGE sql IMMUTABLE;
```

**Create an index by using the wrapper function**

```
postgres=# create function common.to_char(var1 timestamp without time zone, var2 varchar) RETURNS varchar AS $BODY$ select to_char(var1, 'YYYYMMDD'); $BODY$ LANGUAGE sql IMMUTABLE;
CREATE FUNCTION
postgres=# create index funcindex_idx on funcindex(common.to_char(col1,'DD-MM-YYYY HH24:MI:SS'));
CREATE INDEX
```

**Check the volatility of the function**

```
SELECT DISTINCT p.proname as "Name",p.provolatile as "volatility" FROM pg_catalog.pg_proc p
 LEFT JOIN pg_catalog.pg_namespace n ON n.oid = p.pronamespace
 LEFT JOIN pg_catalog.pg_language l ON l.oid = p.prolang
 WHERE n.nspname OPERATOR(pg_catalog.~) '^(pg_catalog)$' COLLATE pg_catalog.default AND p.proname='to_char'GROUP BY p.proname,p.provolatile
ORDER BY 1;
```

**Validate that the index can be used**

```
explain analyze <SQL>

postgres=# explain select col1 from funcindex where common.to_char(col1,'DD-MM-YYYY HH24:MI:SS') = '09-08-2022 16:00:57';
                                                       QUERY PLAN
------------------------------------------------------------------------------------------------------------------------
 Index Scan using funcindex_idx on funcindex  (cost=0.42..8.44 rows=1 width=8)
   Index Cond: ((common.to_char(col1, 'DD-MM-YYYY HH24:MI:SS'::character varying))::text = '09-08-2022 16:00:57'::text)
(2 rows)
```
