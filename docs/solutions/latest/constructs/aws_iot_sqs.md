---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_iot_sqs.html
---

# aws-iot-sqs
<a name="aws_iot_sqs"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_iot_sqs`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-iot-sqs`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.iotsqs`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS IoT MQTT topic rule and an AWS SQS Queue pattern.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { IotToSqsProps, IotToSqs } from '@aws-solutions-constructs/aws-iot-sqs';

const constructProps: IotToSqsProps = {
  iotTopicRuleProps: {
    topicRulePayload: {
      ruleDisabled: false,
      description: "Testing the IotToSqs Pattern",
      sql: "SELECT * FROM 'iot/sqs/#'",
      actions: []
    }
  }
};

new IotToSqs(this, 'test-iot-sqs-integration', constructProps);
```

```
from aws_solutions_constructs.aws_iot_sqs import IotToSqs
from aws_cdk import (
    aws_iot as iot,
    Stack
)
from constructs import Construct

IotToSqs(self, 'test_iot_sqs',
    iot_topic_rule_props=iot.CfnTopicRuleProps(
        topic_rule_payload=iot.CfnTopicRule.TopicRulePayloadProperty(
            rule_disabled=False,
            description="Testing the IotToSqs Pattern",
            sql="SELECT * FROM 'iot/sqs/#'",
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
import software.amazon.awsconstructs.services.iotsqs.*;

new IotToSqs(this, "test_iot_sqs", new IotToSqsProps.Builder()
        .iotTopicRuleProps(new CfnTopicRuleProps.Builder()
                .topicRulePayload(new TopicRulePayloadProperty.Builder()
                        .ruleDisabled(false)
                        .description("Testing the IotToSqs Pattern")
                        .sql("SELECT * FROM 'iot/sqs/#'")
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
| existingQueueObj? |  [`sqs.Queue`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.Queue.html)  | Existing instance of SQS queue object, providing both this and `queueProps` will cause an error. |
| queueProps? |  [`sqs.QueueProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.QueueProps.html)  | Optional - user provided properties to override the default properties for the SQS queue. Providing both this and `existingQueueObj` will cause an error. |
| deadLetterQueueProps? |  [`sqs.QueueProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.QueueProps.html)  | Optional user provided properties for the dead letter queue. |
| deployDeadLetterQueue? |  `boolean`  | Whether to deploy a secondary queue to be used as a dead letter queue. Default `true`. |
| maxReceiveCount? |  `number`  | The number of times a message can be unsuccessfully dequeued before being moved to the dead-letter queue. Required field if `deployDeadLetterQueue`=`true`. |
| enableEncryptionWithCustomerManagedKey? |  `boolean`  | If no key is provided, this flag determines whether the queue is encrypted with a new CMK or an AWS managed key. This flag is ignored if any of the following are defined: queueProps.encryptionMasterKey, encryptionKey or encryptionKeyProps. |
| encryptionKey? |  [`kms.Key`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)  | An optional, imported encryption key to encrypt the SQS Queue with. |
| encryptionKeyProps? |  [`kms.KeyProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html#construct-props)  | Optional user provided properties to override the default properties for the KMS encryption key used to encrypt the SQS queue with. |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| encryptionKey? |  [`kms.Key`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)  | Returns an instance of `kms.Key` used for the SQS queue. |
| iotActionsRole |  [`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of `iam.Role` created by the construct, which allows IoT to publish messages to the SQS Queue |
| sqsQueue |  [`sqs.Queue`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.Queue.html)  | Returns an instance of `sqs.Queue` created by the construct |
| deadLetterQueue? |  [`sqs.Queue`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.Queue.html)  | Returns an instance of the dead-letter SQS queue created by the pattern. |
| iotTopicRule |  [`iot.CfnTopicRule`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRule.html)  | Returns an instance of `iot.CfnTopicRule` created by the construct |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon IoT Rule
<a name="_amazon_iot_rule"></a>
+ Configure an IoT Rule to send messages to the SQS Queue

### Amazon IAM Role
<a name="_amazon_iam_role"></a>
+ Configure least privilege access IAM role for Amazon IoT to be able to publish messages to the SQS Queue

### Amazon SQS Queue
<a name="_amazon_sqs_queue"></a>
+ Deploy a dead-letter queue for the source queue.
+ Enable server-side encryption for the source queue using a customer-managed AWS KMS key.
+ Enforce encryption of data in transit.

## Architecture
<a name="_architecture"></a>

![Diagram showing the IoT rule, SQS queue and dlg, and IAM role created by the construct](https://docs.aws.amazon.com/solutions/latest/constructs/images/aws-iot-sqs.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-iot-sqs) for this pattern to view the code, read/create issues and pull requests and more.
