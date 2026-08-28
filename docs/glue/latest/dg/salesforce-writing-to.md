---
source_url: https://docs.aws.amazon.com/glue/latest/dg/salesforce-writing-to.html
---

# Writing to Salesforce
<a name="salesforce-writing-to"></a>

**Prerequisites**

A Salesforce sObject you would like to write to. You will need the object name such as `Account` or `Case` or `Opportunity`.

The Salesforce connector supports four write operations:
+ INSERT
+ UPSERT
+ UPDATE
+ DELETE

When using the `UPSERT` write operation, the `ID_FIELD_NAMES` option must be provided to specify the external ID field for the records.

 You can also add connection options:
+  `TRANSFER_MODE`: Supports two modes: `SYNC` and `ASYNC`. Default is `SYNC`. When set to `ASYNC`, Bulk API 2.0 Ingest will be utilized for processing.
+  `FAIL_ON_FIRST_ERROR`: The default value is `FALSE`, which means the AWS Glue job will continue processing all the data even if there are some failed write records. When set to `TRUE`, the AWS Glue job will fail if there are any failed write records, and it will not continue processing.

**Example**

```
salesforce_write = glueContext.write_dynamic_frame.from_options(
    frame=frameToWrite,
    connection_type="salesforce",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "Account",
        "API_VERSION": "v60.0",
        "WRITE_OPERATION": "INSERT",
        "TRANSFER_MODE": "ASYNC",
        "FAIL_ON_FIRST_ERROR": "true"
    }
)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
