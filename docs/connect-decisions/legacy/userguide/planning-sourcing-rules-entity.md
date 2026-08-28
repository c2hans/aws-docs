---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/planning-sourcing-rules-entity.html
---

# sourcing\_rules
<a name="planning-sourcing-rules-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| sourcing\_rules | sourcing\_rule\_id, eff\_start\_date, eff\_end\_date |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| sourcing\_rule\_id | string | Yes | Sourcing rule ID. |
| company\_id2 | string | No | Displays the company ID. |
| product\_id2 | string | No | Product ID to be sourced. |
| to\_site\_id2 | string | No | Site ID into which product will be sourced. |
| from\_site\_id2 | string | No | Site ID from which product will be sourced. |
| product\_group\_id2 | string | No | Product group ID. |
| sourcing\_rule\_type | string | No | Type of sourcing rule. The supported sourcing rule types are transfer, buy, and manufacture. Only lower case is allowed. |
| tpartner\_id2 | string | No | Trading partner ID is used depending on sourcing rule type. For example, when sourcing rule type is Buy, Buy is the Vendor ID and you can use this vendor ID along with other attributes to find additional details from vendor\_product and other entities. |
| tpartner\_location | string | No | The location of the trading partner. For example, Seattle, China, New Mexico, and so on. |
| transportation\_lane\_id | string | No | Transportation lane ID is used depending on sourcing rule type. For example, when sourcing type is Transfer, you can use this ID along with other attributes to choose the correct transportation\_lane. |
| sourcing\_priority2 | int | No | Priority of sourcing rule. |
| sourcing\_ratio | double | No | Proportion of product to be sourced from this product/group, to\_site, from\_site/tpartner\_id combination. All sources for a product, site should add to 1 for a specific time period (or application normalizes the ratio to 1). |
| qty\_uom | string | No | Quantity UOM associated with sourcing rule. |
| min\_qty | double | No | Minimum quantity for the sourcing rule. |
| max\_qty | double | No | Maximum quantity for the sourcing rule. |
| qty\_multiple | double | No | Quantity is in multiples of this value. |
| eff\_start\_date | timestamp | Yes1 | Effective start date of the calendar. |
| eff\_end\_date | timestamp | Yes1 | Effective end date of the calendar. |
| source | string | No | Source of data. |
| production\_process\_id | string | No | Type of process operation. For example, stop machine. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1You must enter a value. When you ingest data from SAP or EDI, the default values for *timestamp* is, 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the column names with a foreign key:

|  | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| to\_site\_id, from\_site\_id | Network | site | id |
| company\_id | Organization | company | id |
| product\_id | Product | product | id |
| product\_group\_id | Product | product\_hierarchy | id |
| tpartner\_id | Organization | trading\_partner | id |
| transportation\_lane\_id | Network | transporatation\_lane | id |
| production\_process\_id | Operation | production\_process | production\_process\_id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
