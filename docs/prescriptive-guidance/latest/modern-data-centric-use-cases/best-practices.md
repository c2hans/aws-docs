---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/best-practices.html
---

# Best practices
<a name="best-practices"></a>

We recommend that you follow storage and technical best practices. These best practices can help you get the most out of your data-centric archicture.

## Storage best practices for big data
<a name="storage-best-practices"></a>

The following table describes a common best practice to store files for a big data processing load on Amazon S3. The last column is an example of a lifecycle policy that you can set. If [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) is enabled (which delivers automatic storage cost savings when data access patterns change automatically), then you don't have to manually set the policy.

|
|
| Data layer name | Description | Example lifecycle policy strategy |
| --- |--- |--- |
| Raw | Contains raw, unprocessed dataFor an external data source, the raw data layer is typically a 1:1 copy of the data, but on AWS the data can be partitioned by keys based on AWS Region or date during the ingestion process. | After one year, move files into the S3 Standard-IA [storage class](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html). After two years in S3 Standard-IA, archive the files in [Amazon Simple Storage Service Glacier (Amazon S3 Glacier)](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html).<br />Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/). |
| Stage | Contains intermediate processed data that's optimized for consumption<br />**Example**: CSV to Apache Parquet converted raw files or data transformations | You can delete data after a defined time period or according to your organization's requirements.<br />You can remove some data derivatives (for example, an Apache Avro transform of an original JSON format) from the data lake after a shorter amount of time (for example, after 90 days). |
| Analytics | Contains the aggregated data for your specific use cases in a consumption-ready format<br />**Example**: Apache Parquet | You can move data to S3 Standard-IA, and then delete the data after a defined time period or according to your organization's requirements. |

The following diagram shows an example of a partitioning strategy (corresponding to one S3 folder/prefix) that you can use across all the data layers. We recommend that you choose a partitioning strategy based on how your data is used downstream. For example, if reports are built on your data (where most common queries on the report filter the results based on region and dates), then make sure to include the regions and dates as partitions to improve query performance and runtime.

![Partitioning strategy diagram](http://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/images/guide-img/058e3d2f-f726-4dc0-989b-0f15dcd3bc33/images/82960913-539c-41d5-b8ed-39e8985c289f.png)

## Technical best practices
<a name="technical-best-practices"></a>

Technical best practices depend on the specific AWS services and processing technologies that you use to design your data-centric architecture. However, we recommend that you keep in mind the following best practices. These best practices apply to typical data processing use cases.

|
|
| Area | Best practice |
| --- |--- |
| SQL | Reduce the amount of data that must be queried by projecting attributes on your data. Instead of parsing the entire table, you can use data projection to scan and return only certain required columns in the table.<br />Avoid large joins if possible because joins between multiple tables can significantly impact performance due to their resource-intensive demands. |
| Apache Spark | [Optimize Spark applications](https://aws.amazon.com/blogs/big-data/optimizing-spark-applications-with-workload-partitioning-in-aws-glue/) with workload partitioning in AWS Glue (AWS Big Data blog).<br />[Optimize memory management](https://aws.amazon.com/blogs/big-data/optimize-memory-management-in-aws-glue/) in AWS Glue (AWS Big Data blog). |
| Database design | Follow the [Architecture Best Practices for Databases](https://aws.amazon.com/architecture/databases/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all) (AWS Architecture Center). |
| Data pruning | Use [server-side partition pruning](https://docs.aws.amazon.com/glue/latest/dg/partition-indexes.html) with the `catalogPartitionPredicate`. |
| Scaling | Understand and implement [horizontal scaling](https://aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.horizontal-scaling.en.html). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
