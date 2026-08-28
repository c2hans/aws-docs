---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql_rds_kill_query_id.html
---

# mysql.rds\_kill\_query\_id
<a name="mysql_rds_kill_query_id"></a>

Ends a query running against the MariaDB server in order to terminate long-running or problematic queries. You can identify the query ID and effectively stop a specific query to address performance issues and maintain optimal database operation.

## Syntax
<a name="mysql_rds_kill_query_id-syntax"></a>

```
CALL mysql.rds_kill_query_id(queryID);
```

## Parameters
<a name="mysql_rds_kill_query_id-parameters"></a>

 *queryID*
Integer. The identity of the query to be ended.

## Usage notes
<a name="mysql_rds_kill_query_id-usage-notes"></a>

To stop a query running against the MariaDB server, use the `mysql.rds_kill_query_id` procedure and pass in the ID of that query. To obtain the query ID, query the MariaDB [Information schema PROCESSLIST table](http://mariadb.com/kb/en/mariadb/information-schema-processlist-table/), as shown following:

```
SELECT USER, HOST, COMMAND, TIME, STATE, INFO, QUERY_ID FROM
                INFORMATION_SCHEMA.PROCESSLIST WHERE USER = '<user name>';
```

The connection to the MariaDB server is retained.

## Examples
<a name="mysql_rds_kill_query_id-examples"></a>

The following example ends a query with a query ID of 230040:

```
call mysql.rds_kill_query_id(230040);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
