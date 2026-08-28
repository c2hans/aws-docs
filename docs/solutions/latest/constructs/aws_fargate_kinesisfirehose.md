---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_fargate_kinesisfirehose.html
---

# aws-fargate-kinesisfirehose
<a name="aws_fargate_kinesisfirehose"></a>

![Stability:Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_fargate_kinesisfirehose`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-fargate-kinesisfirehose`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.fargatekinesisfirehose`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct deploys an AWS Fargate Service that can put records on an Amazon Firehose Delivery Stream.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { FargateToKinesisFirehoseProps } from '@aws-solutions-constructs/aws-fargate-kinesisfirehose';
import * as fargate from 'aws-cdk-lib/aws-fargate';

// The construct requires an existing Firehose Delivery Stream, this can be created in raw CDK or extracted
// from a previously instantiated construct that created an Firehose Delivery Stream
const existingFirehoseDeliveryStream = previouslyCreatedKinesisFirehoseToS3Construct.kinesisFirehose;

new FargateToKinesisFirehose(this, 'FargateToKinesisFirehose', {
  publicApi: true,
  ecrRepositoryArn: "arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo",
  existingKinesisFirehose: existingFirehoseDeliveryStream
});
```

```
from aws_solutions_constructs.aws_fargate_kinesisfirehose import FargateToKinesisFirehose
from aws_cdk import (
    aws_fargate as _fargate,
    Stack
)
from constructs import Construct

# The construct requires an existing Firehose Delivery Stream, this can be created in raw CDK or extracted
# from a previously instantiated construct that created an Firehose Delivery Stream
existingFirehoseDeliveryStream = previouslyCreatedKinesisFirehoseToS3Construct.kinesisFirehose;

FargateToKinesisFirehose(self, 'FargateToKinesisFirehose',
                          public_api=True,
                          ecr_repository_arn="arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo",
                          existingKinesisFirehose=existingFirehoseDeliveryStream
                       )
```

```
import software.constructs.Construct;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.fargate.*;
import software.amazon.awscdk.services.fargate.eventsources.*;
import software.amazon.awscdk.services.fargate.Runtime;
import software.amazon.awsconstructs.services.fargatekinesisfirehose.*;

// The construct requires an existing Firehose Delivery Stream, this can be created in raw CDK or extracted
// from a previously instantiated construct that created an Firehose Delivery Stream
existingFirehoseDeliveryStream = previouslyCreatedKinesisFirehoseToS3Construct.kinesisFirehose;

new FargateToKinesisFirehose(this, "FargateToKinesisFirehose", new FargateToKinesisFirehoseProps.Builder()
        .publicApi(true)
        .ecrRepositoryArn("arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo")
        .existingKinesisFirehose(existingFirehoseDeliveryStream)
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| publicApi |  `boolean`  | True if the VPC provisioned by this construct should contain Public/Private Subnets, otherwise False for the VPC to contain Isolated Subnets only. Note this property is ignored if an existing VPC is specified in the existingVpc property. If you are getting a container from a public repo, this must be true so the repo can be accessed from the network. |
| vpcProps? |  [`ec2.VpcProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html)  | Optional custom properties for a new VPC the construct will create. Providing both this and `existingVpc` causes an error. An Amazon Kinesis Firehose Interface Endpoint will be added to this VPC. |
| existingVpc? |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | An existing VPC in which to deploy the Fargate Service. Providing both this and `vpcProps` causes an error. If the client provides an existing Fargate Service in the `existingFargateServiceObject` property, this value must be the VPC where the service is running. An Amazon Kinesis Firehose Interface Endpoint will be added to this VPC. |
| clusterProps? |  [`ecs.ClusterProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ClusterProps.html)  | Optional properties to create a new ECS cluster. To provide an existing cluster, use the cluster attribute of fargateServiceProps. |
| ecrRepositoryArn? |  `string`  | The arn of an ECR Repository containing the image to use to generate the containers. Either this or the image property of containerDefinitionProps must be provided. format: arn:aws:ecr:\_region\_:\_account number\_:repository/*Repository Name*  |
| ecrImageVersion? |  `string`  | The version of the image to use from the repository. Defaults to "Latest"  |
| containerDefinitionProps? |  [`ecs.ContainerDefinitionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinitionProps.html) \| any | Optional props to define the container created for the Fargate Service. (defaults found in fargate-defaults.ts) |
| fargateTaskDefinitionProps? |  [`ecs.FargateTaskDefinitionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateTaskDefinitionProps.html) \| any | Optional props to define the Fargate Task Definition for this construct. (defaults found in fargate-defaults.ts) |
| fargateServiceProps? |  [`ecs.FargateServiceProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateServiceProps.html) \| any | Optional values to override default Fargate Task definition properties (fargate-defaults.ts). The construct will default to launching the service is the most isolated subnets available (precedence: Isolated, Private and Public). Override those and other defaults here. |
| existingFargateServiceObject? |  [`ecs.FargateService`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateService.html)  | A Fargate Service already instantiated (probably by another Solutions Construct). If this is specified, then no props defining a new service can be provided, including: ecrImageVersion, containerDefinitionProps, fargateTaskDefinitionProps, ecrRepositoryArn, fargateServiceProps, clusterProps |
| existingContainerDefinitionObject? |  [`ecs.ContainerDefinition`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinition.html)  | A container definition already instantiated as part of a Fargate service. This must be the container in the `existingFargateServiceObject`. |
| existingKinesisFirehose |  [kinesisfirehose.CfnDeliveryStream](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.html)  | An existing Kinesis Firehose Delivery Stream to which the Fargate container can put data. Note - the delivery stream construct must have already been created and have the deliveryStreamName set. This construct will *not* create a new Delivery Stream. |
| firehoseEnvironmentVariableName? |  `string`  | Optional Name for the Fargate container environment variable set to the name of the delivery stream. Default: FIREHOSE\_DELIVERYSTREAM\_NAME |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| vpc |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | The new or existing VPC used by the construct. |
| fargateService |  [`ecs.FargateService`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateService.html)  | The new or existing AWS Fargate service used by this construct. |
| container |  [`ecs.ContainerDefinition`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinition.html)  | The container associated with the AWS Fargate service in the service property. |
| kinesisFirehose |  [kinesisfirehose.CfnDeliveryStream](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.html)  | The Kinesis Firehose Delivery Stream used by the construct. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any overrides will set the following defaults:

### AWS Fargate Service
<a name="_aws_fargate_service"></a>
+ An AWS Fargate Service running in the isolated subnets of a new VPC
+ Minimally-permissive IAM role for the Fargate Service to put records on the Firehose Delivery Stream
+ Sets an Environment Variable named FIREHOSE\_DELIVERYSTREAM\_NAME that holds the Firehose Delivery Stream Name, which is a required property of the Kinesis Firehose SDK when making calls to it

### Amazon Firehose Delivery Stream
<a name="_amazon_firehose_delivery_stream"></a>
+ This construct must be provided a configured Firehose Data Stream construct, it does not change this Stream.

## Architecture
<a name="_architecture"></a>

![Diagram showing the Fargate service, Kinesis firehose and IAM role created by the construct. A VPC is shown that can be created by the construct or provided by the client.](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-fargate-kinesisfirehose.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-fargate-kinesisfirehose) for this pattern to view the code, read/create issues and pull requests and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
