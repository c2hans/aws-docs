---
source_url: https://docs.aws.amazon.com/glue/latest/dg/hubspot-writing-to-entities.html
---

# Writing to HubSpot Entities
<a name="hubspot-writing-to-entities"></a>

## Prerequisites
<a name="hubspot-writing-prerequisites"></a>
+ A HubSpot object you would like to write to. You will need the object name such as contact or ticket.
+ The HubSpot connector supports following write operations:
  + INSERT
  + UPDATE
+ When using the `UPDATE` write operation, the `ID_FIELD_NAMES` option must be provided to specify the ID field for the records.

## Supported entities for Sync Destination
<a name="hubspot-supported-entities"></a>

| Entity | API Version | Will be supported as Destination Connector | Can be Inserted | Can be Updated |
| --- | --- | --- | --- | --- |
| Companies | v3 | Yes | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Contacts | v3 | Yes | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Deals | v3 | Yes | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Products | v3 | Yes | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Calls | v3 | Yes | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Meetings | v3 | Yes | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Notes | v3 | Yes | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Emails | v3 | Yes | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Tasks | v3 | Yes | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Postal Mails | v3 | Yes | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Custom Objects | v3 | Yes | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Tickets | v3 | Yes | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Associations | v4 | Yes | Yes (Single, Bulk) | No |
| Associations Labels | v4 | Yes | Yes (Single, Bulk) | Yes (Single, Bulk) |

**Examples**:

**INSERT Operation**

```
hubspot_write = glueContext.write_dynamic_frame.from_options(
    frame=frameToWrite,
    connection_type="hubspot",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "contact",
        "API_VERSION": "v3",
        "WRITE_OPERATION": "INSERT"
    }
)
```

**UPDATE Operation**

```
hubspot_write = glueContext.write_dynamic_frame.from_options(
    frame=frameToWrite,
    connection_type="hubspot",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "deal",
        "API_VERSION": "v3",
        "WRITE_OPERATION": "UPDATE",
        "ID_FIELD_NAMES": "hs_object_id"
    }
)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
