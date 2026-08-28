---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/vendor-management-lead-time-entity.html
---

# vendor\_lead\_time
<a name="vendor-management-lead-time-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| vendor\_lead\_time | vendor\_tpartner\_id, product\_id, product\_group\_id, site\_id, region\_id, eff\_start\_date, eff\_end\_date |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| company\_id2 | string | No | Company ID. |
| vendor\_tpartner\_id2 | string | Yes | Trading partner ID of the vendor. |
| product\_id2 | string | Yes1 | Product ID. |
| product\_group\_id2 | string | Yes1 |  Used if lead time is set at product-group level. |
| site\_id2 | string | Yes1 | Site where this product is being supplied. |
| region\_id2 | string | Yes1 | Used if lead time is set at geographical region level. Site level values will override this value. |
| planned\_lead\_time | double | No | Planned lead time from vendor into company's site. |
| planned\_lead\_time\_dev | double | No | Standard deviation of lead time. |
| actual\_lead\_time\_mean | double | No | Field to store actual lead time computed from transactional data. |
| actual\_lead\_time\_sd | double | No | Standard deviation of actual lead time. |
| actual\_p50 | double | No | 50th percentile of actual lead time. |
| actual\_p90 | double | No | 90th percentile of actual lead time. |
| shipping\_cost | double | No | Inbound shipping cost from vendor to company. |
| cost\_uom | string | No | Unit of measure of shipping cost. |
| we\_pay | string | No | Yes or No indicator. Yes if company pays for inbound shipping, and No if vendor pays for shipping. |
| eff\_start\_date | timestamp | Yes1 | Date and time from when this record is effective. |
| eff\_end\_date | timestamp | Yes1 | Date and time till when this record is effective. |
| sap\_eina\_\_infnr | string | No | Record on number of purchases. Predicate key for SAP mapping. Upsert key for EINE. |
| source\_site\_id 2 | string | No | Site from where the inbound shipment is originated. |
| trans\_mode | string | No | Transportation mode. For example, ship, water, truck, or rail. |
| source | string | No | Source of data. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1You must enter a value. When you ingest data from SAP or EDI, the default values for string and timestamp date type values are SCN\_RESERVED\_NO\_VALUE\_PROVIDED for *string*; and for *timestamp*, 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| site\_id | Network | site | id |
| source\_site\_id | Network | site | id |
| company\_id | Organization | company | id |
| region\_id | Organization | geography | id |
| vendor\_tpartner\_id | Organization | trading\_partner | id |
| product\_group\_id | Product | product\_hierarchy | id |
| product\_id | Product | product\_id | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
