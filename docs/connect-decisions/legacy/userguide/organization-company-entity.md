---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/organization-company-entity.html
---

# company
<a name="organization-company-entity"></a>

**Primary key (PK)**

The table below lists the column names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| company | id |

The table below lists the column names supported by the data entity.

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes | ID of the company. |
| description | string | No | Description of the company. |
| address\_1 | string | No | Company address. |
| address\_2 | string | No | Company address. |
| address\_3 | string | No | Company address. |
| city | string | No | City where the company is located. |
| state\_prov | string | No | State where the company is located. |
| postal\_code | string | No | Postal code of the company address. |
| country | string | No | Country where the company is located. |
| phone\_number | string | No | Company's contact number. |
| time\_zone | string | No | Company's local time zone. |
| calendar\_id 1 | string | No | Default calendar that the company uses for planning. |
| source | string | No | Source of data. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| calendar\_id | Reference | calendar | calendar\_id |
