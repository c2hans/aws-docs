---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/reference-fields-entity.html
---

# reference\_field

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| reference\_field | object\_name, object\_field, object\_field\_value, object\_field\_desc |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| company\_id<sup>2</sup> | string | No | Company ID. |
| object\_name | string | Yes<sup>1</sup> | For example, sites, or transportation lanes. |
| object\_field | string | Yes<sup>1</sup> | For example, site\_type, or trans\_mode. |
| object\_field\_value | string | Yes<sup>1</sup> | For example, site\_type:01, or trans\_mode:01. |
| object\_field\_desc | string | Yes<sup>1</sup> | For example, site\_type:01:DC, or trans\_mode:01:Surface. |

<sup>1</sup>You must enter a value. When you ingest data from SAP or EDI, the default value for *string* is SCN\_RESERVED\_NO\_VALUE\_PROVIDED.

<sup>2</sup>Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
