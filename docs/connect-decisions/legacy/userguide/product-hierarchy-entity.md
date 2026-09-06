---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/product-hierarchy-entity.html
---

# product\_hierarchy
<a name="product-hierarchy-entity"></a>

**Primary key (PK)**

The table below lists the column names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| product\_hierarchy | id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes | Product group ID. |
| description | string | No | Description of the product group. |
| company\_id1 | string | No | Company ID. |
| parent\_product\_group\_id1 | string | No | Parent of this product group. If null, it indicates this record is a top level product group. |
| creation\_date | timestamp | No | Date when the product group was created. |
| update\_date | timestamp | No | Date when the product group was updated. |
| source | string | No | Source of data. |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
| parent\_product\_group\_id | Product | product\_hierarchy | id |
