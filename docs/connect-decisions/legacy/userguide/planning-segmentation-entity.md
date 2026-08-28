---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/planning-segmentation-entity.html
---

# segmentation
<a name="planning-segmentation-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| segmentation | segment\_id, creation\_date, site\_id, product\_id, eff\_start\_date, eff\_end\_date |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| segment\_id | string | Yes | Segment ID. |
| creation\_date | timestamp | Yes | Date and time that the segment was created. |
| company\_id2 | string | No | Displays the company ID. |
| site\_id2 | string | Yes | Overrides policies specified for the region for this node in the product hierarchy. |
| product\_id2 | string | Yes1 | Overrides policies specified for the product-group for this node in the geo hierarchy. |
| segment\_description | string | No | Segment description. |
| segment\_type | string | No | Type of segmentation, for example, value based, demand variability based, or demand speed based. |
| segment\_value | double | No | Metric associated with the segment calculated when the segment is generated. Value depends on segment\_type. |
| source | string | No | Information about the segment creator. |
| eff\_start\_date | timestamp | Yes1 | Effective start date of the calendar. |
| eff\_end\_date | timestamp | Yes1 | Effective end date of the calendar. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1You must enter a value. When you ingest data from SAP or EDI, the default values for string and timestamp date type values are SCN\_RESERVED\_NO\_VALUE\_PROVIDED for *string*; and for *timestamp* , 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| site\_id | Network | site | id |
| company\_id | Organization | company | id |
| product\_id | Product | product | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
