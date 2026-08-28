---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/estimate-the-cost-of-a-dynamodb-table-for-on-demand-capacity.html
---

# Estimate the cost of a DynamoDB table for on-demand capacity
<a name="estimate-the-cost-of-a-dynamodb-table-for-on-demand-capacity"></a>

*Moinul Al-Mamun, Amazon Web Services*

## Summary
<a name="estimate-the-cost-of-a-dynamodb-table-for-on-demand-capacity-summary"></a>

[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) is a NoSQL transactional database that provides single-digit millisecond latency even at petabytes scale. This Amazon Web Services (AWS) serverless offering is getting popular because of its consistent performance and scalability.  You do not need to provision underlying infrastructure. Your single table can grow up to petabytes.

With on-demand capacity mode, you pay per request for the data reads and writes that your application performs on the tables. AWS charges are based on the accumulated read request units (RRUs) and write request units (WRUs) in a month. DynamoDB monitors the size of your table continuously throughout the month to determine your storage charges. It supports continuous backup with point-in-time-recovery (PITR). DynamoDB monitors the size of your PITR-enabled tables continuously throughout the month to determine your backup charges.

To estimate the DynamoDB cost for a project, it’s important to calculate how much RRU, WRU, and storage will be consumed at different stages of your product lifecycle. For a rough cost estimation, you can use [AWS Pricing Calculator](https://calculator.aws/#/createCalculator/DynamoDB), but you must provide an approximate number of RRUs, WRUs, and storage requirements for your table. These can be difficult to estimate at the beginning of the project. AWS Pricing Calculator doesn’t consider data growth rate or item size, and it doesn’t consider the number of reads and writes for the base table and global secondary indexes (GSIs) separately. To use AWS Pricing Calculator, you must estimate all those aspects to assume ballpark figures for WRU, RRU, and storage size to obtain your cost estimation.

This pattern provides a mechanism and a re-usable Microsoft Excel template to estimate basic DynamoDB cost factors, such as write, read, storage, backup and recovery cost, for on-demand capacity mode. It is more granular than AWS Pricing Calculator, and it considers base table and GSIs requirements independently. It also considers the monthly item data growth rate and forecasts costs for three years.

## Prerequisites and limitations
<a name="estimate-the-cost-of-a-dynamodb-table-for-on-demand-capacity-prereqs"></a>

**Prerequisites **
+ Basic knowledge of DynamoDB and DynamoDB data model design
+ Basic knowledge of DynamoDB pricing, WRU, RRU, storage, and backup and recovery (for more information, see [Pricing for On-Demand Capacity](https://aws.amazon.com/dynamodb/pricing/on-demand/))
+ Knowledge of your data, data model, and item size in DynamoDB
+ Knowledge of DynamoDB GSIs

**Limitations**
+ The template provides you with an approximate calculation, but it isn’t appropriate for all configurations. To get a more accurate estimate, you must measure the individual item size for each item in the base table and GSIs.
+ For a more accurate estimate, you must consider the expected number of writes (insert, update, and delete) and reads for each item in an average month.
+ This pattern supports estimating only write, read, storage, and backup and recovery costs for next few years based on fixed data growth assumptions.

## Tools
<a name="estimate-the-cost-of-a-dynamodb-table-for-on-demand-capacity-tools"></a>

**AWS services**
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.

**Other tools**
+ [AWS Pricing Calculator](https://calculator.aws/#/createCalculator/DynamoDB) is a web-based planning tool that you can use to create estimates for your AWS use cases.

## Best practices
<a name="estimate-the-cost-of-a-dynamodb-table-for-on-demand-capacity-best-practices"></a>

To help keep costs low, consider the following DynamoDB design best practices.
+ [Partition key design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-uniform-load.html) – Use a high-cardinality partition key to distribute load evenly.
+ [Adjacency list design pattern](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-adjacency-graphs.html) – Use this design pattern for managing one-to-many and many-to-many relationships.
+ [Sparse index](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-general-sparse-indexes.html) – Use sparse index for your GSIs. When you create a GSI, you specify a partition key and optionally a sort key. Only items in the base table that contain a corresponding GSI partition key appear in the sparse index. This helps to keep GSIs smaller.
+ [Index overloading](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-gsi-overloading.html) – Use the same GSI for indexing various types of items.
+ [GSI write sharding](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-gsi-sharding.html) – Shard wisely to distribute data across the partitions for efficient and faster queries.
+ [Large items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-use-s3-too.html) – Store only metadata inside the table, save the blob in Amazon S3, and keep the reference in DynamoDB. Break large items into multiple items, and efficiently index by using sort keys.

For more design best practices, see the [Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html).

## Epics
<a name="estimate-the-cost-of-a-dynamodb-table-for-on-demand-capacity-epics"></a>

### Extract item information from your DynamoDB data model
<a name="extract-item-information-from-your-dynamodb-data-model"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Get item size. | 1. Check how many different types of item you are going to store in your table.<br />2. To calculate the size of each item in kilobytes, add the Key and Value size of each attribute.<br />3. Calculate item size for a base table and for each GSI. | Data engineer |
| Estimate the write cost. | To estimate write cost in on-demand capacity mode, first you have to measure how many WRUs will be consumed in a month. For that, you need to consider the following factors:+ Number of create, update, and delete operations for each item in a month.<br />+ Number of available GSIs. Consider each index independently. Average size of an index itemNumber of synchronization times on an index<br />+ How many new things (for example, components or products) will be added in the table each month? The number of added things could be different every month, but you can assume an average growth rate based on your business cases. <br />For more information, see the *Additional information* section. | Data engineer |
| Estimate the read cost. | To estimate read cost in on-demand mode, first you have to measure how many RRUs will be consumed in a month. For that, you need to consider the following factors: + Number of available GSIs. Consider each index independently. Average size of an index item<br />+ Average number of reads per product per month.<br />+ Number of total available things (components or products) in the DynamoDB table. | Data engineer, App developer |
| Estimate the storage size and cost. | First, estimate the average monthly storage requirement based on your item size in the table. Then calculate storage cost by multiplying storage size by the per GB storage price for your AWS Region. <br />If you already entered data for estimating the write cost, you don't need to enter it again for calculating storage size. Otherwise, to estimate storage size, you need to consider the following factors: + Number of data items in a module (product) based on your table design.<br />+ Average item size in kilobytes.<br />+ Number of available GSIs. Consider each index independently. Average size of an index item<br />+ How many new products will be added in the table each month? The number of new products could be different every month, but you can assume an average growth rate based on your business cases. This example uses an average of 10 million new products each month. | Data engineer |

### Enter the item and object information in the Excel template
<a name="enter-the-item-and-object-information-in-the-excel-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the Excel template from the Attachments section, and adjust it for your use case table. | 1. Download the Excel template.<br />2. Adjust the business module and GSIs, based on your table design. | Data engineer |
| Enter information in the Excel template. | 1. Update item information in the sheet. Update data only in orange cells.<br />2. Adjust the object numbers: How much could be added into the table each month?<br />3. Update the WRU and RRU prices per million for your AWS Region.<br />4. Update the storage and backup prices per GB-month for your AWS Region.<br />5. Update the recovery price per GB for your AWS Region.In the template, there are three items, or entities: information, metadata, and relationship. There are two GSIs. For your use case, if you need more items, create new rows. If you need more GSIs, copy an existing GSI block, and paste to create as many GSI blocks as you need. Then adjust the SUM and TOTAL column calculations. | Data engineer |

## Related resources
<a name="estimate-the-cost-of-a-dynamodb-table-for-on-demand-capacity-resources"></a>

**References**
+ [Amazon DynamoDB pricing for on-demand capacity](https://aws.amazon.com/dynamodb/pricing/on-demand/)
+ [AWS Pricing Calculator for DynamoDB](https://calculator.aws/#/createCalculator/DynamoDB)
+ [Best practices for designing and architecting with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)
+ [Getting started with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html)

**Guides and patterns**
+ [Modeling data with Amazon DynamoDB](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/)
+ [Estimate storage costs for an Amazon DynamoDB table](https://apg-library.amazonaws.com/content/9b74399d-9655-47ee-b9b3-de46b65bc4e3)

## Additional information
<a name="estimate-the-cost-of-a-dynamodb-table-for-on-demand-capacity-additional"></a>

**Write cost calculation example**

The DynamoDB data model design shows three items for a product, and an average item size of 4 KB. When you add a new product into the DynamoDB base table, it consumes the number of items \* (item size/1 KB write unit) = 3 \* (4/1) = 12 WRU. In this example, for writing 1 KB, the product consumes 1 WRU.

**Read cost calculation example**

To get the RRU estimation, consider the average of how many  times each item will be read in a month. For example, the Information item will be read, on average, 10 times in a month, and the metadata item will be read two times, and the relationship item will be read five times. In the example template, total RRU for all components = number of new components created each month \* RRU per component per month = 10 million \* 17 RRU = 170 million RRU each month.

Every month, new things (components or products will be added, and the total number of products will grow over time. So, RRU requirements will also grow over time.
+ For the first month RRU, consumption will be 170 million.
+ For the second month, RRU consumption will be 2 \* 170 million = 340 million.
+ For the third month RRU consumption will be 3 \* 170 million = 510 million.

The following graph shows monthly RRU consumption and cost forecasting.

![The RRU consumption rising more steeply than the cost.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/1797b48f-a183-4f25-811f-44921c3a48ee/images/3505bfc8-694d-4acc-8585-cd71258fa315.png)

Note that prices within the graph are for illustration only. To create accurate forecasts for your use case, check the AWS pricing page, and use those prices in the Excel sheet.

**Storage, backup, and recovery cost calculation examples**

DynamoDB storage, backup and restore all are connected with each other. Backup is directly connected with storage, and recovery is directly connected with backup size. As the table size increases, corresponding storage, backup, and restore costs will increase proportionally.

*Storage size and cost*

Storage cost will increase over time based on your data growth rate. For example, assume that the average size of a component or product in the base table and GSIs is 11 KB, and 10 million new products will be added every month into your database table. In that case, your DynamoDB table size will grow (11 KB \* 10 million)/1024/1024 = 105 GB per month. At the first month, your table storage size will be 105 GB, at second month it will be 105 \+ 105 = 210 GBs, and so on.
+ For the first month, storage cost will be 105 GB \* storage price per GB for your AWS Region.
+ For the second month, storage cost will be 210 GB \* storage price per GB for your Region.
+ For the third month, storage cost will be 315 GB \* storage price per GB for your Region.

For storage size and cost for next three years, see the *Storage size and forecasting* section.

*Backup cost*

Backup cost will increase over time based on your data growth rate. When you turn on continuous backup with point-in-time-recovery (PITR), continuous backup charges are based on average storage GB-Month. In a calendar month, the average backup size would be the same as your table storage size, although the actual size could be a bit different. As new products will be added every month, the total storage size and the backup size will grow over time. For example, for the first month, the average backup size of 105 GB could grow to 210 GB for the second month.
+ For the first month, backup cost will be 105 GB-month \* continuous backup price per GB for your AWS Region.
+ For the second month, backup cost will be 210 GB-month \* continuous backup price per GB for your Region.
+ For the third month, backup cost will be 315 GB-month \* continuous backup price per GB for your Region.
+ and, so on

Backup cost is included in the graph in the *Storage size and cost forecasting* section.

*Recovery cost*

When you are taking continuous backup with PITR enabled, recovery operation charges are based on the size of the restore. Each time that you restore, you pay based on gigabytes of restored data. If your table size is large and you perform restore multiple times in a month, it will be costly.

To estimate restore cost, this example assumes that you perform a PITR recovery one time each month at the end of the month. The example uses the monthly average backup size as the restore data size for that month. For the first month, the average backup size is 105 GB, and for the recovery at end of the month, the restore data size would be 105 GB. For the second month, it would be 210 GBs, and so on.

Recovery cost will increase over time based on your data growth rate.
+ For the first month, recovery cost will be 105 GB \* restore price per GB for your AWS Region.
+ For the second month, recovery cost will be 210 GB \* restore price per GB for your Region.
+ For the third month, recovery cost will be 315 GB \* restore price per GB for your Region.

For more information, see the Storage, backup and recovery tab in the Excel template and the graph in the following section.

*Storage size and cost forecasting*

In the template, actual billable storage size is calculated by subtracting the free tier 25 GB per month for the Standard table class. In the sheet, you will get a forecasting graph broken out into monthly values.

The following example chart forecasts monthly storage size in GB, billable storage cost, on-demand backup cost, and recovery cost for next 36 calendar months. All costs are in USD. From the graph, it’s clear that storage, backup, and recovery costs increase proportionally to increases in storage size.

![The storage size rising above three thousand while the costs are less than one thousand.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/1797b48f-a183-4f25-811f-44921c3a48ee/images/fd9f06d0-bc9c-4b4e-8cbd-3e527fe09e88.png)

Note that prices used in the graph are for illustration purposes only. To create accurate prices for your use case, check the AWS pricing page, and use those prices in the Excel template.

## Attachments
<a name="attachments-1797b48f-a183-4f25-811f-44921c3a48ee"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/1797b48f-a183-4f25-811f-44921c3a48ee/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
