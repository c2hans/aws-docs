---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_fargate_sqs.html
---

# aws-fargate-sqs
<a name="aws_fargate_sqs"></a>

![Stability:Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

All classes are under active development and subject to non-backward compatible changes or removal in any future version. These are not subject to the [Semantic Versioning](https://semver.org/) model. This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_fargate_sqs`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-fargate-sqs`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.fargatesqs`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS Fargate service that can write to an Amazon SQS queue

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { FargateToSqs, FargateToSqsProps } from '@aws-solutions-constructs/aws-fargate-sqs';

const constructProps: FargateToSqsProps = {
    publicApi: true,
    ecrRepositoryArn: "arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo"
};

new FargateToSqs(this, 'test-construct', constructProps);
```

```
from aws_solutions_constructs.aws_fargate_sqs import FargateToSqs, FargateToSqsProps
from aws_cdk import (
    Stack
)
from constructs import Construct

FargateToSqs(self, 'test_construct',
            public_api=True,
            ecr_repository_arn="arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo")
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.fargatesqs.*;

new FargateToSqs(this, "test_construct", new FargateToSqsProps.Builder()
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
| ecrRepositoryArn? | string | The arn of an ECR Repository containing the image to use to generate the containers. Either this or the image property of containerDefinitionProps must be provided. format: arn:aws:ecr:\_region\_:\_account number\_:repository/*Repository Name*  |
| ecrImageVersion? | string | The version of the image to use from the repository. Defaults to "Latest"  |
| containerDefinitionProps? |  [ecs.ContainerDefinitionProps \| any](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinitionProps.html)  | Optional props to define the container created for the Fargate Service (defaults found in fargate-defaults.ts) |
| fargateTaskDefinitionProps? |  [ecs.FargateTaskDefinitionProps \| any](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateTaskDefinitionProps.html)  | Optional props to define the Fargate Task Definition for this construct (defaults found in fargate-defaults.ts) |
| fargateServiceProps? |  [ecs.FargateServiceProps \| any](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateServiceProps.html)  | Optional values to override default Fargate Task definition properties (fargate-defaults.ts). The construct will default to launching the service is the most isolated subnets available (precedence: Isolated, Private and Public). Override those and other defaults here. |
| existingFargateServiceObject? |  [ecs.FargateService](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateService.html)  | A Fargate Service already instantiated (probably by another Solutions Construct). If this is specified, then no props defining a new service can be provided, including: ecrImageVersion, containerDefinitionProps, fargateTaskDefinitionProps, ecrRepositoryArn, fargateServiceProps, clusterProps |
| existingContainerDefinitionObject? |  [ecs.ContainerDefinition](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinition.html)  | A container definition already instantiated as part of a Fargate service. This must be the container in the existingFargateServiceObject |
| existingQueueObj? |  [sqs.Queue](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.Queue.html)  | An optional, existing SQS queue to be used instead of the default queue. Providing both this and queueProps will cause an error. |
| queueProps? |  [sqs.QueueProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.QueueProps.html)  | Optional - user provided properties to override the default properties for the SQS queue. Providing both this and `existingQueueObj` will cause an error. |
| deployDeadLetterQueue? | boolean | Whether to create a secondary queue to be used as a dead letter queue. Defaults to `true`. |
| deadLetterQueueProps? |  [sqs.QueueProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.QueueProps.html)  | Optional user-provided props to override the default props for the dead letter queue. Only used if the `deployDeadLetterQueue` property is set to true. |
| maxReceiveCount? | integer | The number of times a message can be unsuccessfully dequeued before being moved to the dead letter queue. Defaults to `15`. |
| queueUrlEnvironmentVariableName? | string | Optional Name for the container environment variable set to the URL of the queue. Default: SQS\_QUEUE\_URL |
| queueArnEnvironmentVariableName? | string | Optional Name for the container environment variable set to the arn of the queue. Default: SQS\_QUEUE\_ARN |
| queuePermissions? |  `string[]`  | Optional queue permissions to grant to the Fargate service. One or more of the following may be specified: `Read`,`Write`. Default is `Write`  |
| enableEncryptionWithCustomerManagedKey? |  `boolean`  | If no key is provided, this flag determines whether the queue is encrypted with a new CMK or an AWS managed key. This flag is ignored if any of the following are defined: queueProps.encryptionMasterKey, encryptionKey or encryptionKeyProps. |
| encryptionKey? |  [`kms.Key`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)  | An optional, imported encryption key to encrypt the SQS Queue with. |
| encryptionKeyProps? |  [`kms.KeyProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html#construct-props)  | Optional user provided properties to override the default properties for the KMS encryption key used to encrypt the SQS queue with. |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| vpc |  [ec2.IVpc](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | The VPC used by the construct (whether created by the construct or provided by the client) |
| service |  [ecs.FargateService](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateService.html)  | The AWS Fargate service used by this construct (whether created by this construct or passed to this construct at initialization) |
| container |  [ecs.ContainerDefinition](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinition.html)  | The container associated with the AWS Fargate service in the service property. |
| sqsQueue |  [sqs.Queue](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.Queue.html)  | Returns an instance of the SQS queue created by the pattern. |
| deadLetterQueue? |  [sqs.Queue](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.Queue.html)  | Returns an instance of the dead letter queue created by the pattern, if one is deployed. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### AWS Fargate Service
<a name="_aws_fargate_service"></a>
+ Sets up an AWS Fargate service
  + Uses the existing service if provided
  + Creates a new service if none provided.
    + Service will run in isolated subnets if available, then private subnets if available and finally public subnets
  + Adds environment variables to the container with the name of the SQS queue
  + Add permissions to the container IAM role allowing it to publish to the SQS queue

### Amazon SQS Queue
<a name="_amazon_sqs_queue"></a>
+ Sets up an Amazon SQS queue
  + Uses an existing queue if one is provided, otherwise creates a new one
+ Adds an Interface Endpoint to the VPC for SQS (the service by default runs in Isolated or Private subnets)

## Architecture
<a name="_architecture"></a>

![Diagram showing the Fargate service, SQS queue and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-fargate-sqs.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-fargate-sqs) for this pattern to view the code, read/create issues and pull requests and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
