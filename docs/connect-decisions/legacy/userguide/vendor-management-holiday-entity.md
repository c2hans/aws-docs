---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/vendor-management-holiday-entity.html
---

# vendor\_holiday
<a name="vendor-management-holiday-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| vendor\_holiday | vendor\_tpartner\_id, outage\_start\_date, outage\_end\_date |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| company\_id2 | string | No | Company ID. |
| vendor\_tpartner\_id2 | string | Yes | Trading partner ID of the vendor. |
| outage\_start\_date | timestamp | Yes1 | Outage start date. |
| outage\_end\_date | timestamp | Yes1 | Outage end date. |
| outage\_type | string | No | Type of outage. |
| comment | string | No | Comment from the vendor. |

1You must enter a value. When you ingest data from SAP or EDI, the default value for *timestamp* date type value is 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
| vendor\_tpartner\_id | Organization | trading\_partner | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
