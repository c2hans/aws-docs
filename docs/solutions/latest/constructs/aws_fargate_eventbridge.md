---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_fargate_eventbridge.html
---

# aws-fargate-eventbridge
<a name="aws_fargate_eventbridge"></a>

![Stability:Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

All classes are under active development and subject to non-backward compatible changes or removal in any future version. These are not subject to the [Semantic Versioning](https://semver.org/) model. This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_fargate_eventbridge`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-fargate-eventbridge`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.fargateeventbridge`  |

This AWS Solutions Construct implements an AWS Fargate service connected to an Amazon EventBridge.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { FargateToEventbridge, FargateToEventbridgeProps } from '@aws-solutions-constructs/aws-fargate-eventbridge';

const constructProps: FargateToEventbridgeProps = {
  publicApi: true,
  ecrRepositoryArn: "arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo",
};

new FargateToEventbridge(this, 'test-construct', constructProps);
```

```
from aws_solutions_constructs.aws_fargate_eventbridge import FargateToEventbridge, FargateToEventbridgeProps
from aws_cdk import (
    Stack
)
from constructs import Construct

FargateToEventbridge(self, 'test_construct',
            public_api=True,
            ecr_repository_arn="arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo")
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.fargateeventbridge.*;

new FargateToEventbridge(this, "test_construct", new FargateToEventbridgeProps.Builder()
        .publicApi(true)
        .ecrRepositoryArn("arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo")
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| publicApi | boolean | Whether the construct is deploying a private or public API. This has implications for the VPC. |
| vpcProps? |  [ec2.VpcProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html)  | Optional custom properties for a VPC the construct will create. This VPC will be used by any Private Hosted Zone the construct creates (that’s why loadBalancerProps and privateHostedZoneProps can’t include a VPC). Providing both this and existingVpc causes an error. |
| existingVpc? |  [ec2.IVpc](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | An existing VPC in which to deploy the construct. Providing both this and vpcProps causes an error. If the client provides an existing load balancer and/or existing Private Hosted Zone, those constructs must exist in this VPC. |
| clusterProps? |  [ecs.ClusterProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ClusterProps.html)  | Optional properties to create a new ECS cluster. To provide an existing cluster, use the cluster attribute of fargateServiceProps. |
| ecrRepositoryArn? |  `string`  | The arn of an ECR Repository containing the image to use to generate the containers. Either this or the image property of containerDefinitionProps must be provided. format: arn:aws:ecr:\_region\_:\_account number\_:repository/*Repository Name*  |
| ecrImageVersion? |  `string`  | The version of the image to use from the repository. Defaults to "Latest"  |
| containerDefinitionProps? |  [ecs.ContainerDefinitionProps \| any](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinitionProps.html)  | Optional props to define the container created for the Fargate Service (defaults found in fargate-defaults.ts) |
| fargateTaskDefinitionProps? |  [ecs.FargateTaskDefinitionProps \| any](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateTaskDefinitionProps.html)  | Optional props to define the Fargate Task Definition for this construct (defaults found in fargate-defaults.ts) |
| fargateServiceProps? |  [ecs.FargateServiceProps \| any](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateServiceProps.html)  | Optional values to override default Fargate Task definition properties (fargate-defaults.ts). The construct will default to launching the service is the most isolated subnets available (precedence: Isolated, Private and Public). Override those and other defaults here. |
| existingFargateServiceObject? |  [ecs.FargateService](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateService.html)  | A Fargate Service already instantiated (probably by another Solutions Construct). If this is specified, then no props defining a new service can be provided, including: ecrImageVersion, containerDefinitionProps, fargateTaskDefinitionProps, ecrRepositoryArn, fargateServiceProps, clusterProps |
| existingContainerDefinitionObject? |  [ecs.ContainerDefinition](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinition.html)  | A container definition already instantiated as part of a Fargate service. This must be the container in the existingFargateServiceObject |
| existingEventBusInterface? |  [`events.IEventBus`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html)  | Optional - user provided custom EventBus for this construct to use. Providing both this and `eventBusProps` causes an error. |
| eventBusProps? |  [`events.EventBusProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.EventBusProps.html)  | Optional - user provided properties to override the default properties when creating a custom EventBus. Setting this value to `{}` will create a custom EventBus using all default properties. If neither this nor `existingEventBusInterface` is provided the construct will use the default EventBus. Providing both this and `existingEventBusInterface` causes an error. |
| eventBusEnvironmentVariableName? |  `string`  | Optional Name for the container environment variable set to the DynamoDB table name. Default: EVENTBUS\_NAME |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| vpc |  [ec2.IVpc](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | The VPC used by the construct (whether created by the construct or provided by the client) |
| service |  [ecs.FargateService](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateService.html)  | The AWS Fargate service used by this construct (whether created by this construct or passed to this construct at initialization) |
| container |  [ecs.ContainerDefinition](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinition.html)  | The container associated with the AWS Fargate service in the service property. |
| eventBus? |  [`events.IEventBus`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_events.IEventBus.html)  | Returns the instance of `events.IEventBus` used by the construct |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### AWS Fargate Service
<a name="_aws_fargate_service"></a>
+ Sets up an AWS Fargate service
  + Uses the existing service if provided
  + Creates a new service if none provided.
    + Service will run in isolated subnets if available, then private subnets if available and finally public subnets
+ Adds environment variables to the container with the Name of the event bus
  + Default: EVENTBUS\_NAME
+ Add permissions to the container IAM role allowing it to put events in the EventBridge event bus

### Amazon EventBridge Event Bus
<a name="_amazon_eventbridge_event_bus"></a>
+ Sets up an Amazon EventBridge event bus
  + Uses an existing event bus if one is provided, otherwise creates a new one if `eventBusProps` is provided
  + If neither `eventBusProps` nor `existingEventBusInterface` is provided, the construct will use the `default` event bus.
+ Adds an Interface Endpoint to the VPC for EventBridge (the service by default runs in Isolated or Private subnets)

## Architecture
<a name="_architecture"></a>

![Diagram showing the Fargate service, EventBridge bus and IAM role created by the construct](https://docs.aws.amazon.com/solutions/latest/constructs/images/aws-fargate-eventbridge.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-fargate-eventbridge) for this pattern to view the code, read/create issues and pull requests and more.
