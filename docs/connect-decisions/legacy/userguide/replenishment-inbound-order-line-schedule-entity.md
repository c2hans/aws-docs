---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/replenishment-inbound-order-line-schedule-entity.html
---

# inbound\_order\_line\_schedule
<a name="replenishment-inbound-order-line-schedule-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| inbound\_order\_line\_schedule | id, order\_id, order\_line\_id, product\_id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes 1 | Order line ID. The value must be unique. |
| order\_id2 | string | Yes 1 | ID of parent order. |
| order\_line\_id2 | string | Yes | ID of parent order line. |
| company\_id2 | string | No | Company ID. |
| status | string | No | Status of line, for example, submitted, or confirmed. The following are the reserved values for AWS Supply Chain.+  Can celled - Populated in SAP mapping. Also used for deleted. <br />+  Open - Not populated in SAP mapping. <br />+  Closed - Not populated in SAP mapping. <br />+  InTransit - Not populated in SAP mapping. <br />+  Confirmed - Not populated in SAP mapping.  Null is also an accepted value, or you can enter your own value.  |
| schedule\_creation\_date | timestamp | No | Schedule creation date. |
| product\_id2 | string | Yes 1 | Product ID. |
| external\_line\_number | string | No | External line number. |
| expected\_delivery\_date | timestamp | No | Expected delivery date of the products. |
| confirmation\_date | timestamp | No | Date and time when the vendor confirmed the order line schedule, or order. |
| goods\_issue\_date | timestamp | No | Date and time when the material was available at origin to ship. |
| material\_availability\_date | timestamp | No | Date and time when the material was available at origin to ship. |
| ship\_date | timestamp | No | Date and time when vendor will ship products in this order-line-schedule. |
| delivery\_date | timestamp | No | Date and time when the vendor can deliver products in this schedule. |
| quantity\_submitted | double | No | Quantity submitted to vendor (POs) or for transfer. |
| quantity\_confirmed | double | No | Quantity confirmed by the vendor. |
| quantity\_received | double | No | Quantity received into inventory at the destination. |
| sap\_lips\_\_vbeln | string | No | Delivery Number. Predicate key for SAP mapping. Upsert key for VTTP |
| sap\_vttp\_\_tknum | string | No | Shipment Number. Predicate key for SAP mapping. Upsert key for VTTK |
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
| order\_id | Inbound | inbound\_order | id |
| order\_line\_id | Inbound | inbound\_order\_line | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
