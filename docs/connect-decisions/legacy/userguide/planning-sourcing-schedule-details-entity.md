---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/planning-sourcing-schedule-details-entity.html
---

# sourcing\_schedule\_details
<a name="planning-sourcing-schedule-details-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| sourcing\_schedule\_details | sourcing\_schedule\_detail\_id, sourcing\_schedule\_id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| sourcing\_schedule\_detail\_id | string | Yes | Schedule detail ID. |
| sourcing\_schedule\_id | string | Yes | Sourcing schedule ID. |
| company\_id1 | string | No | Displays the company ID. |
| product\_id1 | string | No | Product ID used if schedule details are for a specific product. |
| product\_group\_id1 | string | No | Product group ID used if schedule details are for a product group. |
| day\_of\_week | string | No | Day of the week when the supply schedule is active. Values can be integer or string: Sun: 0 Mon: 1 Tue: 2 Wed: 3 Thu: 4 Fri: 5 Sat: 6 |
| week\_of\_month | string | No | To be used when ordering X times in a month. To be used in conjunction with day\_of\_week. If used multiple times in a month, use multiple rows. |
| time\_of\_day | timestamp | No | If supply schedule detail is for a specific time in a day, use this field to enter that information. Only time value is used. |
| date | timestamp | No | If supply schedule detail is for a specific date, use this field to enter that information. Only date value is used. |
| source | string | No | Source of data. |
| source\_event\_id | string | No | ID of the event created in the source system.  |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
| product\_id | Product | product | id |
| product\_group\_id | Product | product\_hierarchy | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
