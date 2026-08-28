---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-describe-table.html
---

# DESCRIBE
<a name="querying-iceberg-describe-table"></a>

Describes table information.

## Synopsis
<a name="querying-iceberg-describe-table-synopsis"></a>

```
DESCRIBE [FORMATTED] [{{db_name}}.]{{table_name}}
```

When the `FORMATTED` option is specified, the output displays additional information such as table location and properties.

## Example
<a name="querying-iceberg-describe-table-example"></a>

```
DESCRIBE iceberg_table
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
