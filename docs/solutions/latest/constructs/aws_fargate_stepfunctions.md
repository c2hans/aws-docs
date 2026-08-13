---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_fargate_stepfunctions.html
---

# aws-fargate-stepfunctions
<a name="aws_fargate_stepfunctions"></a>

![Stability:Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

All classes are under active development and subject to non-backward compatible changes or removal in any future version. These are not subject to the [Semantic Versioning](https://semver.org/) model. This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_fargate_stepfunctions`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-fargate-stepfunctions`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.fargatestepfunctions`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS Fargate service that can execute an AWS Step Functions state machine

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { FargateToStepfunctions, FargateToStepfunctionsProps } from '@aws-solutions-constructs/aws-fargate-stepfunctions';
import * as stepfunctions from 'aws-cdk-lib/aws-stepfunctions';

const startState = new stepfunctions.Pass(this, 'StartState');

const constructProps: FargateToStepfunctionsProps = {
  publicApi: true,
  ecrRepositoryArn: "arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo",
  stateMachineProps: {
      definition: startState
    }
};

new FargateToStepfunctions(this, 'test-construct', constructProps);
```

```
from aws_solutions_constructs.aws_fargate_stepfunctions import FargateToStepfunctions, FargateToStepfunctionsProps
from aws_cdk import (
    aws_stepfunctions as stepfunctions,
    Stack
)
from constructs import Construct

start_state = stepfunctions.Pass(self, 'start_state')

FargateToStepfunctions(self, 'test_construct',
            public_api=True,
            ecr_repository_arn="arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo",
            state_machine_props=stepfunctions.StateMachineProps(
              definition=start_state))
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.fargatestepfunctions.*;
import software.amazon.awscdk.services.stepfunctions.*;

start_state = stepfunctions.Pass(self, 'start_state')

new FargateToStepfunctions(this, "test-construct", new FargateToStepfunctionsProps.Builder()
        .publicApi(true)
        .ecrRepositoryArn("arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo")
        .stateMachineProps(new StateMachineProps.Builder()
                        .definition(startState)
                        .build()
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| publicApi |  `boolean`  | Whether the construct is deploying a private or public API. This has implications for the VPC. |
| vpcProps? |  [`ec2.VpcProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html)  | Optional custom properties for a VPC the construct will create. This VPC will be used by any Private Hosted Zone the construct creates (that’s why loadBalancerProps and privateHostedZoneProps can’t include a VPC). Providing both this and existingVpc causes an error. |
| existingVpc? |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | An existing VPC in which to deploy the construct. Providing both this and vpcProps causes an error. If the client provides an existing load balancer and/or existing Private Hosted Zone, those constructs must exist in this VPC. |
| clusterProps? |  [`ecs.ClusterProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ClusterProps.html)  | Optional properties to create a new ECS cluster. To provide an existing cluster, use the cluster attribute of fargateServiceProps. |
| ecrRepositoryArn? |  `string`  | The arn of an ECR Repository containing the image to use to generate the containers. Either this or the image property of containerDefinitionProps must be provided. format: arn:aws:ecr:\_region\_:\_account number\_:repository/*Repository Name*  |
| ecrImageVersion? |  `string`  | The version of the image to use from the repository. Defaults to "Latest"  |
| containerDefinitionProps? |  [`ecs.ContainerDefinitionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinitionProps.html) \| any | Optional props to define the container created for the Fargate Service (defaults found in fargate-defaults.ts) |
| fargateTaskDefinitionProps? |  [`ecs.FargateTaskDefinitionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateTaskDefinitionProps.html) \| any | Optional props to define the Fargate Task Definition for this construct (defaults found in fargate-defaults.ts) |
| fargateServiceProps? |  [`ecs.FargateServiceProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateServiceProps.html) \| any | Optional values to override default Fargate Task definition properties (fargate-defaults.ts). The construct will default to launching the service is the most isolated subnets available (precedence: Isolated, Private and Public). Override those and other defaults here. |
| existingFargateServiceObject? |  [`ecs.FargateService`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateService.html)  | A Fargate Service already instantiated (probably by another Solutions Construct). If this is specified, then no props defining a new service can be provided, including: ecrImageVersion, containerDefinitionProps, fargateTaskDefinitionProps, ecrRepositoryArn, fargateServiceProps, clusterProps |
| existingContainerDefinitionObject? |  [`ecs.ContainerDefinition`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinition.html)  | A container definition already instantiated as part of a Fargate service. This must be the container in the existingFargateServiceObject |
| stateMachineProps |  [`sfn.StateMachineProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions.StateMachineProps.html)  | User provided props for the sfn.StateMachine. This or existingStateMachine is required. If you provide a value for logs.destination, it must be an ILogGroup even though the prop type is ILogGroupRef. The CDK change to ILogGroupRef in v2.235.0 is incompatible with our interface without introducing breaking changes, so we still require an ILogGroup (as this implements ILogGroupRef, you can just assign it to logs.destination) |
| createCloudWatchAlarms? |  `boolean`  | Whether to create recommended CloudWatch alarms. Default is true. |
| logGroupProps? |  [`logs.LogGroupProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html)  | Optional user provided props to override the default props for for the CloudWatchLogs LogGroup. |
| stateMachineEnvironmentVariableName? |  `string`  | Optional Name for the container environment variable set to the ARN of the state machine. Default: STATE\_MACHINE\_ARN |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| vpc |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | The VPC used by the construct (whether created by the construct or provided by the client) |
| service |  [`ecs.FargateService`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateService.html)  | The AWS Fargate service used by this construct (whether created by this construct or passed to this construct at initialization) |
| container |  [`ecs.ContainerDefinition`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinition.html)  | The container associated with the AWS Fargate service in the service property. |
| stateMachine |  [`sfn.StateMachine`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions.StateMachine.html)  | Returns an instance of `sfn.StateMachine` created by the construct. |
| stateMachineLogGroup |  [`logs.ILogGroup`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.ILogGroup.html)  | Returns an instance of the `logs.ILogGroup` created by the construct for StateMachine. |
| cloudwatchAlarms? |  [`cloudwatch.Alarm[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html)  | Returns a list of `cloudwatch.Alarm` created by the construct. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### AWS Fargate Service
<a name="_aws_fargate_service"></a>
+ Sets up an AWS Fargate service
  + Uses the existing service if provided
  + Creates a new service if none provided.
    + Service will run in isolated subnets if available, then private subnets if available and finally public subnets
+ Adds an environment variable to the container containing the ARN of the state machine
  + Default name is `STATE_MACHINE_ARN`
+ Add permissions to the container IAM role allowing it to start the execution of a state machine

### AWS Step Functions
<a name="_aws_step_functions"></a>
+ Sets up an AWS Step Functions state machine
  + Uses an existing state machine if one is provided, otherwise creates a new one
+ Adds an Interface Endpoint to the VPC for Step Functions (the service by default runs in Isolated or Private subnets)
+ Enables CloudWatch logging

## Architecture
<a name="_architecture"></a>

![Diagram showing the Fargate service, State Machine, log group and IAM roles created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-fargate-stepfunctions.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-fargate-stepfunctions) for this pattern to view the code, read/create issues and pull requests and more.
