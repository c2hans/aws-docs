---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/reference-calendar-entity.html
---

# calendar
<a name="reference-calendar-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| calendar | calendar\_id, date, eff\_start\_date, eff\_end\_date |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| calendar\_id | string | Yes1 | Calendar ID. |
| company\_id2 | string | No | Company ID. |
| name | string | No | Calendar name. |
| calendar\_type | string | No | Type of Calender, based on customer data. |
| description | string | No | Calendar description. |
| date | timestamp | Yes | Date associated with each calendar record. |
| year | int | Yes | Calendar year. |
| day | int | Yes | Calendar day. |
| week | int | Yes | Calendar week. |
| month | int | Yes | Calendar month. |
| is\_working | string | No | Boolean value that checks if the date is working. |
| is\_holiday | string | No | Boolean value that checks if this date is a holiday. |
| eff\_start\_date | timestamp | Yes1 | Effective start date of the calendar. |
| eff\_end\_date | timestamp | Yes1 | Effective end date of the calendar. |
| source | string | No | Source of data. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1You must enter a value. When you ingest data from SAP or EDI, the default values for string and timestamp date type values are SCN\_RESERVED\_NO\_VALUE\_PROVIDED for *string*; and for *timestamp*, 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
