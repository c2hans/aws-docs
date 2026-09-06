---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/work-order-plan-entity.html
---

# work\_order\_plan
<a name="work-order-plan-entity"></a>

**Primary key (PK)**

The table below lists the column names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| work\_order\_plan | process\_id, product\_id, business\_process\_id, business\_process\_sequence |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| process\_id1 | string | Yes | Process ID. For example, order, work order, maintenance order, or process inquiry. |
| process\_product\_id | string | No | ID associated with the process and product. |
| preferred\_source | string | No | Describes if the product is sourced from inventory (that is, stocked to forecasted) or from direct purchase (for non-stocked products). |
| product\_id | string | Yes | Product ID (material) in the work order. |
| business\_process\_id | string | Yes | Business process identifier. For example, PO, PR, RFQ and so on. Product ID (material) in the work order. The plan should include both the purchasing and distribution business processes. |
| site\_id | string | No | The site linked to the business process. This field is optional for purchasing process and mandatory for distribution related processes. |
| business\_process\_sequence | int | Yes | Business process sequence. |
| duration | int | Yes | Unit in days. |
| notes | string | No | Additional notes on work order plan. |
| flex\_1 | string | No | Plan flexible field 1. |
| flex\_2 | string | No | Plan flexible field 2. |
| flex\_3 | string | No | Plan flexible field 3. |
| flex\_4 | string | No | Plan flexible field 4. |
| flex\_5 | string | No | Plan flexible field 5. |
| source\_event\_id | string | No | ID of the event created in the source system.  |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| process\_id | Insights | process\_header | id |
