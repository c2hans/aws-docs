---
source_url: https://docs.aws.amazon.com/glue/latest/dg/adobe-marketo-engage-writing-to-entities.html
---

# Writing to Adobe Marketo Engage entities
<a name="adobe-marketo-engage-writing-to-entities"></a>

**Prerequisites**
+ An Adobe Marketo object you would like to write to. You will need the object name such as `leads` or `customobjects`.
+ The Adobe Marketo connector supports three write operations:
  + INSERT
  + UPSERT
  + UPDATE
+ For `UPSERT` and `UPDATE` write operations, you must provide the `ID_FIELD_NAMES` option to specify the ID field for the records. When working with the `leads` entity, use `email` as `ID_FIELD_NAMES` for `UPSERT` operations and `id` for `UPDATE` operations. For the `customobjects` entity, use `marketoGUID` as `ID_FIELD_NAMES` for both `UPDATE` and `UPSERT` operations.

**Supported entities for Destination (Synchronous)**

| Entity name | Will be supported as Destination Connector | Can be Inserted | Can be Updated | Can be Upserted |
| --- | --- | --- | --- | --- |
| leads | Yes | Yes(Bulk) | Yes(Bulk) | Yes(Bulk) |
| customobjects | Yes | Yes(Bulk) | Yes(Bulk) | Yes(Bulk) |

**Example**:

**INSERT Operation:**

```
marketo_write = glueContext.write_dynamic_frame.from_options(
    frame=frameToWrite,
    connection_type="marketo",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "leads",
        "API_VERSION": "v1",
        "WRITE_OPERATION": "INSERT"
    }
```

**UPDATE Operation:**

```
marketo_write = glueContext.write_dynamic_frame.from_options(
    frame=frameToWrite,
    connection_type="marketo",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "leads",
        "API_VERSION": "v1",
        "WRITE_OPERATION": "UPDATE",
        "ID_FIELD_NAMES": "id"
    }
```

**Note**
For the `leads` and `customobjects` entities, Adobe Marketo provides endpoints to fetch metadata dynamically so the writable fields are identified from the Marketo API response.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
