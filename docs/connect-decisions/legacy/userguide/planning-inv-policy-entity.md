---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/planning-inv-policy-entity.html
---

# inv\_policy
<a name="planning-inv-policy-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| inv\_policy | id, site\_id, product\_id, product\_group\_id, dest\_geo\_id, vendor\_tpartner\_id, eff\_start\_date, eff\_end\_date |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes | Policy ID. |
| site\_id2 | string | Yes1 | Site ID for the policy being defined. |
| product\_id2 | string | Yes1 | Product ID for the policy being defined. |
| company\_id2 | string | No | Company ID. |
| product\_group\_id2 | string | Yes1 | Product group ID that the policies are being defined for. Overridden at product level. |
| dest\_geo\_id2 | string | Yes1 | Sets default values at geo level of the destination. |
| vendor\_tpartner\_id2 | string | Yes1 | Trading partner ID of the vendor. This field is used when policies vary by vendor. |
| status | string | No | Status of the inventory policy record, for example, on-hold, or active. |
| ss\_policy | string | No | Type of safety stock policy. The safety stock policy is associated with corresponding data.<br />**abs\_level** – Uses units specified in min/max safety stock (SS). Source is customer system or external tool. Ordering is suggested whenever inventory falls below min SS level.<br />**sl** – Targets inventory between min and max service level for in-stock percentages. For example, if min/max service level is 50% and 90%, ordering will be done to maintain inventory between these percentiles of forecast over plan horizon.<br />**DOC\_dem** – Uses days of cover computed from historical demand as target level of inventory.<br />**DOC\_fcst** – Uses days of cover computed from forecast as target level of inventory.  |
| fallback\_policy\_1 | string | No | Fallback inventory policy. |
| repl\_interval | double | No | Specifies the replenishment interval. |
| min\_safety\_stock | double | No | For safety stock policy "abs\_level". This field is absolute value of minimum safety stock level. |
| max\_safety\_stock | double | No | For safety stock policy "abs\_level". This is absolute value of maximum safety stock level. |
| min\_inventory\_qty | double | No | Minimum inventory level quantity threshold. |
| max\_inventory\_qty | double | No | Maximum inventory level quantity threshold. |
| target\_inventory\_qty | double | No | Target inventory level quantity. |
| woc\_limit | double | No | Provides the weeks of cover limit. |
| max\_doc\_limit | double | No | Provides the maximum days of cover value for safety stock policies "DOC\_dem" and "DOC\_fcst". |
| min\_doc\_limit | double | No | Provides the minimum days of cover value for safety stock policies "DOC\_dem" and "DOC\_fcst". |
| target\_doc\_limit | double | No | Provides the target value for safety stock policies "DOC\_dem" and "DOC\_fcst". |
| permitted\_var | double | No | Allowed variance used in policies where deviations from min,max, and target is allowed. |
| min\_sl |  | No | Provides minimum service level (sl). Used for safety stock policy sl. |
| target\_sl | double | No | Target service level used of policy sl. |
| max\_sl | double | No | Provides maximum service level (sl). Used for safety stock policy. |
| qty\_uom | string | No | Quantity UOM associated with this inventory policy. |
| min\_order\_qty | double | No | Minimum order quantity. |
| max\_order\_qty | double | No | Maximum order quantity. |
| order\_qty\_multiple | double | No | Order quantity computed in multiples of this value. |
| holding\_cost\_percent | double | No | Annualized holding cost of inventory in percent. |
| eff\_start\_date | timestamp | Yes1 | Dates from when the record is effective. |
| eff\_end\_date | timestamp | Yes1 | Dates till when the record is effective. |
| salvage\_value\_percentage | double | No | Product cost that can be expected to recovered at the end of Long Term Horizon. |
| segment\_id 2 | string | No | ID of segment associated with the inventory policy |
| demand\_planning\_enabled | string | No | Identifies parts used for demand planning.  |
| inventory\_planning\_enabled | string | No | Identifies parts used for inventory planning. |
| mrp\_enabled | string | No | Identifies parts enabled for planning in MRP. |
| purchased\_item | string | No | Identifies parts that are purchased. |
| source | string | No | Source of data. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1You must enter a value. When you ingest data from SAP or EDI, the default values for string and timestamp date type values are: SCN\_RESERVED\_NO\_VALUE\_PROVIDED for *string*; and for *timestamp* , 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| site\_id | Network | site | id |
| segment\_id | Planning | segmentation | segment\_id |
| company\_id | Organization | company | id |
| dest\_geo\_id | Organization | geography | id |
| vendor\_tpartner\_id | Organization | trading\_partner | id |
| product\_group\_id | Product | product\_hierarchy | id |
| product\_id | Product | product | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
