---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_kinesisstreams_lambda.html
---

# aws-kinesisstreams-lambda
<a name="aws_kinesisstreams_lambda"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws-kinesis-streams-lambda`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-kinesisstreams-lambda`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.kinesisstreamslambda`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct deploys a Kinesis Stream and Lambda function with the appropriate resources/properties for interaction and security.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { KinesisStreamsToLambda } from '@aws-solutions-constructs/aws-kinesisstreams-lambda';
import * as lambda from 'aws-cdk-lib/aws-lambda';

new KinesisStreamsToLambda(this, 'KinesisToLambdaPattern', {
  kinesisEventSourceProps: {
    startingPosition: lambda.StartingPosition.TRIM_HORIZON,
    batchSize: 1
  },
  lambdaFunctionProps: {
    runtime: lambda.Runtime.NODEJS_22_X,
    handler: 'index.handler',
    code: lambda.Code.fromAsset(`lambda`)
  }
});
```

```
from aws_solutions_constructs.aws_kinesis_streams_lambda import KinesisStreamsToLambda
from aws_cdk import (
    aws_lambda as _lambda,
    aws_lambda_event_sources as sources,
    aws_kinesis as kinesis,
    Stack
)
from constructs import Construct

KinesisStreamsToLambda(self, 'KinesisToLambdaPattern',
                        kinesis_event_source_props=sources.KinesisEventSourceProps(
                            starting_position=_lambda.StartingPosition.TRIM_HORIZON,
                            batch_size=1
                        ),
                        lambda_function_props=_lambda.FunctionProps(
                            runtime=_lambda.Runtime.PYTHON_3_14,
                            handler='index.handler',
                            code=_lambda.Code.from_asset(
                                'lambda')
                        )
                        )
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.eventsources.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awsconstructs.services.kinesisstreamslambda.*;

new KinesisStreamsToLambda(this, "KinesisToLambdaPattern", new KinesisStreamsToLambdaProps.Builder()
        .kinesisEventSourceProps(new KinesisEventSourceProps.Builder()
                .startingPosition(StartingPosition.TRIM_HORIZON)
                .batchSize(1)
                .build())
        .lambdaFunctionProps(new FunctionProps.Builder()
                .runtime(Runtime.NODEJS_22_X)
                .code(Code.fromAsset("lambda"))
                .handler("index.handler")
                .build())
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingLambdaObj? |  [`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Optional - instance of an existing Lambda Function object, providing both this and `lambdaFunctionProps` will cause an error. |
| lambdaFunctionProps? |  [`lambda.FunctionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html)  | Optional - user provided props to override the default props for the Lambda function. Providing both this and `existingLambdaObj` causes an error. |
| kinesisStreamProps? |  [`kinesis.StreamProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.StreamProps.html)  | Optional user-provided props to override the default props for the Kinesis stream. |
| existingStreamObj? |  [`kinesis.Stream`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html)  | Existing instance of Kinesis Stream, providing both this and `kinesisStreamProps` will cause an error. |
| kinesisEventSourceProps? |  [`aws-lambda-event-sources.KinesisEventSourceProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda_event_sources.KinesisEventSourceProps.html)  | Optional user-provided props to override the default props for the Lambda event source mapping. |
| createCloudWatchAlarms |  `boolean`  | Whether to create recommended CloudWatch alarms |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| kinesisStream |  [`kinesis.Stream`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html)  | Returns an instance of the Kinesis stream created by the pattern. |
| lambdaFunction |  [`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Returns an instance of the Lambda function created by the pattern. |
| kinesisStreamRole |  [`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for Kinesis stream. |
| cloudwatchAlarms? |  [`cloudwatch.Alarm[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html)  | Returns a list of cloudwatch.Alarm created by the construct |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon Kinesis Stream
<a name="_amazon_kinesis_stream"></a>
+ Configure least privilege access IAM role for Kinesis Stream
+ Enable server-side encryption for Kinesis Stream using AWS Managed KMS Key
+ Deploy best practices CloudWatch Alarms for the Kinesis Stream

### AWS Lambda Function
<a name="_aws_lambda_function"></a>
+ Configure limited privilege access IAM role for Lambda function
+ Enable reusing connections with Keep-Alive for NodeJs Lambda function
+ Enable X-Ray Tracing
+ Enable Failure-Handling features like enable bisect on function Error, set defaults for Maximum Record Age (24 hours) & Maximum Retry Attempts (500) and deploy SQS dead-letter queue as destination on failure
+ Set Environment Variables
  + AWS\_NODEJS\_CONNECTION\_REUSE\_ENABLED (for Node 10.x and higher functions)

## Architecture
<a name="_architecture"></a>

![Diagram showing the Kinesis data stream, CloudWatch log group, Lambda function and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-kinesisstreams-lambda.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-kinesisstreams-lambda) for this pattern to view the code, read/create issues and pull requests and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
