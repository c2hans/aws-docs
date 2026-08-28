---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/product-uom-entity.html
---

# product\_uom
<a name="product-uom-entity"></a>

**Primary key (PK)**

The table below lists the column names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| product\_bom | product\_uom\_id, eff\_start\_date, eff\_end\_date |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| product\_uom\_id | string | Yes | ID for product unit of measurement (UOM) combination. |
| product\_id | string | Yes | Product associated with product-uom combination. |
| uom | string | Yes | UOM identifier. |
| description | string | No | Description of product-uom. |
| company\_id 1 | string | No | Company ID. |
| price | double | No | Price of product-uom. |
| cost | double | No | Cost of product-uom. |
| currency\_uom | string | No | Unit of measure (UOM) of currency. |
| status | string | No | Status of record. For example, Active, Inactive and so on.  |
| is\_standard | string | No | Describe if this is a standard product-uom.  |
| barcode\_type | string | No | Type of barcode.  |
| barcode\_value | string | No | Value of barcode.  |
| type | string | No | Type of product-uom.  |
| quantity | double | No | Displays the quantity for one product uom ID in terms of base UOM for the product.  |
| quantity\_uom | string | No | Unit of measure (UOM) of quantity in base UOM.  |
| length | double | No | Length of the package.  |
| width | double | No | Width of the package.  |
| height | double | No | Height of the package.  |
| dimension\_uom | string | No | Unit of measure (UOM) of dimension.  |
| volume | double | No | Volume of the package.  |
| volume\_uom | string | No | Unit of measure (UOM) of volume.  |
| weight | double | No | Package weight.  |
| weight\_uom | string | No | Unit of measure (UOM) of weight.  |
| eff\_start\_date  | timestamp | Yes | Displays the date and time the record becomes effective. |
| eff\_end\_date  | timestamp | Yes | Displays the date and time the record ends. |
| source | string | No | Source of data.  |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
