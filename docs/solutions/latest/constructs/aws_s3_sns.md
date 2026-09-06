---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_s3_sns.html
---

# aws-s3-sns
<a name="aws_s3_sns"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_s3_sns`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-s3-sns`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.s3sns`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an Amazon S3 Bucket that is configured to send S3 event messages to an Amazon SNS topic.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { S3ToSns } from "@aws-solutions-constructs/aws-s3-sns";

new S3ToSns(this, 'S3ToSNSPattern', {});
```

```
from aws_solutions_constructs.aws_s3_sns import S3ToSns
from aws_cdk import Stack
from constructs import Construct

S3ToSns(self, 'S3ToSNSPattern')
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.s3sns.*;

new S3ToSns(this, "S3ToSNSPattern", new S3ToSnsProps.Builder()
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingBucketObj? |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Optional - existing instance of S3 Bucket. If this is provided, then also providing bucketProps causes an error. |
| bucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Bucket. |
| s3EventTypes? |  [`s3.EventType[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.EventType.html)  | The S3 event types that will trigger the notification. Defaults to s3.EventType.OBJECT\_CREATED. |
| s3EventFilters? |  [`s3.NotificationKeyFilter[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.NotificationKeyFilter.html)  | S3 object key filter rules to determine which objects trigger this event. If not specified no filter rules will be applied. |
| loggingBucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Logging Bucket. |
| logS3AccessLogs? |  `boolean`  | Whether to turn on Access Logging for the S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. default - true |
| existingTopicObj? |  [`sns.Topic`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sns.Topic.html)  | Optional - existing instance of SNS topic object, providing both this and `topicProps` will cause an error. If the SNS Topic is encrypted with a Customer-Managed KMS Key, the key must be specified in the `existingTopicEncryptionKey` property. |
| existingTopicEncryptionKey? |  [`kms.Key`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)  | If an existing topic is provided in the `existingTopicObj` property, and that topic is encrypted with a Customer-Managed KMS key, this property also needs to be set with same key. |
| topicProps? |  [`sns.TopicProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sns.TopicProps.html)  | Optional - user provided properties to override the default properties for the SNS topic. Providing both this and `existingTopicObj` causes an error. |
| enableEncryptionWithCustomerManagedKey? |  `boolean`  | If no key is provided, this flag determines whether the topic is encrypted with a new CMK or an AWS managed key. This flag is ignored if any of the following are defined: topicProps.encryptionMasterKey, encryptionKey or encryptionKeyProps. |
| encryptionKey? |  [`kms.Key`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)  | An optional, imported encryption key to encrypt the SNS Topic with. |
| encryptionKeyProps? |  [`kms.KeyProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html#construct-props)  | Optional user provided properties to override the default properties for the KMS encryption key used to encrypt the SNS Topic with. |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| snsTopic |  [`sns.Topic`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sns.Topic.html)  | Returns an instance of the SNS Topic created by the pattern. |
| encryptionKey? |  [`kms.Key`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)  | Returns an instance of the kms.Key associated with the SNS Topic |
| s3Bucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of the s3.Bucket created by the construct |
| s3LoggingBucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct as the logging bucket for the primary bucket. |
| s3BucketInterface |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Returns an instance of s3.IBucket created by the construct. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon S3 Bucket
<a name="_amazon_s3_bucket"></a>
+ Configure Access logging for the S3 Bucket
+ Enable server-side encryption for S3 Bucket using an AWS managed KMS Key
+ Enforce encryption of data in transit
+ Turn on the versioning for the S3 Bucket
+ Don’t allow public access for the S3 Bucket
+ Retain the S3 Bucket when deleting the CloudFormation stack
+ Applies Lifecycle rule to move noncurrent object versions to Glacier storage after 90 days

### Amazon SNS Topic
<a name="_amazon_sns_topic"></a>
+ Configure least privilege SNS Topic access policy to allow the S3 Bucket to publish messages to it
+ Enable server-side encryption for the SNS Topic using an AWS managed KMS Key
+ Enforce encryption of data in transit

## Architecture
<a name="_architecture"></a>

![Diagram showing the S3 bucket and SNS topic created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-s3-sns.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-s3-sns) for this pattern to view the code, read/create issues and pull requests and more.
