---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/outbound-fulfillment-order-line-entity.html
---

# outbound\_order\_line
<a name="outbound-fulfillment-order-line-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| outbound\_order\_line | id,cust\_order\_id, product\_id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes1 | Outbound order line ID. |
| cust\_order\_id | string | Yes1 | Outbound order ID. |
| company\_id2 | string | No | Company ID. |
| order\_date | timestamp | No | Date and time when customer order was placed. |
| product\_id2 | string | Yes1 | Product ID. |
| product\_group\_id2 | string | No | Product group ID. |
| customer\_tpartner\_id2 | string | No | Trading partner ID for customer. |
| status | string | No | Status of the customer order. |
| init\_quantity\_requested | double | No | Original order quantity. |
| final\_quantity\_requested | double | No | Final quantity after any cancellations or changes. |
| quantity\_uom | string | No | Quantity unit of measure for the order line. |
| requested\_delivery\_date | timestamp | No | Requested delivery date for order line. |
| promised\_delivery\_date | timestamp | No | Delivery date promised for order lines. |
| actual\_delivery\_date | timestamp | No |  Actual delivery date for order line. |
| list\_price | double | No | List price for product in order lines.. |
| sold\_price | double | No | Selling price for product in order line, after any promotions, price changes, discounts, and so on. |
| discount | double | No | Discount applied for order line for this product. |
| discount\_code | string | No | Discount code used on order line. |
| currency\_uom | string | No | UUOM for currency. |
| tax | double | No | Tax amount for order line. |
| incoterm1 | string | No | Place of ownership transfer. |
| incoterm2 | string | No | Place of ownership transfer. |
| ship\_from\_site\_id2 | string | No | Site ID where the product is shipped from. |
| ship\_to\_site\_id2 | string | No | Site ID where the product is shipped to. |
| ship\_to\_site\_address\_1 | string | No | Address of ship-to site. |
| ship\_to\_site\_address\_2 | string | No | Address of ship-to site. |
| ship\_to\_site\_address\_city | string | No | City of ship-to site. |
| ship\_to\_site\_address\_state | string | No | State of ship-to site. |
| ship\_to\_site\_address\_country | string | No | Country of ship-to site. |
| ship\_to\_site\_address\_zip | string | No | Postal code of ship-to site. |
| availability\_status | string | No | In-stock availability status of the product at the time of order. |
| quantity\_promised | double | No | Quantity promised on order line. |
| quantity\_delivered | double | No | Quantity delivered against this order line. |
| channel\_id | string | No | Channel ID that was used to place this order. |
| sap\_2lis\_11\_vahdr\_\_vbeln | string | No | Reference document number. Predicate key for SAP mapping. Upsert key for VEDA. |
| sap\_2lis\_11\_vaitm\_\_kunnr | string | No | Sold to party. Predicate key for SAP mapping. Upsert key for 0CUST\_SALES\_ATTR. |
| sap\_2lis\_11\_vaitm\_\_vkorg | string | No | Sales organization. Predicate key for SAP mapping. Upsert key for 0CUST\_SALES\_ATTR. |
| sap\_2lis\_11\_vaitm\_\_vtweg | string | No | Distribution channel. Predicate key for SAP mapping. Upsert key for 0CUST\_SALES\_ATTR. |
| sap\_2lis\_11\_vaitm\_\_spart | string | No | Division. Predicate key for SAP mapping. Upsert key for 0CUST\_SALES\_ATTR. |
| sap\_2lis\_11\_vaitm\_\_pkunre | string | No | Bill-to party. Predicate key for SAP mapping. |
| source | string | No | Source of data. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1You must enter a value. When you ingest data from SAP or EDI, the default value for *string* is SCN\_RESERVED\_NO\_VALUE\_PROVIDED.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
| product\_id | Product | product | id |
| product\_group\_id | Product | product\_hierarchy | id |
| customer\_tpartner\_id | Organization | trading\_partner | id |
| ship\_from\_site\_id, ship\_to\_site\_id | Network | site | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
