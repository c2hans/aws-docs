---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/customer-cost-entity.html
---

# customer\_cost
<a name="customer-cost-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| customer\_cost | cost\_id, incurred\_date |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| cost\_id | string | Yes1 | A unique identifier for each cost record associated with an user.  |
| customer\_id2 | string | Yes | The unique identifier for the user incurring the cost.  |
| incurred\_date | timestamp | Yes1 | The date and time when the cost was incurred. Displays the timestamp of cost.  |
| order\_id2 | string | No | The unique identifier of the user order associated with the cost.  |
| shipment\_id2 | string | No | Unique identifier of the outbound shipment.  |
| cost\_type | string | No | Displays the cost type. For example, handling, packing, storage, and shipping.  |
| amount | double | No | The amount of cost incurred by the user.  |
| amount\_uom | string | No | Unit of measure for the amount of cost incurred by the user.  |
| tax 1 | string | No | Tax amount incurred by the user. |
| tax 2 | string | No | Tax amount incurred by the user. |
| tax 3 | string | No | Tax amount incurred by the user. |
| tax\_uom | string | No | Unit of measure for the tax amount.  |
| currency\_uom | string | No | Unit of measure for the currency.  |
| payment\_status | string | No | The status of the payment. For example, Pending Paid.  |
| incoterm | string | No | A set of internationally recognized rules which define the responsibilities of sellers and buyers in the export transaction. For example, FOB, ExWorks, DDP. |
| source | string | No | Source of data. |
| source\_event\_id | string | No | ID of the event created in the source system. For example, PO receipt, Shipment schedule, and so on. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |
| discount\_1 | double | No | The discount associated for a specific cost ID. |
| discount\_2 | double | No | The additional discount associated for a specific cost ID. |
| discount\_3 | double | No | The additional discount associated for a specific cost ID. |
| online\_order\_id | string | No | Unique identifier for the order line. |

1You must enter a value. When you ingest data from SAP or EDI, the default value for *string* is SCN\_RESERVED\_NO\_ VALUE\_PROVIDED and the default value for *timestamp* date type value is 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| customer\_id | Organization | trading\_partner | id |
| order\_id | Outbound fulfillment | outbound\_order\_line | id |
| shipment\_id | Outbound fulfillment | outbound\_shipment | id |
| order\_line\_id | Outbound fulfillment | outbound\_order\_line | id |
