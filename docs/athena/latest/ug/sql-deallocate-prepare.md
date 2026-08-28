---
source_url: https://docs.aws.amazon.com/athena/latest/ug/sql-deallocate-prepare.html
---

# DEALLOCATE PREPARE
<a name="sql-deallocate-prepare"></a>

Removes the prepared statement with the specified name from the prepared statements in the current workgroup.

## Synopsis
<a name="sql-deallocate-prepare-synopsis"></a>

```
DEALLOCATE PREPARE statement_name
```

## Examples
<a name="sql-deallocate-prepare-examples"></a>

The following example removes the `my_select1` prepared statement from the current workgroup.

```
DEALLOCATE PREPARE my_select1
```

## Additional resources
<a name="sql-deallocate-prepare-additional-resources"></a>

[Use prepared statements](querying-with-prepared-statements-querying.md)

[PREPARE](sql-prepare.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
