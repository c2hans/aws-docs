---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/operation-process-operation-entity.html
---

# process\_operation
<a name="operation-process-operation-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| process\_operation | process\_operation\_id, process\_id |

The table below lists the column names supported by the *process\_operation* data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| process\_operation\_id | string | Yes | Type of process operation. |
| process\_id1 | string | Yes | Process ID. For example, process, work order, or maintenance order. |
| company\_id1 | string | No | Company ID. |
| type | string | No | Type of operation within the process. For example, open machine. |
| site\_location | string | No | Name of the location or section in site or plant. |
| status | string | No | Status of the process. |
| operation\_name | string | No | Name of the operation. |
| operation\_sequence | string | No | Sequence of the operation within the process. |
| planned\_start\_dttm | timestamp | No | Planned start date-time of operation. |
| planned\_end\_dttm | timestamp | No | Planned end date-time of operation. |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| process\_id | Operation | process\_header | process\_id |
| company\_id | Organization | company | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
