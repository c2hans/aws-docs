---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/network-site-entity.html
---

# site
<a name="network-site-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| site | id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes | Site ID. |
| description | string | No | Description of the site. |
| company\_id1 | string | No | Company ID. |
| geo\_id1 | string | No | If the site belongs to a geography, displays the ID of the geographical hierarchy. |
| address\_1 | string | No | Site address. |
| address\_2 | string | No | Site address. |
| address\_3 | string | No | Site address. |
| city | string | No | City in which the site is located. |
| state\_prov | string | No | State where the site is located. |
| postal\_code | string | No | Postal code of the site. |
| country | string | No | Country where the site is located. |
| phone\_number | string | No | Contact number of the site. |
| email | string | No | Point of contacts email information. |
| time\_zone | string | No | Local time zone of the site. |
| site\_type | string | No | Type of site, for example, warehouse, delivery station, factory, store, and so on. |
| unlocode | string | No | Standardized UN/LOCODE for the site. |
| latitude | double | No | Latitude of the site location. |
| longitude | double | No | Longitude of the site location. |
| is\_active | string | No | Indicates whether site is active ("true") or deleted ("false") |
| site\_calendar\_id1 | string | No | Site's operating and holiday calendar. |
| site\_classifier | string | No | Information about site classification. For example, if a store is "high foot fall store" or if DC is Central DC vs Regional DC. |
| open\_date | timestamp | No | Date when the site started operations. |
| end\_date | timestamp | No | Date when the site discontinued operational perspective. |
| source | string | No | Source of data. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
| geo\_id | Organization | geography | id |
| site\_calendar\_id | Reference | calendar | calendar\_id |
