---
source_url: https://docs.aws.amazon.com/athena/latest/ug/show-create-view.html
---

# SHOW CREATE VIEW
<a name="show-create-view"></a>

Shows the SQL statement that created the specified Athena or Data Catalog view. The SQL returned shows the create view syntax used in Athena. Calling `SHOW CREATE VIEW` on Data Catalog views requires Lake Formation admin or view definer permissions.

## Synopsis
<a name="synopsis"></a>

```
SHOW CREATE VIEW {{view_name}}
```

## Examples
<a name="examples"></a>

```
SHOW CREATE VIEW orders_by_date
```

See also [CREATE VIEW and CREATE PROTECTED MULTI DIALECT VIEW](create-view.md) and [DROP VIEW](drop-view.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
