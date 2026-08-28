---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_iot_kinesisfirehose_s3.html
---

# aws-iot-kinesisfirehose-s3
<a name="aws_iot_kinesisfirehose_s3"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_iot_kinesisfirehose_s3`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-iot-kinesisfirehose-s3`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.iotkinesisfirehoses3`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS IoT MQTT topic rule to send data to an Amazon Kinesis Data Firehose delivery stream connected to an Amazon S3 bucket.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { IotToKinesisFirehoseToS3Props, IotToKinesisFirehoseToS3 } from '@aws-solutions-constructs/aws-iot-kinesisfirehose-s3';

const constructProps: IotToKinesisFirehoseToS3Props = {
    iotTopicRuleProps: {
        topicRulePayload: {
            ruleDisabled: false,
            description: "Persistent storage of connected vehicle telematics data",
            sql: "SELECT * FROM 'connectedcar/telemetry/#'",
            actions: []
        }
    }
};

new IotToKinesisFirehoseToS3(this, 'test-iot-firehose-s3', constructProps);
```

```
from aws_solutions_constructs.aws_iot_kinesisfirehose_s3 import IotToKinesisFirehoseToS3Props, IotToKinesisFirehoseToS3
from aws_cdk import (
    aws_iot as iot,
    Stack
)
from constructs import Construct

IotToKinesisFirehoseToS3(self, 'test_iot_firehose_s3',
                        iot_topic_rule_props=iot.CfnTopicRuleProps(
                            topic_rule_payload=iot.CfnTopicRule.TopicRulePayloadProperty(
                                rule_disabled=False,
                                description="Persistent storage of connected vehicle telematics data",
                                sql="SELECT * FROM 'connectedcar/telemetry/#'",
                                actions=[]
                            )
                        ))
```

```
import software.constructs.Construct;
import java.util.List;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.iot.*;
import software.amazon.awscdk.services.iot.CfnTopicRule.TopicRulePayloadProperty;
import software.amazon.awsconstructs.services.iotkinesisfirehoses3.*;

new IotToKinesisFirehoseToS3(this, "test-iot-firehose-s3", new IotToKinesisFirehoseToS3Props.Builder()
        .iotTopicRuleProps(new CfnTopicRuleProps.Builder()
                .topicRulePayload(new TopicRulePayloadProperty.Builder()
                        .ruleDisabled(false)
                        .description("Persistent storage of connected vehicle telematics data")
                        .sql("SELECT * FROM 'connectedcar/telemetry/#'")
                        .actions(List.of())
                        .build())
                .build())
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| iotTopicRuleProps |  [`iot.CfnTopicRuleProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRuleProps.html)  | User provided CfnTopicRuleProps to override the defaults |
| kinesisFirehoseProps? |  [`kinesisfirehose.CfnDeliveryStreamProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStreamProps.html)  | Optional user provided props to override the default props for Kinesis Firehose Delivery Stream |
| existingBucketObj? |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Optional - existing instance of S3 Bucket. If this is provided, then also providing bucketProps causes an error. `bucketProps` will cause an error. |
| bucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Bucket, providing both this and `existingBucketObj` will cause an error. |
| logGroupProps? |  [`logs.LogGroupProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html)  | User provided props to override the default props for for the CloudWatchLogs LogGroup. |
| loggingBucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Logging Bucket. |
| logS3AccessLogs? | boolean | Whether to turn on Access Logging for the S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. default - true |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| kinesisFirehose |  [`kinesisfirehose.CfnDeliveryStream`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.html)  | Returns an instance of kinesisfirehose.CfnDeliveryStream created by the construct |
| s3Bucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct |
| s3LoggingBucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct as the logging bucket for the primary bucket. |
| iotTopicRule |  [`iot.CfnTopicRule`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRule.html)  | Returns an instance of iot.CfnTopicRule created by the construct |
| iotActionsRole |  [`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for IoT Rule |
| kinesisFirehoseRole |  [`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for Kinesis Data Firehose delivery stream |
| kinesisFirehoseLogGroup |  [`logs.LogGroup`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html)  | Returns an instance of the LogGroup created by the construct for Kinesis Data Firehose delivery stream |
| s3BucketInterface |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Returns an instance of s3.IBucket created by the construct |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon IoT Rule
<a name="_amazon_iot_rule"></a>
+ Configure least privilege access IAM role for Amazon IoT

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

![Diagram showing the IOT rule, Kinesis data firehose, S3 buckets, log group and IAM roles created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-iot-kinesisfirehose-s3.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-iot-kinesisfirehose-s3) for this pattern to view the code, read/create issues and pull requests and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
