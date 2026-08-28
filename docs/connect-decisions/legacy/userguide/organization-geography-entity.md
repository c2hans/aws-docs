---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/organization-geography-entity.html
---

# geography
<a name="organization-geography-entity"></a>

**Primary key (PK)**

The table below lists the column names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| geography | id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes | Geographical ID. Referred to by other entities as geo\_id or region\_id. |
| description | string | No | Geographical location. |
| company\_id 1 | string | No | Company ID. |
| parent\_geo\_id 1 | string | No | Stores parent geographical ID for this record. If blank, this is a top level region in the company. |
| address\_1 | string | No | City corresponding to this geo-region. |
| address\_2 | string | No | City corresponding to this geo-region. |
| address\_3 | string | No | City corresponding to this geo-region. |
| city | string | No | Displays the city corresponding to this geo-region. |
| state\_prov | string | No | State corresponding to this geo-region. |
| postal\_code | string | No | Postal code corresponding to this geo-region. |
| country | string | No | Country corresponding to this geo-region. |
| phone\_number | string | No | Company's contact number. |
| time\_zone | string | No | Company local time zone. |
| source | string | No | Source of data. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1 Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
| parent\_geo\_id | Organization | geography | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
