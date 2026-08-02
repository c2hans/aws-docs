---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_s3_stepfunctions.html
---

# aws-s3-stepfunctions
<a name="aws_s3_stepfunctions"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_s3_stepfunctions`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-s3-stepfunctions`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.s3stepfunctions`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an Amazon S3 bucket connected to an AWS Step Functions.

 *Note - This constructs sends S3 Event Notification to EventBridge, then triggers AWS Step Functions State Machine executions from EventBridge.*

 *An alternative architecture can be built that triggers a Lambda function from S3 Event notifications using aws-s3-lambda and aws-lambda-stepfunctions. Channelling the S3 events through Lambda is less flexible than EventBridge, but is more cost effective and has lower latency.*

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { S3ToStepfunctions, S3ToStepfunctionsProps } from '@aws-solutions-constructs/aws-s3-stepfunctions';
import * as stepfunctions from 'aws-cdk-lib/aws-stepfunctions';

const startState = new stepfunctions.Pass(this, 'StartState');

new S3ToStepfunctions(this, 'test-s3-stepfunctions-stack', {
    stateMachineProps: {
      definition: startState
    }
});
```

```
from aws_solutions_constructs.aws_s3_stepfunctions import S3ToStepfunctions
from aws_cdk import (
    aws_stepfunctions as stepfunctions,
    Stack
)
from constructs import Construct

start_state = stepfunctions.Pass(self, 'start_state')

S3ToStepfunctions(
    self, 'test_s3_stepfunctions_stack',
    state_machine_props=stepfunctions.StateMachineProps(
        definition=start_state)
)
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.stepfunctions.*;
import software.amazon.awsconstructs.services.s3stepfunctions.*;

final Pass startState = new Pass(this, "StartState");

new S3ToStepfunctions(this, "test_s3_stepfunctions_stack",
        new S3ToStepfunctionsProps.Builder()
                .stateMachineProps(new StateMachineProps.Builder()
                        .definition(startState)
                        .build())
                .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingBucketObj? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Optional - existing instance of S3 Bucket. If this is provided, then also providing bucketProps causes an error. **The existing bucket must have [EventBridge enabled](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications-eventbridge.html) for this to work.**  |
| bucketProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Bucket, providing both this and `existingBucketObj` will cause an error. |
| stateMachineProps |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions.StateMachineProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions.StateMachineProps.html)  | User provided props for the sfn.StateMachine. This or existingStateMachine is required. If you provide a value for logs.destination, it must be an ILogGroup even though the prop type is ILogGroupRef. The CDK change to ILogGroupRef in v2.235.0 is incompatible with our interface without introducing breaking changes, so we still require an ILogGroup (as this implements ILogGroupRef, you can just assign it to logs.destination) |
| eventRuleProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.RuleProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.RuleProps.html)  | Optional user provided eventRuleProps to override the defaults. |
| deployCloudTrail? |  `boolean`  | Whether to deploy a Trail in AWS CloudTrail to log API events in Amazon S3. Defaults to `true`. **This is now deprecated and ignored because the construct no longer needs CloudTrail since it uses S3 Event Notifications**. |
| createCloudWatchAlarms |  `boolean`  | Whether to create recommended CloudWatch alarms. |
| logGroupProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html)  | Optional user provided props to override the default props for for the CloudWatchLogs LogGroup. |
| loggingBucketProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Logging Bucket. |
| logS3AccessLogs? | boolean | Whether to turn on Access Logging for the S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. default - true |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| stateMachine |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions.StateMachine.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions.StateMachine.html)  | Returns an instance of sfn.StateMachine created by the construct. |
| stateMachineLogGroup |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.ILogGroup.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.ILogGroup.html)  | Returns an instance of the ILogGroup created by the construct for StateMachine. |
| cloudwatchAlarms? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html)  | Returns a list of cloudwatch.Alarm created by the construct. |
| s3Bucket? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of the s3.Bucket created by the construct. |
| s3LoggingBucket? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct as the logging bucket for the primary bucket. |
| s3BucketInterface |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Returns an instance of s3.IBucket created by the construct. |

 *Note - with the release of Enable EventBridge for Amazon S3, AWS CloudTrail is no longer required to implement this construct. Because of this, the following properties have been removed:* - cloudtrail - cloudtrailBucket - cloudtrailLoggingBucket

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon S3 Bucket
<a name="_amazon_s3_bucket"></a>
+ Enable EventBridge to send events from the S3 Bucket
+ Configure Access logging for S3 Bucket
+ Enable server-side encryption for S3 Bucket using AWS managed KMS Key
+ Enforce encryption of data in transit
+ Turn on the versioning for S3 Bucket
+ Don’t allow public access for S3 Bucket
+ Retain the S3 Bucket when deleting the CloudFormation stack
+ Applies Lifecycle Rule to move noncurrent object versions to Glacier storage after 90 days

### AWS S3 Event Notification
<a name="_aws_s3_event_notification"></a>
+ Enable S3 to send events to EventBridge when an object is created.

### Amazon CloudWatch Events Rule
<a name="_amazon_cloudwatch_events_rule"></a>
+ Grant least privilege permissions to CloudWatch Events to trigger the Lambda Function

### AWS Step Functions
<a name="_aws_step_functions"></a>
+ Enable CloudWatch logging for API Gateway
+ Deploy best practices CloudWatch Alarms for the Step Functions

## Architecture
<a name="_architecture"></a>

![Diagram showing the S3 bucket, EventBridge rule, Step Functions state machine, CloudWatch log group and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-s3-stepfunctions.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-s3-stepfunctions) for this pattern to view the code, read/create issues and pull requests and more.
