---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_kinesisstreams_kinesisfirehose_s3.html
---

# aws-kinesisstreams-kinesisfirehose-s3
<a name="aws_kinesisstreams_kinesisfirehose_s3"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_kinesisstreams_kinesisfirehose_s3`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-kinesis-streams-kinesis-firehose-s3`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.kinesisstreamskinesisfirehoses3`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an Amazon Kinesis Data Stream (KDS) connected to Amazon Kinesis Data Firehose (KDF) delivery stream connected to an Amazon S3 bucket.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { KinesisStreamsToKinesisFirehoseToS3 } from '@aws-solutions-constructs/aws-kinesisstreams-kinesisfirehose-s3';

new KinesisStreamsToKinesisFirehoseToS3(this, 'test-stream-firehose-s3', {});
```

```
from aws_solutions_constructs.aws_kinesis_streams_kinesis_firehose_s3 import KinesisStreamsToKinesisFirehoseToS3
from aws_cdk import Stack
from constructs import Construct

KinesisStreamsToKinesisFirehoseToS3(self, 'test_stream_firehose_s3')
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.kinesisstreamskinesisfirehoses3.*;

new KinesisStreamsToKinesisFirehoseToS3(this, "test_stream_firehose_s3", new KinesisStreamsToKinesisFirehoseToS3Props.Builder()
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| bucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Bucket. |
| createCloudWatchAlarms? |  `boolean`  | Optional whether to create recommended CloudWatch alarms. |
| existingBucketObj? |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Optional - existing instance of S3 Bucket. If this is provided, then also providing bucketProps causes an error. then also providing bucketProps causes an error. |
| existingLoggingBucketObj? |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Optional existing instance of logging S3 Bucket object for the S3 Bucket created by the pattern. |
| existingStreamObj? |  [`kinesis.Stream`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html)  | Optional existing instance of Kinesis Stream, providing both this and `kinesisStreamProps` will cause an error. |
| kinesisFirehoseProps? |  [`kinesisfirehose.CfnDeliveryStreamProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStreamProps.html)\|`any` | Optional user provided props to override the default props for Kinesis Firehose Delivery Stream. |
| kinesisStreamProps? |  [`kinesis.StreamProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.StreamProps.html)  | Optional user-provided props to override the default props for the Kinesis stream. |
| logGroupProps? |  [`logs.LogGroupProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html)  | Optional user provided props to override the default props for for the CloudWatchLogs LogGroup. |
| loggingBucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Logging Bucket. |
| logS3AccessLogs? | boolean | Whether to turn on Access Logging for the S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. default - true |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| cloudwatchAlarms? |  [`cloudwatch.Alarm[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html)  | Returns a list of cloudwatch.Alarm created by the construct |
| kinesisFirehose |  [`kinesisfirehose.CfnDeliveryStream`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.html)  | Returns an instance of kinesisfirehose.CfnDeliveryStream created by the construct |
| kinesisFirehoseLogGroup |  [`logs.LogGroup`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html)  | Returns an instance of the logs.LogGroup created by the construct for Kinesis Data Firehose delivery stream |
| kinesisFirehoseRole |  [`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for Kinesis Data Firehose delivery stream |
| kinesisStream |  [`kinesis.Stream`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html)  | Returns an instance of the Kinesis stream created by the pattern |
| kinesisStreamRole |  [`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for Kinesis stream |
| s3Bucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct |
| s3LoggingBucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct as the logging bucket for the primary bucket |
| s3BucketInterface |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Returns an instance of s3.IBucket created by the construct |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon Kinesis Stream
<a name="_amazon_kinesis_stream"></a>
+ Configure least privilege access IAM role for Kinesis Stream
+ Enable server-side encryption for Kinesis Stream using AWS Managed KMS Key
+ Deploy best practices CloudWatch Alarms for the Kinesis Stream

### Amazon Kinesis Firehose
<a name="_amazon_kinesis_firehose"></a>
+ Enable CloudWatch logging for Kinesis Firehose
+ Configure least privilege access IAM role for Amazon Kinesis Firehose

### Amazon S3 Bucket
<a name="_amazon_s3_bucket"></a>
+ Configure Access logging for S3 Bucket
+ Enable server-side encryption for S3 Bucket using AWS managed KMS Key
+ Enforce encryption of data in transit
+ Turn on the versioning for S3 Bucket
+ Don’t allow public access for S3 Bucket
+ Retain the S3 Bucket when deleting the CloudFormation stack
+ Applies Lifecycle rule to move noncurrent object versions to Glacier storage after 90 days

## Architecture
<a name="_architecture"></a>

![Diagram showing the Kinesis data stream, Kinesis data firehose, CloudWatch log group, S3 buckets and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-kinesisstreams-kinesisfirehose-s3.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-kinesisstreams-kinesisfirehose-s3) for this pattern to view the code, read/create issues and pull requests and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
