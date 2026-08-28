---
source_url: https://docs.aws.amazon.com/glue/latest/dg/connecting-to-smartsheet.html
---

# Connecting to Smartsheet
<a name="connecting-to-smartsheet"></a>

Smartsheet is a work management and collaboration SaaS product. Fundamentally, Smartsheet allows users to use spreadsheet-like objects to create, store, and utilize business data.

**Topics**
+ [AWS Glue support for Smartsheet](smartsheet-support.md)
+ [Policies containing the API operations for creating and using connections](smartsheet-configuring-iam-permissions.md)
+ [Configuring Smartsheet](smartsheet-configuring.md)
+ [Configuring Smartsheet connections](smartsheet-configuring-connections.md)
+ [Reading from Smartsheet entities](smartsheet-reading-from-entities.md)
+ [Smartsheet connection options](smartsheet-connection-options.md)
+ [Creating an Smartsheet account](smartsheet-create-account.md)
+ [Limitations](smartsheet-connector-limitations.md)

**Entities with dynamic metadata:**

For the following entity, Smartsheet provides an endpoint to fetch metadata dynamically, allowing operator support to be captured at the datatype level.

| Entity |  Data Type  | Supported Operators |
| --- | --- | --- |
| Sheet Data | String | NA |
| Sheet Data | Long | "=" |
| Sheet Data | Integer | NA |
| Sheet Data | DateTime | > |

 **Example**

```
Smartsheet_read = glueContext.create_dynamic_frame.from_options(
    connection_type="smartsheet",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "list-sheets",
        "API_VERSION": "2.0",
        "INSTANCE_URL": "https://api.smartsheet.com"
    }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
