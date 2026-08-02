---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_sns_lambda.html
---

# aws-sns-lambda
<a name="aws_sns_lambda"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_sns_lambda`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-sns-lambda`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.snslambda`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an Amazon SNS connected to an AWS Lambda function.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { SnsToLambda, SnsToLambdaProps } from "@aws-solutions-constructs/aws-sns-lambda";
import * as lambda from 'aws-cdk-lib/aws-lambda';

new SnsToLambda(this, 'test-sns-lambda', {
  lambdaFunctionProps: {
    runtime: lambda.Runtime.NODEJS_22_X,
    handler: 'index.handler',
    code: lambda.Code.fromAsset(`lambda`)
  }
});
```

```
from aws_solutions_constructs.aws_sns_lambda import SnsToLambda
from aws_cdk import (
    aws_lambda as _lambda,
    Stack
)
from constructs import Construct

SnsToLambda(self, 'test_sns_lambda',
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
import software.amazon.awsconstructs.services.snslambda.*;

new SnsToLambda(this, "test-lambda-sqs-stack", new SnsToLambdaProps.Builder()
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
| existingLambdaObj? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Optional - instance of an existing Lambda Function object, providing both this and `lambdaFunctionProps` will cause an error. |
| lambdaFunctionProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html)  | Optional - user provided props to override the default props for the Lambda function. Providing both this and `existingLambdaObj` causes an error. |
| existingTopicObj? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Optional - existing instance of SNS topic object, providing both this and `topicProps` will cause an error. |
| topicProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sns.TopicProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sns.TopicProps.html)  | Optional - user provided properties to override the default properties for the SNS topic. Providing both this and `existingTopicObj` causes an error. |
| enableEncryptionWithCustomerManagedKey? |  `boolean`  | If no key is provided, this flag determines whether the SNS Topic is encrypted with a new CMK or an AWS managed key. This flag is ignored if any of the following are defined: topicProps.masterKey, encryptionKey or encryptionKeyProps. |
| encryptionKey? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)  | An optional, imported encryption key to encrypt the SNS Topic with. |
| encryptionKeyProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html#construct-props](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html#construct-props)  | Optional user provided properties to override the default properties for the KMS encryption key used to encrypt the SNS Topic with. |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| lambdaFunction |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Returns an instance of the Lambda function created by the pattern. |
| snsTopic |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sns.Topic.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sns.Topic.html)  | Returns an instance of the SNS topic created by the pattern. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon SNS Topic
<a name="_amazon_sns_topic"></a>
+ Configure least privilege access permissions for SNS Topic
+ Enable server-side encryption for SNS Topic using AWS managed KMS Key
+ Enforce encryption of data in transit

### AWS Lambda Function
<a name="_aws_lambda_function"></a>
+ Configure limited privilege access IAM role for Lambda function
+ Enable reusing connections with Keep-Alive for NodeJs Lambda function
+ Enable X-Ray Tracing
+ Set Environment Variables
  + AWS\_NODEJS\_CONNECTION\_REUSE\_ENABLED (for Node 10.x and higher functions)

## Architecture
<a name="_architecture"></a>

![Diagram showing the SNS topic, Lambda Function, CloudWatch log group and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-sns-lambda.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-sns-lambda) for this pattern to view the code, read/create issues and pull requests and more.
