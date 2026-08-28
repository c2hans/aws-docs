---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/product-alternate-entity.html
---

# product\_alternate
<a name="product-alternate-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| product\_alternate | product\_alternate\_id, eff\_start\_date, eff\_end\_date |

**Note**
To avoid data ingestion failure, you must enter a value for *eff\_start\_date* and *eff\_end\_date*.

The table below lists the column names supported by the data entity:

|  Column name | Data type | Required | Description |
| --- | --- | --- | --- |
| product\_alternate\_id | string | Yes | Unique identifier for a record. |
| product\_id 2 | string | Yes | Product ID. |
| alternative\_product\_id | string | Yes | Alternate product ID. |
| site\_id | string | No | Site ID. |
| alternate\_type | string | No | Alternate product type. For example, similar\_demand\_value. |
| company\_id 2 | string | No | Company ID. |
| priority | int | No | Priority or rank of alternatives. |
| alternate\_group\_id | string | No | Used to group interchangeable alternate products. Note, this field does not correspond to product\_group in product\_hierarchy. |
| status | string | No | Status of the alternate product record. For example, Active, Inactive. |
| alternate\_product\_qty | double | No | Quantity of the alternate product. The conversion is done per base\_UOM of primary product. |
| alternate\_product\_qty\_uom | string | No | Unit of measure (UOM) of alternative product quantity. |
| eff\_start\_date | timestamp | Yes | Displays the date and time the record becomes effective. |
| eff\_end\_date  | timestamp | Yes | Displays the date and time the record ends. |
| source | string | No | Source of data.  |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1You must enter a value. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| product\_id | Product | product | id |
| company\_id | Organization | company | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
