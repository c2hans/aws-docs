---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/replenishment-inbound-order-line-entity.html
---

# inbound\_order\_line
<a name="replenishment-inbound-order-line-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| inbound\_order\_line | id, order\_id, tpartner\_id, product\_id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes1 | Order line ID. The value must be unique. |
| order\_id2 | string | Yes1 | ID of parent order. |
| company\_id2 | string | No | Company ID. |
| tpartner\_id2 | string | Yes1 | Partner that the order will be sent to. |
| line\_creation\_date | timestamp | No | Line creation date. |
| product\_id2 | string | Yes1 | Product ID. |
| product\_group\_id2 | string | No | Product group ID. |
| supplier\_product\_id | string | No | Product number used by supplier. |
| order\_type | string | No | Type of order. |
| external\_line\_number | string | No | Alternate line number if used by customer system. |
| status | string | No | Status of the line, for example, canceled, closed, or open. |
| from\_site\_id2 | string | No | Site where order line originates. |
| to\_site\_id2 | string | No | Site where the order will arrive. |
| vendor\_status | string | No | Status of the line in the vendor system.. |
| cost | double | No | Cost of the product in company's currency, after all discounts. |
| cost\_uom | string | No | Cost UOM in company's currency. |
| submitted\_cost | double | No | Cost of the product at the time of submission, in company's currency. |
| submitted\_cost\_vendor | double | No | Cost of the product at the time of submission, in vendor's currency. |
| shipping\_cost | double | No | Inbound shipping cost from vendor to company. |
| tax\_cost | double | No | Tax cost for the product. |
| quantity\_submitted | double | Yes | Quantity submitted to vendor. |
| quantity\_confirmed | double | No | Quantity confirmed by the vendor. |
| quantity\_received | double | No | Quantity received into inventory. |
| quantity\_uom | string | No | Quantity UOM for the order line. |
| submitted\_date | timestamp | No | Date and time when the order was submitted to vendor. |
| expected\_delivery\_date | timestamp | No | Date when the order is expected to be delivered. |
| confirmation\_date | timestamp | No | Date and time when the order was confirmed by the vendor. |
| earliest\_ship\_date | timestamp | No | Earliest date and time when the vendor can ship products in this order. |
| latest\_ship\_date | timestamp | No | Latest date and time when the vendor can ship products in this order. |
| earliest\_delivery\_date | timestamp | No | Earliest date and time when the vendor can deliver products in this order. |
| latest\_delivery\_date | timestamp | No | Latest date and time when the vendor can deliver products in this order. |
| incoterm | string | No | Three letter incoterm code. |
| incoterm2 | string | No | Place of ownership transfer. |
| incoterm\_location\_1 | string | No | Incoterm location 1. Can be a site\_id or the location used on order/EDI. |
| incoterm\_location\_2 | string | No | Incoterm location 2. Can be a site\_id or the location used on order/EDI. |
| requisition\_number | string | No | Requisition number. |
| order\_receive\_date | timestamp | No | Date and time when the order is unloaded into the company location. |
| reservation\_id2 | string | No | Reservation ID associated with the line. |
| reference\_object | string | No | If record is created by or in response to another object / entity, then enter the entity name. For example, inbound\_order, outbound\_order |
| reference\_object\_type | string | No | If activity is created by or in response to a specific type of object, specify the type here. For example, PO (Purchase Order) vs TO (Transfer Order) |
| reference\_object\_id | string | No | ID of associated reference object. |
| reference\_detail\_id | string | No | ID of associated reference object ID's detail/line, if any. |
| inbound\_order\_line\_url | string | No | URL to access inbound order line record in source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source | string | No | Source of data. |
| sap\_lips\_\_vbeln | string | No | Delivery Number. Predicate key for SAP mapping. Upsert key for VTTP, LIKP.  |
| sap\_vttp\_\_tknum | string | No | Shipment Number. Predicate key for SAP mapping. Upsert key for VTTK.  |

1You must enter a value. When you ingest data from SAP or EDI, the default value for *string* is SCN\_RESERVED\_NO\_VALUE\_PROVIDED.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| tpartner\_id | Organization | trading\_partner | id |
| company\_id | Organization | company | id |
| product\_id | Product | product | id |
| from\_site\_id | Network | site | id |
| product\_group\_id | Product | product\_hierarchy | id |
| order\_id | Inbound | inbound\_order | id |
| reservation\_id | Planning | reservation | reservation\_id |
