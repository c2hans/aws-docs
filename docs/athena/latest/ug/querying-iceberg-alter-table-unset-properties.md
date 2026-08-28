---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-alter-table-unset-properties.html
---

# ALTER TABLE UNSET TBLPROPERTIES
<a name="querying-iceberg-alter-table-unset-properties"></a>

Drops existing properties from an Iceberg table.

## Synopsis
<a name="querying-iceberg-alter-table-unset-properties-synopsis"></a>

```
ALTER TABLE [{{db_name}}.]{{table_name}} UNSET TBLPROPERTIES ('{{property_name}}' [ , ... ])
```

## Example
<a name="querying-iceberg-alter-table-unset-properties-example"></a>

```
ALTER TABLE iceberg_table UNSET TBLPROPERTIES ('write_compression')
```

The following example removes the `write.data.path` property from an Iceberg table.

```
ALTER TABLE iceberg_table UNSET TBLPROPERTIES ('write.data.path')
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
