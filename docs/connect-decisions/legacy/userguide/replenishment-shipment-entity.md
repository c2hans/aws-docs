---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/replenishment-shipment-entity.html
---

# shipment
<a name="replenishment-shipment-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| shipment | id, supplier\_tpartner\_id, product\_id, order\_id, order\_line\_id, package\_id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes | Shipment ID. |
| creation\_date | timestamp | No | Creation date. |
| packaging\_hierarchy\_type | string | No | Information on how the shipment is structured, for example, container, pallet, carton, or pallet. |
| supplier\_tpartner\_id2 | string | Yes1 | Supplier partner ID of the vendor. |
| supplier\_description | string | No | Partner description. |
| company\_id2 | string | No | Company ID. |
| customer\_description | string | No | Customer description. |
| ship\_from\_site\_id2 | string | No | Site where this shipment starts from. |
| ship\_from\_site\_description | string | No | Site description for outbound shipments. |
| ship\_from\_site\_address\_1 | string | No | Address of ship-from site. |
| ship\_from\_site\_address\_2 | string | No | Address of ship-from site. |
| ship\_from\_site\_address\_city | string | No | Site shipping city. |
| ship\_from\_site\_address\_state | string | No | Site shipping state. |
| ship\_from\_site\_address\_country | string | No | Site shipping country. |
| ship\_from\_site\_address\_zip | string | No | Site shipping postal code. |
| ship\_to\_site\_id2 | string | No | Site where this shipment ends. |
| ship\_to\_site\_description | string | No | Site description for inbound shipments. |
| ship\_to\_site\_address\_1 | string | No | Address of ship-to site. |
| ship\_to\_site\_address\_2 | string | No | Address of ship-to site. |
| ship\_to\_site\_address\_city | string | No | Site shipping city. |
| ship\_to\_site\_address\_state | string | No | Site shipping state. |
| ship\_to\_site\_address\_country | string | No | Site shipping country. |
| ship\_to\_site\_address\_zip | string | No | Site shipping postal code. |
| origin\_port | string | No | Port of loading. |
| destination\_port | string | No | Port of destination. |
| transportation\_mode | string | No | Mode of transport. |
| routing\_sequence | string | No | Routing sequence ID from the ASN. |
| routing\_description | string | No | Routing description. |
| carrier\_id2 | string | No | ID of the carrier. |
| carrier\_description | string | No | Carrier description. |
| service\_level | string | No | Service level of shipment. |
| transportation\_id | string | No | Vessel code or trailer number. |
| transportation\_description | string | No | Vessel description. |
| conveyance\_id | string | No | Trip number. |
| bill\_of\_lading\_number | string | No | Bill of lading number. |
| master\_bill\_of\_lading\_number | string | No | Master bill of lading number. |
| carrier\_reference\_number | string | No | Carrier reference number. |
| shipper\_reference\_number | string | No | Shipper reference number. |
| equipment\_code | string | No | Equipment code. |
| equipment\_number | string | No | Equipment number. |
| seal\_number | string | No | Seal number. |
| equipment\_type | string | No | Type of equipment. |
| package\_type | string | No | Type of package. |
| package\_quantity | double | No | Quantity of the package. |
| weight\_qualifier | string | No | Code specifying the type of weight in EDI, for example, consolidated weight. |
| weight | double | No | Weight of the product. |
| weight\_uom | string | No | Weight UOM of the product. |
| shipment\_status | string | No | Status of the shipment. |
| planned\_ship\_date | timestamp | No | Planned shipping date. |
| actual\_ship\_date | timestamp | No | Actual shipping date. |
| planned\_delivery\_date | timestamp | No | Planned delivery date. |
| actual\_delivery\_date | timestamp | No | Actual delivery date. |
| carrier\_eta\_date | timestamp | No | ETA date from the carrier. |
| latest\_milestone | string | No | Text or string field required to capture event or status related to the milestone\_date, for example, arrived at consolidation center. |
| latest\_milestone\_date | timestamp | No | Latest milestone date. |
| incoterms | string | No | Three letter incoterm code. |
| line\_id | string | No | Shipment line ID. |
| product\_id2 | string | Yes | Product ID. |
| product\_description | string | No | Product description. |
| tp\_product\_id | string | No | Trading partner product ID. |
| upc | string | No | UPC |
| units\_shipped | double | No | Units shipped. |
| uom | string | No | UOM. |
| hts\_code | string | No | Harmonized Tariff Schedule code. |
| order\_id2 | string | Yes1 | Order ID. |
| order\_type | string | No | Order type. |
| order\_customer\_tpartner\_id | string | No | Customer ID of the order. |
| order\_supplier\_tpartner\_id | string | No | Supplier ID of the order. |
| order\_line\_id2 | string | Yes1 | Order line ID. |
| ship\_to\_site2 | string | No | Final ship to location. |
| package\_id | string | Yes1 | Package ID. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source | string | No | Source of data. |
| volume | double | No | Volume of the shipment. |
| volume\_uom | string | No | Volume unit of measurement of the shipment. |
| sap\_vttp\_\_vbeln | string | No | Delivery Number. Predicate key for SAP mapping. Upsert key for LIKP, LIPS. |
| sap\_but021\_fs\_\_addrnumber | string | No | Address Number. Predicate key for ADRC (for Ship-to Address). |
| sap\_t001w\_\_adrnr | string | No | Address Number. Predicate key for SAP mapping. Upsert key for ADRC. |
| sap\_vttk\_\_bev1\_rpmowa | string | No | Vehicle number. Predicate key for SAP mapping. Upsert key for Equi. |
| units\_received | double | No | Represent the received quantity for a shipment for users who track receipts at a shipment level. |

1You must enter a value. When you ingest data from SAP or EDI, the default value for *string* is SCN\_RESERVED\_NO\_VALUE\_PROVIDED.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| supplier\_tpartner\_id | Organization | trading\_partner | id |
| company\_id | Organization | company | id |
| ship\_from\_site\_id, ship\_to\_site\_id, ship\_to\_site | Network | site | id |
| product\_id | Product | product | id |
| order\_id | Inbound | inbound\_order | id |
| order\_line\_id | Inbound | inbound\_order\_line | id |
