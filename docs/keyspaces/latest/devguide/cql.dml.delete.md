---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.dml.delete.html
---

# DELETE
<a name="cql.dml.delete"></a>

Use the `DELETE` statement to remove a row from a table.

**Syntax**

```
delete_statement ::=  DELETE [ simple_selection ( ',' simple_selection ) ]
                      FROM table_name
                      [ USING update_parameter ( AND update_parameter )* ]
                      WHERE where_clause
                      [ IF ( EXISTS | condition ( AND condition )*) ]

simple_selection ::=  column_name
                     | column_name '[' term ']'
                     | column_name '.' `field_name

condition        ::=  simple_selection operator term
```

Where:
+ `table_name` is the table that contains the row you want to delete.

**Example**

```
DELETE manager_id FROM "myGSGKeyspace".employees_tbl WHERE id='789-01-2345' AND division='Executive' ;
```

`DELETE` supports the following value as `update_parameter`:
+ `TIMESTAMP` – A `bigint` value representing the number of microseconds since the standard base time known as the epoch: January 1 1970 at 00:00:00 GMT.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
