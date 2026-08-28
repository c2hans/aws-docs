---
source_url: https://docs.aws.amazon.com/glue/latest/dg/sap-odata-writing.html
---

# Writing to SAP OData
<a name="sap-odata-writing"></a>

 This section describes how to write data to your SAP OData Service using the AWS Glue connector for SAP OData.

**Prerequisites**
+ Access to an SAP OData service
+ An SAP OData EntitySet Object you would like to write to. You will need the Object name.
+ Valid SAP OData credentials and a valid connection
+ Appropriate permissions as described in [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-configuring-iam-permissions.html)

The SAP OData connector supports two write operations:
+ INSERT
+ UPDATE

While using the UPDATE write operation, ID\_FIELD\_NAMES must be provided to specify the external ID field for the records.

**Example:**

```
sapodata_write = glueContext.write_dynamic_frame.from_options(
    frame=frameToWrite,
    connection_type="sapodata",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "WRITE_OPERATION": "INSERT"
    }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
