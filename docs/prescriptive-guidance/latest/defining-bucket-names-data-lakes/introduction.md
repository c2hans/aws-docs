---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/defining-bucket-names-data-lakes/introduction.html
---

# Defining Amazon S3 bucket and path names for data lake layers
<a name="introduction"></a>

*Andres Cantor, Amazon Web Services*

This guide helps you create a consistent naming standard for Amazon Simple Storage Service (Amazon S3) buckets and paths in data lakes hosted on the AWS Cloud. The guide's naming standard for Amazon S3 buckets and paths helps you to improve governance and observability in your data lakes, identify costs by data layer and AWS account, and provides an approach for naming AWS Identity and Access Management (IAM) roles and policies.

We recommend that you use at least three data layers in your data lakes and that each layer uses a separate Amazon S3 bucket. However, some use cases might require an additional Amazon S3 bucket and data layer, depending on the data types that you generate and store. For example, if you store sensitive data, we recommend that you use a landing zone data layer and a separate Amazon S3 bucket. The following list describes the three recommended data layers for your data lake:
+ **Raw data layer** – Contains raw data and is the layer in which data is initially ingested. If possible, we recommend that you retain the original file format and turn on versioning in the Amazon S3 bucket.
+ **Stage data layer** – Contains intermediate, processed data that is optimized for consumption (for example CSV to Apache Parquet converted raw files or data transformations). An AWS Glue job reads the files from the raw layer and validates the data. The AWS Glue job then stores the data in an Apache Parquet-formatted file, and the metadata is stored in a table in the AWS Glue Data Catalog.
+ **Analytics data layer** – Contains the aggregated data for your specific use cases in a consumption-ready format, such as Apache Parquet.

## Intended audience
<a name="intended-audience"></a>

This guide's recommendations are based on the authors' experience in implementing data lakes with the [serverless data lake framework (SDLF)](https://sdlf.workshop.aws/en/) and are intended for data architects, data engineers, or solutions architects who want to set up a data lake on the AWS Cloud. However, make sure that you adapt this guide's approach to meet your organization's policies and requirements.

The guide contains the following sections:
+ [Recommended data layers](data-layer-definitions.md)
+ [Naming Amazon S3 buckets in your data layers](naming-structure-data-layers.md)
+ [Mapping Amazon S3 buckets to IAM policies in your data lake](iam-policies-data-lake.md)
+ [Handling sensitive data](sensitive-data.md)

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

You should expect the following outcomes after implementing a naming standard for Amazon S3 buckets and paths in data lakes on the AWS Cloud:
+ Improved governance in your data lake by being able to provide differentiated access policies to the buckets
+ Increased visibility into your overall costs for individual AWS accounts by using the relevant AWS account ID in the Amazon S3 bucket name and for data layers by using [cost allocation tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CostAllocTagging.html) for the buckets
+ More cost-effective data storage by using layer-based versioning and path-based lifecycle policies
+ Meet security requirements for data masking and data encryption
+ Simplify data source tracing by enhancing developer visibility into the AWS Region and AWS account of the underlying data storage

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
