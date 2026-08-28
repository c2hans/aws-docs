---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/planning-reservation-entity.html
---

# reservation
<a name="planning-reservation-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| reservation | reservation\_id, reservation\_detail\_id |

The table below lists the column names supported by the *reservation* data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| reservation\_id | string | Yes | Reservation ID. |
| reservation\_detail\_id | string | Yes | Reservation detail ID. |
| reservation\_type | string | No | Type of reservation. For example, procurement or build-to-stock. |
| company\_id1 | string | No | Company ID. |
| status | string | No | Status of the reservation. |
| product\_id1 | string | No | Product ID. |
| site\_id1 | string | No | Site ID. |
| quantity | double | No | Reservation quantity. |
| quantity\_uom | string | No | Quantity UOM associated with reservation. |
| reservation\_date | timestamp | No | Date when the reservation is generated. |
| is\_deleted | string | No | Yes or No indicator to indicate whether the reservation is deleted or not. |
| requisition\_id1 | string | No | Source object identifier reference to inbound order type. |
| requisition\_line\_id1 | string | No | Source object identifier reference to inbound order line. |
| rfq\_id1 | string | No | Source object identifier reference to inbound order type RFQ. |
| rfq\_line\_id1 | string | No | Source object identifier reference to inbound order line of type RFQ. |
| order\_id1 | string | No | Source object identifier reference to inbound order. |
| order\_line\_id1 | string | No | Source object identifier reference to inbound order line. |
| order\_line\_schedule\_id1 | string | No | Source object identifier reference to inbound order line schedule. |
| stock\_transfer\_1\_order\_id | string | No | Stock transfer order ID. |
| stock\_transfer\_1\_order\_line\_id | string | No | Stock transfer order line ID. |
| stock\_transfer\_2\_order\_id | string | No | Stock transfer order ID. |
| stock\_transfer\_2\_order\_line\_id | string | No | Stock transfer order line ID. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source | string | No | Source of data. |
| flex\_1 | string | No | Reservation flexible field 1 |
| flex\_2 | string | No | Reservation flexible field 2 |
| flex\_3 | string | No | Reservation flexible field 3 |
| flex\_4 | string | No | Reservation flexible field 4 |
| flex\_5 | string | No | Reservation flexible field 5 |

1Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| site\_id | Network | site | id |
| company\_id | Organization | company | id |
| product\_id | Product | product | id |
| requisition\_id, rfq\_id | Inbound | inbound\_order\_line | order\_id |
| requisition\_line\_id, rfq\_line\_id | Inbound | inbound\_order\_line | id |
| order\_line\_schedule\_id | Inbound | inbound\_order\_line\_schedule | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
