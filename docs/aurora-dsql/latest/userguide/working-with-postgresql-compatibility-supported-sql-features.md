---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-postgresql-compatibility-supported-sql-features.html
---

# Supported SQL for Aurora DSQL
<a name="working-with-postgresql-compatibility-supported-sql-features"></a>

Aurora DSQL supports a wide range of core PostgreSQL SQL features. In the following sections, you can learn about general PostgreSQL expression support. This list is not exhaustive.

## `SELECT` command
<a name="dsql-select"></a>

Aurora DSQL supports the following clauses of the `SELECT` command.

| Primary clause | Supported clauses |
| --- | --- |
| `FROM` |  |
| `GROUP BY` | `ALL`, `DISTINCT` |
| `ORDER BY` | `ASC`, `DESC`, `NULLS` |
| `LIMIT` |  |
| `DISTINCT` |  |
| `HAVING` |  |
| `USING` |  |
| `WITH` (common table expressions) |  |
| `INNER JOIN` | `ON` |
| `OUTER JOIN` | `LEFT`, `RIGHT`, `FULL`, `ON` |
| `CROSS JOIN` | `ON` |
| `UNION` | `ALL` |
| `INTERSECT` | `ALL` |
| `EXCEPT` | `ALL` |
| `OVER` | `RANK ()`, `PARTITION BY` |
| `FOR UPDATE` |  Specify equality predicates on all primary key columns (for example, `WHERE pk = value`). If you use range, `IN`, `OR`, or other non-equality predicates, the query returns `ERROR: locking clause such as FOR UPDATE can be applied only on tables with equality predicates on the key`. <br /> Specify on a single table query. If you use joins or multiple tables, the query returns `ERROR: locking clause such as FOR UPDATE can be applied on a single table`.  |

## Data Definition Language (DDL)
<a name="dsql-ddl"></a>

Aurora DSQL supports the following PostgreSQL DDL commands.

| Command | Primary Clause | Supported Clauses |
| --- | --- | --- |
| `CREATE` | `TABLE` | For information about the supported syntax of the `CREATE TABLE` command, see [`CREATE TABLE`](create-table-syntax-support.md). |
| `ALTER` | `TABLE` | For information about the supported syntax of the `ALTER TABLE` command, see [`ALTER TABLE`](alter-table-syntax-support.md). |
| `DROP` | `TABLE` |  |
| `CREATE` | `[UNIQUE] INDEX ASYNC` | You can use this command with the following parameters: `ON`, `NULLS FIRST`, `NULLS LAST`.<br />For information about the supported syntax of the `CREATE INDEX ASYNC` command, see [Asynchronous indexes in Aurora DSQL](working-with-create-index-async.md). |
| `DROP` | `INDEX` |  |
| `CREATE` | `VIEW` | For more information about the supported syntax of the `CREATE VIEW` command, see [`CREATE VIEW`](create-view.md).  |
| ALTER | VIEW | For information about the supported syntax of the `ALTER VIEW` command, see [`ALTER VIEW`](alter-view-syntax-support.md). |
| DROP | VIEW | For information about the supported syntax of the DROP VIEW command, see [`DROP VIEW`](drop-view-overview.md). |
| `CREATE` | `SEQUENCE` | For information about the supported syntax of the `CREATE SEQUENCE` command, see [`CREATE SEQUENCE`](create-sequence-syntax-support.md). |
| `ALTER` | `SEQUENCE` | For information about the supported syntax of the `ALTER SEQUENCE` command, see [`ALTER SEQUENCE`](alter-sequence-syntax-support.md). |
| `DROP` | `SEQUENCE` | For information about the supported syntax of the `DROP SEQUENCE` command, see [`DROP SEQUENCE`](drop-sequence-syntax-support.md). |
| `CREATE` | `ROLE`, `WITH` |  |
| `CREATE` | `FUNCTION` | `LANGUAGE SQL` |
| `CREATE` | `DOMAIN` |  |

## Data Manipulation Language (DML)
<a name="dsql-dml"></a>

Aurora DSQL supports the following PostgreSQL DML commands.

| Command | Primary clause | Supported clauses |
| --- | --- | --- |
| `INSERT` | `INTO` | `VALUES`<br />`SELECT`<br />`[ON CONFLICT]` |
| `UPDATE` | `SET` | `WHERE (SELECT)`<br />`FROM, WITH` |
| DELETE | FROM | USING, WHERE |

## Data Control Language (DCL)
<a name="dsql-dcl"></a>

Aurora DSQL supports the following PostgreSQL DCL commands.

| Command | Supported clauses |
| --- | --- |
| `GRANT` | `ON`, `TO` |
| `REVOKE` | `ON`, `FROM`, `CASCADE`, `RESTRICT` |

## Transaction Control Language (TCL)
<a name="dsql-tcl"></a>

Aurora DSQL supports the following PostgreSQL TCL commands.

| Command | Supported clauses | Alias |
| --- | --- | --- |
| `COMMIT` | [`WORK` \| `TRANSACTION`]<br />[`AND NO CHAIN`] | `END` |
| `BEGIN` | [`WORK` \| `TRANSACTION`]<br />[`ISOLATION LEVEL REPEATABLE READ`]<br />[`READ WRITE` \| `READ ONLY`] |  |
| `START TRANSACTION` | [`ISOLATION LEVEL REPEATABLE READ`]<br />[`READ WRITE` \| `READ ONLY`] |  |
| `ROLLBACK` | [`WORK` \| `TRANSACTION`]<br />[`AND NO CHAIN`] | `ABORT` |

## Utility commands
<a name="dsql-utility"></a>

Aurora DSQL supports the following PostgreSQL utility commands:
+ `EXPLAIN`
+ `ANALYZE` (relation name only)
