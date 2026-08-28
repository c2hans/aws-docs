---
source_url: https://docs.aws.amazon.com/athena/latest/ug/describe-view.html
---

# DESCRIBE VIEW
<a name="describe-view"></a>

Shows the list of columns for the specified Athena or AWS Glue Data Catalog view. Useful for examining the attributes of a complex view.

 For Data Catalog views, the output of the statement is controlled by Lake Formation access control and shows only the columns that the caller has access to.

## Synopsis
<a name="synopsis"></a>

```
DESCRIBE [{{db_name}}.]{{view_name}}
```

## Example
<a name="examples"></a>

```
DESCRIBE orders
```

See also [SHOW COLUMNS](show-columns.md), [SHOW CREATE VIEW](show-create-view.md), [SHOW VIEWS](show-views.md), and [DROP VIEW](drop-view.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
