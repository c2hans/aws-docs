---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/inventory_mgmnt-inv-level-entity.html
---

# inv\_level

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| inv\_level | snapshot\_date, site\_id, product\_id, inv\_condition, lot\_number |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| snapshot\_date | timestamp | Yes<sup>1</sup> | Date and time when the inventory snapshot was taken. |
| site\_id<sup>2</sup> | string | Yes<sup>1</sup> | Site ID of the inventory. |
| product\_id<sup>2</sup> | string | Yes<sup>1</sup> | Product ID of the inventory displayed. |
| company\_id<sup>2</sup> | string | No | Company ID. |
| on\_hand\_inventory | double | Yes | Physical inventory available at the site. |
| allocated\_inventory | double | No | Inventory allocated for some process. |
| bound\_inventory | double | No | Inventory bound to some process. |
| quantity\_uom | string | No | Quantity unit of measure for inventory. |
| inv\_condition | string | Yes <sup>1</sup> | Condition of the inventory. Inventory in different conditions are displayed in different rows. You can also enter your own value.<br />Reserved inventory condition values in AWS Supply Chain are as follows:+  Unrestricted - Inventory is available. <br />+  Inspection - Below quality or any other inspection. <br />+  Returns - Inventory goes to return area. <br />+  Blocked - Inventory is blocked for a reason. <br />+  InTransfer - Used during inventory stock transfer. <br />+  Restricted - Restricted for other reasons but not blocked.  |
| lot\_number | string | Yes<sup>1</sup> | Lot number of the inventory. |
| expiry\_date | timestamp | No | Expiry date of the inventory. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| tpartner\_id | string | No | Unique identifier for a trading partner. |

<sup>1</sup>You must enter a value. When you ingest data from SAP or EDI, the default value for *string* date type value is SCN\_RESERVED\_NO\_VALUE\_PROVIDED.

<sup>2</sup>Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| product\_id | Product | product | id |
| company\_id | Organization | company | id |
| site\_id | Network | site | id |
| tpartner\_id | Organization | trading\_partner | id |
