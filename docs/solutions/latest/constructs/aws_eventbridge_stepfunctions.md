---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_eventbridge_stepfunctions.html
---

# aws-eventbridge-stepfunctions
<a name="aws_eventbridge_stepfunctions"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_eventbridge_stepfunctions`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-eventbridge-stepfunctions`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.eventbridgestepfunctions`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS Events rule and an AWS Step Functions State Machine

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps, Duration } from 'aws-cdk-lib';
import { EventbridgeToStepfunctions, EventbridgeToStepfunctionsProps } from '@aws-solutions-constructs/aws-eventbridge-stepfunctions';
import * as stepfunctions from 'aws-cdk-lib/aws-stepfunctions';
import * as events from 'aws-cdk-lib/aws-events';

const startState = new stepfunctions.Pass(this, 'StartState');

const constructProps: EventbridgeToStepfunctionsProps = {
  stateMachineProps: {
    definition: startState
  },
  eventRuleProps: {
    schedule: events.Schedule.rate(Duration.minutes(5))
  }
};

new EventbridgeToStepfunctions(this, 'test-eventbridge-stepfunctions-stack', constructProps);
```

```
from aws_solutions_constructs.aws_eventbridge_stepfunctions import EventbridgeToStepfunctions, EventbridgeToStepfunctionsProps
from aws_cdk import (
    aws_stepfunctions as stepfunctions,
    aws_events as events,
    Duration,
    Stack
)
from constructs import Construct

startState = stepfunctions.Pass(self, 'StartState')

EventbridgeToStepfunctions(self, 'test-eventbridge-stepfunctions-stack',
                            state_machine_props=stepfunctions.StateMachineProps(
                                definition=startState
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
import software.amazon.awscdk.services.stepfunctions.*;
import software.amazon.awsconstructs.services.eventbridgestepfunctions.*;

final Pass startState = new Pass(this, "StartState");

new EventbridgeToStepfunctions(this,
        "test-eventbridge-stepfunctions-stack",
        new EventbridgeToStepfunctionsProps.Builder()
                .stateMachineProps(new StateMachineProps.Builder()
                        .definition(startState)
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
| stateMachineProps |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions.StateMachineProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions.StateMachineProps.html)  | User provided props for the sfn.StateMachine. This or existingStateMachine is required. If you provide a value for logs.destination, it must be an ILogGroup even though the prop type is ILogGroupRef. The CDK change to ILogGroupRef in v2.235.0 is incompatible with our interface without introducing breaking changes, so we still require an ILogGroup (as this implements ILogGroupRef, you can just assign it to logs.destination) |
| existingEventBusInterface? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html)  | Optional - user provided custom EventBus for this construct to use. Providing both this and `eventBusProps` causes an error. |
| eventBusProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.EventBusProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.EventBusProps.html)  | Optional - user provided properties to override the default properties when creating a custom EventBus. Setting this value to `{}` will create a custom EventBus using all default properties. If neither this nor `existingEventBusInterface` is provided the construct will use the default EventBus. Providing both this and `existingEventBusInterface` causes an error. |
| eventRuleProps |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.RuleProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.RuleProps.html)  | User provided eventRuleProps to override the defaults |
| createCloudWatchAlarms |  `boolean`  | Whether to create recommended CloudWatch alarms |
| logGroupProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html)  | User provided props to override the default props for for the CloudWatchLogs LogGroup. |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| eventBus? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html)  | Returns the instance of events.IEventBus used by the construct |
| eventsRule |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.Rule.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.Rule.html)  | Returns an instance of events.Rule created by the construct |
| stateMachine |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions.StateMachine.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions.StateMachine.html)  | Returns an instance of sfn.StateMachine created by the construct |
| stateMachineLogGroup |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.ILogGroup.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.ILogGroup.html)  | Returns an instance of the ILogGroup created by the construct for StateMachine |
| cloudwatchAlarms? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html)  | Returns a list of cloudwatch.Alarm created by the construct |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon CloudWatch Events Rule
<a name="_amazon_cloudwatch_events_rule"></a>
+ Grant least privilege permissions to CloudWatch Events to trigger the Lambda Function

### AWS Step Function
<a name="_aws_step_function"></a>
+ Enable CloudWatch logging for API Gateway
+ Deploy best practices CloudWatch Alarms for the Step Function

## Architecture
<a name="_architecture"></a>

![Diagram showing the CloudWatch event rule, State Machine, log group and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-eventbridge-stepfunctions.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-eventbridge-stepfunctions) for this pattern to view the code, read/create issues and pull requests and more.
