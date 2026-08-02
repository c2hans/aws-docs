---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/replenishment-shipment-stop-order-entity.html
---

# shipment\_stop\_order
<a name="replenishment-shipment-stop-order-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| shipment\_stop\_order | shipment\_stop\_order\_id, shipment\_stop\_id, shipment\_id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| shipment\_stop\_order\_id | string | Yes | Shipment stop order ID. |
| shipment\_stop\_id1 | string | Yes | Shipment stop ID. |
| shipment\_id1 | string | Yes | Shipment ID. |
| company\_id1 | string | No | Company ID. |
| site\_id1 | string | No | Site ID. |
| inbound\_order\_id1 | string | No | Inbound order ID. |
| inbound\_order\_line\_id1 | string | No | Inbound order line ID. |
| inbound\_order\_line\_schedule\_id1 | string | No | Inbound order line schedule ID. |
| action | string | No | Pickup or drop off shipment. |
| quantity | double | No | Quantity associated with action and order. |
| quantity\_uom | string | No | Quantity UOM of the shipment. |
| source\_event\_id | string | No | ID of the event created in the source system.  |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
| site\_id | Network | site | id |
| shipment\_id | Inbound | shipment | id |
| shipment\_stop\_id | Inbound | shipment\_stop | shipment\_stop\_id |
| inbound\_order\_id | Inbound | inbound\_order\_line | order\_id |
| inbound\_order\_line\_id | Inbound | inbound\_order\_line | id |
| inbound\_order\_line\_schedule\_id | Inbound | inbound\_order\_line\_schedule | id |
