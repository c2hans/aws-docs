---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_lambda_translate.html
---

# aws-lambda-translate
<a name="aws_lambda_translate"></a>

![Stability:Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_lambda_translate`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-lambda-translate`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.lambdatranslate`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS Lambda function connected to Amazon Translate service. For asynchronous translation jobs, the construct can optionally create source and destination S3 buckets with appropriate IAM permissions for the Lambda function to interact with both buckets and Amazon Translate service.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { LambdaToTranslate } from '@aws-solutions-constructs/aws-lambda-translate';
import * as lambda from 'aws-cdk-lib/aws-lambda';

new LambdaToTranslate(this, 'LambdaToTranslatePattern', {
    lambdaFunctionProps: {
        runtime: lambda.Runtime.NODEJS_22_X,
        handler: 'index.handler',
        code: lambda.Code.fromAsset(`lambda`)
    }
});
```

```
from aws_solutions_constructs.aws_lambda_translate import LambdaToTranslate
from aws_cdk import (
    aws_lambda as _lambda,
    Stack
)
from constructs import Construct

LambdaToTranslate(self, 'LambdaToTranslatePattern',
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
import software.amazon.awsconstructs.services.lambdatranslate.*;

new LambdaToTranslate(this, "LambdaToTranslatePattern", new LambdaToTranslateProps.Builder()
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
| asyncJobs? |  `boolean`  | Whether to enable asynchronous translation jobs. When true, source and destination S3 buckets will be created and the Lambda function will be granted permissions to start and stop translation jobs. Default: false |
| existingSourceBucketObj? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Existing instance of S3 Bucket object for source files. If this is provided, then also providing sourceBucketProps causes an error. Only valid when asyncJobs is true. |
| sourceBucketProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the source S3 Bucket. Only valid when asyncJobs is true. |
| existingDestinationBucketObj? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Existing instance of S3 Bucket object for translation results. If this is provided, then also providing destinationBucketProps causes an error. Only valid when asyncJobs is true. |
| destinationBucketProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the destination S3 Bucket. Only valid when asyncJobs is true. |
| useSameBucket? |  `boolean`  | Whether to use the same S3 bucket for both source and destination files. When true, only the source bucket will be created and used for both purposes. Only valid when asyncJobs is true. Default: false |
| additionalPermissions? |  `string[]`  | Optional array of additional IAM permissions to grant to the Lambda function for Amazon Translate. This is intended for use with Translate actions and will assign a resource of '\*' - permissions for other services with specific resources should add the permssion using Function.addToRolePolicy(). Always added: ['translate:TranslateText', 'translate:TranslateDocument'] |
| existingVpc? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | An optional, existing VPC into which this pattern should be deployed. When deployed in a VPC, the Lambda function will use ENIs in the VPC to access network resources and Interface Endpoints will be created in the VPC for Amazon Translate. If asyncJobs is true, Interface Endpoints for Amazon S3 will also be created. If an existing VPC is provided, the `deployVpc` property cannot be `true`. This uses `ec2.IVpc` to allow clients to supply VPCs that exist outside the stack using the [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Vpc.html#static-fromwbrlookupscope-id-options](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Vpc.html#static-fromwbrlookupscope-id-options) method. |
| vpcProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html)  | Optional user provided properties to override the default properties for the new VPC. `enableDnsHostnames`, `enableDnsSupport`, `natGateways` and `subnetConfiguration` are set by the pattern, so any values for those properties supplied here will be overridden. If `deployVpc` is not `true` then this property will be ignored. |
| deployVpc? |  `boolean`  | Whether to create a new VPC based on `vpcProps` into which to deploy this pattern. Setting this to true will deploy the minimal, most private VPC to run the pattern. |
| sourceBucketEnvironmentVariableName? |  `string`  | Optional Name for the Lambda function environment variable set to the name of the source bucket. Only valid when asyncJobs is true. Default: SOURCE\_BUCKET\_NAME |
| destinationBucketEnvironmentVariableName? |  `string`  | Optional Name for the Lambda function environment variable set to the name of the destination bucket. Only valid when asyncJobs is true. Default: DESTINATION\_BUCKET\_NAME |
| dataAccessRoleArnEnvironmentVariableName? |  `string`  | Optional Name for the Lambda function environment variable set to the ARN of the IAM role used for asynchronous translation jobs. Only valid when asyncJobs is true. Default: DATA\_ACCESS\_ROLE\_ARN |
| sourceLoggingBucketProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the source S3 Logging Bucket. Only valid when asyncJobs is true. |
| destinationLoggingBucketProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the destination S3 Logging Bucket. Only valid when asyncJobs is true. |
| logSourceS3AccessLogs? | boolean | Whether to turn on Access Logging for the source S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. Only valid when asyncJobs is true. default - true |
| logDestinationS3AccessLogs? | boolean | Whether to turn on Access Logging for the destination S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. Only valid when asyncJobs is true. default - true |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| lambdaFunction |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Returns an instance of the Lambda function created by the pattern. |
| sourceBucket? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of the source S3 bucket if it is created by the pattern. |
| destinationBucket? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of the destination S3 bucket if it is created by the pattern. |
| sourceLoggingBucket? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct as the logging bucket for the source bucket. |
| destinationLoggingBucket? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct as the logging bucket for the destination bucket. |
| vpc? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | Returns an interface on the VPC used by the pattern (if any). This may be a VPC created by the pattern or the VPC supplied to the pattern constructor. |
| sourceBucketInterface? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Returns an interface of s3.IBucket used by the construct for the source bucket whether created by the pattern or supplied from the client. |
| destinationBucketInterface? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Returns an interface of s3.IBucket used by the construct for the destination bucket whether created by the pattern or supplied from the client. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### AWS Lambda Function
<a name="_aws_lambda_function"></a>
+ Configure limited privilege access IAM role for Lambda function
+ Enable reusing connections with Keep-Alive for NodeJs Lambda function
+ Enable X-Ray Tracing
+ Set Environment Variables
  + (default) SOURCE\_BUCKET\_NAME (when asyncJobs is true)
  + (default) DESTINATION\_BUCKET\_NAME (when asyncJobs is true)
  + (default) DATA\_ACCESS\_ROLE\_ARN (when asyncJobs is true)
  + AWS\_NODEJS\_CONNECTION\_REUSE\_ENABLED (for Node 10.x and higher functions)
+ Grant permissions to use Amazon Translate service (['translate:TranslateText', 'translate:TranslateDocument'] by default)
+ When asyncJobs is true, grant permissions to start and stop batch translation jobs (translate:StartTextTranslationJob and translate:StopTextTranslationJob), read from source bucket, and read and write to destination bucket

### Amazon S3 Buckets (when asyncJobs is true)
<a name="_amazon_s3_buckets_when_asyncjobs_is_true"></a>
+ Configure Access logging for both S3 Buckets
+ Enable server-side encryption for both S3 Buckets using AWS managed KMS Key
+ Enforce encryption of data in transit
+ Turn on the versioning for both S3 Buckets
+ Don’t allow public access for both S3 Buckets
+ Retain the S3 Buckets when deleting the CloudFormation stack
+ Applies Lifecycle rule to move noncurrent object versions to Glacier storage after 90 days

### Amazon Translate Service
<a name="_amazon_translate_service"></a>
+ Lambda function will have permissions to ['translate:TranslateText', 'translate:TranslateDocument'] operations by default
+ When asyncJobs is true, Lambda function will have permissions to start and stop batch translation jobs
+ A role granting access to the source and destination buckets will be created to pass to Translate for StartTextTranslationJob calls

### Amazon VPC
<a name="_amazon_vpc"></a>
+ If deployVpc is true, a minimal VPC will be created with:
  + Interface Endpoints for Amazon Translate
  + Interface Endpoints for Amazon S3 (when asyncJobs is true)
  + Private subnets for Lambda function
  + Appropriate security groups and routing

## Architecture
<a name="_architecture"></a>

 **Default Implementation**

![Diagram showing the Lambda functionAmazon Translate service, and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-lambda-translate.png)

 **Default Implementation when asyncJobs = true**

![Diagram showing the Lambda function, source and destination S3 buckets (when asyncJobs is true), Amazon Translate service, and IAM roles created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-lambda-translate-async.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-lambda-translate) for this pattern to view the code, read/create issues and pull requests and more.

© Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
