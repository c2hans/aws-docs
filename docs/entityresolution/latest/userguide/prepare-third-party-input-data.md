---
source_url: https://docs.aws.amazon.com/entityresolution/latest/userguide/prepare-third-party-input-data.html
---

# Preparing third-party input data
<a name="prepare-third-party-input-data"></a>

Third-party data services provide identifiers that can be matched with your known identifiers.

AWS Entity Resolution currently supports the following third-party data provider services:

**Data provider services**

| Company Name | Available AWS Regions | Identifier |
| --- | --- | --- |
| LiveRamp | US East (N. Virginia) (us-east-1), US East (Ohio) (us-east-2), and US West (Oregon) (us-west-2) | Ramp ID |
| TransUnion | US East (N. Virginia) (us-east-1), US East (Ohio) (us-east-2), and US West (Oregon) (us-west-2) | TransUnion Individual and Household IDs |
| Unified ID 2.0 | US East (N. Virginia) (us-east-1), US East (Ohio) (us-east-2), and US West (Oregon) (us-west-2) | raw UID 2 |

The following steps describe how to prepare third-party data to use a [provider service-based matching workflow](glossary.md#provider-service-matching) or a [provider service-based ID mapping workflow](create-IDMW-provider-services-one-acct.md).

**Topics**
+ [Step 1: Subscribe to a provider service on AWS Data Exchange](#subscribe-provider-service)
+ [Step 2: Prepare third-party data tables](#prepare-third-party-data-tables)
+ [Step 3: Save your input data table in a supported data format](#save-third-party-data-tables)
+ [Step 4: Upload your input data table to Amazon S3](#upload-third-party-data-tables)
+ [Step 5: Create an AWS Glue table](#create-glue-table-third-party-data-tables)

## Step 1: Subscribe to a provider service on AWS Data Exchange
<a name="subscribe-provider-service"></a>

If you have a subscription with a provider service through AWS Data Exchange, you can run a matching workflow with one of the following provider services to match your known identifiers with your preferred provider. Your data will be matched with a set of inputs defined by your preferred provider.

To subscribe to a provider service on AWS Data Exchange

1. View the provider listing on AWS Data Exchange. The following provider listings are available:
   + LiveRamp
     + [LiveRamp Identity Resolution](https://aws.amazon.com/marketplace/pp/prodview-v4557zxjo6ykq)
     + [LiveRamp Transcoding](https://aws.amazon.com/marketplace/pp/prodview-bpp2fvfcxk2kg)
   + TransUnion
     + TruAudience Identity Resolution & Enrichment
   + Unified ID 2.0
     + [Unified ID 2.0 Identity Resolution](https://aws.amazon.com/marketplace/pp/prodview-66zqls7iqsm6o?sr=0-4&ref_=beagle&applicationId=AWSMPContessa#offers)

1. Complete one of the following steps, depending on your offer type.
   + **Private offer** – If you have an existing relationship with a provider, follow the [Private products and offers](https://docs.aws.amazon.com/data-exchange/latest/userguide/subscribe-to-private-offer.html) procedure in the *AWS Data Exchange User Guide* to accept a private offer on AWS Data Exchange.
   + **Bring your own subscription** – If you already have an existing data subscription with a provider, follow the [Bring Your Own Subscription (BYOS) offers](https://docs.aws.amazon.com/data-exchange/latest/userguide/subscribe-to-byos-offer.html) procedure in the *AWS Data Exchange User Guide* to accept a BYOS offer on AWS Data Exchange.

1. After you have subscribed to a provider service on AWS Data Exchange, you can then create a matching workflow or an ID mapping workflow with that provider service.

For more information about how to access a provider product that contains APIs, see [Accessing an API product](https://docs.aws.amazon.com/data-exchange/latest/userguide/subscribing-to-product.html#use-API-product) in the in the *AWS Data Exchange User Guide*.

## Step 2: Prepare third-party data tables
<a name="prepare-third-party-data-tables"></a>

Each third-party service has a different set of recommendations and guidelines to help ensure a successful matching workflow.

To prepare third-party data tables, consult the following table:

**Data provider services guidelines**

| Provider service | Unique ID needed? | Actions |
| --- | --- | --- |
| LiveRamp | Yes | Ensure the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/prepare-third-party-input-data.html) |
| TransUnion | Yes | Ensure the following are a `string` type column in the input view: [See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/prepare-third-party-input-data.html) |
| Unified ID 2.0 | Yes | Ensure the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/prepare-third-party-input-data.html) A specific email or phone number, at any specific time, results in the same raw UID2 value, no matter who made the request. <br />Raw UID2s are created by adding salts from salt buckets which are rotated approximately once a year, causing the raw UID2 to also be rotated with it. Different salt buckets rotate at different times throughout the year. AWS Entity Resolution currently doesn't keep track of rotating salt buckets and raw UID2s, so it is recommended that you regenerate the raw UID2s daily. For more information, see [How often should UID2s be refreshed for incremental updates?](https://unifiedid.com/docs/getting-started/gs-faqs#how-often-should-uid2s-be-refreshed-for-incremental-updates) in the UID 2.0 documentation.  |

## Step 3: Save your input data table in a supported data format
<a name="save-third-party-data-tables"></a>

If you already saved your third-party input data in a supported data format, you can skip this step.

To use AWS Entity Resolution, the input data must be in a format that AWS Entity Resolution supports.

AWS Entity Resolution supports the following data formats:
+ comma-separated value (CSV)
**Note**
LiveRamp only supports CSV files.
+ Parquet

## Step 4: Upload your input data table to Amazon S3
<a name="upload-third-party-data-tables"></a>

If you already have your third-party data table in Amazon S3, you can skip this step.

**Note**
You can store the input data in Amazon S3 resources in any Region in the AWS commercial partition where S3 is supported. This data can be accessed from a different Region or AWS account when running the matching workflow.

**To upload your input data table to Amazon S3**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose **Buckets**, and then choose a bucket to store your data table.

1. Choose **Upload**, and then follow the prompts.

1. Choose the **Objects** tab to view the prefix where your data is stored. Make a note of the name of the folder.

   You can select the folder to view the data table.

## Step 5: Create an AWS Glue table
<a name="create-glue-table-third-party-data-tables"></a>

The input data in Amazon S3 must be cataloged in AWS Glue and represented as an AWS Glue table. For more information about how to create an AWS Glue table with Amazon S3 as the input, see [Working with crawlers on the AWS Glue console](https://docs.aws.amazon.com/glue/latest/dg/console-crawlers.html) in the *AWS Glue Developer Guide.*

**Note**
AWS Entity Resolution doesn't support partitioned tables.

In this step, you set up a crawler in AWS Glue that crawls all the files in your S3 bucket and create an AWS Glue table.

**Note**
AWS Entity Resolution doesn't currently support Amazon S3 locations registered with AWS Lake Formation.

**To create an AWS Glue table**

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. From the navigation bar, select **Crawlers**.

1. Select your S3 bucket from the list, and then choose **Add crawler**.

1. On the **Add crawler** page, enter a **Crawler name** and then choose **Next**.

1. Continue through the **Add crawler page**, specifying the details.

1. On the **Choose an IAM role** page, choose **Choose an existing IAM role** and then choose **Next**.

   You can also choose **Create an IAM role** or have your administrator create the IAM role if needed.

1. For **Create a schedule for this crawler**, keep the **Frequency** default (**Run on demand**) and then choose **Next**.

1. For **Configure the crawler’s output**, enter the AWS Glue database and then choose **Next**.

1. Review all of the details, and then choose **Finish**.

1. On the **Crawlers** page, select the check box next to your S3 bucket and then choose **Run crawler**.

1. After the crawler is finished running, on the AWS Glue navigation bar, choose **Databases**, and then choose your database name.

1. On the **Database** page, choose **Tables in {your database name}**.

   1. View the tables in the AWS Glue database.

   1. To view a table's schema, select a specific table.

   1. Make a note of the AWS Glue database name and AWS Glue table name.

You are now ready to create a schema mapping. For more information, see [Creating a schema mapping](create-schema-mapping.md).
