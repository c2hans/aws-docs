---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_lambda_transcribe.html
---

# aws-lambda-transcribe
<a name="aws_lambda_transcribe"></a>

![Stability:Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_lambda_transcribe`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-lambda-transcribe`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.lambdatranscribe`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS Lambda function connected to Amazon S3 buckets for use with Amazon Transcribe. The construct creates a source bucket for audio files and a destination bucket for transcription results, with appropriate IAM permissions for the Lambda function to interact with both buckets and Amazon Transcribe service.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { LambdaToTranscribe } from '@aws-solutions-constructs/aws-lambda-transcribe';
import * as lambda from 'aws-cdk-lib/aws-lambda';

new LambdaToTranscribe(this, 'LambdaToTranscribePattern', {
    lambdaFunctionProps: {
        runtime: lambda.Runtime.NODEJS_22_X,
        handler: 'index.handler',
        code: lambda.Code.fromAsset(`lambda`)
    }
});
```

```
from aws_solutions_constructs.aws_lambda_transcribe import LambdaToTranscribe
from aws_cdk import (
    aws_lambda as _lambda,
    Stack
)
from constructs import Construct

LambdaToTranscribe(self, 'LambdaToTranscribePattern',
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
import software.amazon.awsconstructs.services.lambdatranscribe.*;

new LambdaToTranscribe(this, "LambdaToTranscribePattern", new LambdaToTranscribeProps.Builder()
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
| lambdaFunctionProps? |  [`lambda.FunctionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html)  | Optional user provided props to override the default props for the Lambda function. |
| existingSourceBucketObj? |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Existing instance of S3 Bucket object for source audio files. If this is provided, then also providing sourceBucketProps causes an error. |
| sourceBucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the source S3 Bucket. |
| existingDestinationBucketObj? |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Existing instance of S3 Bucket object for transcription results. If this is provided, then also providing destinationBucketProps causes an error. |
| destinationBucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the destination S3 Bucket. |
| useSameBucket? |  `boolean`  | Whether to use the same S3 bucket for both source and destination files. When true, only the source bucket will be created and used for both purposes. Default: false |
| existingVpc? |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | An optional, existing VPC into which this pattern should be deployed. When deployed in a VPC, the Lambda function will use ENIs in the VPC to access network resources and Interface Endpoints will be created in the VPC for Amazon S3 and Amazon Transcribe. If an existing VPC is provided, the `deployVpc` property cannot be `true`. This uses `ec2.IVpc` to allow clients to supply VPCs that exist outside the stack using the [`ec2.Vpc.fromLookup()`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Vpc.html#static-fromwbrlookupscope-id-options) method. |
| vpcProps? |  [`ec2.VpcProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html)  | Optional user provided properties to override the default properties for the new VPC. `enableDnsHostnames`, `enableDnsSupport`, `natGateways` and `subnetConfiguration` are set by the pattern, so any values for those properties supplied here will be overridden. If `deployVpc` is not `true` then this property will be ignored. |
| deployVpc? |  `boolean`  | Whether to create a new VPC based on `vpcProps` into which to deploy this pattern. Setting this to true will deploy the minimal, most private VPC to run the pattern. |
| sourceBucketEnvironmentVariableName? |  `string`  | Optional Name for the Lambda function environment variable set to the name of the source bucket. Default: SOURCE\_BUCKET\_NAME |
| destinationBucketEnvironmentVariableName? |  `string`  | Optional Name for the Lambda function environment variable set to the name of the destination bucket. Default: DESTINATION\_BUCKET\_NAME |
| sourceLoggingBucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the source S3 Logging Bucket. |
| destinationLoggingBucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the destination S3 Logging Bucket. |
| logSourceS3AccessLogs? | boolean | Whether to turn on Access Logging for the source S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. default - true |
| logDestinationS3AccessLogs? | boolean | Whether to turn on Access Logging for the destination S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. default - true |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| lambdaFunction |  [`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Returns an instance of the Lambda function created by the pattern. |
| sourceBucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of the source S3 bucket if it is created by the pattern. |
| destinationBucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of the destination S3 bucket if it is created by the pattern. |
| sourceLoggingBucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct as the logging bucket for the source bucket. |
| destinationLoggingBucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct as the logging bucket for the destination bucket. |
| vpc? |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | Returns an interface on the VPC used by the pattern (if any). This may be a VPC created by the pattern or the VPC supplied to the pattern constructor. |
| sourceBucketInterface |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Returns an interface of s3.IBucket used by the construct for the source bucket whether created by the pattern or supplied from the client. |
| destinationBucketInterface |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Returns an interface of s3.IBucket used by the construct for the destination bucket whether created by the pattern or supplied from the client. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### AWS Lambda Function
<a name="_aws_lambda_function"></a>
+ Configure limited privilege access IAM role for Lambda function
+ Enable reusing connections with Keep-Alive for NodeJs Lambda function
+ Enable X-Ray Tracing
+ Set Environment Variables
  + (default) SOURCE\_BUCKET\_NAME
  + (default) DESTINATION\_BUCKET\_NAME
  + AWS\_NODEJS\_CONNECTION\_REUSE\_ENABLED (for Node 10.x and higher functions)
+ Grant permissions to use Amazon Transcribe service, write permissions to the source bucket, and read permissions to the destination bucket

### Amazon S3 Buckets
<a name="_amazon_s3_buckets"></a>
+ Configure Access logging for both S3 Buckets
+ Enable server-side encryption for both S3 Buckets using AWS managed KMS Key
+ Enforce encryption of data in transit
+ Turn on the versioning for both S3 Buckets
+ Don’t allow public access for both S3 Buckets
+ Retain the S3 Buckets when deleting the CloudFormation stack
+ Applies Lifecycle rule to move noncurrent object versions to Glacier storage after 90 days

### Amazon Transcribe Service
<a name="_amazon_transcribe_service"></a>
+ The Transcribe service will have read access to the source bucket and write permissions to the destination bucket
+ Lambda function will have permissions to start transcription jobs, get job status, and list transcription jobs

### Amazon VPC
<a name="_amazon_vpc"></a>
+ If deployVpc is true, a minimal VPC will be created with:
  + Interface Endpoints for Amazon S3 and Amazon Transcribe
  + Private subnets for Lambda function
  + Appropriate security groups and routing

## Architecture
<a name="_architecture"></a>

![Diagram showing the Lambda function, source and destination S3 buckets, Amazon Transcribe service, and IAM roles created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-lambda-transcribe.png)

## Example Lambda Function Implementation
<a name="_example_lambda_function_implementation"></a>

While Solutions Constructs does not publish code for the Lambda function to call Transcribe, here is an example of calling Transcribe: ['example'](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/transcribe/src/transcribe_create_job.js). (this example is in JavaScript, but examples in other languages can also be found at this site)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-lambda-transcribe) for this pattern to view the code, read/create issues and pull requests and more.

© Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
