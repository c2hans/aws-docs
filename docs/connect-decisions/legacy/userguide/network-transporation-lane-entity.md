---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/network-transporation-lane-entity.html
---

# transportation\_lane
<a name="network-transporation-lane-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| transportation\_lane | id, from\_site\_id, to\_site\_id, from\_geo\_id, to\_geo\_id, carrier\_tpartner\_id, trans\_mode, service\_type, product\_group\_id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes | Lane ID. |
| from\_site\_id2 | string | Yes1 | Origin site location for the lane. You can exclude this field if the from\_geo\_id is populated. |
| to\_site\_id2 | string | Yes1 | Destination site location for the lane. You can exclude this field if the to\_geo\_id is populated. |
| company\_id2 | string | No | Company ID. |
| from\_geo\_id2 | string | Yes1 | When lane definition is at geographical level, displays the 'from' or 'source' geographical region. |
| to\_geo\_id2 | string | Yes1 | When lane definition is at geographical level, displays the 'to' or 'source' geographical region. |
| carrier\_tpartner\_id2 | string | Yes1 | ID of the carrier. |
| trans\_mode | string | Yes1 | Transportation mode, for example, ship, rail, or truck. |
| service\_type | string | Yes1 | Provides information on the shipping method for the carrier. |
| product\_group\_id2 | string | Yes1 | Product group ID if transit time varies by product group. |
| product\_id2 | string | No | Product ID is used when a lane has product-specific configuration. |
| transit\_time | double | No | Transit time of products. |
| transit\_time\_sd | double | No | Standard deviation of transit time. |
| time\_uom | string | No | Unit of measure of transit time. |
| distance | double | No | Distance traveled on the lane. |
| distance\_uom | string | No | Unit of measure (UOM) of distance. |
| eff\_start\_date | timestamp | No | Date and time when this record becomes effective.  |
| eff\_end\_date | timestamp | No | Date and time till when this record becomes effective. |
| daily\_start\_time | string | No | Time when the lane begins operating. |
| daily\_end\_time | string | No | Time when the lane ends operation. |
| open\_sun | string | No | Displays whether the lane is open on Sunday. |
| open\_mon | string | No | Displays whether the lane is open on Monday. |
| open\_tue | string | No | Displays whether the lane is open on Tuesday. |
| open\_wed | string | No | Displays whether the lane is open on Wednesday. |
| open\_thu | string | No | Displays whether the lane is open on Thursday. |
| open\_fri | string | No | Displays whether the lane is open on Thursday. |
| open\_sat | string | No | Displays whether the lane is open on Saturday. |
| cost\_per\_unit | double | No | Cost per distance UOM. |
| cost\_per\_weight | double | No | Cost per weight UOM. |
| cost\_currency | string | No | Currency UOM of costs. |
| weight\_uom | string | No | Unit of measurement for weight. |
| emissions\_per\_unit | double | No | Carbon emissions emitted per unit distance UOM. |
| emissions\_per\_weight | double | No | Carbon emissions emitted per weight UOM. |
| source | string | No | Source of data. |
| transportation\_cost  | double | No | Transportation cost related to the transport lane. |
| transportation\_cost\_uom  | string | No | Transportation cost UOM related to the transport lane. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1You must enter a value. When you ingest data from SAP or EDI, the default value for *string* is: SCN\_RESERVED\_NO\_VALUE\_PROVIDED.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| from\_site\_id, to\_site\_id | Network | site | id |
| company\_id | Organization | company | id |
| from\_geo\_id, to\_geo\_id | Organization | geography | id |
| carrier\_tpartner\_id | Organization | trading\_partner | id |
| product\_group\_id | Product | product\_hierarchy | id |
| product\_id | Product | product\_id | id |
