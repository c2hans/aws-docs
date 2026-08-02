---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-data-lake.html
---

# Creating an Amazon Chime SDK data lake
<a name="ca-data-lake"></a>

The Amazon Chime SDK call analytics data lake allows you to stream your machine learning powered insights and any metadata from Amazon Kinesis Data Stream to your Amazon S3 bucket. For example, using the data lake to access URLs to recordings. To create the data lake, you deploy a set of AWS CloudFormation templates from either the Amazon Chime SDK console or programmatically using the AWS CLI. The data lake enables you to query your call metadata and voice analytics data by referencing AWS Glue data tables in Amazon Athena.

**Topics**
+ [Prerequisites](#data-lake-prereqs)
+ [Data lake terminology and concepts](#data-lake-terms)
+ [Creating multiple data lakes](#creating-multiple-data-lakes)
+ [Data lake regional availability](#data-lake-regions)
+ [Data lake architecture](#data-lake-architecture)
+ [Data lake setup](#data-lake-setup)

## Prerequisites
<a name="data-lake-prereqs"></a>

You must have the following items in order to create an Amazon Chime SDK lake:
+ An Amazon Kinesis data stream. For more information, refer to [Creating a Stream via the AWS Management Console](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-create-a-stream.html) in the *Amazon Kinesis Streams Developer Guide*.
+ An S3 bucket. For more information, refer to [Create your first Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) in the *Amazon S3 User Guide*.

## Data lake terminology and concepts
<a name="data-lake-terms"></a>

Use the following terms and concepts to understand how the data lake works.

**Amazon Kinesis Data Firehose**
An extract, transform, and load (ETL) service that reliably captures, transforms, and delivers streaming data to data lakes, data stores, and analytics services. For more information, see What Is Amazon Kinesis Data Firehose?

**Amazon Athena**
Amazon Athena is an interactive query service that enables you to analyze data in Amazon S3 using standard SQL. Athena is serverless, so you have no infrastructure to manage, and you pay only for the queries that you run. To use Athena, point to your data in Amazon S3, define the schema, and use standard SQL queries. You can also use workgroups to group users and control the resources they have access to when running queries. Workgroups enable you to manage query concurrency and prioritize query execution across different groups of users and workloads.

**Glue Data Catalog**
In Amazon Athena, tables and databases contain the metadata that details a schema for underlying source data. For each dataset, a table must exist in Athena. The metadata in the table tells Athena the location of your Amazon S3 bucket. It also specifies the data structure, such as column names, data types, and the table's name. Databases only hold the metadata and schema information for a dataset.

## Creating multiple data lakes
<a name="creating-multiple-data-lakes"></a>

Multiple data lakes can be created by providing a unique Glue database name to specify where to store call insights. For a given AWS account, there can be several call analytics configurations, each with a corresponding data lake. This means that data separation can be applied for certain use cases, such as customizing retention policy, and access policy on how the data is stored. There can be different security policies applied for access of insights, recordings, and metadata.

## Data lake regional availability
<a name="data-lake-regions"></a>

The Amazon Chime SDK data lake is available in the following Regions.

| Region | Glue table | Quick |
| --- | --- | --- |
| us-east-1 | Available | Available |
| us-west-2 | Available | Available |
| eu-central-1 | Available | Available |

## Data lake architecture
<a name="data-lake-architecture"></a>

The following diagram shows the data lake architecture. Numbers in the drawing correspond to the numbered text below.

![The program flow through a data lake.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/call-analytics-data-lake-architecture.png)

In the diagram, once you use the AWS console to deploy the CloudFormation template from the media insights pipeline configuration setup workflow, the following data flows to the Amazon S3 bucket:

1. The Amazon Chime SDK call analytics will start streaming real-time data to the customer's Kinesis Data Stream.

1. The Amazon Kinesis Firehose buffers this real-time data until it accumulates 128 MB, or 60 seconds elapses, whichever is first. Firehose then uses the `amazon_chime_sdk_call_analytics_firehose_schema` in the Glue Data Catalog to compress the data and transforms the JSON records to a parquet file.

1. The parquet file resides in your Amazon S3 bucket, in a partitioned format.

1. In addition to real-time data, post-call Amazon Transcribe Call Analytics summary .wav files (redacted and non-redacted, if specified in the configuration), and call recording .wav files are also sent to your Amazon S3 Bucket.

1. You can use Amazon Athena and standard SQL to query the data in the Amazon S3 bucket.

1. The CloudFormation template also creates a Glue Data Catalog to query this post-call summary data through Athena.

1. All the data on Amazon S3 bucket can also be visualized using Quick. QuickSight builds up a connection with an Amazon S3 bucket using Amazon Athena.

The Amazon Athena table uses the following features to optimize query performance:

**Data partitioning**
Partitioning divides your table into parts and keeps the related data together based on column values such as date, country, and region. Partitions act as virtual columns. In this case, the CloudFormation template defines partitions at table creation, which helps reduce the amount of data scanned per query and improves performance. You can also filter by partition to restrict the amount of data scanned by a query. For more information, refer to [Partitioning data in Athena](https://docs.aws.amazon.com/athena/latest/ug/partitions.html) in the *Amazon Athena User Guide*.
This example shows partitioning structure with a date of January 1, 2023:

1.

   ```
   s3://example-bucket/amazon_chime_sdk_data_lake
                               /serviceType=CallAnalytics/detailType={{{DETAIL_TYPE}}}/year={{2023}}
                               /month={{01}}/day={{01}}/example-file.parquet
   ```

1. where `DETAIL_TYPE` is one of the following:

   1. `CallAnalyticsMetadata`

   1. `TranscribeCallAnalytics`

   1. `TranscribeCallAnalyticsCategoryEvents`

   1. `Transcribe`

   1. `Recording`

   1. `VoiceAnalyticsStatus`

   1. `SpeakerSearchStatus`

   1. `VoiceToneAnalysisStatus`

**Optimize columnar data store generation**
Apache Parquet uses column-wise compression, compression based on data type, and predicate pushdown to store data. Better compression ratios or skipping blocks of data means reading fewer bytes from your Amazon S3 bucket. That leads to better query performance and reduced cost. For this optimization, data conversion from JSON to parquet is enabled in the Amazon Kinesis Data Firehose.

**Partition Projection**
This Athena feature automatically creates partitions for each day to improve date-based query performance.

## Data lake setup
<a name="data-lake-setup"></a>

Use the Amazon Chime SDK console to complete the following steps.

1. Start the Amazon Chime SDK console ([ https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home)) and in the navigation pane, under **Call Analytics**, choose **Configurations**.

1. Complete Step 1, choose **Next** and on the Step 2 page, choose the **Voice Analytics** check box.

1. Under **Output details**, select the **Data warehouse to perform historical analysis** checkbox, then choose the **Deploy CloudFormation stack** link.

   The system sends you to the **Quick create stack** page in the CloudFormation console.

1. Enter a name for the stack, then enter the following parameters:

   1. `DataLakeType` – Choose **Create Call Analytics DataLake**.

   1. `KinesisDataStreamName` – Choose your stream. It should be the stream used for call analytics streaming.

   1. `S3BucketURI` – Choose your Amazon S3 bucket. The URI must have the prefix `s3://{{bucket-name}}`

   1. `GlueDatabaseName` – Choose a unique AWS Glue Database name. You cannot reuse an existing database in AWS account.

1. Choose the acknowledgment checkbox, then choose **Create data lake**. Allow 10 minutes for the system to create the lake.

### Data lake setup using AWS CLI
<a name="data-lake-setup-using-cli"></a>

Use AWS CLI to create a role with permissions to call CloudFormation’s create stack. Follow the procedure below to create and setup the IAM roles. For more information, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-cli-creating-stack.html) in the *AWS CloudFormation User Guide*.

1. Create a role called *AmazonChimeSdkCallAnalytics-Datalake-Provisioning-Role* and attach a trust policy to the role allowing CloudFormation to assume the role.

   1. Create an IAM trust policy using the following template and save the file in .json format.

------
#### [ JSON ]

****

      ```
      {
          "Version":"2012-10-17",
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": {
                      "Service": "cloudformation.amazonaws.com"
                  },
                  "Action": "sts:AssumeRole",
                  "Condition": {}
              }
          ]
      }
      ```

------

   1. Run the **aws iam create-role** command and pass the trust policy as a parameter.

      ```
                                          aws iam create-role \
          --role-name AmazonChimeSdkCallAnalytics-Datalake-Provisioning-Role
          --assume-role-policy-document file://role-trust-policy.json
      ```

   1. Note down the *role arn* that is returned from the response. *role arn* is required in the next step.

1. Create a policy with permission to create a CloudFormation stack.

   1. Create an IAM policy using the following template and save the file in .json format. This file is required when calling create-policy.

------
#### [ JSON ]

****

      ```
      {
          "Version":"2012-10-17",
          "Statement": [
              {
                  "Sid": "DeployCloudFormationStack",
                  "Effect": "Allow",
                  "Action": [
                      "cloudformation:CreateStack"
                  ],
                  "Resource": "*"
              }
          ]
      }
      ```

------

   1. Run **aws iam create-policy** and pass create stack policy as a parameter.

      ```
                                      aws iam create-policy --policy-name testCreateStackPolicy
      --policy-document file://create-cloudformation-stack-policy.json
      ```

   1. Note down the *role arn* that is returned from the response. *role arn* is required in the next step.

1. Attach the policy to the role **aws iam attach-role-policy**.

   ```
                               aws iam attach-role-policy --role-name {Role name created above}
   --policy-arn {Policy ARN created above}
   ```

1. Create a CloudFormation stack and enter the required parameters: **aws cloudformation create-stack**.

   Provide parameter values for each ParameterKey using ParameterValue.

   ```
                               aws cloudformation create-stack  --capabilities CAPABILITY_NAMED_IAM
   --stack-name testDeploymentStack
   --template-url https://chime-sdk-assets.s3.amazonaws.com/public_templates/AmazonChimeSDKDataLake.yaml
   --parameters  ParameterKey=S3BucketURI,ParameterValue={S3 URI}
   ParameterKey=DataLakeType,ParameterValue="Create call analytics datalake"
   ParameterKey=KinesisDataStreamName,ParameterValue={Name of Kinesis Data Stream}
   --role-arn {Role ARN created above}
   ```

#### Resources created by data lake setup
<a name="cf-resources"></a>

The following table lists the resources created when you create a data lake.

- **AWS Glue Data Catalog Database**
  - **Resource name and description:** **GlueDatabaseName** – Logically groups all AWS Glue Data tables belonging to call insights and voice analytics.
  - **Service name:** Call analytics, voice analytics

- ** AWS Glue Data Catalog Tables **
  - **Resource name and description:** **amazon\_chime\_sdk\_call\_analytics\_firehose\_schema** – Combined schema for call analytics voice analytics that is fed to the Kinesis Firehose. / **Service name:** Call analytics, voice analytics
  - **Resource name and description:** **call\_analytics\_metadata** – Schema for call analytics metadata. Contains SIPmetadata and OneTimeMetadata. / **Service name:** Call analytics
  - **Resource name and description:** call\_analytics\_recording\_metadata – Schema for Recording and Voice Enhancement metadata / **Service name:** Call analytics, voice analytics
  - **Resource name and description:** **transcribe\_call\_analytics** – Schema for TranscribeCallAnalytics Payload "utteranceEvent" / **Service name:** Call analytics
  - **Resource name and description:** **transcribe\_call\_analytics\_category\_events** – Schema for TranscribeCallAnalytics Payload "categoryEvent" / **Service name:** Call analytics
  - **Resource name and description:** **transcribe\_call\_analytics\_post\_call** – Schema for Post Call Transcribe Call Analytics summary payload / **Service name:** Call analytics
  - **Resource name and description:** **transcribe** – Schema for Transcribe Payload / **Service name:** Call analytics
  - **Resource name and description:** **voice\_analytics\_status** – Schema for voice analytics ready events / **Service name:** Voice analytics
  - **Resource name and description:** **speaker\_search\_status** – Schema for identification matches / **Service name:** Voice analytics
  - **Resource name and description:** **voice\_tone\_analysis\_status** – Schema for voice tone analysis events / **Service name:** Voice analytics

- **Amazon Kinesis Data Firehose**
  - **Resource name and description:** **AmazonChimeSDK-call-analytics-{{UUID}}** – Kinesis Data Firehose piping data for call analytics
  - **Service name:** Call analytics, voice analytics

- **Amazon Athena Workgroup**
  - **Resource name and description:** **GlueDatabaseName-AmazonChimeSDKDataAnalytics** – Logical group of users to control the resources they have access to when running queries.
  - **Service name:** Call analytics, voice analytics
