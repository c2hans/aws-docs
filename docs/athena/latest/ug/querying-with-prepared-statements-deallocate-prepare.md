---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-deallocate-prepare.html
---

# DEALLOCATE PREPARE
<a name="querying-with-prepared-statements-deallocate-prepare"></a>

Removes the prepared statement with the specified name from the list of prepared statements in the current workgroup.

## Syntax
<a name="querying-with-prepared-statements-deallocate-prepare-syntax"></a>

```
DEALLOCATE PREPARE {{statement_name}}
```

{{statement\_name}} is the name of the prepared statement to be removed.

## Example
<a name="querying-with-prepared-statements-deallocate-prepare-examples"></a>

The following example removes the `my_select1` prepared statement from the current workgroup.

```
DEALLOCATE PREPARE my_select1
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
