---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/planning-sourcing-schedule-entity.html
---

# sourcing\_schedule
<a name="planning-sourcing-schedule-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| sourcing\_schedule | sourcing\_schedule\_id, eff\_start\_date, eff\_end\_date |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| sourcing\_schedule\_id | string | Yes | Sourcing schedule ID. |
| company\_id2 | string | No | Displays the company ID. |
| tpartner\_id2 | string | No | Trading partner ID. |
| status | string | No | Status of the supply schedule. For example, active, inactive. |
| from\_site\_id2 | string | No | Origin site ID. For example, hub, vendor. |
| to\_site\_id2 | string | No | Destination site ID. For example, hub or a customer in the network. |
| schedule\_type | string | No | Type of schedule. For example, inbound ordering, outbound shipping. |
| eff\_start\_date | timestamp | Yes1 | Date-time when schedule becomes effective. |
| eff\_end\_date | timestamp | Yes1 | Date-time till when schedule is effective. |
| source | string | No | Source of data. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1You must enter a value. When you ingest data from SAP or EDI, the default values for *timestamp* is, 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| from\_site\_id, to\_site\_id | Network | site | id |
| company\_id | Organization | company | id |
| tpartner\_id | Organization | trading\_partner | id |
