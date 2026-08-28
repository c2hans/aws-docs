---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_fargate_dynamodb.html
---

# aws-fargate-dynamodb
<a name="aws_fargate_dynamodb"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_fargate_dynamodb`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-fargate-dynamodb`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.fargatedynamodb`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS Fargate service that can write/read to an Amazon DynamoDB table

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { FargateToDynamoDB, FargateToDynamoDBProps } from '@aws-solutions-constructs/aws-fargate-dynamodb';

const constructProps: FargateToDynamoDBProps = {
  publicApi: true,
  ecrRepositoryArn: "arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo",
};

new FargateToDynamoDB(stack, 'test-construct', constructProps);
```

```
from aws_solutions_constructs.aws_fargate_dynamodb import FargateToDynamoDB, FargateToDynamoDBProps
from aws_cdk import (
    Stack
)
from constructs import Construct

FargateToDynamoDB(self, 'test_construct',
            public_api=True,
            ecr_repository_arn="arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo")
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.fargatedynamodb.*;

new FargateToDynamoDB(this, "test-construct", new FargateToDynamoDBProps.Builder()
        .publicApi(true)
        .ecrRepositoryArn("arn:aws:ecr:us-east-1:123456789012:repository/your-ecr-repo")
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
| dynamoTableProps? |  [`dynamodb.TableProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_dynamodb.TableProps.html)  | Optional user provided props to override the default props for the DynamoDB Table. Providing both this and `existingTableInterface` causes an error. |
| existingTableInterface? |  [`dynamodb.ITable`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_dynamodb.ITable.html)  | Optional - existing DynamoDB table, providing both this and `dynamoTableProps` will cause an error. |
| tablePermissions? |  `string`  | Optional table permissions to grant to the Fargate service. One of the following may be specified: `All`, `Read`, `ReadWrite`, `Write`. |
| tableArnEnvironmentVariableName? |  `string`  | Optional Name for the container environment variable set to the ARN for the DynamoDB table. Default: DYNAMODB\_TABLE\_ARN |
| tableEnvironmentVariableName? |  `string`  | Optional Name for the container environment variable set to the DynamoDB table name. Default: DYNAMODB\_TABLE\_NAME |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| vpc |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | The VPC used by the construct (whether created by the construct or provided by the client) |
| service |  [`ecs.FargateService`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.FargateService.html)  | The AWS Fargate service used by this construct (whether created by this construct or passed to this construct at initialization) |
| container |  [`ecs.ContainerDefinition`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs.ContainerDefinition.html)  | The container associated with the AWS Fargate service in the service property. |
| dynamoTableInterface |  [`dynamodb.ITable`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_dynamodb.ITable.html)  | Returns an instance of `dynamodb.ITable` created by the construct or the interface provided in existingTableInterface. |
| dynamoTable? |  [`dynamodb.Table`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_dynamodb.Table.html)  | Returns an instance of `dynamodb.Table` created by the construct. IMPORTANT: If existingTableInterface was provided in Pattern Construct Props, this property will be `undefined`. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### AWS Fargate Service
<a name="_aws_fargate_service"></a>
+ Sets up an AWS Fargate service
  + Uses the existing service if provided
  + Creates a new service if none provided.
    + Service will run in isolated subnets if available, then private subnets if available and finally public subnets
  + Adds environment variables to the container with the ARN and Name of the DynamoDB table
  + Add permissions to the container IAM role allowing it to publish to the DynamoDB table

### Amazon DynamoDB Table
<a name="_amazon_dynamodb_table"></a>
+ Sets up an Amazon DynamoDB table
  + Uses an existing table if one is provided, otherwise creates a new one
+ Adds an Interface Endpoint to the VPC for DynamoDB (the service by default runs in Isolated or Private subnets)

## Architecture
<a name="_architecture"></a>

![Diagram showing the Fargate service, DynamoDB table, and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-fargate-dynamodb.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-fargate-dynamodb) for this pattern to view the code, read/create issues and pull requests and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
