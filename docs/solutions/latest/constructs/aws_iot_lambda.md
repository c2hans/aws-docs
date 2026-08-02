---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_iot_lambda.html
---

# aws-iot-lambda
<a name="aws_iot_lambda"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_iot_lambda`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-iot-lambda`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.iotlambda`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS IoT MQTT topic rule and an AWS Lambda function pattern.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { IotToLambdaProps, IotToLambda } from '@aws-solutions-constructs/aws-iot-lambda';
import * as lambda from 'aws-cdk-lib/aws-lambda';

const constructProps: IotToLambdaProps = {
  lambdaFunctionProps: {
    code: lambda.Code.fromAsset(`lambda`),
    runtime: lambda.Runtime.NODEJS_22_X,
    handler: 'index.handler'
  },
  iotTopicRuleProps: {
    topicRulePayload: {
      ruleDisabled: false,
      description: "Processing of DTC messages from the AWS Connected Vehicle Solution.",
      sql: "SELECT * FROM 'connectedcar/dtc/#'",
      actions: []
    }
  }
};

new IotToLambda(this, 'test-iot-lambda-integration', constructProps);
```

```
from aws_solutions_constructs.aws_iot_lambda import IotToLambdaProps, IotToLambda
from aws_cdk import (
    aws_iot as iot,
    aws_lambda as _lambda,
    Stack
)
from constructs import Construct

IotToLambda(self, 'test_iot_lambda',
            lambda_function_props=_lambda.FunctionProps(
                code=_lambda.Code.from_asset('lambda'),
                runtime=_lambda.Runtime.PYTHON_3_14,
                handler='index.handler'
            ),
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
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.iot.*;
import software.amazon.awscdk.services.iot.CfnTopicRule.TopicRulePayloadProperty;
import software.amazon.awsconstructs.services.iotlambda.*;

new IotToLambda(this, "test-iot-lambda-integration", new IotToLambdaProps.Builder()
        .lambdaFunctionProps(new FunctionProps.Builder()
                .runtime(Runtime.NODEJS_22_X)
                .code(Code.fromAsset("lambda"))
                .handler("index.handler")
                .build())
        .iotTopicRuleProps(new CfnTopicRuleProps.Builder()
                .topicRulePayload(new TopicRulePayloadProperty.Builder()
                        .ruleDisabled(false)
                        .description("Processing of DTC messages from the AWS Connected Vehicle Solution.")
                        .sql("SELECT * FROM 'connectedcar/dtc/#'")
                        .actions(List.of())
                        .build())
                .build())
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingLambdaObj? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Optional - instance of an existing Lambda Function object, providing both this and `lambdaFunctionProps` will cause an error. |
| lambdaFunctionProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html)  | Optional - user provided props to override the default props for the Lambda function. Providing both this and `existingLambdaObj` causes an error. |
| iotTopicRuleProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRuleProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRuleProps.html)  | User provided CfnTopicRuleProps to override the defaults |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| iotTopicRule |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRule.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iot.CfnTopicRule.html)  | Returns an instance of iot.CfnTopicRule created by the construct |
| lambdaFunction |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Returns an instance of lambda.Function created by the construct |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon IoT Rule
<a name="_amazon_iot_rule"></a>
+ Configure least privilege access IAM role for Amazon IoT

### AWS Lambda Function
<a name="_aws_lambda_function"></a>
+ Configure limited privilege access IAM role for Lambda function
+ Enable reusing connections with Keep-Alive for NodeJs Lambda function
+ Enable X-Ray Tracing
+ Set Environment Variables
  + AWS\_NODEJS\_CONNECTION\_REUSE\_ENABLED (for Node 10.x and higher functions)

## Architecture
<a name="_architecture"></a>

![Diagram showing the IoT rule, Lambda function, log group and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-iot-lambda.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-iot-lambda) for this pattern to view the code, read/create issues and pull requests and more.
