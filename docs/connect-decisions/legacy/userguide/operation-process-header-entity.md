---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/operation-process-header-entity.html
---

# process\_header
<a name="operation-process-header-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| process\_header | process\_id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| process\_id | string | Yes | Process ID. For example, order, work order, maintenance order, or process inquiry. |
| type | string | No | Type of process. For example, customer order, maintenance, or repair, etc. |
| company\_id1 | string | No | Company ID. |
| site\_id1 | string | No | Site or plant ID. |
| site\_location | string | No | Name of the location or section in site or plant. |
| planning\_group | string | No | Group planning the work. This field will be an organization entity in the source system. |
| execution\_group | string | No | Group executing the work. This field will be an organization entity in the source system. |
| program\_group | string | No | Long running program or project name used for group work. For example, maintenance campaign. |
| status | string | No | Status of the process. |
| revision | string | No | Revision number associated with planning or program group. |
| latest\_start\_date | timestamp | No | Latest start date for the process. |
| description | string | No | Process description. |
| priority | string | No | Priority of the process. |
| planned\_cost | double | No | Total planned costs for the process. |
| currency\_uom | string | No | Currency in which value is specified. |
| planned\_completion\_date | timestamp | No | Planned completion date of the process. |
| planned\_closing\_date | timestamp | No | Planned closing date of the process. |
| planned\_release\_date | timestamp | No | Date when the process is planned to be released. |
| planned\_start\_date | timestamp | No | Planned start date for the process. |
| actual\_completion\_date | timestamp | No | Actual completion date of the process. |
| actual\_closing\_date | timestamp | No | Actual close date of the process. |
| actual\_release\_date | timestamp | No | Actual release date for process. |
| actual\_start\_date | timestamp | No | Actual start date for process. |
| process\_url | string | No | URL to access process record in source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source | string | No | Source of data. |
| flex\_1 | string | No | Process flexible field 1 |
| flex\_2 | string | No | Process flexible field 2 |
| flex\_3 | string | No | Process flexible field 3 |
| flex\_4 | string | No | Process flexible field 4 |
| flex\_5 | string | No | Process flexible field 5 |

1Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| site\_id | Network | site | id |
| company\_id | Organization | company | id |
