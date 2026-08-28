---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/operation-production-process-entity.html
---

# production\_process
<a name="operation-production-process-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| production\_process | production\_process\_id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| production\_process\_id | string | Yes | ID associated with the process and product. |
| production\_process\_type | string | No | Type of the specific production process. For example, assembly, machining. |
| production\_process\_name | string | No | Name of the specific production process. For example, milling, drilling, welding. |
| product\_id1 | string | No | Product associated with the production process. |
| company\_id1 | string | No | Company ID associated with the production process. |
| site\_id1 | string | No | Site ID where the production process is taking place. |
| start\_location | string | No | Location where the process starts. |
| end\_location | string | No | Location where the process ends. |
| setup\_time | double | No | Time to setup the process. |
| setup\_time\_uom | string | No | Unit of measure of the setup time. |
| operation\_time | double | No | Total time to complete the process. |
| operation\_time\_uom | string | No | Unit of measure of the operation time. |
| frozen\_horizon | double | No | Time period when there are no changes to the production process. |
| frozen\_horizon\_uom | string | No | Unit of measure for the frozen horizon. |
| unit\_cost | double | No | Cost of the production process. |
| cost\_uom | string | No | Unit of measure of the production process cost. |
| source | string | No | Source of data. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |
| source\_event\_id | string | No | ID of the event created in the source system. |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column name |
| --- | --- | --- | --- |
| product\_id | Product | product | id |
| company\_id | Organization | company | id |
| site\_id | Network | site | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
