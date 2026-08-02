---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_iot_s3.html
---

# aws-iot-s3
<a name="aws_iot_s3"></a>

![Stability:Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

All classes are under active development and subject to non-backward compatible changes or removal in any future version. These are not subject to the [Semantic Versioning](https://semver.org/) model. This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_iot_s3`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-iot-s3`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.iots3`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS IoT MQTT topic rule and an Amazon S3 Bucket pattern.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { IotToS3Props, IotToS3 } from '@aws-solutions-constructs/aws-iot-s3';

const constructProps: IotToS3Props = {
  iotTopicRuleProps: {
    topicRulePayload: {
      ruleDisabled: false,
      description: "Testing the IotToS3 Pattern",
      sql: "SELECT * FROM 'solutions/constructs'",
      actions: []
    }
  }
};

new IotToS3(this, 'test-iot-s3-integration', constructProps);
```

```
from aws_solutions_constructs.aws_iot_s3 import IotToS3Props, IotToS3
from aws_cdk import (
    aws_iot as iot,
    Stack
)
from constructs import Construct

IotToS3(self, 'test_iot_s3',
        iot_topic_rule_props=iot.CfnTopicRuleProps(
            topic_rule_payload=iot.CfnTopicRule.TopicRulePayloadProperty(
                rule_disabled=False,
                description="Testing the IotToS3 Pattern",
                sql="SELECT * FROM 'solutions/constructs'",
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
import software.amazon.awsconstructs.services.iots3.*;

new IotToS3(this, "test_iot_s3", new IotToS3Props.Builder()
        .iotTopicRuleProps(new CfnTopicRuleProps.Builder()
                .topicRulePayload(new TopicRulePayloadProperty.Builder()
                        .ruleDisabled(false)
                        .description("Testing the IotToS3 Pattern")
                        .sql("SELECT * FROM 'solutions/constructs'")
                        .actions(List.of())
                        .build())
                .build())
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingBucketInterface? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Existing S3 Bucket interface. Providing this property and `bucketProps` results in an error. |
| bucketProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Bucket. Providing this and `existingBucketObj` reults in an error. |
| loggingBucketProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Logging Bucket. |
| iotTopicRuleProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRuleProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRuleProps.html)  | User provided CfnTopicRuleProps to override the defaults. |
| s3Key |  `string`  | User provided s3Key to override the default (`${topic()}/${timestamp()}`) object key. Used to store messages matched by the IoT Rule. |
| logS3AccessLogs? |  `boolean`  | Whether to turn on Access Logging for the S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. default - true |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| s3Bucket? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of the S3 bucket created by the pattern. If an existingBucketInterface is provided in IotToS3Props, then this value will be undefined |
| s3BucketInterface? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Returns S3 Bucket interface created or used by the pattern. If an existingBucketInterface is provided in IotToS3Props, then only this value will be set and s3Bucket will be undefined. If the construct creates the bucket, then both properties will be set. |
| s3LoggingBucket? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of `s3.Bucket` created by the construct as the logging bucket for the primary bucket. |
| iotActionsRole |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of `iam.Role` created by the construct, which allows IoT to publish messages to the S3 bucket. |
| iotTopicRule |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRule.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRule.html)  | Returns an instance of `iot.CfnTopicRule` created by the construct |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon IoT Rule
<a name="_amazon_iot_rule"></a>
+ Configure an IoT Rule to send messages to the S3 Bucket

### Amazon IAM Role
<a name="_amazon_iam_role"></a>
+ Configure least privilege access IAM role for Amazon IoT to be able to publish messages to the S3 Bucket

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

![Diagram showing the IoT rule, S3 buckets and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-iot-s3.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-iot-s3) for this pattern to view the code, read/create issues and pull requests and more.
