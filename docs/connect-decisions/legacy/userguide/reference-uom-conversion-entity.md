---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/reference-uom-conversion-entity.html
---

# uom\_conversion
<a name="reference-uom-conversion-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| uom\_conversion | uom, conversion\_uom\_id, eff\_start\_date, eff\_end\_date |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| uom | string | Yes | Unit of measure (UOM). For example, weight\_uom, currency\_uom. |
| company\_id2 | string | No | Company ID. |
| uom\_code | string | No | Alternate code for UOM. |
| uom\_description | string | No | UOM description. |
| uom\_type | string | No | UOM type, for example, currency, weight, volume, or unit. |
| conversion\_uom\_id | string | Yes | UOM ID for conversion. |
| conversion\_factor | double | Yes | Conversion factor. |
| eff\_start\_date | timestamp | Yes1 | Effective start date and time. |
| eff\_end\_date | timestamp | Yes1 | Effective end date and time. |
| source | string | No | Source of data. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1You must enter a value. When you ingest data from SAP or EDI, the default value for *timestamp* date type value is 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
