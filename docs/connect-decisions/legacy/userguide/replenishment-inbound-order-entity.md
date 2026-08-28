---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/replenishment-inbound-order-entity.html
---

# inbound\_order
<a name="replenishment-inbound-order-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| inbound\_order | id, tpartner\_id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes 1 | Object ID. |
| company\_id2 | string | No | Company ID. |
| order\_creation\_date | timestamp | No | Order creation date. |
| order\_type | string | No | Displays the type of order. Reserved order types in AWS Supply Chain:+  PO - Purchase order <br />+  TO - Transfer order <br />+  MO - Manufacturing order <br />+  BO - Blanket order <br />+  CO - Consumption order  |
| order\_status | string | No | Status of the order. |
| to\_site\_id2 | string | No | Site where the order will arrive. |
| tpartner\_id2 | string | Yes1 | Trading partner that the order will be sent to. |
| order\_currency\_uom | string | No | Currency UOM that the company uses. |
| vendor\_currency\_uom | string | No | Currency UOM that the vendor uses. |
| exchange\_rate | double | No | Exchange rate used for conversion. |
| exchange\_rate\_date | timestamp | No | Date and time when exchange rate was calculated. |
| incoterm | string | No | Three letter incoterm code. |
| incoterm2 | string | No | Place of ownership transfer. |
| incoterm\_location\_1 | string | No | Incoterm location 1. Can be a site\_id or the location used on order/EDI. |
| incoterm\_location\_2 | string | No | Incoterm location 2. Can be a site\_id or the location used on order/EDI. |
| submitted\_date | timestamp | No | Date and time when order was submitted to vendor. |
| agreement\_start\_date | timestamp | No | If PO is associated with contract or agreement, then start datetime of contract. |
| agreement\_end\_date | timestamp | No | If PO is associated with contract or agreement, then end datetime of contract. |
| shipping\_instr\_code | string | No | Code for shipping instructions. |
| payment\_terms\_code | string | No | Code for payment instructions. |
| std\_terms\_agreement | string | No | Agreement between company and vendor. |
| std\_terms\_agreement\_ver | string | No | Version of agreement between company and vendor. |
| agreement\_number | string | No | Number associated with contract or agreement. |
| inbound\_order\_url | string | No | URL to access inbound order record in source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source | string | No | Source of data. |

1You must enter a value. When you ingest data from SAP or EDI, the default value for *string* is SCN\_RESERVED\_NO\_VALUE\_PROVIDED.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| tpartner\_id | Organization | trading\_partner | id |
| company\_id | Organization | company | id |
| to\_site\_id | Network | site | id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
