---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_constructs_factories.html
---

# aws-constructs-factories
<a name="aws_constructs_factories"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_constructs_factories`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-constructs-factories`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.constructsfactories`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct exposes the same code used to create our underlying resources as factories, so clients can create individual resources that are well-architected. There are factories to create:

 [Launch an S3 Bucket](#s3-buckets-docs) - Create a well architected S3 bucket (e.g. - includes an access logging bucket)

 [Launch an Step Functions State Machine](#step-functions-state-machines-docs) - - Create a well architected Step Functions state machine and log group (e.g. log group has /aws/vendedlogs/ name prefix to avoid resource policy issues)

 [Launch an SQS Queue](#sqs-queues-docs) - Create a well architected SQS queue (with configured Dead Letter Queue)

 [Launch a VPC](#vpc-docs) - Create a well architected VPC

## S3 Buckets
<a name="s3-buckets-docs"></a>

Create fully well-architected S3 buckets with as little as one function call. Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { ConstructsFactories } from '@aws-solutions-constructs/aws-constructs-factories';

const factories = new ConstructsFactories(this, 'MyFactories');

factories.s3BucketFactory('GoodBucket', {});
```

```
from aws_cdk import (
    Stack,
)
from constructs import Construct

from aws_solutions_constructs import (
    aws_constructs_factories as cf
)

factories = cf.ConstructsFactories(self, 'MyFactories')
factories.s3_bucket_factory('GoodBucket')
```

```
import software.constructs.Construct;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;

import software.amazon.awsconstructs.services.constructsfactories.ConstructsFactories;
import software.amazon.awsconstructs.services.constructsfactories.S3BucketFactoryProps;

final ConstructsFactories factories = new ConstructsFactories(this, "MyFactories");
factories.s3BucketFactory("GoodBucket",
  new S3BucketFactoryProps.Builder().build());
```

## S3BucketFactory Function Signature
<a name="_s3bucketfactory_function_signature"></a>

```
s3BucketFactory(id: string, props: S3BucketFactoryProps): S3BucketFactoryResponse
```

## S3BucketFactoryProps
<a name="_s3bucketfactoryprops"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| bucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Bucket. |
| logS3AccessLogs? |  `boolean`  | Whether to turn on Access Logging for the S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. default - true |
| loggingBucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Logging Bucket. |

## S3BucketFactoryResponse
<a name="_s3bucketfactoryresponse"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| s3Bucket |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | The s3.Bucket created by the factory. |
| s3LoggingBucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | The s3.Bucket created by the construct as the logging bucket for the primary bucket. If the logS3AccessLogs property is false, this value will be undefined. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:
+ An S3 Content Bucket
  + AWS managed Server Side Encryption (AES256)
  + Lifecycle rule to transition objects to Glacier storage class in 90 days
  + Access Logging enabled
  + All Public access blocked
  + Versioning enabled
  + UpdateReplacePolicy is delete
  + Deletion policy is delete
  + Bucket policy requiring SecureTransport
+ An S3 Bucket for Access Logs
  + AWS managed Server Side Encryption (AES256)
  + All public access blocked
  + Versioning enabled
  + UpdateReplacePolicy is delete
  + Deletion policy is delete
  + Bucket policy requiring SecureTransport
  + Bucket policy granting PutObject privileges to the S3 logging service, from the content bucket in the content bucket account.
  + cfn\_nag suppression of access logging finding (not logging access to the access log bucket)

## Architecture
<a name="_architecture"></a>

![Diagram showing the S3 bucket and Access Log bucket created by the factory.](https://docs.aws.amazon.com/solutions/latest/constructs/images/aws-constructs-factories-s3.png)

## Step Functions State Machines
<a name="step-functions-state-machines-docs"></a>

Create fully well-architected Step Functions state machine with log group. The log group name includes the vendedlogs prefix. Here but is unique to the stack, avoiding naming collions between instances. is a minimal deployable pattern definition:

**Example**

```
import { App, Stack } from "aws-cdk-lib";
import { ConstructsFactories } from "../../lib";
import { generateIntegStackName, CreateTestStateMachineDefinitionBody } from '@aws-solutions-constructs/core';
import { IntegTest } from '@aws-cdk/integ-tests-alpha';

const placeholderTask = new sftasks.EvaluateExpression(this, 'placeholder', {
  expression: '$.argOne + $.argTwo'
});

const factories = new ConstructsFactories(this, 'minimalImplementation');

factories.stateMachineFactory('testsm', {
  stateMachineProps: {
    definitionBody: sfn.DefinitionBody.fromChainable(placeholderTask)
  }
});
```

```
# Pending
```

```
// Pending
```

## stateMachineFactory Function Signature
<a name="_statemachinefactory_function_signature"></a>

```
stateMachineFactory(id: string, props: StateMachineFactoryProps): StateMachineFactoryResponse
```

## StateMachineFactoryProps
<a name="_statemachinefactoryprops"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| stateMachineProps |  [sfn.StateMachineProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions.StateMachineProps.html)  | The CDK properties that define the state machine. This property is required and must include a definitionBody or definition (definition is deprecated) |
| logGroupProps |  [`ogs.LogGroupProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html)  | An existing LogGroup to which the new state machine will write log entries. Default: LogGroup will use default AWS settings |
| logGroup? |  [logs.LogGroup](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html)  | An existing LogGroup to which the new state machine will write log entries. Default: none, the construct will create a new log group. |
| createCloudWatchAlarms? | boolean | Whether to create recommended CloudWatch alarms for the State Machine. Default: the alarms are created |
| cloudWatchAlarmsPrefix? | string | Creating multiple State Machines with one Factories construct will result in name collisions as the cloudwatch alarms originally had fixed resource ids. This value was added to avoid collisions while not making changes that would be destructive for existing stacks. Unless you are creating multiple State Machines using factories you can ignore it |

## StateMachineFactoryResponse
<a name="_statemachinefactoryresponse"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| stateMachine |  [`sfn.StateMachine](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions.StateMachine.html)  | The state machine created by the factory (the state machine role is available as a property on this resource |
| logGroup? |  [`logs.LogGroup`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html)  | The log group that will receive log messages from the state machine. |
| cloudwatchAlarms? |  [`cloudwatch.Alarm[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html)  | The alarms created by the factory (ExecutionFailed, ExecutionThrottled, ExecutionAborted) |

## Default settings
<a name="_default_settings_2"></a>

Out of the box implementation of the Construct without any override will set the following defaults:
+ An AWS Step Functions State Machine
  + Configured to log to the new log group at LogLevel.ERROR
+ Amazon CloudWatch Logs Log Group
  + Log name is prefaced with /aws/vendedlogs/ to avoid resource policy [issues](https://docs.aws.amazon.com/step-functions/latest/dg/cw-logs.html#cloudwatch-iam-policy). The Log Group name is still created to be unique to the stack to avoid name collisions.
+ CloudWatch alarms for:
  + 1 or more failed executions
  + 1 or more executions being throttled
  + 1 or more executions being aborted

## Architecture
<a name="_architecture_2"></a>

![Diagram showing the State Machine, CloudWatch Logs and Alarms, and IAM Role launched by the factory.](https://docs.aws.amazon.com/solutions/latest/constructs/images/aws-constructs-factories-sf.png)

## SQS Queues
<a name="sqs-queues-docs"></a>

Create SQS queues complete with DLQs and KMS CMKs with one function call. Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { ConstructsFactories } from '@aws-solutions-constructs/aws-constructs-factories';

const factories = new ConstructsFactories(this, 'MyFactories');

factories.sqsQueueFacgory('GoodQueue', {});
```

```
Pending
```

```
Pendiong
```

## SqsQueueFactory Function Signature
<a name="_sqsqueuefactory_function_signature"></a>

```
SqsQueueFactory(id: string, props: SqsQueueFactoryProps): SqsQueueFactoryResponse
```

## SqsQueueFactoryProps
<a name="_sqsqueuefactoryprops"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| queueProps? |  [sqs.QueueProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.QueueProps.html)  | Optional user provided props to override the default props for the primary queue. |
| enableEncryptionWithCustomerManagedKey? | boolean | If no key is provided, this flag determines whether the queue is encrypted with a new CMK or an AWS managed key. This flag is ignored if any of the following are defined: queueProps.encryptionMasterKey, encryptionKey or encryptionKeyProps. default - False if queueProps.encryptionMasterKey, encryptionKey, and encryptionKeyProps are all undefined. |
| encryptionKey? |  [kms.Key](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)  | An optional, imported encryption key to encrypt the SQS Queue with. Default - none |
| encryptionKeyProps? |  [kms.KeyProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.KeyProps.html)  | Optional user provided properties to override the default properties for the KMS encryption key used to encrypt the SQS Queue with. @default - None |
| deployDeadLetterQueue? | boolean | Whether to deploy a secondary queue to be used as a dead letter queue. |
| deadLetterQueueProps? |  [sqs.QueueProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.QueueProps.html)  | Optional user provided properties for the dead letter queue |
| maxReceiveCount? | number | The number of times a message can be unsuccessfully dequeued before being moved to the dead letter queue. default - [code](https://github.com/awslabs/aws-solutions-constructs/blob/8b30791902e09db2f7c49410a03d5d95ccc2ef51/source/patterns/%40aws-solutions-constructs/core/lib/sqs-defaults.ts#L32)  |

## SqsQueueFactoryResponse
<a name="_sqsqueuefactoryresponse"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| queue |  [sqs.Queue](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.Queue.html)  | The queue created by the factory. |
| key |  [kms.IKey](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.IKey.html)  | The key used to encrypt the queue, if the queue was configured to use a CMK |
| deadLetterQueue? |  [sqs.DeadLetterQueue](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sqs.DeadLetterQueue.html)  | The dead letter queue associated with the queue created by the factory |

## Default settings
<a name="_default_settings_3"></a>

Out of the box implementation of the Construct without any override will set the following defaults:
+ An SQS queue
  + Encrypted by default with KMS managed key by default, can be KMS CMK if flag is set
  + Only queue owner can perform operations by default (your IAM policies can override)
  + Enforced encryption for data in transit
  + DLQ configured
+ An SQS dead letter queue
  + Receives messages not processable in maxReceiveCount attempts
  + Encrypted with KMS managed key
  + Enforced encryption for data in transit

## Architecture
<a name="_architecture_3"></a>

![Diagram showing the KMS keys, SQS Queue and Dead Letter Queue launched by the factory.](https://docs.aws.amazon.com/solutions/latest/constructs/images/aws-constructs-factories-sqs.png)

## Virtual Private Cloud (VPC)
<a name="vpc-docs"></a>

Creates a VPC with a flow log enabled and any requested VPC Endpoints configured.

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { ConstructsFactories } from '@aws-solutions-constructs/aws-constructs-factories';

const factories = new ConstructsFactories(this, 'MyFactories');

// This will create a VPC with subnets that cannot interact with the Internet,
// e.g. - there is no Internet Gateway, nor NAT Gateway(s)
factories.vpcFactory('new-vpc', {
  subnetTypes: [
    ec2.SubnetType.PRIVATE_ISOLATED
]});
```

```
Pending
```

```
Pendiong
```

## VpcFactory Function Signature
<a name="_vpcfactory_function_signature"></a>

```
VpcFactory(id: string, props: VpcFactoryProps): VpcFactoryResponse
```

## VpcFactoryProps
<a name="_vpcfactoryprops"></a>

This construct can either create subnets wholly based on the subnetTypes and subnetIPAddresses specified in attributes of the VpcFactoryProps object ddefined below; or wholly based on values passed in the VpcProps.subnetConfiguration property passed in the vpcProps property of VpcFactoryProps. It cannot combine and blend those two sources - so clients must provide subnet configuration information in one, and only one, of vpcProps.subnetConfiguration or the direct VpcFactoryProps attributes (vpcProps.subnetTypes, vpcProps.subnetIPAddresses). Other vpcProps attributes can be combined with a subnetConfiguration generated from the direct VpcFactoryProps attributes.

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| vpcProps? |  [ec2.VpcProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Vpc.html) \| any | Optional user provided props to override the default props for the vpc. If this property defines subnetConfiguration, then subnetTypes and subnetIPAddrresses must be undefined. |
| subnetTypes? |  [ec2.SubnetType[]](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.SubnetType.html)  | Optional - Determines the various groups of subnets that will be created in the VPC. Multiple types of subnets can be specified. If this value is populated, then vpcProps.subnetConfiguration must be undefined. |
| subnetIPAddresses? | number | Optional - the number of available IP addresses to required in each subnet. This value is used to calculate the cidrMask. If omitted, the cidrMask uses The CDK default of 17 (up to 32763 addresses). If this value is populated, then vpcProps.subnetConfiguration must be undefined. |
| endPoints? | ServiceEndpointTypes[] | Optional - A list of all VPC service endpoints to launch in the VPC. They are specified using ServiceEndpointTypes, an enum defined in the Factories construct. @default - None |

## VpcFactoryResponse
<a name="_vpcfactoryresponse"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| vpc |  [ec2.Vpc](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Vpc.html)  | The vpc created by the factory. |

## Default settings
<a name="_default_settings_4"></a>

The minimal implementation of the VPC requires the client to specify what types of subnets to launch. Any values not specified default to the default values implemented by the CDK L2 VPC construct:
+ A Virtual Private Cloud
  + All requested subnet layers. By default each subnet type is deployed to 2 Availability Zones. To use more AZs, create an enviroment for your stack (account and region) and set maxAZs on vpcProps. PUBLIC subnets will cause the construct to deploy an Internet Gateway. PRIVATE\_WITH\_EGRESS subnets will cause the construct to deploy a Nat Gateway in each AZ, as well as an Internet Gateway.
  + A configured VPC Flow log in CloudWatch Logs
  + All VPC Endpoints that are specified in endPoints. Interface endpoints are deployed with recommended Security Groups.

## Architecture
<a name="_architecture_4"></a>

Wnile the architecture deployed will vary depending on the Subnet configuration, the diagram below represents what is deployed if the client requests PUBLIC and PRIVATE\_WITH\_EGRESS subnet.

![Diagram showing the VPC, Subnets, Route Tables, Internet Gateway, NAT Gateways, Interface Endpoint and Flow Log.](https://docs.aws.amazon.com/solutions/latest/constructs/images/aws-constructs-factories-vpc.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-constructs-factories) for this pattern to view the code, read/create issues and pull requests and more.
