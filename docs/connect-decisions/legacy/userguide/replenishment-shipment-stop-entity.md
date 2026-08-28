---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/replenishment-shipment-stop-entity.html
---

# shipment\_stop
<a name="replenishment-shipment-stop-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| shipment\_stop | shipment\_stop\_id, shipment\_id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| shipment\_stop\_id | string | Yes | Shipment stop ID. |
| shipment\_id1 | string | Yes | Shipment ID. |
| sequence | int | No | Sequence of the shipment. |
| company\_id1 | string | No | Company ID. |
| site\_id1 | string | No | Site ID. |
| planned\_arrival\_start\_dttm | timestamp | No | Planned start date and time for the shipment arrival. |
| planned\_arrival\_end\_dttm | timestamp | No | Planned end date and time for the shipments arrival. |
| planned\_departure\_start\_dttm | timestamp | No | Planned start date and time for the shipment departure. |
| planned\_departure\_end\_dttm | timestamp | No | Planned end date and time for the shipment departure. |
| actual\_arrival\_start\_dttm | timestamp | No | Actual start date and time for the shipment arrival. |
| actual\_arrival\_end\_dttm | timestamp | No | Actual end date and time for the shipments arrival. |
| actual\_departure\_start\_dttm | timestamp | No | Actual start date and time for the shipment departure. |
| actual\_departure\_end\_dttm | timestamp | No | Actual end date and time for the shipment departure. |
| appointment\_numberAWS Supply Chain web application will display this column as *appointment\_number*. | string | No | Appointment number. |
| delivery\_number | string | No | Delivery number of the shipment. |
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
