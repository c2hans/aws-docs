---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/template-tech-req.html
---

# Technical-requirements assessment template
<a name="template-tech-req"></a>

Provide information about data ingestion types:

|
|
| Data ingestion type | Y/N | Description | Frequency |
| --- |--- |--- |--- |
| *Application access* | *Y* |   |   |
| *API gateway* | *Y* |   |   |
| *Data streaming* | *N* |   |   |
| *Batch process* | *N* |   |   |
| *ETL* | *N* |   |   |
| *Data import* | *N* |   |   |
| *Time series* | *N* |   |   |

Provide information about data consumption types:

|
|
| Data consumption type | Y/N | Description | Frequency |
| --- |--- |--- |--- |
| *Application access* |   |   |   |
| *API gateway* |   |   |   |
| *Data export* |   |   |   |
| *Data analytics* |   |   |   |
| *Data aggregation* |   |   |   |
| *Reporting* |   |   |   |
| *Search* |   |   |   |
| *Data streaming* |   |   |   |
| *ETL* |   |   |   |

Provide data volume estimates:

|
|
| Entity name | Estimated \# of records | Record size | Data volume |
| --- |--- |--- |--- |
| *Game Player* | *1 MM* | *< 1 KB* | *\~ 1 GB*<br />* (1 MM \* 1 KB)* |
| *Game Instance* | *6 MM*<br />*(100K/day \* 60 days)* | *< 1 KB* | *\~ 6 GB*<br />* (6 MM \* 1 KB)* |
| *Game User Mapping* | *300 MM*<br />*(6 MM games \* 50 players)* | *< 1 KB* | *\~ 300 GB*<br />* (300 MM \* 1 KB)* |

**Note**
The period for data retention is 60 days. After 60 days, data must be stored in Amazon S3 for analytics, by using [DynamoDB Time to Live (TTL)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) to automatically move data out of DynamoDB to Amazon S3.

Answer these questions about time patterns:
+ What time frame is the application available to the user (for example, 24/7 or 9 AM to 5 PM on weekdays)?
+ Is there a peak in usage during the day? How many hours? What is the percentage of application usage?

Specify write throughput requirements:

|
|
| Entity name | Writes/day | Hours/day | Writes/second |
| --- |--- |--- |--- |
| *Game Player* | *10,000 updates* | *18* | *< 1* |
| *Game Instance* | *300,000* | *18* | *< 5* |
| *Game User Mapping* | *1,800,000,000* | *18* | *\~ 27.777* |

**Note**
**Game Player write operations:** 1 percent of users update their profiles every day, so we expect 10,000 updates for 1,000,000 users.

**Note**
**Game Instance write operations:** 100,000 games/day. For each game we have at least 3 write operations—at creation, start, and end—so the total is 300,000 write operations.

**Note**
**Game User Mapping write operations:** 100,000 games/day for each game with 50 players. The average game duration is 30 minutes, and the gamer position is updated every 5 seconds. We estimate an average of 360 updates per gamer, so the total is 100,000 × 50 × 360 = 1,800,000,000 write operations.

Specify read throughput requirements:

|
|
| Entity name | Reads / day | Hours / day | Reads/sec |
| --- |--- |--- |--- |
| *Game Player* | *200,000* | *18* | *\~ 3* |
| *Game Instance* | *5,000,000* | *18* | *\~ 77* |
| *Game User Mapping* | *1,800,000,000* | *18* | *\~ 27.777* |

**Note**
**Game Player read operations:** 20 percent of users start games, so 1 MM × 0.2 = 200,000.

**Note**
**Game Instance read operations**: 100,000 games/day. For each game we have at least 1 read operation per player, and 50 players per game, so the total is 5,000,000 read operations.

**Note**
**Game User Mapping read operations**: 100,000 games/day for 50 players. The average game duration is 30 minutes, and the gamer position is updated every 5 seconds. We estimate an average of 360 updates per gamer, and each update requires a read operation, so the total is 100,000 × 50 × 360 = 1,800,000,000 read operations.

Specify data access latency requirements:

|
|
| Operation | 99 percentiles | Maximum latency |
| --- |--- |--- |
| *Read* | *30 ms* | *100 ms* |
| *Write* | *10 ms* | *50 ms* |

Specify data availability requirements:

|
|
| Requirement | Y/N | Metric | Notes |
| --- |--- |--- |--- |
| *High availability* | *Y* | *99.9%* |   |
| *RTO* | *Y* | *1 hour* | *Recovery time objective* |
| *RPO* | *Y* | *1 hour* | *Recovery point objective* |
| *Disaster recovery* | *N* |   |   |
| *In-Region data replication* | *N* |   |   |
| *Cross-Region data replication* | *N* | *3 sec latency* | *Which AWS Regions?* |

Specify security requirements:

|
|
| Requirement | Y/N | Notes |
| --- |--- |--- |
| *Sensitive data store* | *N* | *Protected health information (PHI), payment card industry (PCI) information, personally identifiable information (PII)?* |
| *Encryption at rest* | *Y* |   |
| *Encryption in transit* | *Y* |   |
| *Client-side encryption* | *N* |   |
| *Any proprietary or third- vendor encryption library* | *N* |   |
| *Data access logging* | *N* |   |
| *Data access auditing* | *N* |   |
