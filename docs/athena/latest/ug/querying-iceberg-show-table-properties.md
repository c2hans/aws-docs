---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-show-table-properties.html
---

# SHOW TBLPROPERTIES
<a name="querying-iceberg-show-table-properties"></a>

Shows one or more table properties of an Iceberg table. Only Athena-supported table properties are shown.

## Synopsis
<a name="querying-iceberg-show-table-properties-synopsis"></a>

```
SHOW TBLPROPERTIES [{{db_name}}.]{{table_name}} [('{{property_name}}')]
```

## Example
<a name="querying-iceberg-show-table-properties-example"></a>

```
SHOW TBLPROPERTIES iceberg_table
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
