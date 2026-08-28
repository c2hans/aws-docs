---
source_url: https://docs.aws.amazon.com/athena/latest/ug/show-views.html
---

# SHOW VIEWS
<a name="show-views"></a>

Lists the Athena or Data Catalog views in a list of `STRING` type values. Each value in the list is the name of a view in the specified database, or in the current database if you omit the database name. Use the optional `LIKE` clause with a regular expression to restrict the list of view names. For Data Catalog views, lists only the views that use Athena SQL syntax. Other Data Catalog views are filtered out.

## Synopsis
<a name="synopsis"></a>

```
SHOW VIEWS [IN {{database_name}}] [LIKE '{{regular_expression}}']
```

### Parameters
<a name="parameters"></a>

**[IN database\_name]**
Specifies the `database_name` from which views will be listed. If omitted, the database from the current context is assumed.

**[LIKE 'regular\_expression']**
Filters the list of views to those that match the `regular_expression` you specify. Only the wild card character `*`, which indicates any character, or `|`, which indicates a choice between characters, can be used.

## Examples
<a name="examples"></a>

```
SHOW VIEWS
```

```
SHOW VIEWS IN marketing_analytics LIKE 'orders*'
```

See also [SHOW COLUMNS](show-columns.md), [SHOW CREATE VIEW](show-create-view.md), [DESCRIBE VIEW](describe-view.md), and [DROP VIEW](drop-view.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
