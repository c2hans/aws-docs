---
source_url: https://docs.aws.amazon.com/glue/latest/dg/docusign-monitor-reading-from-entities.html
---

# Reading from Docusign Monitor entities
<a name="docusign-monitor-reading-from-entities"></a>

**Prerequisite**

A Docusign Monitor object you would like to read from.

**Supported entities for source**:

| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| --- | --- | --- | --- | --- | --- |
| Monitoring Data | Yes | Yes | No | Yes | No |

**Example**:

```
docusignmonitor_read = glueContext.create_dynamic_frame.from_options(
    connection_type="docusign_monitor",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "monitoring-data",
        "API_VERSION": "v2.0"
    }
```

## Docusign Monitor entity and field details
<a name="docusign-monitor-reading-from-entities-field-details"></a>

Entities with static metadata:

- **Monitoring Data**
  - **Field:** timestamp / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** eventId / **Data type:** String / **Supported operators:** N/A
  - **Field:** application / **Data type:** String / **Supported operators:** N/A
  - **Field:** environment / **Data type:** String / **Supported operators:** N/A
  - **Field:** site / **Data type:** String / **Supported operators:** N/A
  - **Field:** traceToken / **Data type:** String / **Supported operators:** N/A
  - **Field:** organizationId / **Data type:** String / **Supported operators:** N/A
  - **Field:** accountId / **Data type:** String / **Supported operators:** N/A
  - **Field:** userId / **Data type:** String / **Supported operators:** N/A
  - **Field:** object / **Data type:** String / **Supported operators:** N/A
  - **Field:** action / **Data type:** String / **Supported operators:** N/A
  - **Field:** property / **Data type:** String / **Supported operators:** N/A
  - **Field:** field / **Data type:** String / **Supported operators:** N/A
  - **Field:** result / **Data type:** String / **Supported operators:** N/A
  - **Field:** IntegratorKey / **Data type:** String / **Supported operators:** N/A
  - **Field:** customerVisible / **Data type:** String / **Supported operators:** N/A
  - **Field:** version / **Data type:** String / **Supported operators:** N/A
  - **Field:** userAgent / **Data type:** String / **Supported operators:** N/A
  - **Field:** userAgentClientInfo / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** ipAddress / **Data type:** String / **Supported operators:** N/A
  - **Field:** ipAddressLocation / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** data / **Data type:** String / **Supported operators:** N/A
  - **Field:** source / **Data type:** String / **Supported operators:** N/A
  - **Field:** latitude / **Data type:** Double / **Supported operators:** N/A
  - **Field:** longitude / **Data type:** Double / **Supported operators:** N/A
  - **Field:** city / **Data type:** String / **Supported operators:** N/A
  - **Field:** state / **Data type:** String / **Supported operators:** N/A
  - **Field:** country / **Data type:** String / **Supported operators:** N/A
  - **Field:** usUserMemberOfDomain / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** affectedUserIsMemberOfDomain / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** proxyStatus / **Data type:** String / **Supported operators:** N/A
  - **Field:** proxyType / **Data type:** String / **Supported operators:** N/A
  - **Field:** proxyLevel / **Data type:** String / **Supported operators:** N/A
  - **Field:** referencedUserId / **Data type:** String / **Supported operators:** N/A
  - **Field:** device / **Data type:** String / **Supported operators:** N/A
  - **Field:** browser / **Data type:** String / **Supported operators:** N/A
  - **Field:** cursor / **Data type:** DateTime / **Supported operators:** EQUAL\_TO

**Partitioning queries**

Docusign Monitor doesn’t support either field-based or record-based partitioning.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
