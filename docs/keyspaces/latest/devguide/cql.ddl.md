---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.ddl.html
---

# DDL statements (data definition language) in Amazon Keyspaces
<a name="cql.ddl"></a>

*Data definition language* (DDL) is the set of Cassandra Query Language (CQL) statements that you use to manage data structures in Amazon Keyspaces (for Apache Cassandra), such as keyspaces and tables. You use DDL to create these data structures, modify them after they are created, and remove them when they're no longer in use. Amazon Keyspaces performs DDL operations asynchronously. For more information about how to confirm that an asynchronous operation has completed, see [Asynchronous creation and deletion of keyspaces and tables](functional-differences.md#functional-differences.table-keyspace-management).

 The following DDL statements are supported:
+  [CREATE KEYSPACE](cql.ddl.keyspace.md#cql.ddl.keyspace.create)
+  [ALTER KEYSPACE](cql.ddl.keyspace.md#cql.ddl.keyspace.alter)
+  [DROP KEYSPACE](cql.ddl.keyspace.md#cql.ddl.keyspace.drop)
+  [USE](cql.ddl.keyspace.md#cql.ddl.keyspace.use)
+  [CREATE TABLE](cql.ddl.table.md#cql.ddl.table.create)
+  [ALTER TABLE](cql.ddl.table.md#cql.ddl.table.alter)
+  [RESTORE TABLE](cql.ddl.table.md#cql.ddl.table.restore)
+  [DROP TABLE](cql.ddl.table.md#cql.ddl.table.drop)
+  [CREATE TYPE](cql.ddl.type.md#cql.ddl.type.create)
+  [DROP TYPE](cql.ddl.type.md#cql.ddl.type.drop)

**Topics**
+ [Keyspaces](cql.ddl.keyspace.md)
+ [Tables](cql.ddl.table.md)
+ [User-defined types (UDTs)](cql.ddl.type.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
