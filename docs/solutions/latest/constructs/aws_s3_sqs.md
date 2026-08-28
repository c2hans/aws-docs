---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_s3_sqs.html
---

# aws-s3-sqs
<a name="aws_s3_sqs"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_s3_sqs`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-s3-sqs`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.s3sqs`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an Amazon S3 Bucket that is configured to send notifications to an Amazon SQS queue.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { S3ToSqs } from "@aws-solutions-constructs/aws-s3-sqs";

new S3ToSqs(this, 'S3ToSQSPattern', {});
```

```
from aws_solutions_constructs.aws_s3_sqs import S3ToSqs
from aws_cdk import Stack
from constructs import Construct

S3ToSqs(self, 'S3ToSQSPattern')
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.s3sqs.*;

new S3ToSqs(this, "S3ToSQSPattern", new S3ToSqsProps.Builder()
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingBucketObj? |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Optional - existing instance of S3 Bucket. If this is provided, then also providing bucketProps causes an error. |
| bucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Bucket, providing both this and `existingBucketObj` will cause an error. |
| s3EventTypes? |  [`s3.EventType[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.EventType.html)  | The S3 event types that will trigger the notification. Defaults to s3.EventType.OBJECT\_CREATED. |
| s3EventFilters? |  [`s3.NotificationKeyFilter[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.NotificationKeyFilter.html)  | S3 object key filter rules to determine which objects trigger this event. If not specified no filter rules will be applied. |
| existingQueueObj? |  [`sqs.Queue`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.Queue.html)  | Existing SQS queue to be used instead of the default queue. Providing both this and `queueProps` will cause an error. If the SQS queue is encrypted, the KMS key utilized for encryption must be a customer managed CMK. |
| queueProps? |  [`sqs.QueueProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.QueueProps.html)  | Optional - user provided properties to override the default properties for the SQS queue. Providing both this and `existingQueueObj` will cause an error. |
| deadLetterQueueProps? |  [`sqs.QueueProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.QueueProps.html)  | Optional user provided props to override the default props for the dead letter SQS queue. |
| deployDeadLetterQueue? |  `boolean`  | Whether to create a secondary queue to be used as a dead letter queue. Defaults to true. |
| maxReceiveCount? |  `number`  | The number of times a message can be unsuccessfully dequeued before being moved to the dead letter queue. Defaults to 15. |
| enableEncryptionWithCustomerManagedKey? |  `boolean`  | If no key is provided, this flag determines whether the queue is encrypted with a new CMK or an AWS managed key. This flag is ignored if any of the following are defined: queueProps.encryptionMasterKey, encryptionKey or encryptionKeyProps. |
| encryptionKey? |  [`kms.Key`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)  | An optional, imported encryption key to encrypt the SQS Queue with. |
| encryptionKeyProps? |  [`kms.KeyProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html#construct-props)  | Optional user provided properties to override the default properties for the KMS encryption key used to encrypt the SQS queue with. |
| loggingBucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Logging Bucket. |
| logS3AccessLogs? | boolean | Whether to turn on Access Logging for the S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. default - true |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| sqsQueue |  [`sqs.Queue`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.Queue.html)  | Returns an instance of the SQS queue created by the pattern. |
| deadLetterQueue? |  [`sqs.Queue`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.Queue.html)  | Returns an instance of the dead-letter SQS queue created by the pattern. |
| encryptionKey |  [`kms.IKey`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.IKey.html)  | Returns an instance of kms.Key used for the SQS queue. |
| s3Bucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of the s3.Bucket created by the construct |
| s3LoggingBucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct as the logging bucket for the primary bucket. |
| s3BucketInterface |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Returns an instance of s3.IBucket created by the construct. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon S3 Bucket
<a name="_amazon_s3_bucket"></a>
+ Configure Access logging for S3 Bucket
+ Enable server-side encryption for S3 Bucket using AWS managed KMS Key
+ Enforce encryption of data in transit
+ Turn on the versioning for S3 Bucket
+ Don’t allow public access for S3 Bucket
+ Retain the S3 Bucket when deleting the CloudFormation stack
+ Applies Lifecycle rule to move noncurrent object versions to Glacier storage after 90 days

### Amazon SQS Queue
<a name="_amazon_sqs_queue"></a>
+ Configure least privilege access permissions for SQS Queue
+ Deploy SQS dead-letter queue for the source SQS Queue
+ Enable server-side encryption for SQS Queue using Customer managed KMS Key
+ Enforce encryption of data in transit

## Architecture
<a name="_architecture"></a>

![Diagram showing the S3 bucket and SQS queue and dlq created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-s3-sqs.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-s3-sqs) for this pattern to view the code, read/create issues and pull requests and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
