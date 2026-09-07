---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_fargate_kinesisstreams.html
---

# aws-fargate-kinesisstreams
<a name="aws_fargate_kinesisstreams"></a>

![Stability:Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_fargate_kinesisstreams`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-fargate-kinesisstreams`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.fargatekinesisstreams`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct deploys an AWS Fargate Service that can put records on an Amazon Kinesis Data Stream.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { FargateToKinesisStreamsProps } from '@aws-solutions-constructs/aws-fargate-kinesisstreams';
import * as fargate from 'aws-cdk-lib/aws-fargate';

new FargateToKinesisStreams(this, 'FargateToKinesisStreams', {
  publicApi: true,
  ecrRepositoryArn: "arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo",
});
```

```
from aws_solutions_constructs.aws_fargate_kinesisstreams import FargateToKinesisStreams
from aws_cdk import (
    aws_fargate as _fargate,
    Stack
)
from constructs import Construct

FargateToKinesisStreams(self, 'FargateToKinesisStreams',
                          public_api=True,
                          ecr_repository_arn="arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo"
                       )
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.fargate.*;
import software.amazon.awscdk.services.fargate.eventsources.*;
import software.amazon.awscdk.services.fargate.Runtime;
import software.amazon.awsconstructs.services.fargatekinesisstreams.*;

new FargateToKinesisStreams(this, "FargateToKinesisStreams", new FargateToKinesisStreamsProps.Builder()
        .publicApi(true)
        .ecrRepositoryArn("arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo")
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| publicApi |  `boolean`  | True if the VPC provisioned by this construct should contain Public/Private Subnets, otherwise False for the VPC to contain Isolated Subnets only. Note this property is ignored if an existing VPC is specified in the `existingVpc` property. |
| vpcProps? |  [`ec2.VpcProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html)  | Optional custom properties for a new VPC the construct will create. Providing both this and `existingVpc` causes an error. An Amazon Kinesis Streams Interface Endpoint will be added to this VPC. |
| existingVpc? |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | An existing VPC in which to deploy the Fargate Service. Providing both this and `vpcProps` causes an error. If the client provides an existing Fargate Service in the `existingFargateServiceObject` property, this value must be the VPC where the service is running. An Amazon Kinesis Streams Interface Endpoint will be added to this VPC. |
| clusterProps? |  [`ecs.ClusterProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ClusterProps.html)  | Optional properties to create a new ECS cluster. To provide an existing cluster, use the cluster attribute of fargateServiceProps. |
| ecrRepositoryArn? |  `string`  | The arn of an ECR Repository containing the image to use to generate the containers. Either this or the image property of containerDefinitionProps must be provided. format: arn:aws:ecr:\_region\_:\_account number\_:repository/*Repository Name*  |
| ecrImageVersion? |  `string`  | The version of the image to use from the repository. Defaults to "Latest"  |
| containerDefinitionProps? |  [`ecs.ContainerDefinitionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinitionProps.html) \| any | Optional props to define the container created for the Fargate Service. (defaults found in fargate-defaults.ts) |
| fargateTaskDefinitionProps? |  [`ecs.FargateTaskDefinitionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateTaskDefinitionProps.html) \| any | Optional props to define the Fargate Task Definition for this construct. (defaults found in fargate-defaults.ts) |
| fargateServiceProps? |  [`ecs.FargateServiceProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateServiceProps.html) \| any | Optional values to override default Fargate Task definition properties (fargate-defaults.ts). The construct will default to launching the service is the most isolated subnets available (precedence: Isolated, Private and Public). Override those and other defaults here. |
| existingFargateServiceObject? |  [`ecs.FargateService`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateService.html)  | A Fargate Service already instantiated (probably by another Solutions Construct). If this is specified, then no props defining a new service can be provided, including: ecrImageVersion, containerDefinitionProps, fargateTaskDefinitionProps, ecrRepositoryArn, fargateServiceProps, clusterProps |
| existingContainerDefinitionObject? |  [`ecs.ContainerDefinition`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinition.html)  | A container definition already instantiated as part of a Fargate service. This must be the container in the `existingFargateServiceObject`. |
| existingStreamObj? |  [`kinesis.Stream`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html)  | Existing instance of a Kinesis Data Stream. Providing both this and `kinesisStreamProps` will cause an error. |
| kinesisStreamProps? |  [`kinesis.StreamProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.StreamProps.html)  | Optional user-provided props to override the default props for the Kinesis Data Stream. Providing both this and `existingStreamObj` will cause an error. |
| createCloudWatchAlarms |  `boolean`  | Whether to create recommended CloudWatch Alarms for the Kinesis Stream (defaults to true). |
| streamEnvironmentVariableName? |  `string`  | Optional Name to override the Fargate Service default environment variable name that holds the Kinesis Data Stream name value. Default: KINESIS\_DATASTREAM\_NAME |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| vpc |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | The new or existing VPC used by the construct. |
| service |  [`ecs.FargateService`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateService.html)  | The new or existing AWS Fargate service used by this construct. |
| container |  [`ecs.ContainerDefinition`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinition.html)  | The container associated with the AWS Fargate service in the service property. |
| kinesisStream |  [`kinesis.Stream`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html)  | The new or existing Kinesis Data Stream used by this construct. |
| cloudwatchAlarms? |  [`cloudwatch.Alarm[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html)  | Returns the CloudWatch Alarms created to monitor the Kinesis Data Stream. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any overrides will set the following defaults:

### AWS Fargate Service
<a name="_aws_fargate_service"></a>
+ An AWS Fargate Service running in the isolated subnets of a new VPC
+ Minimally-permissive IAM role for the Fargate Service to put records on the Kinesis Data Stream
+ Sets an Environment Variable named KINESIS\_DATASTREAM\_NAME that holds the Kinesis Data Stream Name, which is a required property of the Kinesis Data Streams SDK when making calls to it

### Amazon Kinesis Stream
<a name="_amazon_kinesis_stream"></a>
+ Enable server-side encryption for the Kinesis Data Stream using an AWS Managed CMK
+ Deploy best practices CloudWatch Alarms for the Kinesis Data Stream
+ An Interface Endpoint on the VPC for private communication between the Fargate Service and the Kinesis Data Stream

## Architecture
<a name="_architecture"></a>

![Diagram showing the Fargate service, Kinesis data stream and CloudWatch alarms created by the construct](https://docs.aws.amazon.com/solutions/latest/constructs/images/aws-fargate-kinesisstreams.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-fargate-kinesisstreams) for this pattern to view the code, read/create issues and pull requests and more.
