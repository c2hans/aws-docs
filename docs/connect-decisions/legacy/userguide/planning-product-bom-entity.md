---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/planning-product-bom-entity.html
---

# product\_bom
<a name="planning-product-bom-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| product\_bom | id, product\_id, component\_product\_id |

The table below lists the column names supported by the data entity:

| column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes | Displays the BOM ID. |
| product\_id 2 | string | Yes | Product for which the BOM is defined. |
| site\_id 2 | string | No | Site for which the BOM is defined. |
| company\_id2 | string | No | Displays the company ID. |
| level | int | No | Displays the level of the BOM in multi-level BOM. |
| component\_product\_id | string | Yes 1 | Displays the component's product ID. |
| component\_quantity\_per | double | Yes | Quantity of component required to produce one unit of parent product. |
| component\_quantity\_uom | string | No | Unit of measurement of the component. |
| component\_line\_number | int | No | Line ID of the child record. |
| lifecycle\_phase | string | No | Information about the life cycle phase associated with the BOM. |
| assembly\_cost | double | No | UOM of the product. |
| assembly\_cost\_uom | string | No | Assembly cost of the product. |
| eff\_start\_date | timestamp | No | Dates from when the record is effective. |
| eff\_end\_date | timestamp | No | Dates till when the record is effective. |
| description | string | No | BOM description. |
| production\_process\_id | string | No | ID associated with a specific production process. |
| alternative\_product\_id | string | No1 | ID of the alternate product used in the BOM. |
| priority | string | No | Priority of the product or components used in the BOM. |
| alternate\_group\_id | string | No | ID of the alternate product group. |
| alternate\_product\_qty | double | No | Quantity of the alternate product used in the BOM. |
| alternate\_product\_qty\_uom | string | No | UOM associated with the quantity of the alternate product. |
| ratio | double | No | Ratio of the products in the BOM. |
| creation\_date | timestamp | No1 | Date when the BOM was created. |
| change\_date | timestamp | No1 | Date when the BOM was updated. |
| source | string | No | Source of data. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system.  |

1You must enter a value. When you ingest data from SAP or EDI, the default values for string and timestamp date type values are: SCN\_RESERVED\_NO\_VALUE\_PROVIDED for *string*; and for *timestamp* , 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
| product\_id | Product | product | id |
| site\_id | Network | site | id |
| production\_process\_id | Operation | production\_process | production\_process\_id |
| alternative\_product\_id | Product | product\_alternate | product\_alternate\_id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
