---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_eventbridge_kinesisfirehose_s3.html
---

# aws-eventbridge-kinesisfirehose-s3
<a name="aws_eventbridge_kinesisfirehose_s3"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_eventbridge_kinesisfirehose_s3`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-eventbridge-kinesisfirehose-s3`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.eventbridgekinesisfirehoses3`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an Amazon EventBridge Rule to send data to an Amazon Kinesis Data Firehose delivery stream connected to an Amazon S3 bucket.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps, Duration } from 'aws-cdk-lib';
import { EventbridgeToKinesisFirehoseToS3, EventbridgeToKinesisFirehoseToS3Props } from '@aws-solutions-constructs/aws-eventbridge-kinesisfirehose-s3';
import * as events from 'aws-cdk-lib/aws-events';

const EventbridgeToKinesisFirehoseToS3Props: EventbridgeToKinesisFirehoseToS3Props = {
  eventRuleProps: {
    schedule: events.Schedule.rate(Duration.minutes(5))
  }
};

new EventbridgeToKinesisFirehoseToS3(this, 'test-eventbridge-firehose-s3', EventbridgeToKinesisFirehoseToS3Props);
```

```
from aws_solutions_constructs.aws_eventbridge_kinesis_firehose_s3 import EventbridgeToKinesisFirehoseToS3, EventbridgeToKinesisFirehoseToS3Props
from aws_cdk import (
    aws_events as events,
    Duration,
    Stack
)
from constructs import Construct

EventbridgeToKinesisFirehoseToS3(self, 'test-eventbridge-firehose-s3',
                                event_rule_props=events.RuleProps(
                                    schedule=events.Schedule.rate(
                                        Duration.minutes(5))
                                ))
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.Duration;
import software.amazon.awscdk.services.events.*;
import software.amazon.awsconstructs.services.eventbridgekinesisfirehoses3.*;

new EventbridgeToKinesisFirehoseToS3(this, "test-eventbridge-firehose-s3",
        new EventbridgeToKinesisFirehoseToS3Props.Builder()
                .eventRuleProps(new RuleProps.Builder()
                        .schedule(Schedule.rate(Duration.minutes(5)))
                        .build())
                .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingEventBusInterface? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html)  | Optional - user provided custom EventBus for this construct to use. Providing both this and `eventBusProps` causes an error. |
| eventBusProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.EventBusProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.EventBusProps.html)  | Optional - user provided properties to override the default properties when creating a custom EventBus. Setting this value to `{}` will create a custom EventBus using all default properties. If neither this nor `existingEventBusInterface` is provided the construct will use the default EventBus. Providing both this and `existingEventBusInterface` causes an error. |
| eventRuleProps |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.RuleProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.RuleProps.html)  | User provided eventRuleProps to override the defaults. |
| kinesisFirehoseProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStreamProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStreamProps.html)  | Optional user provided props to override the default props for Kinesis Firehose Delivery Stream |
| existingBucketObj? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Optional - existing instance of S3 Bucket. If this is provided, then also providing bucketProps causes an error. |
| bucketProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Bucket, providing both this and `existingBucketObj` will cause an error. |
| logGroupProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html)  | User provided props to override the default props for for the CloudWatchLogs LogGroup. |
| loggingBucketProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Logging Bucket. |
| logS3AccessLogs? | boolean | Whether to turn on Access Logging for the S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. default - true |

**Note**
 `existingLoggingBucketObj` has been deprecated - to specify an existing Log Bucket, use `bucketProps.serverAccessLogsBucket`.

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| eventBus? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html)  | Returns the instance of events.IEventBus used by the construct |
| eventsRule |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.Rule.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.Rule.html)  | Returns an instance of events.Rule created by the construct. |
| kinesisFirehose |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.html)  | Returns an instance of kinesisfirehose.CfnDeliveryStream created by the construct |
| s3Bucket? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct |
| s3LoggingBucket? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct as the logging bucket for the primary bucket. |
| eventsRole |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for Events Rule |
| kinesisFirehoseRole |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for Kinesis Data Firehose delivery stream |
| kinesisFirehoseLogGroup |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html)  | Returns an instance of the LogGroup created by the construct for Kinesis Data Firehose delivery stream |
| s3BucketInterface |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Returns an instance of s3.IBucket created by the construct |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon EventBridge Rule
<a name="_amazon_eventbridge_rule"></a>
+ Configure least privilege access IAM role for Amazon EventBridge Rule to publish to the Kinesis Firehose Delivery Stream.

### Amazon Kinesis Firehose
<a name="_amazon_kinesis_firehose"></a>
+ Enable CloudWatch logging for Kinesis Firehose
+ Configure least privilege access IAM role for Amazon Kinesis Firehose

### Amazon S3 Bucket
<a name="_amazon_s3_bucket"></a>
+ Configure Access logging for S3 Bucket
+ Enable server-side encryption for S3 Bucket using AWS managed KMS Key
+ Turn on the versioning for S3 Bucket
+ Don’t allow public access for S3 Bucket
+ Retain the S3 Bucket when deleting the CloudFormation stack
+ Applies Lifecycle rule to move noncurrent object versions to Glacier storage after 90 days

## Architecture
<a name="_architecture"></a>

![Diagram showing the EventBridge rule, IAM roles, Kinesis data firehose, S3 buckets, CloudWatch log group and IAM roles created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-eventbridge-kinesisfirehose-s3.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-eventbridge-kinesisfirehose-s3) for this pattern to view the code, read/create issues and pull requests and more.
