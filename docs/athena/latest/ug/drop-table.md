---
source_url: https://docs.aws.amazon.com/athena/latest/ug/drop-table.html
---

# DROP TABLE
<a name="drop-table"></a>

Removes the metadata table definition for the table named `table_name`. When you drop an external table, the underlying data remains intact.

## Synopsis
<a name="synopsis"></a>

```
DROP TABLE [IF EXISTS] table_name
```

## Parameters
<a name="parameters"></a>

**[ IF EXISTS ]**
Causes the error to be suppressed if `table_name` doesn't exist.

## Examples
<a name="examples"></a>

```
DROP TABLE fulfilled_orders
```

```
DROP TABLE IF EXISTS fulfilled_orders
```

When using the Athena console query editor to drop a table that has special characters other than the underscore (\_), use backticks, as in the following example.

```
DROP TABLE `my-athena-database-01.my-athena-table`
```

When using the JDBC connector to drop a table that has special characters, backtick characters are not required.

```
DROP TABLE my-athena-database-01.my-athena-table
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
