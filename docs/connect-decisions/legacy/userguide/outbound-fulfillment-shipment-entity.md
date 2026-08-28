---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/outbound-fulfillment-shipment-entity.html
---

# outbound\_shipment
<a name="outbound-fulfillment-shipment-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| outbound\_shipment | id, cust\_order\_id, cust\_order\_line\_id, product\_id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes 1 | Outbound shipment ID. |
| company\_id2 | string | No | Company ID. |
| cust\_order\_id2 | string | Yes 1 | Customer order ID.  |
| cust\_order\_line\_id2 | string | Yes 1 | Customer order line ID. |
| product\_id2 | string | Yes 1 | Product ID. |
| shipped\_qty | double | No | Shipment quantity. |
| cust\_shipment\_status | string | No | Status of the shipment, for example, canceled, open, closed, or delivered. |
| expected\_ship\_date | timestamp | No | Date product was expected to ship from the company location. |
| actual\_ship\_date | timestamp | No | Date product was actually shipped from the company location. |
| from\_site\_id2 | string | No | Site ID where the product is shipped from. |
| to\_site\_id2 | string | No | Destination site ID for outbound shipments. |
| expected\_delivery\_date | timestamp | No | Expected delivery date of the products to the customer. |
| actual\_delivery\_date | timestamp | No | Displays when the product was actually delivered to the customer. |
| shipping\_cost | double | No | Final shipping cost. |
| tracking\_number | string | No | Tracking number associated with the shipment. |
| bill\_weight | double | No | Shipped weight of product used for billing. |
| sap\_2lis\_08trtlp\_\_vbeln | string | No | Delivery number. Predicate key for SAP mapping. Upsert key for 2LIS\_12\_VCITM. |
| sap\_2lis\_08trtlp\_\_posnr | string | No | Delivery item number. Predicate key for SAP mapping. Upsert key for 2LIS\_12\_VCITM. |
| sap\_2lis\_08trtlp\_\_tknum | string | No | Shipment item number. Predicate key for SAP mapping. Upsert key for 2LIS\_08TRTK. |
| source | string | No | Source of data. |
| source\_event\_id | string | No | ID of the event created in the source system.  |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |
| tpartner\_id | string | No | Unique identifier for a trading partner. |
| service\_level | string | No |  Focuses on the quality and speed of the shipment. For example, Standard, next day, two-day, expedited, and so on. |

1You must enter a value. When you ingest data from SAP or EDI, the default value for *string* is SCN\_RESERVED\_NO\_ VALUE\_PROVIDED.

2Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
| product\_id | Product | product | id |
| cust\_order\_line\_id | OutboundFulfillment | outbound\_order\_line | id |
| cust\_order\_id | OutboundFulfillment | outbound\_order\_line | cust\_order\_id |
| from\_site\_id, to\_site\_id | Network | site | id |
| tpartner\_id | Organization | trading\_partner | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
