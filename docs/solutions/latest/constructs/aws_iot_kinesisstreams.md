---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_iot_kinesisstreams.html
---

# aws-iot-kinesisstreams
<a name="aws_iot_kinesisstreams"></a>

![Stability:Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

All classes are under active development and subject to non-backward compatible changes or removal in any future version. These are not subject to the [Semantic Versioning](https://semver.org/) model. This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_iot_kinesisstreams`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-iot-kinesisstreams`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.iotkinesisstreams`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS IoT MQTT topic rule to send data to an Amazon Kinesis Data Stream.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { IotToKinesisStreamsProps, IotToKinesisStreams } from '@aws-solutions-constructs/aws-iot-kinesisstreams';

const constructProps: IotToKinesisStreamsProps = {
  iotTopicRuleProps: {
    topicRulePayload: {
      ruleDisabled: false,
      description: "Sends data to kinesis data stream",
      sql: "SELECT * FROM 'solutions/construct'",
      actions: []
    }
  }
};

new IotToKinesisStreams(this, 'test-iot-kinesisstreams', constructProps);
```

```
from aws_solutions_constructs.aws_iot_kinesisstreams import IotToKinesisStreamsProps, IotToKinesisStreams
from aws_cdk import (
    aws_iot as iot,
    Stack
)
from constructs import Construct

IotToKinesisStreams(self, 'test-iot-kinesisstreams',
                    iot_topic_rule_props=iot.CfnTopicRuleProps(
                        topic_rule_payload=iot.CfnTopicRule.TopicRulePayloadProperty(
                            rule_disabled=False,
                            description="Sends data to kinesis data stream",
                            sql="SELECT * FROM 'solutions/construct'",
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
import software.amazon.awsconstructs.services.iotkinesisstreams.*;

new IotToKinesisStreams(this, "test-iot-kinesisstreams", new IotToKinesisStreamsProps.Builder()
        .iotTopicRuleProps(new CfnTopicRuleProps.Builder()
                .topicRulePayload(new TopicRulePayloadProperty.Builder()
                        .ruleDisabled(false)
                        .description("Sends data to kinesis data stream")
                        .sql("SELECT * FROM 'solutions/construct'")
                        .actions(List.of())
                        .build())
                .build())
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| iotTopicRuleProps |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRuleProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRuleProps.html)  | User provided CfnTopicRuleProps to override the defaults |
| existingStreamObj? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html)  | Existing instance of Kinesis Stream, providing both this and `kinesisStreamProps` will cause an error. |
| kinesisStreamProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.StreamProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.StreamProps.html)  | Optional user-provided props to override the default props for the Kinesis data stream, providing both this and `existingStreamObj` will cause an error |
| createCloudWatchAlarms |  `boolean`  | Whether to create recommended CloudWatch alarms for Kinesis Data Stream. Default value is set to `true`  |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| iotTopicRule |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRule.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRule.html)  | Returns an instance of iot.CfnTopicRule created by the construct |
| iotActionsRole |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for IoT Rule |
| kinesisStream |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html)  | Returns an instance of the Kinesis stream created by the construct. |
| cloudwatchAlarms? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html)  | Returns an array of recommended CloudWatch Alarms created by the construct for Kinesis Data stream |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon IoT Rule
<a name="_amazon_iot_rule"></a>
+ Configure least privilege access IAM role for Amazon IoT Rule

### Amazon Kinesis Data Stream
<a name="_amazon_kinesis_data_stream"></a>
+ Configure recommended CloudWatch Alarms for Amazon Kinesis Data Stream
+ Configure least privilege access IAM role for Amazon Kinesis Data Stream

## Architecture
<a name="_architecture"></a>

![Diagram showing the IoT rule, Kinesis data stream, CloudWatch alarm and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-iot-kinesisstreams.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-iot-kinesisstreams) for this pattern to view the code, read/create issues and pull requests and more.
