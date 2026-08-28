---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/planning-supply_planning_parameters-entity.html
---

# supply\_planning\_parameters
<a name="planning-supply_planning_parameters-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| supply\_planning\_parameters | product\_id, product\_group\_id, site\_id, eff\_start\_date, eff\_end\_date, connection\_id |

The table below lists the column names supported by the *supply\_planning\_parameters* data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| product\_id1 | string | Yes | ID of product |
| product\_group\_id1 | string | Yes |  For future Use. Please populate SCN\_RESERVED\_NO\_VALUE\_PROVIDED for now. |
| site\_id1 | string | Yes | For future Use. Please populate SCN\_RESERVED\_NO\_VALUE\_PROVIDED for now. |
| planner\_name | string | No | name of the supply planner who manages a product or a product group |
| demand\_time\_fence\_days | int | No | For future Use. |
| forecast\_consumption\_backward\_days | int | No | For future Use |
| forecast\_consumption\_forward\_days | int | No | For future Use. |
| eff\_start\_date | timestamp | Yes | effective start date time |
| eff\_end\_date | timestamp | Yes | effective end date time |
| connection\_id | string | Yes | Unique identifier for the data source (i.e. connection). Auto populated by ASC. |

1Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| product\_id | Product | product | id |
| product\_group\_id | Product | product\_hierarchy | id |
| site\_id | Network | site | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
