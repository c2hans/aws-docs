---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/defining-bucket-names-data-lakes/data-layer-definitions.html
---

# Recommended data layers
<a name="data-layer-definitions"></a>

If you work with non-sensitive data, such as data that doesn't contain personally identifiable information (PII), we recommend that you use at least three different data layers in a data lake on the AWS Cloud.

However, you might require additional layers depending on the data's complexity and use cases. For example, if you work with sensitive data, such as PII data, we recommend that you use an additional Amazon Simple Storage Service (Amazon S3) bucket as a landing zone. You then mask the data before it is moved into the raw data layer. For more information about this, see the [Handling sensitive data](sensitive-data.md) section of this guide.

Each data layer must have an individual Amazon S3 bucket. The following table describes the recommended data layers.

|
|
| Data layer name | Description | Sample lifecycle policy strategy |
| --- |--- |--- |
| *Raw* | Contains the raw, unprocessed data. Data is ingested into the data lake in this layer.<br />If possible, you should keep the original file format and turn on versioning in the Amazon S3 bucket. | After one year, move files into the [Amazon S3 infrequent access (IA) storage class](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-infreq-data-access). After two years in Amazon S3 IA, archive them to [Amazon Glacier storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/glacier-storage-classes.html). |
| *Stage* | Contains intermediate, processed data that is optimized for consumption (for example CSV to Apache Parquet converted raw files or data transformations).<br />An AWS Glue job reads the files from the raw layer and validates the data. The AWS Glue job then stores the data in an Apache Parquet-formatted file, and the metadata is stored in a table in the AWS Glue Data Catalog. | Data can be deleted after a defined time period or according to your organization's requirements.<br />Some data derivatives, such as an Apache Avro transform of an original JSON format, can be removed from the data lake after a shorter amount of time, such as  after 90 days. |
| *Analytics* | Contains the aggregated data for your specific use cases in a consumption-ready format, such as Apache Parquet. | Data can be moved to Amazon S3 IA and then deleted after a defined time period or according to your organization's requirements. |

**Note**
You must evaluate all the recommended lifecycle policy strategies against your organizational needs, regulatory requirements, query patterns, and cost considerations.
