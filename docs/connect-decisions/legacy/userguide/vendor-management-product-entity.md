---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/vendor-management-product-entity.html
---

# vendor\_product
<a name="vendor-management-product-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| vendor\_product | vendor\_tpartner\_id, product\_id, eff\_start\_date, eff\_end\_date |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| company\_id2 | string | No | Company ID. |
| vendor\_tpartner\_id2 | string | Yes | Trading partner ID of the vendor. |
| product\_id2 | string | Yes | Product ID. |
| vendor\_product\_code | string | No | Product identifier used by the vendor. |
| vendor\_product\_desc | string | No | Product description used by the vendor. |
| vendor\_cost | double | No | Cost of product from this vendor. |
| vendor\_cost\_uom | string | No | Unit of measure (UOM) of the product cost from this vendor. |
| status | string | No | Status of the product, for example, new product (NP), and obsolete (OB). |
| unit\_volume | double | No | Volume of one unit of product. |
| volume\_uom | string | No | Unit of measure (UOM) for volume. |
| unit\_weight | double | No | Weight of one unit of product. |
| weight\_uom | string | No | Weight unit of measurement for weight. |
| release\_date | timestamp | No | Date when the product was released by the vendor. |
| end\_date | timestamp | No | Date when the vendor stopped supplying the product. |
| eff\_start\_date | timestamp | Yes1 | Displays the date and time from when the vendor's product is active. |
| eff\_end\_date | timestamp | Yes1 | Displays the date and time till when the vendor's product will be active. |
| min\_order\_unit | double | No | Minimum order quantity for a product from this vendor. |
| country\_of\_origin | string | No | Country of origin by product. |
| sap\_eina\_\_infnr | string | No | Record on number of purchases. Predicate key for SAP mapping. Upsert key for EINE. |
| sap\_eine\_\_ebeln | string | No | Purchasing Document Number. Predicate key for SAP mapping. Upsert key for EKPO. |
| sap\_eine\_\_ebelp | string | No | Item Number of Purchasing Document. Predicate key for SAP mapping. Upsert key for EKPO. |
| max\_order\_unit | double | No | Maximum order quantity for the vendor. |
| source | string | No | Source of data. |
| source\_event\_id | string | No | ID of the event created in the source system.  |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1You must enter a value. When you ingest data from SAP or EDI, the default value for *timestamp* date type value is 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
| vendor\_tpartner\_id | Organization | trading\_partner | id |
| product\_id | Product | product\_id | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
