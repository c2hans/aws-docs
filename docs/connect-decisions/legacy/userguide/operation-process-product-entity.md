---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/operation-process-product-entity.html
---

# process\_product
<a name="operation-process-product-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| process\_product | process\_product\_id, process\_id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| process\_product\_id1 | string | Yes | ID associated with the process and product. |
| process\_id1 | string | Yes | Process ID. For example, order, work order, maintenance order, or process inquiry. |
| process\_operation\_id1 | string | No | Process operational ID. This is an optional field. |
| company\_id1 | string | No | Company ID. |
| product\_id1 | string | No | Product ID of the requested product. |
| type | string | No | Type associated within the process. For example, consumption or production. |
| product\_value | double | No | Monetary value of product being requested. |
| currency\_uom | string | No | Currency UOM of the product. |
| status | string | No | Status of the product process. |
| requested\_availability\_date | timestamp | No | Date when the material was requested to be available. |
| quantity\_submitted | double | No | Quantity submitted as part of the process for product. |
| quantity\_confirmed | double | No | Quantity confirmed against the request. |
| quantity\_consumed | double | No | Quantity consumed against the quantity on this process/work order. |
| reservation\_id1 | string | No | Link to reservation ID associated with this record. |
| reservation\_detail\_id1 | string | No | Link to reservation detail ID associated with this record. |
| quantity\_uom | string | No | Unit of measure for quantity. |
| process\_product\_url | string | No | URL to access process product record in source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| allocation\_status | string | No | Status of the allocation for the product. |
| allocation\_type | string | No | Type of allocation for the product. |
| flex\_1 | string | No | Process flexible field 1. |
| flex\_2 | string | No | Process flexible field 2. |
| flex\_3 | string | No | Process flexible field 3. |
| flex\_4 | string | No | Process flexible field 4. |
| flex\_5 | string | No | Process flexible field 5. |
| reservation\_type | string | No | Type of reservation of the product. |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column name |
| --- | --- | --- | --- |
| product\_id | Product | product | id |
| company\_id | Organization | company | id |
| process\_id | Operation | process\_header | process\_id |
| process\_operation\_id | Operation | process\_operation | process\_operation\_id |
| reservation\_id | Planning | reservation | reservation\_id |
| reservation\_detail\_id | Planning | reservation | reservation\_detail\_id |
