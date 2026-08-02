---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_lambda_kinesisfirehose.html
---

# aws-lambda-kinesisfirehose
<a name="aws_lambda_kinesisfirehose"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_lambda_kinesisfirehose`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-lambda-kinesisfirehose`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.lambdakinesisfirehose`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS Lambda function connected to an existing Amazon Kinesis Firehose Delivery Stream.

Here is a minimal deployable pattern definition :

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { LambdaToS3 } from '@aws-solutions-constructs/aws-lambda-kinesisfirehose';
import * as lambda from 'aws-cdk-lib/aws-lambda';

// The construct requires an existing Firehose Delivery Stream, this can be created in raw CDK or extracted
// from a previously instantiated construct that created an Firehose Delivery Stream
const existingFirehoseDeliveryStream = previouslyCreatedKinesisFirehoseToS3Construct.kinesisFirehose;

new LambdaToKinesisFirehose(this, 'LambdaToFirehosePattern', {
  lambdaFunctionProps: {
      runtime: lambda.Runtime.NODEJS_22_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset(`lambda`)
  },
  existingKinesisFirehose: existingFirehoseDeliveryStream
});
```

```
from aws_solutions_constructs.aws_lambda_kinesisfirehose import LambdaToKinesisFirehose
from aws_cdk import (
    aws_lambda as _lambda,
    Stack
)
from constructs import Construct

# The construct requires an existing Firehose Delivery Stream, this can be created in raw CDK or extracted
# from a previously instantiated construct that created an Firehose Delivery Stream
existingFirehoseDeliveryStream = previouslyCreatedKinesisFirehoseToS3Construct.kinesisFirehose;

LambdaToKinesisFirehose(self, 'LambdaToFirehosePattern',
        existingKinesisFirehose=existingFirehoseDeliveryStream,
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
import software.amazon.awsconstructs.services.lambdakinesisfirehose.*;

// The construct requires an existing Firehose Delivery Stream, this can be created in raw CDK or extracted
// from a previously instantiated construct that created an Firehose Delivery Stream
existingFirehoseDeliveryStream = previouslyCreatedKinesisFirehoseToS3Construct.kinesisFirehose;

new LambdaToKinesisFirehose(this, "LambdaToFirehosePattern", new LambdaToKinesisFirehoseProps.Builder()
        .existingKinesisFirehose(existingFirehoseDeliveryStream)
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
| existingKinesisFirehose |  [kinesisfirehose.CfnDeliveryStream](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.html)  | An existing Kinesis Firehose Delivery Stream to which the Lambda function can put data. Note - the delivery stream construct must have already been created and have the deliveryStreamName set. This construct will *not* create a new Delivery Stream. |
| existingVpc? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | An optional, existing VPC into which this pattern should be deployed. When deployed in a VPC, the Lambda function will use ENIs in the VPC to access network resources and an Interface Endpoint will be created in the VPC for Amazon Kinesis Data Firehose. If an existing VPC is provided, the `deployVpc` property cannot be `true`. This uses `ec2.IVpc` to allow clients to supply VPCs that exist outside the stack using the [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Vpc.html#static-fromwbrlookupscope-id-options](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Vpc.html#static-fromwbrlookupscope-id-options) method. |
| vpcProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html)  | Optional user provided properties to override the default properties for the new VPC. `enableDnsHostnames`, `enableDnsSupport`, `natGateways` and `subnetConfiguration` are set by the pattern, so any values for those properties supplied here will be overridden. If `deployVpc` is not `true` then this property will be ignored. |
| deployVpc? |  `boolean`  | Whether to create a new VPC based on `vpcProps` into which to deploy this pattern. Setting this to true will deploy the minimal, most private VPC to run the pattern: |
| firehoseEnvironmentVariableName? |  `string`  | Optional Name for the Lambda function environment variable set to the name of the delivery stream. Default: FIREHOSE\_DELIVERYSTREAM\_NAME |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| lambdaFunction |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Returns an instance of the Lambda function created by the pattern. |
| kinesisFirehose |  [kinesisfirehose.CfnDeliveryStream](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.html)  | The Kinesis Firehose Delivery Stream used by the construct. |
| vpc? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | Returns an interface on the VPC used by the pattern (if any). This may be a VPC created by the pattern or the VPC supplied to the pattern constructor. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### AWS Lambda Function
<a name="_aws_lambda_function"></a>
+ Configure limited privilege access IAM role for Lambda function
+ Enable reusing connections with Keep-Alive for NodeJs Lambda function
+ Enable X-Ray Tracing
+ Set Environment Variables
  + (default) FIREHOSE\_DELIVERYSTREAM\_NAME
  + AWS\_NODEJS\_CONNECTION\_REUSE\_ENABLED

### Amazon Kinesis Firehose Delivery Stream
<a name="_amazon_kinesis_firehose_delivery_stream"></a>
+ This construct must be provided a configured Stream construct, it does not change this Stream.

## Architecture
<a name="_architecture"></a>

![Diagram showing the Lambda function, Kinesis firehose and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-lambda-kinesisfirehose.png)

## Example Lambda Function Implementation
<a name="_example_lambda_function_implementation"></a>

While Solutions Constructs does not publish code for the Lambda function to call Firehose, here is an example of calling Firehose: ['example'](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/firehose/scenarios/firehose-put-actions/firehose.py). (this example is in Python, but examples in other languages can also be found at this site)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-lambda-kinesisfirehose) for this pattern to view the code, read/create issues and pull requests and more.
