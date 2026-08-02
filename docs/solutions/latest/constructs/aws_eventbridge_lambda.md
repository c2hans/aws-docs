---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_eventbridge_lambda.html
---

# aws-eventbridge-lambda
<a name="aws_eventbridge_lambda"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_eventbridge_lambda`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-eventbridge-lambda`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.eventbridgelambda`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS EventBridge rule and an AWS Lambda function.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps, Duration } from 'aws-cdk-lib';
import { EventbridgeToLambdaProps, EventbridgeToLambda } from '@aws-solutions-constructs/aws-eventbridge-lambda';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as events from 'aws-cdk-lib/aws-events';

const constructProps: EventbridgeToLambdaProps = {
  lambdaFunctionProps: {
    code: lambda.Code.fromAsset(`lambda`),
    runtime: lambda.Runtime.NODEJS_22_X,
    handler: 'index.handler'
  },
  eventRuleProps: {
    schedule: events.Schedule.rate(Duration.minutes(5))
  }
};

new EventbridgeToLambda(this, 'test-eventbridge-lambda', constructProps);
```

```
from aws_solutions_constructs.aws_eventbridge_lambda import EventbridgeToLambda, EventbridgeToLambdaProps
from aws_cdk import (
    aws_lambda as _lambda,
    aws_events as events,
    Duration,
    Stack
)
from constructs import Construct

EventbridgeToLambda(self, 'test-eventbridge-lambda',
                    lambda_function_props=_lambda.FunctionProps(
                        code=_lambda.Code.from_asset('lambda'),
                        runtime=_lambda.Runtime.PYTHON_3_14,
                        handler='index.handler'
                    ),
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
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awsconstructs.services.eventbridgelambda.*;

new EventbridgeToLambda(this, "test-eventbridge-lambda",
        new EventbridgeToLambdaProps.Builder()
                .lambdaFunctionProps(new FunctionProps.Builder()
                        .runtime(Runtime.NODEJS_22_X)
                        .code(Code.fromAsset("lambda"))
                        .handler("index.handler")
                        .build())
                .eventRuleProps(new RuleProps.Builder()
                        .schedule(Schedule.rate(Duration.minutes(5)))
                        .build())
                .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingLambdaObj? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Existing instance of Lambda Function object, providing both this and `lambdaFunctionProps` will cause an error. |
| lambdaFunctionProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html)  | Optional - user provided props to override the default props for the Lambda function. Providing both this and `existingLambdaObj` causes an error. |
| existingEventBusInterface? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html)  | Optional - user provided custom EventBus for this construct to use. Providing both this and `eventBusProps` causes an error. |
| eventBusProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.EventBusProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.EventBusProps.html)  | Optional - user provided properties to override the default properties when creating a custom EventBus. Setting this value to `{}` will create a custom EventBus using all default properties. If neither this nor `existingEventBusInterface` is provided the construct will use the default EventBus. Providing both this and `existingEventBusInterface` causes an error. |
| eventRuleProps |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.RuleProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.RuleProps.html)  | User provided eventRuleProps to override the defaults |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| eventBus? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html)  | Returns the instance of events.IEventBus used by the construct |
| eventsRule |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.Rule.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.Rule.html)  | Returns an instance of events.Rule created by the construct |
| lambdaFunction |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Returns an instance of lambda.Function created by the construct |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon EventBridge Rule
<a name="_amazon_eventbridge_rule"></a>
+ Grant least privilege permissions to EventBridge rule to trigger the Lambda Function

### AWS Lambda Function
<a name="_aws_lambda_function"></a>
+ Configure limited privilege access IAM role for Lambda function
+ Enable reusing connections with Keep-Alive for NodeJs Lambda function
+ Enable X-Ray Tracing
+ Set Environment Variables
+ AWS\_NODEJS\_CONNECTION\_REUSE\_ENABLED (for Node 10.x and higher functions)

## Architecture
<a name="_architecture"></a>

![Diagram showing the EventBridge rule, Lambda function, CloudWatch log group and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-eventbridge-lambda.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-eventbridge-lambda) for this pattern to view the code, read/create issues and pull requests and more.
