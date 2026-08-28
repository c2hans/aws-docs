---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_dynamodbstreams_lambda.html
---

# aws-dynamodbstreams-lambda
<a name="aws_dynamodbstreams_lambda"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_dynamodbstreams_lambda`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-dynamodbstreams-lambda`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.dynamodbstreamslambda`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an Amazon DynamoDB table with stream that invokes an AWS Lambda function with the least privileged permissions.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { DynamoDBStreamsToLambdaProps,  DynamoDBStreamsToLambda} from '@aws-solutions-constructs/aws-dynamodbstreams-lambda';
import * as lambda from 'aws-cdk-lib/aws-lambda';

new DynamoDBStreamsToLambda(this, 'test-dynamodbstreams-lambda', {
  lambdaFunctionProps: {
      code: lambda.Code.fromAsset(`lambda`),
      runtime: lambda.Runtime.NODEJS_22_X,
      handler: 'index.handler'
  },
});
```

```
from aws_solutions_constructs.aws_dynamodbstreams_lambda import DynamoDBStreamsToLambda
from aws_cdk import (
  aws_lambda as _lambda,
  Stack
)
from constructs import Construct

DynamoDBStreamsToLambda(self, 'test-dynamodbstreams-lambda',
                        lambda_function_props=_lambda.FunctionProps(
                            code=_lambda.Code.from_asset('lambda'),
                            runtime=_lambda.Runtime.PYTHON_3_14,
                            handler='index.handler'
                        )
                        )
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awsconstructs.services.dynamodbstreamslambda.*;

new DynamoDBStreamsToLambda(this, "test-dynamodbstreams-lambda",
        new DynamoDBStreamsToLambdaProps.Builder()
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
| dynamoTableProps? |  [`dynamodb.TableProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_dynamodb.TableProps.html)  | Optional user provided props to override the default props for the DynamoDB Table. Providing both this and `existingTableInterface` causes an error. |
| existingTableInterface? |  [`dynamodb.ITable`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_dynamodb.ITable.html)  | Optional - existing DynamoDB table, providing both this and `dynamoTableProps` will cause an error. this and `dynamoTableProps` will cause an error. |
| dynamoEventSourceProps? |  [`aws-lambda-event-sources.DynamoEventSourceProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda_event_sources.DynamoEventSourceProps.html)  | Optional user provided props to override the default props for DynamoDB Event Source |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| dynamoTableInterface |  [`dynamodb.ITable`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_dynamodb.ITable.html)  | Returns an instance of dynamodb.ITable created by the construct |
| dynamoTable? |  [`dynamodb.Table`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_dynamodb.Table.html)  | Returns an instance of dynamodb.Table created by the construct. IMPORTANT: If existingTableInterface was provided in Pattern Construct Props, this property will be `undefined`  |
| lambdaFunction |  [`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Returns an instance of lambda.Function created by the construct |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon DynamoDB Table
<a name="_amazon_dynamodb_table"></a>
+ Set the billing mode for DynamoDB Table to On-Demand (Pay per request)
+ Enable server-side encryption for DynamoDB Table using AWS managed KMS Key
+ Creates a partition key called "id" for DynamoDB Table
+ Retain the Table when deleting the CloudFormation stack
+ Enable continuous backups and point-in-time recovery

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

![Diagram showing data flow between AWS services including DynamoDB, Lambda, CloudWatch and an IAM Role](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-dynamodbstreams-lambda.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-dynamodbstreams-lambda) for this pattern to view the code, read/create issues and pull requests and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
